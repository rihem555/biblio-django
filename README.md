# 📚 BiblioTech — Projet Django

Application de gestion de bibliothèque développée avec Django.

## 🚀 Installation & Lancement

### 1. Cloner le projet
```bash
git clone <votre-lien-github>
cd bibliotheque_project
```

### 2. Créer et activer l'environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations (création de SQLite)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un superutilisateur (pour se connecter)
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

### 7. Accéder à l'application
- **Application** : http://127.0.0.1:8000/
- **Admin Django** : http://127.0.0.1:8000/admin/

---

## ✅ Fonctionnalités

### Base (15 pts)
- ✅ **CRUD complet** sur les livres (Créer, Lire, Modifier, Supprimer)
- ✅ **SQLite3** comme base de données
- ✅ **Architecture MVT** (Modèle - Vue - Template)
- ✅ **Environnement virtuel** (venv)
- ✅ **Templates Django** avec Django Template Language

### Bonus (jusqu'à +5 pts)
- ✅ **Page d'accueil esthétique** avec statistiques (+1)
- ✅ **Authentification** login/logout (+2)
- ✅ **2 tables avec relation** : `Livre` ←→ `Commentaire` (+2)
- ✅ **Recherche** par titre, auteur, genre (+1)
- ✅ **Bootstrap 5** framework CSS (+1)
- ✅ **Upload d'images** pour les couvertures (+2)



---

## 🗂️ Structure du projet

```
bibliotheque_project/
├── venv/                          # Environnement virtuel
├── manage.py
├── requirements.txt
├── db.sqlite3                     # Base de données (générée automatiquement)
├── media/                         # Images uploadées
│   └── covers/
├── bibliotheque/                  # Configuration du projet
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── livres/                        # Application principale
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py                  # Livre + Commentaire
    ├── urls.py
    ├── views.py                   # CRUD + Recherche + Commentaires
    └── templates/
        └── livres/
            ├── base.html          # Template de base (navbar, footer)
            ├── home.html          # Page d'accueil avec stats
            ├── liste.html         # Catalogue avec recherche
            ├── detail.html        # Détail livre + commentaires
            ├── ajouter.html       # Formulaire ajout/modification
            ├── supprimer.html     # Confirmation suppression
            └── login.html         # Authentification
```

---

## 🎨 Design

- **Style** : Dark mode moderne & coloré
- **Framework CSS** : Bootstrap 5
- **Typographie** : Syne (titres) + DM Sans (texte)
- **Thème** : Dégradés violet/rose/vert sur fond sombre

---

## 📊 Modèles de données

### Livre
| Champ | Type | Description |
|-------|------|-------------|
| titre | CharField | Titre du livre |
| auteur | CharField | Nom de l'auteur |
| genre | CharField | Genre (roman, SF, fantasy...) |
| description | TextField | Description |
| image | ImageField | Couverture (upload) |
| note | IntegerField | Note de 1 à 5 étoiles |
| disponible | BooleanField | Disponibilité |
| date_ajout | DateTimeField | Date d'ajout automatique |

### Commentaire (relation avec Livre)
| Champ | Type | Description |
|-------|------|-------------|
| livre | ForeignKey | Relation vers Livre |
| auteur | ForeignKey | Relation vers User |
| contenu | TextField | Texte du commentaire |
| date | DateTimeField | Date automatique |

---

*Projet réalisé dans le cadre du module Programmation Python Avancée — AU 25-26*
*Enseignante : Dr. Sghaier Amra*
