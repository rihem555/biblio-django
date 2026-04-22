import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblio.settings')
django.setup()

from livres.models import Livre

livres_data = [
    {'titre': 'Le Petit Prince', 'auteur': 'Antoine de Saint-Exupéry', 'genre': 'roman', 'note': 5, 'disponible': True, 'description': "Un pilote échoué dans le désert rencontre un petit prince venu d'une autre planète. Un conte poétique et philosophique sur l'amitié, l'amour et le sens de la vie."},
    {'titre': '1984', 'auteur': 'George Orwell', 'genre': 'science_fiction', 'note': 5, 'disponible': True, 'description': "Dans un futur totalitaire, Winston Smith travaille pour le Parti. Un roman dystopique sur la surveillance, la manipulation et la liberté."},
    {'titre': "Harry Potter à l'école des sorciers", 'auteur': 'J.K. Rowling', 'genre': 'fantasy', 'note': 5, 'disponible': True, 'description': "Harry Potter découvre le jour de ses 11 ans qu'il est un sorcier et est admis à Poudlard. Le début d'une grande saga magique."},
    {'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien', 'genre': 'fantasy', 'note': 5, 'disponible': False, 'description': "Frodon Sacquet doit détruire l'Anneau Unique pour sauver la Terre du Milieu. Une épopée fantastique monumentale."},
    {'titre': 'Dune', 'auteur': 'Frank Herbert', 'genre': 'science_fiction', 'note': 5, 'disponible': True, 'description': "Paul Atréides arrive sur la planète désertique Arrakis, seule source d'une précieuse épice. Un chef-d'œuvre de la science-fiction."},
    {'titre': "L'Étranger", 'auteur': 'Albert Camus', 'genre': 'roman', 'note': 4, 'disponible': True, 'description': "Meursault, un homme indifférent au monde, commet un meurtre absurde sous le soleil d'Alger. Un roman existentialiste fondamental."},
    {'titre': 'Les Misérables', 'auteur': 'Victor Hugo', 'genre': 'roman', 'note': 5, 'disponible': False, 'description': "Jean Valjean, ancien forçat, cherche à se racheter dans la France du XIXe siècle. Un roman monumental sur la justice et la rédemption."},
    {'titre': 'Sherlock Holmes : Etude en rouge', 'auteur': 'Arthur Conan Doyle', 'genre': 'policier', 'note': 4, 'disponible': True, 'description': "La première rencontre entre Sherlock Holmes et le Dr Watson, qui enquêtent sur un meurtre mystérieux à Londres."},
    {'titre': 'Une brève histoire du temps', 'auteur': 'Stephen Hawking', 'genre': 'science', 'note': 4, 'disponible': True, 'description': "Stephen Hawking explique les grands mystères de l'univers : le Big Bang, les trous noirs, la relativité."},
    {'titre': 'Sapiens', 'auteur': 'Yuval Noah Harari', 'genre': 'histoire', 'note': 5, 'disponible': True, 'description': "L'histoire de l'humanité depuis l'Homo sapiens jusqu'à nos jours. Un regard fascinant sur notre passé et notre avenir."},
    {'titre': 'Le Nom de la rose', 'auteur': 'Umberto Eco', 'genre': 'policier', 'note': 4, 'disponible': True, 'description': "Un moine franciscain enquête sur des meurtres mystérieux dans une abbaye médiévale. Un thriller intellectuel captivant."},
    {'titre': 'Crime et Châtiment', 'auteur': 'Fiodor Dostoïevski', 'genre': 'roman', 'note': 5, 'disponible': False, 'description': "Raskolnikov, un étudiant pauvre, commet un meurtre et lutte contre sa propre culpabilité. Un roman psychologique bouleversant."},
]

created = 0
for data in livres_data:
    livre, is_new = Livre.objects.get_or_create(titre=data['titre'], defaults=data)
    if is_new:
        created += 1
        print(f"✅ Ajouté : {livre.titre} — {livre.auteur}")
    else:
        print(f"⚠️  Existe déjà : {livre.titre}")

print(f"\n🎉 {created} livre(s) ajouté(s) !")
