# Créé par Ordinateur, le 23/06/2018
from __future__ import division
from lycee import *
n= demande(" Entrez n < 256")
alphabet=" 0123456789ABCDEF"
q= quotient(n,16)
r= reste (n,16)
hexa= alphabet[q]+ alphabet[r]
print n,"s 'écrit" ,hexa ,"en base 16"