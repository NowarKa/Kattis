# Créé par Ordinateur, le 24/06/2018
from __future__ import division
from lycee import *
n = texte_demande("Entrez un nombre")
A,B,C,D,E,F = 10,11,12,13,14,15
decnum = 0
ok = True
m=str(n)
p = 0;
while (((p<len(m))) and ok):
    ok = ok and ((m[p] in ("0123456789ABCDEF")))
    p = p+1
if ok == True :
    for i in range (0,len(n)):
        k=(eval(n[i]))*puissance(16,len(num)-i-1)
        decnum = decnum + k
    print decnum
else:
    exit