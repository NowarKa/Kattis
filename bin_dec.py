# Créé par Ordinateur, le 24/06/2018
from __future__ import division
from lycee import *
n=texte_demande("Entrez un nombre binière ")
ok = True
m=str(n)
p = 0;
while (((p<len(m))) and ok):
    ok = ok and ((m[p] in ("01")))
    p = p+1
if ok == True :
    base = 2
    num = str(n)
    dec=0
    for i in range (0,len(num)):
        k=(eval(num[i]))*puissance(base,len(num)-i-1)
        dec=dec+k
    print dec
else:
    exit
    print "le nombre",n,"n'est pas un nombre binière"