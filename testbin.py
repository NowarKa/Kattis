# Créé par Ordinateur, le 24/06/2018
from __future__ import division
from lycee import *
n=texte_demande("Entrez un nombre binière")
ok = True
m=str(n)
p = 0;
while (((p<len(m))) and ok):
    ok = ok and ((m[p] in ("01")))
    p = p+1
print ok