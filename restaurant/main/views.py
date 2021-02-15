from django.http import HttpResponse
from django.shortcuts import render
from .models import IdentityStore

# Create your views here.

def index(request):
    # /main
    identity = IdentityStore.objects.all()
    # render(request, le html, les data a passer dans le html)
    return render(request, 'main/index.html', {'identity': identity})
    # return HttpResponse("home")
