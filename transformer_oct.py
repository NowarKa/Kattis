# Créé par Ordinateur, le 23/06/2018
from __future__ import division
from lycee import *
n=demande("Entrez un nombre")
m=n
octa=""
octa2=""
while n>0:
    r=reste(n,8)
    octa=octa+str(r)
    n=quotient(n,8)
p= len( octa )-1
while p >=0:
    octa2=octa2+(octa [p])
    p=p-1
print m,"s'écrit ",octa2,"en base 8"