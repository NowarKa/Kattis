# Créé par Nowar , le 24/06/2018
from __future__ import division
from lycee import *
base = texte_demande("quelle base?")
if eval(base) == 16 :
    n= demande(" Entrez n < 256")
    hexa=""
    c= quotient(n,16)
    for i in range(2):
            if c<10 :
                 hexa= hexa+ str(c)
            elif c==10 :
                hexa= hexa+"A"
            elif c==11 :
                hexa= hexa+"B"
            elif c==12 :
                hexa= hexa+"C"
            elif c==13 :
                hexa= hexa+"D"
            elif c==14 :
                hexa= hexa+"E"
            elif c==15 :
                hexa= hexa+"F"
            c= reste (n,16)
    print n,"s'écrit ",hexa ,"en base 16"
elif eval(base) == 2:
        n=demande("Entrez un nombre ")
        m=n
        bina=""
        bina2=""
        while n>0:
            r=reste(n,2)
            bina=bina+str(r)
            n=quotient(n,2)
        p= len( bina )-1
        while p >=0:
            bina2=bina2+(bina [p])
            p=p-1
        print m,"s'écrit ",bina2,"en base 2"
elif eval(base) == 8:
        n=demande("Entrez un nombre")
        m=n
        octa=""
        octa2=""
        while n>0:
            r=reste(n,8)
            octa=octa+str(r)
            n=quotient(n,8)
        p= len( octa )-1
        while p >=0:
            octa2=octa2+(octa [p])
            p=p-1
        print m,"s'écrit ",octa2,"en base 8"
else :
        exit
        print "il n'y a pas une base",base