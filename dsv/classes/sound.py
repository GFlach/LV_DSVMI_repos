# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:48:01 2016

@author: Admin_1

Klasse Soundgenerator
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from time import strftime
import scipy
from scipy.io import wavfile

class Sound:
    def __init__(self, amplitude=1, atf=16000, duration=1):
        self.Amplitude = amplitude
        self.ATF = atf
        self.Duration = duration

    def show_params(self):
        print('Amplitude: {0:.2f}'.format(self.Amplitude))
        print('ATF(Hz): {0:.2f}'.format(self.ATF))
        print('Dauer(s): {0:.2f}'.format(self.Duration))
    
    def get_params(self):
        liste = [self.Amplitude, self.ATF, self.Duration]
        return liste
    
    def set_params(self, amplitude, atf, duration):
        self.Amplitude = amplitude
        self.ATF = atf
        self.Duration = duration

    def generate_tone(self, frequency):
        t = np.linspace(0, self.Duration, self.Duration*self.ATF)
        sig = np.sin(2*np.pi*frequency*t)
        return sig

    def generate_sound(self, frequency=440, ow=1):
        t = np.linspace(0, self.Duration, self.Duration*self.ATF)
        sig = np.zeros(self.Duration*self.ATF)
        for k in range(ow):
            sig = sig + np.sin((k+1)*2*np.pi*frequency*t)
        return sig
    
    def blend_sounds(self, sound1, sound2):
        if len(sound1) != len(sound2):
            print('Sounds sind unterschiedlich lang')
            return
        sound = sound1 + sound2
        return sound
    
    def normalize_sound(self, sound, amplitude=1):
        max_sound = max(max(sound),abs(min(sound)))
        sound_norm = amplitude*sound/max_sound
        return sound_norm
    
    def generate_noise(self):
        noise = np.random.normal(0,1,self.Duration*self.ATF)
        return noise
    
    def save_as_wav(self, sig, 
                    file_name='C:\\WinPython\\notebooks\\sound\\sig.wav'):
        wavfile.write(file_name, self.ATF, sig)
    
