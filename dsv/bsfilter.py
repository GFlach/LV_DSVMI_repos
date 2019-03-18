# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:23:25 2016

@author: Admin_1
"""
from pylab import *


from scipy.signal import butter, lfilter
from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np
#from scipy.io import wavfile
from dsv import dsvorg


def butter_hp_filter(data, fgu=1000, fs=44100, order=5):
    b, a = butter_hp(fgu, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lp_filter(data, fgo=1000, fs=44100, order=5):
    b, a = butter_lp(fgo, fs, order=order)
    y = lfilter(b, a, data)
    return y


def filter_fgang(fs=44100, fgu=1000,  fgo=1000, order=5, typ='lp'):
    nyq = 0.5 * fs
    low = fgu / nyq
    high = fgo / nyq
    fig = plt.figure(figsize=(16,4))
    if typ == 'lp':
        b, a = butter(order, [high])
    elif typ == 'hp':
        b, a = butter(order, [low], btype='highpass')
    elif typ == 'bp':
        b, a = butter(order, [low, high], btype='bandpass')
    elif typ == 'bs':
        b, a = butter(order, [low, high], btype='bandstop')
    else:
        print('Filtertyp nicht bekannt.')
        return
    w, h = freqz(b, a, worN=None)
    plt.plot((fs * 0.5 / np.pi) * w, abs(h))
    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)], 
             '--')    
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Verstärkung')
    plt.grid(True)
    plt.axis([8,8000,0,1.5])
    plt.title('Frequenzgang Butterworth-Filter Ordnung %s' %order)
    return fig

def filter_appl(fs, data_in, fgu=1000, fgo=1000, order=5, typ='lp'):
    nyq = 0.5 * fs
    low = fgu / nyq
    high = fgo / nyq
    if typ == 'lp':
        b, a = butter(order, [high])
    elif typ == 'hp':
        b, a = butter(order, [low], btype='highpass')
    elif typ == 'bp':
        b, a = butter(order, [low, high], btype='bandpass')
    elif typ == 'bs':
        b, a = butter(order, [low, high], btype='bandstop')
    else:
        print('Filtertyp nicht bekannt.')
        return
    data_out = lfilter(b, a, data_in)
    return data_out
    
def bandfilter(fgu=1000, fgo=1000, order=5):
    fs = 44100
    b_lp, a_lp = butter_lp(fgo, fs, order)
    b_hp, a_hp = butter_hp(fgu, fs, order)
    w_lp, h_lp = freqz(b_lp, a_lp, worN=None)
    w_hp, h_hp = freqz(b_hp, a_hp, worN=None)
    w_bp = w_lp
    if fgu > fgo:
        h_bp = (h_lp + h_hp)
        #typ = 'Bandsperre'
    else:
        h_bp = h_lp * h_hp
        #typ = 'Bandpass'
        
    plt.plot((fs * 0.5 / np.pi) * w_bp, abs(h_bp))

    plt.plot([fs, 0.5 * 1], [np.sqrt(0.5), np.sqrt(0.5)],
             '--')
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Verstärkung')
    plt.grid(True)
    plt.axis([0,4000,0,1.5])
    plt.title('Bandfilter Ordnung %s' %order)    


##filter_design(44100, 500, 2000)
#filter_applic(500,2000)
#bandfilter(fgu=1500, fgo=2000,order=10)

#data_in = dsvorg.load_data('dsv1_rauschen')
#plt.plot(np.abs(fft(data_in))[0:25000])
#data_out_lp = filter_applic_lp(data_in, fgo=1000, order=5)
#plt.plot(np.abs(fft(data_out_lp))[0:25000])

#data_in_hp = data_out_lp
#data_out_hp = filter_applic_hp(data_in_hp, fgu=1000, order=5)
#dsvorg.write_data('dsv1_kind_bp', data_out_hp)
#plt.plot(np.abs(fft(data_out_hp))[0:25000])
#data_out = data_out_lp * data_out_hp
#plt.plot(np.abs(fft(data_out_hp))[0:25000] * np.abs(fft(data_out_lp))[0:25000])
#plt.plot(np.abs(fft(data_out))[0:25000])


#data_in = dsvorg.load_data('dsv1_rauschen')
#plt.plot(np.abs(fft(data_in))[0:25000])
#data_out_lp = filter_applic_lp(data_in, fgo=500, order=5)
#plt.plot(np.abs(fft(data_out_lp))[0:25000])
#data_out_hp = filter_applic_hp(data_in, fgu=2000, order=5)
#plt.plot(np.abs(fft(data_out_hp))[0:25000])

#data_out = data_in_hp - data_out_lp
#plt.plot(np.abs(fft(data_out))[0:25000])

#dsvorg.write_data('dsv1_kind_bp', data_out_hp)
#data_out = data_out_lp * data_out_hp
#plt.plot(np.abs(fft(data_out_hp))[0:25000] * np.abs(fft(data_out_lp))[0:25000])
#plt.plot(np.abs(fft(data_out))[0:25000])
