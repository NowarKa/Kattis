# Créé par Ordinateur, le 10/04/2020
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
Rargent = argent
x = 0
while Rargent > 1 and x < 10 :
    if Rargent == 10*argent:
        print "Vous avez gagné 10 fois de la somme mise au départ"
        quit()
    else:
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
            Rargent = 3 * Rargent
            print "C'est vrai ! votre somme maintenant est: ",Rargent
        elif tn == tvn :
            Rargent = Rargent + 0.5 * Rargent
            print "Les deux nombre sont",tn,"votre somme maintenant est: ",Rargent
        else:
            Rargent = int(0.5*Rargent)
            if Rargent > 0:
                print "C'est faux votre somme maintenant est: ",Rargent
            else :
                print "C'est faux votre somme maintenant est : 0"
        x = x + 1
if Rargent <= 1 :
    print "désolé , vous avez perdu tous vos argent"
elif x == 10 :
    print "Vous avez joué 10 fois "