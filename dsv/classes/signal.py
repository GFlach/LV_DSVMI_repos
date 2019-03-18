# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:59:33 2016

@author: Admin_1
"""
import numpy as np
from scipy.io import wavfile
from pylab import *
from scipy.signal import butter, freqz, lfilter

class Signal:
    def __init__(self, pfad='', name=''):
        self.Pfad = pfad
        self.Name = name
        self.ATF = None
        self.Format = None
        self.Length = None
        self.Duration = None
        self.Sig = None
        self.FFT = None
        self.IFFT = None
        self.BS = None
        self.PS = None
        
    def read(self):
        fname = self.Pfad + self.Name
        self.ATF, self.Sig = wavfile.read(fname)
        self.Length = len(self.Sig)
        self.Duration = self.Length/self.ATF
        self.fft_abs()
        self.fft_phase()
        
    def write(self):
        fname = self.Pfad + self.Name
        wavfile.write(fname, self.ATF, self.Sig)
    
    def fft_abs(self):
        self.FFT = np.fft.fft(self.Sig)
        self.FFT[np.abs(self.FFT)<e-10]=0+0j
        self.BS = np.abs(np.fft.fftshift(self.FFT/self.Length))

    def fft_phase(self):
        self.PS = np.angle(np.fft.fftshift(self.FFT/self.Length))

    def fft_inv(self):
        self.IFFT = np.fft.ifft(self.FFT)

class Lp_filter():
    def __init__(self, fS=16000, fgo=1000, order=1):
        self.Fgo = fgo
        self.FS = fS
        self.Ftyp = 'lp'
        self.Order = order
        self.B = None
        self.A = None
        self.W = None
        self.H = None
        
        high = 2*self.Fgo/self.FS
        self.B, self.A = butter(self.Order,[high])
        self.W, self.H = freqz(self.B, self.A)
        
    def apply_filter(data_in):
        data_out = lfilter(self.B, self.A, data_in)
        return data_out
        
class Sweep:
    def __init__(self):
        self.fS, self.Data = wavfile.read('sound\\sweep.wav')
        self.Data = self.Data/max(max(self.Data), abs(min(self.Data)))*0.8
        self.Duration = len(self.Data)/self.fS
        
    def plot(self):        
        plt.figure(figsize=(15,4))
        t = np.linspace(0, self.Duration, len(self.Data))
        plt. plot(t, self.Data)
        plt.title('Sweepsignal')
        plt.grid(True)
        plt.xlabel('t in s')
        plt.axis([0,max(t),-1,1])

    def plot_selection(self, start=0, stop=0):
        plt.figure(figsize=(15,6))
        t = np.linspace(start, stop, int(stop*self.fS)-int(start*self.fS))
        plt.subplot(211)
        plt.plot(t, self.Data[int(start*self.fS):int(stop*self.fS)])
        plt.title('Ausschnitt Sweepsignal')
        plt.grid(True)
        plt.xlabel('t in s', x=1)
        plt.axis([start,stop,-1,1])
    
    def plot_spektrum(self, start=0, stop=0):
        l = len(self.Data[int(start*self.fS):int(stop*self.fS)])
        bs = np.abs(np.fft.fft(self.Data[int(start*self.fS):int(stop*self.fS)]))/l
        f = np.linspace(0,self.fS/2,l//2)
        plt.subplot(212)
        plt.plot(f, bs[0:len(bs)//2])
        plt.title('Amplitudenspektrum Ausschnitt Sweepsignal')
        plt.grid(True)
        plt.xlabel('f in Hz', x=1)
        
class Rechteck:
    def __init__(self, ampl=1, tv=1, vs=0, offs=0, per=1):
        self.Ampl = ampl
        self.Tv = 1/(1/tv+1)
        self.Vs = vs
        self.Offs = offs
        self.Per = per
        self.Data = None
        self.Spek = None
        self.SpekB = None
        self.SpekP = None
        self.Max = None
        t = np.linspace(0,1,1000)
        x = ampl*np.ones(len(t))
        eins = int(self.Tv*1000)
        #eins = tv*1000//(1+tv)
        x[eins:1000] = 0
        x = x - 0.5 + offs
        self.Data = np.append(x[500+int(eins/2):1000],x[0:500+int(eins/2)])
        if vs > 0:
            self.Data = np.append(self.Data[1000*(1-vs):1000],self.Data[0:1000*(1-vs)])
        if vs < 0:
            self.Data = np.append(self.Data[abs(vs)*1000:1000],self.Data[0:1000*abs(vs)])
        if per > 1:
            dneu = self.Data[np.array(range(0,1000,per))]
            d1 = dneu
            for i in range(per-1):
                d1 = np.append(d1,dneu)
            self.Data = d1
            if len(d1)<1000:
                self.Data = np.append(self.Data, np.zeros(1000-len(d1)))
    
    def plot_rechteck(self):
        plt.figure(figsize=(15,5))
        ax1 = plt.subplot2grid((2,2), (0,0), rowspan=2)
        t = np.linspace(-0.5,0.5,1000)
        ax1.plot(t,self.Data)
        ax1.set_title('Rechteckfunktion')
        ax1.axis([-0.5, 0.5, min(self.Data)-0.1, max(self.Data)+0.1])
        ax1.set_xlabel('t in s')
        ax1.grid(True)
        
        
    def spektrum_rechteck(self):
        n = np.linspace(-500, 499, num=1000)
        self.SpekB = self.Tv*np.abs(np.round(np.sinc(self.Tv*n), decimals=4))
        self.Max = max(self.SpekB)
        self.SpekP = np.arccos(np.sign(np.round(np.sinc(self.Tv*n), decimals = 4)))

    def plot_spektrum(self, fmax=10):
        ax2 = plt.subplot2grid((2,2),(0,1))
        ax3 = plt.subplot2grid((2,2),(1,1))
        f = np.linspace(-fmax,fmax,2*fmax+1)
        ax2.stem(f,self.SpekB[500-fmax:500+fmax+1])
        ax2.set_title('Amplitudenspektrum Rechteckfunktion', fontsize=10)
        ax2.set_xlim([-fmax, fmax])
        ax2.set_xlabel('f in Hz', x=1)
        ax2.grid(True)
        ax3.stem(f,self.SpekP[500-fmax:500+fmax+1])
        ax3.set_title('Phasenspektrum Rechteckfunktion', fontsize=10)
        ax3.set_xlim([-fmax, fmax])
        ax3.set_xlabel('f in Hz', x=1)
        ax3.grid(True)
        
    def reko_rechteck(self, anzh=10):
        if (anzh > 500):
            print('Die Anzahl der Aufbaufunktionen wird auf 500 begrenzt.')
            anzh = 500
        plt.figure(figsize=(15,5))
        plt.subplot(121)
        t = np.linspace(-0.5,0.5,1000)
        xges = self.SpekB[500]*np.ones(1000)
        plot(t,xges)
        for i in range(1,anzh):
             x = 2*self.SpekB[500+i]*np.cos(2*pi*i*t+self.SpekP[500+i])
             plt.plot(t,x)
             plt.grid(True)
             plt.title('Aufbaufunktionen')
             plt.xlim([-0.5,0.5])
             plt.xlabel('t in s')
             xges = xges + x
        plt.subplot(122)
        plt.plot(t,xges)
        plt.grid(True)
        plt.title('rekonstruierte Zeitfunktion')
        plt.xlim([-0.5,0.5])
        plt.xlabel('t in s')
        
    
            
            
        
         
        
        
        