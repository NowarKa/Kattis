# Créé par Ordinateur, le 01/08/2018
from __future__ import division
from lycee import *
def pascale (n):
    listeA = [1,1]
    listeB = [1]
    for l in range(1,n):
        for i in range (1,len(listeA)):
            m = listeA[i] + listeA[i-1]
            listeB.append(m)
        listeB.append(1)
        listeA = listeB[:]
        listeB = [1]
    print listeA