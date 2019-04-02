# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:34:47 2016

@author: Admin_1

Funktionen:
sprung, rampe, exponent, gauss, impulsfolge, oszi_simple, 
exp_oszi, plot_signal, plot_sigfolge
"""


import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, subplot
import numpy as np
from pylab import *

def sprung(shift=0, cs_x = 1, cs_y = 1, mirr = 1):
    """
    Berechnung von Werten der Sprungfunktion für -10<=n<=10
    Parameter: 
        shift - Verschiebung (default 0)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = int(-10/cs_x)
    nmax = int(10/cs_x)
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(nmin, nmax, nanz, dtype=int):
        if np.sign(i-shift)<0:
            s_n[i+int((nanz-1)/2)] = 0
        else:
            s_n[i+int((nanz-1)/2)] = cs_y*1
    if shift == 0:
        typ = 'sprung'
    else:
        typ = 'sprung_shift'

    if mirr == -1:
        s_n = s_n[::-1]
    return s_n, typ        

    
def rampe(shift=0, cs_x = 1, cs_y = 1, mirr = 1):
    """
    Berechnung von Werten der Rampenfunktion für -10<=n<=10
    Parameter: 
        shift - Verschiebung (default 0)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = int(-10/cs_x)
    nmax = int(10/cs_x)
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(nmin, nmax, nanz, dtype=int):
        if np.sign(i-shift) < 0:
            s_n[i+int((nanz-1)/2)] = 0
        else:
            s_n[i+int((nanz-1)/2)] = cs_y*(i-shift)
    if shift == 0:
        typ = 'rampe'
    else:
        typ = 'rampe_shift'
        
    if mirr == -1:
        s_n = s_n[::-1]

    return s_n, typ       

def exponent(type=1, a=1, cs_x = 1, cs_y = 1, mirr = 1):
    """
    Berechnung von Werten der Exponentialfunktion für -10<=n<=10
    Parameter: 
        type=1 - einseitige Exponentialfunktion (default)
        type=2 - zweiseitige Exponentialfunktion
        a (default 1)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = int(-10/cs_x)
    nmax = int(10/cs_x)
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(nmin, nmax, nanz, dtype=int):
        if type == 1:
            if np.sign(i)<0:
                s_n[i+int((nanz-1)/2)] = 0
            else:
                s_n[i+int((nanz-1)/2)] = cs_y*a**i
            typ = 'exp1'
        else:
            s_n[i+int((nanz-1)/2)] = cs_y*a**abs(i)
            typ = 'exp2'

    if mirr == -1:
        s_n = s_n[::-1]

    return s_n, typ       

def gauss(a=1):
    """
    Berechnung von Werten der Gaussfunktion für -10<=n<=10
    Parameter: 
        a  (default 1)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    s_n = np.zeros(21)
    for i in np.linspace(-10,10, 21, dtype=int):
        s_n[i+10] = exp(-a*i**2)
    typ = 'gauss'
    return s_n, typ       

def impulsfolge(periode=1):
    """
    Berechnung von Werten der Impulsfolge für -10<=n<=10
    Parameter: 
        periode  (default 1)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    n = np.linspace(-10,10, 21, dtype=int)
    data = np.zeros(21)
    for i in range(0,len(n)//(2*periode)+1):
        data[10-i*periode]=1
        data[10+i*periode]=1
    typ = 'if'
    return data, typ
            
def oszi_simple():
    """
    Berechnung von Werten des einfachsten oszillierenden Signals für -10<=n<=10
    Parameter: 
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    n = np.linspace(-10,10, 21, dtype=int)
    data = np.zeros(21)
    for i in range(0,len(n)):
        data[i]=(-1)**i
    typ = 'oszi_s'
    return data, typ

def exp_oszi(theta_fak=1, cs_x = 1, cs_y = 1, mirr = 1):
    """
    Berechnung von Werten der komplexen Exponentialschwingung für -10<=n<=10
    Parameter: 
        theta_fak  (default 1) - Faktor für 2*pi
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = int(-10/cs_x)
    nmax = int(10/cs_x)
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    n = np.linspace(nmin, nmax, nanz, dtype=int)
    data = np.zeros(nanz,dtype=complex)
    theta_0=2*np.pi*theta_fak
    for i in range(0,len(n)//2+1):
        data[int((nanz-1)/2)-i]=cs_y*exp(1j*theta_0*i)
        data[int((nanz-1)/2)+i]=cs_y*exp(1j*theta_0*i)
    typ = 'exp_oszi'

    if mirr == -1:
        data = data[::-1]
        
    return data, typ
    
        
def plot_signal(data=[], sig_typ=''):
    """
    Darstellung von Signalfunktionen für -10<=n<=10
    Parameter: 
        data  - Datenfeld
        sig_typ - Funktionstyp
    Rückgabe:
    """
    
    n = np.linspace(-(int(len(data-1)/2)), (int(len(data-1)/2)), len(data), dtype=int)
    stem(n, data)
    axis([-(int(len(data-1)/2)), (int(len(data-1)/2)), min(data)-1, max(data)+1])
    grid(True)
    if sig_typ == 'sprung':
        title('Ausschnitt aus Sprungfunktion')
    if sig_typ == 'sprung_shift':
        title('Ausschnitt aus verschobener Sprungfunktion')
    if sig_typ == 'rampe':
        title('Ausschnitt aus Rampenfunktion')
    if sig_typ == 'rampe_shift':
        title('Ausschnitt aus verschobener Rampenfunktion')
    if sig_typ == 'exp1':
        title('Ausschnitt aus einseitiger Exponentialfunktion')
    if sig_typ == 'exp2':
        title('Ausschnitt aus zweiseitiger Exponentialfunktion')
    if sig_typ == 'gauss':
        title('Ausschnitt aus Gaussfunktion')
    if sig_typ == 'if':
        title('Ausschnitt aus Impulsfolge')
    if sig_typ == 'oszi_s':
        title('Ausschnitt aus einfachstem oszillierenden Signal')
    if sig_typ == 'exp_oszi':
        title('Ausschnitt aus komplexer Exponentialschwingung')
    xlabel('n')
    ylabel('x(n)')
    plt.show()
    
def plot_sigfolge(data=[], mytitle=''):
    """
    Darstellung von Signalfunktionen für -10<=n<=10
    Parameter: 
        data  - Datenfeld
        mytitle (default '') - Titel für Darstellung
    Rückgabe:
    """
    n = np.linspace(-10,10, 21, dtype=int)
    stem(n, data)
    grid(True)
    axis([-10, 10, min(data)-1, max(data)+1])
    title(mytitle)
    xlabel('n')
    ylabel('x(n)')
    plt.show()
    


