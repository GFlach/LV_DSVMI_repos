# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, subplot
from time import strftime
import cmath
import numpy as np
from PIL import Image

def plot_plane(handle, amp = 1):
    """
    Darstellung der Zeigerebene
    Parameter: 
        amp - maximale Amplitude (default 1)
        handle - Handle des Ausgabefensters
    Rückgabe:
        fig - Figurobjekt
    """
    #plt.figure(figsize=(6,6))
    #plt.hold(True)
    # erzeugt neue Figur
    #fig=plt.figure(1)
    #setzt die Größe der Figur
    limits = [-amp,amp,-amp,amp]
    handle.axis(limits)
    hw=(limits[1]-limits[0])/100
    hl=(limits[1]-limits[0])/50
    # Auswahl einer Teilfigur (111 ... ganze Figur)
    #ax=fig.add_subplot(1,1,1)

    # Einheitskreis erzeugen
    circ=plt.Circle((0,0), radius=amp, color='b', fill=False, ls='dashed')
    # Achsenpfeile erzeugen
    a1 = handle.arrow(limits[0], 0, 2*limits[1], 0, length_includes_head=True, head_width=hw, head_length=hl, fc='k', ec='k')
    a2 = handle.arrow(0, limits[2], 0, 2*limits[3], length_includes_head=True, head_width=hw, head_length=hl, fc='k', ec='k')

    # Objekte in Figur einbauen  
    #ax.add_patch(circ)
    #ax.add_patch(a1)
    #ax.add_patch(a2)
    handle.add_patch(circ)
    handle.add_patch(a1)
    handle.add_patch(a2)

    # Gitternetz und Beschriftung
    #ax.grid()
    #ax.set_title('Zeigerdarstellung')
    handle.grid()
    handle.set_title('Zeigerdarstellung')
    #ax.set_xlabel('Realteil')
    #ax.set_ylabel('j*Imaginärteil')

    #Figur darstellen
    #plt.show()
    #return fig
    
def plot_pointer(handle, data=[], amp=1):      
    """
    Darstellung von Zeigern
    Aufruf:
        plot_pointer(data=[], amp=1)
    Parameter: 
        data - Liste der darzustellenden Zeiger (Real- und Imaginärteil)
        amp - maximale Amplitude (default 1)
        handle - Handle des Ausgabefensters
    Rückgabe:
        keine
    """
    # Ermitteln des größten Zeigerbetrags
    amp = 0
    for k in range(0, len(data)):
        if abs(data[k]) > amp:
            amp = abs(data[k])

    # Erzeugen einer Zeigerebene
    #fig = plot_plane(amp)
    plot_plane(handle, amp)
    
    # angepasste Werte für Pfeilspitzen und Zeigerbeschriftung ermitteln
    limits = [-amp,amp,-amp,amp]
    hw=(limits[1]-limits[0])/100
    hl=(limits[1]-limits[0])/50
    offset = (limits[1]-limits[0])/40
    # Verabeitung aller Zeiger der Eingabeliste
    for k in range(0, len(data)):
        cn_real = data[k].real
        cn_imag = data[k].imag
        if (abs(cn_real)+abs(cn_imag) != 0):
            #cn = plt.arrow(0, 0, cn_real, cn_imag, length_includes_head=True, head_width=hw, head_length=hl, fc='r', ec='r')
            cn = handle.arrow(0, 0, cn_real, cn_imag, length_includes_head=True, head_width=hw, head_length=hl, fc='r', ec='r')
            #ax=fig.add_subplot(1,1,1)
            #ax.add_patch(cn)
            handle.add_patch(cn)
    

def generate_pointer(anz=1, ampl=1, phase=0):
    """
    Erzeugen von Zeigern
    Aufruf:
        generate_pointer(anz=1, ampl=1, phase=0)
    Parameter: 
        anz - Anzahl der zwischen 0 und 2*pi zu erzeugenden Zeiger
        ampl - maximale Amplitude (default 1)
        phase - Nullphasenwinkel des Zeigers 
    Rückgabe:
        Zeiger bzw. Liste von Zeigern
    """
    z = []
    for i in range(0,anz):
        z.append(cmath.rect(ampl, i*2*np.pi/anz+phase+np.pi/2))
    return z

def plot_single_wave(anz=1, ampl=1, phase=0):
    """
    Darstellung eines Liniendiagramms mit Markierungen fuer rotierende Zeiger
    Aufruf:
        plot_single_wave(anz=1, ampl=1, phase=0)
    Parameter: 
        anz - Anzahl der zwischen 0 und 2*pi zu erzeugenden Markierungen (default 1)
        ampl - maximale Amplitude (default 1)
        phase - Nullphasenwinkel der Cosinusschwingung (default 0)
        Zeiger bzw. Liste von Zeigern
    """
    plt.figure(figsize=(6,6))
    fig=plt.figure(1)
    x = np.linspace(0, 2*np.pi, 100)
    plt.plot(x, np.cos(x + phase))
    plt.grid()
    x1 = np.linspace(0, 2*np.pi, anz)
    plt.stem(x1, np.cos(x1 + phase))
    plt.axis([0, 2*np.pi, -ampl, ampl])
    plt.title('Liniendiagramm')
    return fig
    
def generate_wave(phase=0):
    """
    Erzeugen der x- und y-Werte für eine Periode einer Cosinusschwingung
    Aufruf:
        generate_wave(phase=0)
    Parameter: 
        phase - Nullphasenwinkel der Cosinusschwingung (default 0)
    Rückgabe:
        x- und y-Werte für eine Periode
    """
    x = np.linspace(0, 2*np.pi, 100)
    return x, np.cos(x + phase)

def plot_wave(data):
    """
    Darstellung eines Liniendiagramms 
    Aufruf:
        plot_wave(data)
    Parameter: 
        data - Funktionswerte der Cosinusschwingung
    Rückgabe:
        x- und y-Werte für eine Periode
    """
    plt.figure(figsize=(6,6))
    fig=plt.figure(1)
    x = np.linspace(0, 2*np.pi, 100)
    plt.plot(x, data)
    plt.axis([0, 2*np.pi, min(data), max(data)])
    plt.title('Liniendiagramm')
    plt.grid()
    return x, data

def plot_point_wave(phase=0):
    """
    Darstellung eines Zeiger- und eines Liniendiagramms 
    Aufruf:
        plot_point_wave(phase=0)
    Parameter: 
        phase - Nullphasenwinkel der Cosinusschwingung (default 0)
    Rückgabe:
    """
    fig = plt.figure(figsize=(14,6))
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    
    plot_pointer(ax1, generate_pointer(phase=phase))
     
    a, b = generate_wave(phase=phase)
    #ax = fig.add_subplot(1,1,1)
    ax2.plot(a, b)
    ax2.set_title('Liniendiagramm')
    ax2.grid()
    ax2.axis([0, 2*np.pi, min(b), max(b)])
    
