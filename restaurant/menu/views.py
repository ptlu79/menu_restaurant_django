from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Pizza

def index(request):
    # /menu

    pizzas = Pizza.objects.all().order_by('prix')
    # render(request, le html, les data a passer dans le html)
    return render(request, 'menu/index.html', {'pizzas': pizzas})



# envoie des données pizzas en format json pour une api
# une fois fait aller dans urls.py
def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)
