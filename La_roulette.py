# Créé par Ordinateur, le 08/04/2020
from __future__ import division
from lycee import *
print "maintenant , on veut jouer la rollette ! Voici les règle :"
print "1) on choisi un nombre entre 0 et 50"
print "2) il faut deviner ce nombre"
print "3) si vous avez deviné le meme nombre vous recevez le triple de votre somme d'argent précédente"
print "4) si les deux nombres ont pair ou impair vous recevez 50% plus sur votre somme d'argent précédente"
print "5) sinon vous perd 500 de votre somme d'argent précédente"
print "6) le jeu se termine quand vous perd tous votre argent"
argent = int(input("Entrez la somme de votre argent"))
if argent <= 0 :
    print "Vous ne pouvez pas avec cette somme d'argent"
    quit()
while argent > 0 :
    n = randint(0,50)
    vn = int(input("Devinez le nombre!"))
    if vn < 0:
        print "il faut choisir un nombre entre 0 et 50"
        quit()
    elif vn > 50 :
        print "il faut choisir un nombre entre 0 et 50"
        quit()
    if reste(n,2)==0 :
        tn = "pair"
    else:
        tn = "impair"
    if reste(vn,2)==0 :
        tvn = "pair"
    else:
        tvn = "impair"
    if n == vn :
        argent = 3 * argent
        print "C'est vrai ! votre somme maintenant est: ",argent
    elif tn == tvn :
        argent = argent + 0.5 * argent
        print "Les deux nombre sont",tn,"votre somme maintenant est: ",argent
    else:
        argent = argent - 500
        if argent > 0:
            print "C'est faux votre somme maintenant est: ",argent
        else :
            print "C'est faux votre somme maintenant est : 0"
print "désolé , vous avez perdu"