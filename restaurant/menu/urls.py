
from django.urls import path
from . import views


app_name = 'menu'  # namespace

urlpatterns = [
    path('', views.index, name="index"),  # si menu/ donc rien apres alors utilise la view index
]
