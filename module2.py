# Créé par Ordinateur, le 12/05/2018
from __future__ import division
from lycee import *
u,n, ecart=0,0,1
while ecart > puissance(10 ,-5) :
 u=u+1/ factorial(n)
 v=u+1/ factorial(n)
 print "u",n,"=",u," et v",n,"=",v
 ecart=v-u
 n=n+1
print "la limite de ( u_n) et ( v_n) vaut " ,u,"à 0. 00001 près"
