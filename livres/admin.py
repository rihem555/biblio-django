from django.contrib import admin
from .models import Livre, Commentaire, NoteUtilisateur


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'genre', 'note', 'disponible', 'date_ajout']
    list_filter = ['genre', 'disponible', 'note']
    search_fields = ['titre', 'auteur']
    list_editable = ['disponible']


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['livre', 'auteur', 'date']
    list_filter = ['date']


@admin.register(NoteUtilisateur)
class NoteUtilisateurAdmin(admin.ModelAdmin):
    list_display = ['livre', 'utilisateur', 'note', 'date']
    list_filter = ['note']
