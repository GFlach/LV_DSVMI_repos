# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:48:01 2016

@author: Admin_1

Klasse Dynamikkompression
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from time import strftime
import scipy
from scipy.io import wavfile

class Dynamic:    
    def __init__(self, threshold=0.5, ratio=1.0, typ='komp'):
        self.Threshold = threshold
        """
        Grenze Dynamikbearbeitung
        """
        self.Ratio = ratio              # Begrenzungsverhältnis
        self.Typ = typ                  # Dynamikbearbeitungstyp
        self.Eval = None                # Bewertungsfunktion
        self.Max = 2**15-1              # Amplitudenstufen
        self.Weight = None              # Gewichtsfunktion
    
    def create_eval(self):
        """
        Dynamikbewertung wird erzeugt, Typ wird bei Objekterzeugung festgelegt

        typ = komp ... Kompressor mit Schwellwert threshold und Komprimierungswert ratio
        typ = expand ... Expander mit Schwellwert threshold und Expansionswert ratio
        typ = limit ... Begrenzer mit Schwellwert threshold
        typ = gate ... Ausblenden der Werte unterhalb Schwellwert threshold
        """

        xs = round(self.Max * self.Threshold)
        if self.Typ == 'komp':
           if self.Ratio > 1:
                print('Fehler Kompressionswert')
                return 0            
           y1_w = np.linspace(0, self.Threshold, num=xs)
           y2_w = np.linspace(self.Threshold, self.Threshold + (1 - self.Threshold)*self.Ratio, num=self.Max-xs)
           y1 = np.ones(xs)
           y2 = np.linspace(1, self.Ratio * (1-self.Threshold) + self.Threshold, num=self.Max-xs)
           self.Eval = np.append(y1,y2)
           self.Weight = np.append(y1_w,y2_w)
           return 1
           
        if self.Typ == 'limit':
           y1_w = np.linspace(0, self.Threshold, num=xs)
           y2_w = np.ones(self.Max-xs) * self.Threshold
           y1 = np.ones(xs)
           y2 = np.ones(self.Max-xs)*self.Max/np.linspace(xs, self.Max, num=self.Max-xs)*self.Threshold
           self.Eval = np.append(y1,y2)
           self.Weight = np.append(y1_w,y2_w)
           return 1

        if self.Typ == 'expand':
           if self.Ratio < 1:
                print('Fehler Expansionswert')
                return 0              
           y1_w = np.linspace(0, self.Threshold, num=xs)
           y2_w = np.linspace(self.Threshold, self.Threshold + (1 - self.Threshold)*self.Ratio, num=self.Max-xs)
           y1 = np.ones(xs)
           y2 = np.linspace(1, self.Ratio * (1-self.Threshold) + self.Threshold, num=self.Max-xs)
           self.Eval = np.append(y1,y2)
           self.Weight = np.append(y1_w,y2_w)
           return 1

        if self.Typ == 'gate':
           y1_w = np.zeros(xs)
           y2_w = np.linspace(xs, self.Max, num=self.Max-xs)
           y1 = np.zeros(xs)
           y2 = np.ones(self.Max-xs)
           self.Eval = np.append(y1,y2)/max(y2)
           self.Weight = np.append(y1_w,y2_w)/max(y2_w)
           return 1


    def plot_eval(self, fig):
        """
        Dynamikbewertung wird gedruckt

        fig ... Handle auf Grafik
        """
        dyn_in = np.linspace(0, 1, num = self.Max)
        
        fig.add_subplot(121)
        plot(dyn_in, self.Weight)
        grid(True)
        title('Dynamik Typ %s'%self.Typ)
        xlabel('Eingangssignal')
        ylabel('Ausgangssignal')
        
        return fig

           
