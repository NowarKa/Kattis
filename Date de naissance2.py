#Créé par Ordinateur, le 31/05/2018
from __future__ import division
from lycee import *
j1,m1=demande("Entrez la date de naissance 1")
j2,m2=demande("Entrez la date de naissance 2")
mois=[" Janvier" ," Février"," Mars"," Avril"," Mai"," Juin"," Juillet"," Août" ," Septembre"," Octobre","Novembre","Décembre"]
jours=[31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
print "Date 1: tu es né(e) en",j1, mois[m1-1]
print "Date 2: tu es né(e) en",j2, mois[m2-1]
if m1==m2:
    sumk=j1-j2
else:
    if m2>m1:
     mdiff=m2-m1-1;
     sumk = jours[m1-1]-j1+j2;
     for k in range(m1,m2-1):
      sumk=sumk+jours[k];
      print k,sumk
print sumk