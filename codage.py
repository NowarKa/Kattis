# Créé par Ordinateur, le 22/06/2018
from __future__ import division
from lycee import *
phrase2=""
phrase ="Coucou ,il, Sarah, fait beau"
p= len( phrase )-1
while p >=0:
    if (ord(phrase[p])==32) or ((ord(phrase[p])>64) and (ord(phrase[p])<91)) or ((ord(phrase[p])>96) and (ord(phrase[p])<123)):
        phrase2=phrase2+(phrase [p])
        p=p-1
    else:
        p=p-1
phrase2=phrase2.lower()
phrase2=phrase2.capitalize()
print phrase
print phrase2