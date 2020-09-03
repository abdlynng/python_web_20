from django.db import models

# Create your models here.
class Personne(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    
    class Meta:
        abstract = True


class Conducteur(Personne):
    nbre_place = models.IntegerField()

    
class Passager(Personne):
    pass


class Trajet(models.Model):
    depart = models.CharField(max_length=10)
    arrive = models.CharField(max_length=10)
    prix = models.PositiveIntegerField(default=4000)
    
    passagers = models.ManyToManyField(Passager)
    conducteur = models.ForeignKey(Conducteur,on_delete=models.CASCADE)
