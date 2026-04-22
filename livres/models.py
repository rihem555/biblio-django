from django.db import models
from django.contrib.auth.models import User

GENRE_CHOICES = [
    ('roman', 'Roman'),
    ('science_fiction', 'Science-Fiction'),
    ('fantasy', 'Fantasy'),
    ('policier', 'Policier'),
    ('biographie', 'Biographie'),
    ('histoire', 'Histoire'),
    ('science', 'Science'),
    ('philosophie', 'Philosophie'),
    ('autre', 'Autre'),
]

NOTE_CHOICES = [(i, '⭐' * i) for i in range(1, 6)]


class Livre(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre")
    auteur = models.CharField(max_length=100, verbose_name="Auteur")
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='roman', verbose_name="Genre")
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Couverture")
    note = models.IntegerField(choices=NOTE_CHOICES, default=3, verbose_name="Note")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ajout']
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

    def __str__(self):
        return self.titre

    def get_stars(self):
        return range(self.note)

    def get_empty_stars(self):
        return range(5 - self.note)


class NoteUtilisateur(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='notes_utilisateurs')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField(choices=NOTE_CHOICES)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('livre', 'utilisateur')
        verbose_name = "Note utilisateur"
        verbose_name_plural = "Notes utilisateurs"

    def __str__(self):
        return f"{self.utilisateur} — {self.livre} : {self.note}⭐"


class Commentaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Auteur")
    contenu = models.TextField(verbose_name="Commentaire")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.livre}"
