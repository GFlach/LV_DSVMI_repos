# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:03:20 2016

@author: Flach
"""

from pylab import *
from random import gauss,triangular

def generate_signals(nx,ny,nz):
    X = []
    Y = []
    Z = []
    for i in range(nx):
        X.append(round(gauss(0,1)*100))

    for i in range(ny):
        Y.append(round(triangular(-0.5,0.5)*100))
        

    for i in range(nz):
        Z.append(round(uniform(-100,100)))

    return(X,Y,Z)

