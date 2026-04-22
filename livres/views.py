from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q, Count, Avg
from .models import Livre, Commentaire, NoteUtilisateur
from .forms import LivreForm, CommentaireForm


def home(request):
    """Page d'accueil avec statistiques"""
    total_livres = Livre.objects.count()
    livres_disponibles = Livre.objects.filter(disponible=True).count()
    total_commentaires = Commentaire.objects.count()
    note_moyenne = Livre.objects.aggregate(Avg('note'))['note__avg']
    derniers_livres = Livre.objects.all()[:4]

    context = {
        'total_livres': total_livres,
        'livres_disponibles': livres_disponibles,
        'total_commentaires': total_commentaires,
        'note_moyenne': round(note_moyenne, 1) if note_moyenne else 0,
        'derniers_livres': derniers_livres,
    }
    return render(request, 'livres/home.html', context)


def liste_livres(request):
    """READ - Affichage de tous les livres avec recherche"""
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')
    disponible = request.GET.get('disponible', '')

    livres = Livre.objects.all()

    if query:
        livres = livres.filter(
            Q(titre__icontains=query) |
            Q(auteur__icontains=query) |
            Q(description__icontains=query)
        )

    if genre:
        livres = livres.filter(genre=genre)

    if disponible == 'true':
        livres = livres.filter(disponible=True)
    elif disponible == 'false':
        livres = livres.filter(disponible=False)

    genres = Livre.objects.values_list('genre', flat=True).distinct()

    context = {
        'livres': livres,
        'query': query,
        'genre_filtre': genre,
        'genres': genres,
        'disponible_filtre': disponible,
        'total': livres.count(),
    }
    return render(request, 'livres/liste.html', context)


def detail_livre(request, pk):
    """Détail d'un livre + commentaires + notes"""
    livre = get_object_or_404(Livre, pk=pk)
    commentaires = livre.commentaires.all()
    form = CommentaireForm()

    # Note moyenne des utilisateurs
    from django.db.models import Avg
    notes = livre.notes_utilisateurs.all()
    note_moyenne = notes.aggregate(Avg('note'))['note__avg']
    total_votes = notes.count()

    # Note de l'utilisateur connecté
    ma_note = None
    if request.user.is_authenticated:
        try:
            ma_note = NoteUtilisateur.objects.get(livre=livre, utilisateur=request.user).note
        except NoteUtilisateur.DoesNotExist:
            pass

    if request.method == 'POST':
        # Vote
        if 'note' in request.POST:
            if not request.user.is_authenticated:
                messages.warning(request, 'Connectez-vous pour noter.')
                return redirect('login')
            note_val = int(request.POST.get('note'))
            if 1 <= note_val <= 5:
                NoteUtilisateur.objects.update_or_create(
                    livre=livre, utilisateur=request.user,
                    defaults={'note': note_val}
                )
                messages.success(request, f'⭐ Votre note ({note_val}/5) a été enregistrée !')
            return redirect('detail_livre', pk=pk)

        # Commentaire
        if not request.user.is_authenticated:
            messages.warning(request, 'Connectez-vous pour commenter.')
            return redirect('login')
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.livre = livre
            commentaire.auteur = request.user
            commentaire.save()
            messages.success(request, '💬 Commentaire ajouté avec succès !')
            return redirect('detail_livre', pk=pk)

    context = {
        'livre': livre,
        'commentaires': commentaires,
        'form': form,
        'stars': range(livre.note),
        'empty_stars': range(5 - livre.note),
        'note_moyenne': round(note_moyenne, 1) if note_moyenne else None,
        'total_votes': total_votes,
        'ma_note': ma_note,
    }
    return render(request, 'livres/detail.html', context)


@login_required
def ajouter_livre(request):
    """CREATE - Ajouter un livre (admin uniquement)"""
    if not request.user.is_staff:
        messages.error(request, "⛔ Accès réservé aux administrateurs.")
        return redirect('liste_livres')
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save()
            messages.success(request, f'✅ Le livre "{livre.titre}" a été ajouté avec succès !')
            return redirect('liste_livres')
    else:
        form = LivreForm()

    return render(request, 'livres/ajouter.html', {'form': form, 'titre_page': 'Ajouter un livre'})


@login_required
def modifier_livre(request, pk):
    """UPDATE - Modifier un livre (admin uniquement)"""
    if not request.user.is_staff:
        messages.error(request, "⛔ Accès réservé aux administrateurs.")
        return redirect('liste_livres')
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES, instance=livre)
        if form.is_valid():
            form.save()
            messages.success(request, f'✏️ Le livre "{livre.titre}" a été modifié avec succès !')
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)

    return render(request, 'livres/ajouter.html', {'form': form, 'livre': livre, 'titre_page': 'Modifier le livre'})


@login_required
def supprimer_livre(request, pk):
    """DELETE - Supprimer un livre (admin uniquement)"""
    if not request.user.is_staff:
        messages.error(request, "⛔ Accès réservé aux administrateurs.")
        return redirect('liste_livres')
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        titre = livre.titre
        livre.delete()
        messages.success(request, f'🗑️ Le livre "{titre}" a été supprimé.')
        return redirect('liste_livres')

    return render(request, 'livres/supprimer.html', {'livre': livre})


@login_required
def supprimer_commentaire(request, pk):
    """Supprimer un commentaire"""
    commentaire = get_object_or_404(Commentaire, pk=pk)
    livre_pk = commentaire.livre.pk
    if request.user == commentaire.auteur or request.user.is_staff:
        commentaire.delete()
        messages.success(request, '🗑️ Commentaire supprimé.')
    return redirect('detail_livre', pk=livre_pk)


def register(request):
    """Page d'inscription"""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'🎉 Bienvenue {user.username} ! Votre compte a été créé.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'livres/register.html', {'form': form})
