# Créé par Ordinateur, le 23/06/2018
from __future__ import division
from lycee import *
n=demande("Entrez un nombre binière")
m=n
bina=""
bina2=""
while n>0:
    r=reste(n,2)
    bina=bina+str(r)
    n=quotient(n,2)
p= len( bina )-1
while p >=0:
    bina2=bina2+(bina [p])
    p=p-1
print m,"s'écrit ",bina2,"en base 2"