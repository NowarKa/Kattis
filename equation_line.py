# Créé par Ordinateur, le 09/06/2018
from __future__ import division
from lycee import *
repere.clf()
x=np.arange(-10,10,0.1)
x1,y1,x2,y2=demande('Entrez le coordonné de deux point')
if x2==x1:
    n==x1
    for v in range (-10,10,0.1):
      repere.plot(n,v)
    print "y=",n
else:
    a=(y1-y2)/(x1-x2)
    a=abs(a)
    b=y1-a*x1
    repere.plot(x,a*x+b)
    if a==0 :
        print "x=",b
    elif a==1:
        print "x+",b
    else:
        print a,"*x","+", b
repere.show()