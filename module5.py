# Créé par Ordinateur, le 27/04/2018
from __future__ import division
from lycee import *
a=demande("Entrez A")
b=demande("Entrez B")
if b<0:
  print "x=",sqrt(-b/a)
else:
    print "il faut que B doit etre un nombre négatif"