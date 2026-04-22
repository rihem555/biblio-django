from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/<int:pk>/', views.detail_livre, name='detail_livre'),
    path('livres/ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('livres/<int:pk>/modifier/', views.modifier_livre, name='modifier_livre'),
    path('livres/<int:pk>/supprimer/', views.supprimer_livre, name='supprimer_livre'),
    path('commentaire/<int:pk>/supprimer/', views.supprimer_commentaire, name='supprimer_commentaire'),
]
