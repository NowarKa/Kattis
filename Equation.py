# Créé par Ordinateur, le 23/03/2020
from __future__ import division
from lycee import *
x1,y1=demande("Entrez la coordination de le premier point separé par une virgule")
x2,y2=demande("Entrez la coordination de le deuxiéme point separé par une virgule")
if y1==y2 and x1==x2:
    print "il faut entrer deux point different"
    quit
if x1==x2:
    print "C'est pas une fonction car x prend une unique valeur y"
    quit
a = (y2-y1)/(x2-x1)
b = y1-(a*x1)
if a == 0:
    print "L'équation de la droite est: f(x)=",b
else:
    print "L'équation de la droite est: f(x)=",a,"x + ",b