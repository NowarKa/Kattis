# Créé par Ordinateur, le 24/06/2018
from __future__ import division
from lycee import *
n=texte_demande("Entrez un nombre")
ok = True
m=str(n)
p = 0;
while (((p<len(m))) and ok):
    ok = ok and ((m[p] in ("0123456789ABCDEF")))
    p = p+1
print ok