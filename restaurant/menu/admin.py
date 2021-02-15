from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    # affichage de la liste des data a cote du nom, les colonnes
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    # mettre un champs de recherche et [ par quoi je recherche]
    search_fields = ['nom', 'ingredients', 'prix']

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
