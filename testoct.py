# Créé par Ordinateur, le 24/06/2018
from __future__ import division
from lycee import *
def testoct(n,ok):
    n=texte_demande("Entrez un nombre")
    ok = True
    m=str(n)
    p = 0;
    while (((p<len(m))) and ok):
        ok = ok and ((m[p] in ("012345678")))
        p = p+1
    print ok