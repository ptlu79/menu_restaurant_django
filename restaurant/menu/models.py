from django.db import models


# Create your models here.
class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

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
