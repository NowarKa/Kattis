# Créé par Ordinateur, le 20/06/2018
from __future__ import division
from lycee import *
repere.clf()
De1=[1,2,2,3,3,4]
De2=[1,3,4,5,6,8]
L1 =[]; L2 =[]
for i in range( 10000 ):
    L1. append ( randint(1,6)+ randint(1,6))
    L2. append ( De1[ randint(0,5)]+ De2[ randint(0,5 )])
X1,F1= compte (L1 ,'frequence')
repere . plot(X1,F1,'bo ')
X,F= compte (L2 ,'frequence')
repere . plot(X,F,'rx ')
repere.show()
a=mediane(L1)
b=mediane(X1,F1)
n=moyenne(L1)
m=moyenne(X1,F1)
print m,n
print a,b
print '_________________'
a=mediane(L2)
b=mediane(X,F)
n=moyenne(L2)
m=moyenne(X,F)
d1=quartile(X,F,1)
d2=quartile(X,F,2)
print m,n
print a,b
print '_________________'
print d1,d2