# Créé par Ordinateur, le 10/06/2018
from __future__ import division
from lycee import *
N= demande(" Obtenir les nombres premiers inférieurs à ?")
indice =0
liste = range(2,N)
while indice < len( liste ):
   nombre = liste[ indice ]
   n=2
   while n*nombre <N:
       multiple=n* nombre
       if multiple in liste :
           liste . remove ( multiple)
       n=n+1
   indice = indice +1
print liste