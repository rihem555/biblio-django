from django import forms
from .models import Livre, Commentaire


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'genre', 'description', 'image', 'note', 'disponible']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre du livre'
            }),
            'auteur': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de l\'auteur'
            }),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description du livre...'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'note': forms.Select(attrs={'class': 'form-select'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Partagez votre avis sur ce livre...'
            }),
        }
        labels = {
            'contenu': 'Votre commentaire',
        }
