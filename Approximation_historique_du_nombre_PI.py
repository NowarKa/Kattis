# Créé par Ordinateur, le 01/07/2018
from __future__ import division
from lycee import *
err=22/7-pi
print " erreur historique",err
for d in range(1, 100):
    for n in range (3*d,4*d):
        f=n/d
        e = abs(pi -f)
        if e< err :
            err=e
            print "J'ai trouvé mieux :",n,"/",d," L 'erreur est :",err