# Créé par Ordinateur, le 19/05/2018
from __future__ import division
from lycee import *
a,b= demande(" Entrez le coefficient directeur et l'ordonnée à l'origine")
x = np. arange (-10 , 10 , 0.1)
repere . plot(x, a*x+b)
