# Créé par Ordinateur, le 15/07/2018
from __future__ import division
from lycee import *
A= liste_demande('entrez les coefficients de A(x) par ordre des puissances croissantes')
B= liste_demande('entrez les coefficients de B(x) par ordre des puissances croissantes')
C=[]
i=0
lenA,lenB = len(A),len(B)
sumB,sumA = lenB,lenA
if lenA < lenB :
    while i < lenA:
        sumC = A[i] + B[i]
        C.append(sumC)
        i=i+1
    while sumB < lenB+(lenB-lenA):
        C.append(B[sumB-lenA])
        sumB=sumB+1
else:
    while i < lenB :
        sumC = A[i] + B[i]
        C.append(sumC)
        i=i+1
    while sumA < lenA+(lenA-lenB):
        C.append(A[sumA-lenB])
        sumA=sumA+1
print affiche_poly(A),'+',affiche_poly(B),'=',affiche_poly(C)