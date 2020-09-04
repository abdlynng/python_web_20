from django.shortcuts import render
from django.http import HttpResponse
from .models import Trajet
from .models import  Conducteur
from .models import  Passager

from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse("COVOITURAGE URBAINE Welcome")

def trajet(request, pk):
    t = Trajet.objects.get(id=pk)
    c = Conducteur.objects.get(id=t.id)
    p = []
    p.append(t.depart)
    p.append(t.arrive)
    p.append(str(t.prix))
    p.append(c.prenom)
    p.append(c.nom)
    m = ' | '.join(p)
    #p = t.depart +" | "+ t.arrive +" | "+str(t.prix) +" | "+ c.prenom+" | "+ c.nom +" |"
    return HttpResponse(m)


def conducteur(request,pk):
    c = Conducteur.objects.get(id=pk)
    p = c.prenom +" | "+ c.nom +" | "+str(c.nbre_place) +" | "
    return HttpResponse(p)