# Créé par Ordinateur, le 20/07/2018
from __future__ import division
from lycee import *
liste = []
liste3 = []
n,n2 = demande("Entrez un nombre")
for i in range (1,n+1):
    m = reste(n,i)
    if m == 0 :
        liste.append(i)
    if n in liste :
        liste.remove(n)
    if 1 in liste :
        liste.remove(1)
if liste == [] :
    print "le nombre",n,"est un nombre premier"
else :
    print "le nombre",n,"n'est pas un nombre premier"
    liste.append(1)
    liste.append(n)
    print liste
liste2 = []
for i in range (1,n2+1):
    m = reste(n2,i)
    if m == 0 :
        liste2.append(i)
    if n2 in liste2 :
        liste2.remove(n2)
    if 1 in liste2 :
        liste2.remove(1)
if liste2 == [] :
    print "le nombre",n2,"est un nombre premier"
else :
    print "le nombre",n2,"n'est pas un nombre premier"
    liste2.append(1)
    liste2.append(n2)
    print liste2
if len(liste)>len(liste2) :
    for i in range (0,len(liste)):
        if liste[i] in liste2:
            liste3.append(liste[i])
else :
    for i in range (0,len(liste2)):
        if liste2[i] in liste:
            liste3.append(liste2[i])
liste3.append(1)
print liste3
for i in range (0,len(liste3)-1):
    if liste3[i]>liste3[i+1]:
        max = liste3[i]
print max