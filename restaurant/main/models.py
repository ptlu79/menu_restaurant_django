from django.db import models


# Create your models here.
class IdentityStore(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=400)
    code_postal = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    telephone = models.CharField(max_length=400)



    def __str__(self):
        return self.nom  # pour utiliser le nom dans l'interface admin au lieu de pizza(1) ...

# on migre le model vers la bdd...
# python manage.py makemigrations
# resultat : no changes detected alors allez dans restaurant/settings.py
# rajoute :     'menu.apps.MenuConfig', dans INSTALLED_APPS
# puis il faut appliquer a la bdd :
#python manage.py migrate
# --------- A FAIRE SI CHANGEMENT DU MODEL DE LA BDD ------------
# créer la table d'association