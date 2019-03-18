# -*- coding: utf-8 -*-
"""
Funktionen zur Berechnung und Veranschaulichung zur Prüfungsaufgaben DSV

hf(Null, Pol): Approximation des Amplitudengangs aus PN-Diagramm

falt(x, h): Berechnung und Darstellung der Faltung

stat(x1, x2, x3): Berechnung statistischer Kenngrößen für drei Messreihen
"""
import numpy as np
import matplotlib.pyplot as plt
def hf(Null, Pol):    
    """
    Darstellung des Betrages einer Übertragungsfunktion

    Eingabe: 
    -----
    Pole, Nullstellen (PN, zweidimensional)
    
    Beispiel: 
    
    Null = np.array([[N11, N12],[N21, N22], ...])
    
    Pol = np.array([[P11, P12],[P21, P22], ...])
    
    Aufruf:
    
    helpers.hf(Null, Pol)
    
    Ausgabe:
    -----
    Betrag der Übertragungsfunktion für 0 <= f <= fS/2

    Autor:
    ----- 
    Gudrun Flach
    
    last edited:
    -----
    Februar 2016
    """
    # Wertebereich (Punkte des Einheitskreises)
    x1 = np.linspace(1, -1, 100)
    x2 = np.sqrt(1-x1**2)
    z = np.array([x1,x2])
    # Pole und Nullstellen entsprechend erweitern
    null_r = Null[0][0]*np.ones(100)
    null_i = Null[0][1]*np.ones(100)
    nenner = 1
    zaehler = 1    

    for i in range(0, np.shape(Null)[1]):
        null_r = Null[i][0]*np.ones(100)
        null_i = Null[i][1]*np.ones(100)
        ns = np.array([null_r,null_i])
        abst_n = z - ns
        fak1 = np.sqrt(abst_n[0]**2 + abst_n[1]**2)
        zaehler = zaehler * fak1
    for i in range(0, np.shape(Pol)[1]):
        pol_r = Pol[i][0]*np.ones(100)
        pol_i = Pol[i][1]*np.ones(100)
        ps = np.array([pol_r,pol_i])
        abst_p = z - ps
        fak2 = np.sqrt(abst_p[0]**2 + abst_p[1]**2)
        nenner = nenner * fak2
    result = zaehler/nenner
    plt.plot(result)
    plt.grid(True)
    plt.xticks( np.arange(0,100,25), ('0', 'fS/8', 'fS/4', '3fS/8', 'fS/2') )

def falt(x,h):
#x = np.array([0,1,0,1])
#h = np.array([1, 0.5, 0.5, 0.125])

    y = np.convolve(x,h)
    plt.stem(y)
    plt.grid(True)
    plt.axis([-1, 7, -0.1, 1.6])
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.savefig('dsv_a2_15.jpg')

def stat(x1, x2, x3):
#x1 = np.array([2, 5, 1, 4, 3])
#x2 = np.array([5, 11, 3, 9, 7])
#x3 = np.array([6, 3, 2, 3, -4])

    x1_m = np.mean(x1)
    x2_m = np.mean(x2)
    x3_m = np.mean(x3)

    x1_v = np.var(x1)
    x2_v = np.var(x2)
    x3_v = np.var(x3)

    x_matrix = np.array([x1, x2, x3])
    x_cov = np.cov(x_matrix, bias = 1)
    x_cor = np.corrcoef(x_matrix)
    
def sig_stem(x, title='Titel', xlabel='xlabel', ylabel='ylabel'):
    plt.stem(x)
    plt.grid(True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axis([-1, len(x)+1, min(x)-0.1, max(x)+0.1])
    plt.savefig('dsv_a5-'+ title +'_15.jpg')
 
