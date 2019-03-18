# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:48:01 2016

@author: Admin_1

Klasse Hüllkurve
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from time import strftime
import scipy
from scipy.io import wavfile

class Huellkurve:
    def __init__(self, t_attack=0.25, t_decay=0.2, t_sustain=0.4, 
                 t_release=0.15, maximum=1, sustain_level=0.7):
        if t_attack + t_decay + t_sustain + t_release > 1:
            print('Achtung Fehler Zeitparameter')
        self.Attack = t_attack
        self.Decay = t_decay
        self.Sustain = t_sustain
        self.Release = t_release
        self.Maximum = maximum
        self.SL = sustain_level
        self.hk = None
    
    def show_params(self):
        print('Attack Time: {0:.2f}'.format(self.Attack))
        print('Decay Time: {0:.2f}'.format(self.Decay))
        print('Sustain Time: {0:.2f}'.format(self.Sustain))
        print('Release  Time: {0:.2f}'.format(self.Release))
        print('Maximum: {0:.2f}'.format(self.Maximum))
        print('Sustain Level: {0:.2f}'.format(self.SL))
    
    def get_params(self):
        liste = [self.Attack, self.Decay, self.Sustain, self.Release, 
                 self.Maximum, self.SL]
        return liste
    
    def set_params(self, t_attack=0.25, t_decay=0.2, t_sustain=0.4, t_release=0.15, maximum=1, 
                   sustain_level=0.7):
        self.Attack = t_attack
        self.Decay = t_decay
        self.Sustain = t_sustain
        self.Release = t_release
        self. Maximum = maximum
        self.SL = sustain_level
    
    def generate_hk(self, typ='adsr', dauer=1, fs=16000, s_on=10, s_off=3):
        if typ == 'adsr':
            if self.Attack + self.Decay + self.Sustain + self.Release > 1:
                print('Fehler Zeitparameter')
                return
            ta = round(dauer*fs*self.Attack)
            td = round(dauer*fs*self.Decay)
            ts = round(dauer*fs*self.Sustain)
            tr = round(dauer*fs*self.Release)
            
            t1 = np.linspace(0, self.Maximum, num=ta)
            t2 = np.linspace(self.Maximum, self.SL, num=td)
            t3 = self.SL*np.ones(ts)
            t4 = np.linspace(self.SL, 0, num=tr)
            
            hk = np.append(np.append(np.append(t1,t2),t3),t4)
            
        if typ == 'triangle':
            if self.Attack + self.Release != 1:
                print('Fehler Zeitparameter')
                return
            ta = round(dauer*fs*self.Attack)
            tr = round(dauer*fs*self.Release)
            
            t1 = np.linspace(0, self.Maximum, num=ta)
            t2 = np.linspace(self.Maximum, 0, num=tr)
            
            hk = np.append(t1,t2)

        if typ == 'exponent':
            if self.Attack + self.Release != 1:
                print('Fehler Zeitparameter')
                return
            ta = round(dauer*fs*self.Attack)
            tr = round(dauer*fs*self.Release)
            
            t1 = (np.exp(np.linspace(0, s_on, num=ta))-1)/np.exp(s_on)
            t2 = (np.exp(np.linspace(s_off, 0, num=tr))-1)/np.exp(s_off)
            
            hk = np.append(t1,t2)
            
        self.hk = hk[:]
    
    def repeat_hk(self, times, hk):
        hk1 = hk
        for k in range(times):
            hk1 = np.append(hk1,hk)
        return hk1
    
    def plot_hk(self):
        fig = plt.figure(figsize=(10,5))
        ax = fig.add_subplot(111)
        ax.plot(self.hk)
        ax.grid()
        ax.set_title('Hüllkurve für Audiodesign')
        ax.set_xlabel('Abtastwerte')
        ax.set_ylabel('Gewicht')
        #plt.savefig('C:\\WinPython\\notebooks\\image\\dsv'
        #+strftime("%Y-%m-%d_%H-%M")+'.jpg')

