# Créé par Ordinateur, le 28/05/2018
from __future__ import division
from lycee import *
a,b,c=demande("Entrez a,b et c")
x=np.arange(-10,10,0.1)
repere.plot(x,a*puissance(x,2)+b*x+c)
repere.show()