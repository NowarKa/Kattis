# Créé par Ordinateur, le 01/04/2020
from __future__ import division
from lycee import *
j,m,a = demande("Entrez la date de naissance par jours mois et an separés par des virgules")
somme = 0
year = ""
if j>31 :
    print "Le jour ne peut pas etre plus grand que 31"
    exit()
    quit()
if m>12:
    print "il n'y a que 12 mois dans l'an"
    exit()
    quit()
if a>2020:
    print "la date maintenant est 1/4/2020"
    exit()
    quit()
for i in range(a+1,2020,1):
    if ( reste (i,4)==0 and reste (i, 100)<>0) or reste (i, 400 )==0:
        somme = somme + 366
    else:
        somme = somme + 365
if m==1 or 3 or 5 or 7 or 9 or 11:
    somme = somme + (31 - j)
elif m == 2:
    somme = somme + (28 - j)
else:
    somme = somme + (30 - j)
somme = somme + 30 * (12 - m)
somme = somme + 120
print somme,"jours"