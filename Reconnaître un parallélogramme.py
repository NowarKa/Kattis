# Créé par Ordinateur, le 09/06/2018
from __future__ import division
from lycee import *
a=texte_demande('Entrez le nom du quadrilatère')
quad=liste_demande('Entrez les coordonnés des points')
if quad[2]- quad[0 ]== quad[4]- quad[6] and quad[3]-quad[1]== quad[5]-quad[7]:
 print "Le quadrilatère ",a," est un parallélogramme."
else:
 print " Le quadrilatère ",a," n 'est pas un parallélogramme."
#repere.clf()
repere.plot(quad[0],quad[1],'go')
repere.plot(quad[2],quad[3],'go')
repere.plot(quad[4],quad[5],'go')
repere.plot(quad[6],quad[7],'go')
repere.show()
repere.axis([0,10,0,10])