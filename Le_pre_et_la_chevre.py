# Créé par Ordinateur, le 30/06/2018
from __future__ import division
from lycee import *
def corde (x):
    if x<5:
        Aire=pi*x*x/2
    elif x<10:
        AngleAEF= acos(5/x)
        AngleFEG=180 -2* AngleAEF
        Aire=5* sqrt(x*x-5*5)+pi*x*x/360* AngleFEG
    elif x < sqrt(125):
        unite_angle('rad')
        Aire = 5*sqrt(x*x-25)+10*sqrt(x*x-100)+x*x*((pi/2)-(acos(10/x))-(acos(5/x)))
    else:
        Aire = 100
    print Aire