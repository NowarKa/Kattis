# Créé par Ordinateur, le 16/07/2018
from __future__ import division
from lycee import *
N1,M1 = demande("Entrez un nombre ")
N2,M2 = demande("Entrez un nombre ")
if M1 == M2 :
    somme = N1+N2
    print N1,"/",M1,"+",N2,"/",M2,"=",somme,"/",M1
elif M1 == 0 or M2 == 0:
    exit
elif M2 == N2 :
    somme = N1 + M1
    print N1,"/",M1,"+",N2,"/",M2,"=",somme,"/",M1
elif M1 == N1 :
    somme = N2 + M2
    print N1,"/",M1,"+",N2,"/",M2,"=",somme,"/",M2
else :
    pg = pgcd(M1,M2)
    if pg == 1 :
        comN1 = N1 * M2
        comN2 = N2 * M1
        comM = M1 * M2
        somme = comN1 + comN2
        print N1,"/",M1,"+",N2,"/",M2,"=",somme,"/",comM
    else :
        comN1,comN2 = N1/quotient(M1,pg),N2/quotient(M2,pg)
        somme = comN1 + comN2
        print N1,"/",M1,"+",N2,"/",M2,"=",somme,"/",pg
        if str(somme) is not int :
            comN1 = N1 * M2
            comN2 = N2 * M1
            comM = M1 * M2
            somme = comN1 + comN2
            pg = pgcd(somme,comM)
            somme = somme/pg
            comM = comM/pg
            print N1,"/",M1,"+",N2,"/",M2,"=",int(somme),"/",int(comM)