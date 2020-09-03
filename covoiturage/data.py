#-*-coding: utf-8-*-
from models import *
import sqlite3
import sqlobject as so

mabase = "db.sqlite3"

db = sqlite3.connect(mabase)

connexion = so.connectionForURI("sqlite:"+ mabase)
so.sqlhub.processConnection = connexion
connexion.debug = True

print ("connexion reussi a la base reussi")
#db_cursor = db.cursor()

"""
#=========================================================================
# creation des classes qui vont donner les tables 

class Personne(so.SQLObject):
    prenom = so.StringCol()
    nom = so.StringCol()
    
class Conducteur (Personne):
    nbre_places = so.IntCol()
    trajet = so.MultipleJoin("Trajet")
    
class Passager(Personne):
    pass

class Trajet(so.SQLObject):
    depart = so.StringCol()
    arrive = so.StringCol()
    prix = so.IntCol()
    conducteur = so.ForeignKey("Conducteur",cascade="null")

class Constituer(so.SQLObject):
    trajet = so.ForeignKey("Trajet")
    passager = so.ForeignKey("Passager")       

#=====================FIN de la creation ======================================
    
def creation_table():
    Conducteur.createTable(ifNotExists=True)
    Passager.createTable(ifNotExists=True)
    Trajet.createTable(ifNotExists=True)
    Constituer.createTable(ifNotExists=True)

def supprimer_table():
    if Conducteur.tableExists == True:
        Conducteur.dropTable()
    if Passager.tableExists == True:
        Passager.dropTable()
    if Trajet.tableExists == True:
        Trajet.dropTable()
    if Constituer.tableExists == True:
        Constituer.dropTable()


supprimer_table()
creation_table()
"""
#===============insertion des datas dans la base ==============================================

pas1 = Passager(id = 1, nom = "Sarr", prenom = "Atou")
pas2 = Passager(nom = "Mbaye", prenom = "Birima")
pas3 = Passager(nom = "Gaye", prenom = "Soda")
pas4 = Passager(nom = "Dibo", prenom = "ibou")
pas5 = Passager(nom = "Traore", prenom = "Issa")
pas6 = Passager(nom = "Gadiaga", prenom = "Mouhamet ben Abdou")
pas7 = Passager(nom = "Thiam", prenom = "Amadou")
pas8 = Passager(nom = "Diouf", prenom = "Pape Modou")
pas9 = Passager(nom = "Dia", prenom = "Papa ")
pas10 = Passager(nom = "Beye", prenom = "Mariama")
pas11 = Passager(nom = "Ndiaye", prenom = "Alima")

# donnees de la table conducteur 
c1 = Conducteur(nom="Mendy", prenom = "Jacques", nbre_places = 7)
c2 = Conducteur(nom = "Diop", prenom = "Isseu", nbre_places = 4)
c3 = Conducteur(nom = "Fall", prenom = "Balla", nbre_places = 9)

# donnees de la table trajet 
t1 = Trajet(depart = "10h00", arrive = "12h00", prix = 4000, conducteur = c2.id)
t2 = Trajet(depart = "11h30", arrive = "13h30", prix = 3000, conducteur = c1.id)
t3 = Trajet(depart = "17h00", arrive = "19h20", prix = 5000, conducteur = c3.id)


Constituer(trajet = t1.id, passager = pas1.id)
Constituer(trajet = t1.id, passager = pas4.id)
Constituer(trajet = t1.id, passager = pas8.id)
Constituer(trajet = t1.id, passager = pas5.id)
Constituer(trajet = t1.id, passager = pas10.id)

Constituer(trajet = t2.id, passager = pas9.id)
Constituer(trajet = t2.id, passager = pas7.id)
Constituer(trajet = t2.id, passager = pas11.id)
Constituer(trajet = t2.id, passager = pas6.id)

Constituer(trajet = t3.id, passager = pas1.id)
Constituer(trajet = t3.id, passager = pas4.id)
Constituer(trajet = t3.id, passager = pas3.id)
Constituer(trajet = t3.id, passager = pas11.id)
Constituer(trajet = t3.id, passager = pas7.id)
