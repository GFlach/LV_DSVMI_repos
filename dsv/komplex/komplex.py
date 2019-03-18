# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:24:01 2016

Funktionen zur Verarbeitung und Darstellung komplexer Zahlen

plot_cplx_plane - Darstellung der komplexen Ebene

plot_cplx_number - Darstellung von komplexen Zahlen in der komplexen Ebene

@author: Admin_1

@date: 19.03.2016
"""
# import numpy as np
# from pylab import *


import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, subplot
from time import strftime

def plot_cplx_plane(limits=[-5,5,-5,5]):
    """
    Darstellung der komplexen Ebene
    Parameter: 
        limits - Grenzen (default [-5,5,-5,5])
    Rückgabe:
        fig - Figurobjekt
    """
    plt.figure(figsize=(10,10))
    plt.hold(True)
    # erzeugt neue Figur
    fig=plt.figure(1)
    #setzt die Größe der Figur
    plt.axis(limits)
    hw=(limits[1]-limits[0])/100
    hl=(limits[1]-limits[0])/50
    # Auswahl einer Teilfigur (111 ... ganze Figur)
    ax=fig.add_subplot(1,1,1)

    # Einheitskreis erzeugen
    circ=plt.Circle((0,0), radius=1, color='b', fill=False, ls='dashed')
    # Achsenpfeile erzeugen
    a1 = plt.arrow(limits[0], 0, 2*limits[1], 0, length_includes_head=True, head_width=hw, head_length=hl, fc='k', ec='k')
    a2 = plt.arrow(0, limits[2], 0, 2*limits[3], length_includes_head=True, head_width=hw, head_length=hl, fc='k', ec='k')

    # Objekte in Figur einbauen  
    ax.add_patch(circ)
    ax.add_patch(a1)
    ax.add_patch(a2)

    # Gitternetz und Beschriftung
    ax.grid()
    ax.set_title('Komplexe Ebene')
    ax.set_xlabel('Realteil')
    ax.set_ylabel('j*Imaginärteil')

    #Figur darstellen
    #plt.show()
    return fig

def plot_cplx_number(data=[], limits=[-5,5,-5,5]):
    """
    Darstellung von komplexen Zahlen in der komplexen Ebene
    Aufruf:
        plot_cplx_number(data=[], limits=[-5,5,-5,5])
    Parameter: 
        data - Liste der darzustellenden komplexen Zahlen
        limits - Grenzen (default [-5,5,-5,5])
    Rückgabe:
        keine
        Abbildung wird in C:\\WinPython\\notebooks\\image unter cn_+Zeitstempel
        gespeichert
    """
    # Erzeugen einer komplexen Ebene
    fig = plot_cplx_plane(limits)
    # angepasste Werte für Pfeilspitzen und Zeigerbeschriftung ermitten
    hw=(limits[1]-limits[0])/100
    hl=(limits[1]-limits[0])/50
    offset = (limits[1]-limits[0])/40
    # Verabeitung aller komplexen Zahlen der Eingabeliste
    for k in range(0, len(data)):
        cn_real = data[k].real
        cn_imag = data[k].imag
        if (abs(cn_real)+abs(cn_imag) != 0):
            cn = plt.arrow(0, 0, cn_real, cn_imag, length_includes_head=True, head_width=hw, head_length=hl, fc='r', ec='r', ls='dotted')
            ax=fig.add_subplot(1,1,1)
            ax.add_patch(cn)
            ax.annotate('z_%s'%(k+1), xy=(cn_real/2, cn_imag/2), xytext=(cn_real/2+offset, cn_imag/2))
    # Speichern der Abbildung
    plt.savefig('C:\\WinPython\\notebooks\\image\\cn'+strftime("%Y-%m-%d_%H-%M")+'.jpg')
    plt.show()
