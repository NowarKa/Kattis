# Créé par Ordinateur, le 08/04/2020
from __future__ import division
from lycee import *
mot = ["j","e","u"]
print ("ici un mot qui contenu ",len(mot)," lettres")
print ("il faut deviner ce mot vous avez trois essaies")
ch = ""
x = 0
while x < 3:
    ch = texte_demande("devinez la 1ére lettre")
    if ch == "j":
        print ("Bravo! vous avez devinés la 1ére lettre ")
        while x < 3 :
            ch = texte_demande("devinez la 2éme lettre")
            if ch == "e":
                print ("Bravo! vous avez devinés la 2éme lettre ")
                while x < 3 :
                    ch = texte_demande("devinez la 3éme lettre")
                    if ch == "u":
                        print ("Bravo! vous avez devinés la 3éme lettre ")
                        print ("vous avez gagné ! le mot est jeu")
                        quit()
                    else:
                        print("Désolé , ce n'est pas la vrai lettre")
                        x = x + 1
            else:
                print("Désolé , ce n'est pas la vrai lettre")
                x = x + 1
    else:
        print("Désolé , ce n'est pas la vrai lettre")
        x = x + 1
if x==3 :
    print ("vous avez perdu! le mot est jeu")