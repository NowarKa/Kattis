# Créé par Ordinateur, le 23/03/2020
from __future__ import division
from lycee import *
print "Ce programme trouve tous les nombres(de -100 à 100 dans Z) dont leur somme égale à leur multiple"
for i in range(-100,98,1):
    n = i+1;
    m = i+2;
    if m*n*i==m+n+i:
        print m,"*",n,"*",i,"=",m,"+",n,"+",i,"  (",i,",",n,",",m,")"