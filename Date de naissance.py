#Créé par Ordinateur, le 31/05/2018
from __future__ import division
from lycee import *
j1,m1,y1=demande("Entrez la date de naissance 1")
j2,m2,y2=demande("Entrez la date de naissance 2")
mois=[" Janvier" ," Février"," Mars"," Avril"," Mai"," Juin"," Juillet"," Août" ," Septembre"," Octobre","Novembre","Décembre"]
jours=[31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
print "Date 1: tu es né(e) en",j1, mois[m1-1],y1
print "Date 2: tu es né(e) en",j2, mois[m2-1],y2
if y1==y2:
    ydiff==0
else:
    ydiff=y1-y2
ydiff=ydiff*365
ydiff=abs(ydiff)
if m1==m2:
    sumk=j1-j2
else:
    mdiff=m2-m1;
    sumk = -j1+j2;
    for k in range(1,mdiff):
     sumk=sumk+jours[k]
sumk=sumk+ydiff
abs(sumk)
print sumk