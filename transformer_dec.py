# Créé par Ordinateur, le 23/06/2018
from __future__ import division
from lycee import *
n=demande("Entrez un nombre")
base = 2
num = str(n)
dec=0
for i in range (0,len(num)):
    k=(eval(num[i]))*puissance(base,len(num)-i-1)
    dec=dec+k
print dec