# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:06:50 2016

@author: Admin_1
"""

from __future__ import division
from pylab import *
from random import randrange
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np


def get_infos(file, fs, data = []):
    string0 = 'Dateiname: ' + file + '.wav \n'
    string1 = 'Abtastfrequenz: ' + str(fs) + ' Hz \n'
    string2 = 'Datenformat: ' + str(data.dtype) + '\n'
    string3 = 'Anzahl ATW: ' + str(len(data)) + '\n'
    string4 = 'Maximum: ' + str(max(data)) + '\n'
    string5 = 'Minimum: ' + str(min(data)) + '\n'
    info_string = string0 + string1 + string2 + string3 + string4 + string5
    return info_string

def demo_komp(sig, weight):
    fig = plt.figure(figsize=(15,4))
    if weight.create_eval() == 1:
        weight.plot_eval(fig)  
        #sig_weight =sig * weight.Eval[np.round(abs(sig)*(weight.Max-1)).astype(int)] 
        sig_weight =weight.Weight[np.round(abs(sig)*(weight.Max-1)).astype(int)]*np.sign(sig) 
        #sig_weight =sig * weight.Weight[np.round(abs(sig)*(weight.Max-1)).astype(int)] 

        fig.add_subplot(122)
        plot(sig[0:100], label='sig')   
        grid(True)
        hold(True)
        plot(sig_weight[0:100], label='sig_weight')
        legend()
        title('Zeitfunktion vor und nach Dynamikbearbeitung') 
        return sig_weight
        
def sig_komp(sig, weight):
    norm = max(max(sig), abs(min(sig)))
    sig_norm = np.array(sig,dtype=np.float32)/norm

    if weight.create_eval() == 1:
        sig_weight = weight.Weight[np.round(abs(sig_norm)*(weight.Max-1)).astype(int)]*np.sign(sig_norm) 
        norm = max(max(sig_weight), abs(min(sig_weight)))
        sig_weight = np.array(sig_weight,dtype=np.float32)/norm
        return sig_weight

def read_sig(file):
    path_name = 'sound\\'
    file_name = path_name + file + '.wav'
    fs, o_sig = wavfile.read(file_name)
    norm = max(max(o_sig), abs(min(o_sig)))
    sig_norm = np.array(o_sig,dtype=np.float32)/norm
    return sig_norm, fs

def generate_signal(freq, num=16000):
    n = np.linspace(0, 1, num)
    if freq == 0:
        return np.ones(num)
    else:
        return np.sin(2*np.pi*freq*n)

def sys1(data, freq):
    n = np.linspace(0, 1, num=16000)
    return np.sin(2*np.pi*freq*n)*data
    
def sys2(data, freq):
    n = np.linspace(0, 1, num=16000)
    return np.sin(2*np.pi*freq*n)+data
    

def plot_sig(data1, data2, data3):
    n = np.linspace(0, 1, num=16000)
    fig = plt.figure(figsize=(15,4))
    fig.add_subplot(131)
    plt.plot(n[0:400],data1[0:400])
    plt.grid()
    plt.title('Eingangssignal')
    plt.xlabel('t in s')
    fig.add_subplot(132)
    plt.plot(n[0:400],data2[0:400])
    plt.grid()
    plt.title('Ausgangssignal System 1')
    plt.xlabel('t in s')
    fig.add_subplot(133)
    plt.plot(n[0:400],data3[0:400])
    plt.grid()
    plt.title('Ausgangssignal System 2')
    plt.xlabel('t in s')
    plt.show()

def misch(file1, file2, w1=1, w2=1):
    path_name = 'sound\\'
    file_name1 = path_name + file1 + '.wav'
    file_name2 = path_name + file2 + '.wav'
    fs1, data_file1 = wavfile.read(file_name1)
    fs2, data_file2 = wavfile.read(file_name2)
    norm1 = max(max(data_file1), abs(min(data_file1)))
    data_file1_norm = np.array(data_file1,dtype=np.float32)/norm1
    norm2 = max(max(data_file2), abs(min(data_file2)))
    data_file2_norm = np.array(data_file2,dtype=np.float32)/norm2
    
    if len(data_file1) < len(data_file2):
        data_file2_norm = data_file2_norm[:len(data_file1)]
    else:
        data_file1_norm = data_file1_norm[:len(data_file2)]
    
    data = w1*data_file1_norm + w2*data_file2_norm
    norm = max(max(data), abs(min(data)))
    data_norm = data/norm
    return data_norm
    
def trim(file1, file2):
    path_name = 'sound\\'
    file_name1 = path_name + file1 + '.wav'
    file_name2 = path_name + file2 + '.wav'
    fs1, data_file1 = wavfile.read(file_name1)
    fs2, data_file2 = wavfile.read(file_name2)
     
    if len(data_file1) < len(data_file2):
        data_file2 = data_file2[:len(data_file1)]
        return data_file1, data_file2
    else:
        data_file1_norm = data_file1_norm[:len(data_file2)]
        return data_file1, data_file2
        
def read(file):
    path_name = 'sound\\'
    file_name = path_name + file + '.wav'
    fs, data_file = wavfile.read(file_name)
    data_file = data_file/max(max(data_file),abs(min(data_file)))
    return fs, data_file
    
    
def spektrum(fs, data_in):
    f = np.linspace(0, fs/2, len(data_in)/2)
    #fig = plt.figure(figsize=(15,3))
    plt.plot(f, np.abs(fft(data_in))[0:len(data_in)/2]/len(data_in))
    plt.axis([0,8000,0,max(np.abs(fft(data_in))[0:len(data_in)/2]/len(data_in))])
    plt.title('Spektrum')
    plt.xlabel('f in Hz')
    #plt.axis('tight')

def spektrogramm(fs, data_in, fmax=8000):
    specgram(data_in, NFFT=1024, Fs=fs, noverlap=512, cmap=None, window=None)
    #fig = plt.figure(figsize=(15,3))
    plt.axis([0,len(data_in)/fs,0,fmax])
    plt.title('Spektrogramm')
    plt.xlabel('t in s')
    #plt.axis('tight')

   
def fgang_spec_single(file, fmax=8000):
    path_name = 'sound\\'
    file_name = path_name + file + '.wav'
    fs, data = wavfile.read(file_name)
    data = data/max(max(data),abs(min(data)))

    f = np.linspace(0, fs/2, len(data)/2)
    fig = plt.figure(figsize=(15,6))
    
    fig.add_subplot(211)
    plt.plot(f, np.abs(fft(data))[0:len(data)/2]/len(data))
    plt.axis([0,fmax,0,max(np.abs(fft(data))[0:len(data)/2]/len(data))])
    plt.title('Spektrum Nutzsignal')
    
    fig.add_subplot(212)
    specgram(data, NFFT=1024, Fs=fs, noverlap=512, cmap=None, window=None)
    plt.axis([0,5.4,0,fmax])
    plt.title('Spektrogramm Nutzsignal')
    
    return fig

def load_data_o(filename):
    path_name = 'sound\\'
    file_name = path_name + filename + '.wav'
    fs, data = wavfile.read(file_name)
    return fs, data

def load_data(filename):
    path_name = 'sound\\'
    file_name = path_name + filename + '.wav'
    fs, data = wavfile.read(file_name)
    data = data/max(max(data),abs(min(data)))
    return fs, data

def write_data(filename,data, fs=44100):
    path_name = 'sound\\'
    file_name = path_name + filename + '.wav'
    wavfile.write(file_name, fs, data)
    
def conv_input(data1, data2):
    pmax = max(max(data1),max(data2))
    pmin = min(min(data1),min(data2))
    kmax = max(len(data1),len(data2))
    plt.figure(figsize=(15,4))
    plt.subplot(121)
    ax1 = plt.subplot2grid((2,2), (0,0))
    ax1.stem(data1,basefmt='b-')
    ax1.grid(True)
    ax1.set_title ('zu faltende Signale')
    ax1.set_ylabel('x1(k)')
    ax1.axis([-1,kmax+1,pmin-1, pmax+1])

    ax2 = plt.subplot2grid((2,2), (1,0))
    ax2.stem(data2,basefmt='b-')
    ax2.set_xlabel('k')
    ax2.set_ylabel('x2(k)')
    ax2.axis([-1,kmax+1,pmin-1, pmax+1])
    ax2.grid(True)

    y = np.convolve(data1,data2)
    plt.subplot(122)
    ax3 = plt.subplot2grid((2,2), (0,1), rowspan=2)
    ax3.stem(y,basefmt='b-')
    ax3.set_title ('Faltungsergebnis')
    ax3.set_xlabel('n')
    ax3.set_ylabel('y(n)')
    ax3.axis([-1,len(y)+1,min(y)-1, max(y)+1])
    plt.grid(True)
    plt.show()
    

def demo_samp1(fS, lage):
    fig = plt.figure(figsize=(15, 4))
    f = 1.0         # Hz, signal frequency
    #fs = 10.0       # Hz, sampling rate
    #lage = 0.25
    t = np.arange(-1, 1+1/fS, 1/fS)  # sample interval, symmetric
    t = np.arange(-1+lage, 1+1/fS+lage, 1/fS)  # sample interval, symmetric
    x = np.sin(2*np.pi*f*t)
    fig.add_subplot(121)
    plot(t, x, 'o-')
    xlabel('Zeit')
    ylabel('Amplitude')
    ylim([-1, 1])
    title('Lineare Interpolation')
    grid(True)

    interval = []
    apprx = []
    tp = np.hstack([np.linspace(t[i], t[i+1], 20, False) for i in range(len(t)-1)])
    for i in range(len(t)-1):
        interval.append(np.logical_and(t[i] <= tp, tp < t[i+1]))
        apprx.append((x[i+1]-x[i])/(t[i+1]-t[i])*(tp[interval[-1]]-t[i]) + x[i])
        x_hat = np.piecewise(tp, interval, apprx)  # piecewise linear approximation

    ax1 = fig.add_subplot(122)
    ax1.fill_between(tp, x_hat, np.sin(2*np.pi*f*tp), facecolor='red')
    ax1.set_xlabel('Zeit')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Fehler bei linearer Interpolation')
    ax2 = ax1.twinx()  # create clone of ax1
    sqe = (x_hat-np.sin(2*np.pi*f*tp))**2  # quadratischer Fehler
    ax2.plot(tp, sqe, 'b')
    ax2.axis(xmin=-1, ymax=sqe.max())
    ax2.set_ylabel('Quadratischer Fehler', color='b')

def demo_samp2():
    fig = plt.figure(figsize=(15,4))
    k=0
    fs=3 
    t = linspace(-1,1,100)
    ax = fig.add_subplot(111)
    ax.plot(t,np.sinc(k - fs * t), t,np.sinc(k+1 - fs * t),'--',k/fs,1,'o',(k)/fs,0,'o',
        t,np.sinc(k-1 - fs * t),'--',k/fs,1,'o',(-k)/fs,0,'o')
    ax.set_xlabel('Zeit in s')
    ax.set_title('Lage der Spaltfunktionen für fS = 3 Hz')
    ax.hlines(0,-1,1) 
    ax.vlines(0,-.2,1) 
    ax.annotate('Spaltfunktion für t=0',xy=(0,1), xytext=(-1+.1,1.1),
            arrowprops={'facecolor':'red','shrink':0.05})
    ax.annotate('Einfluss anderer Spaltfunktionen',xy=(0,0), xytext=(-1+.1,0.5),
            arrowprops={'facecolor':'green','shrink':0.05})
    ax.grid(True)



def demo_samp3(fS, anz_p):
    fig = plt.figure(figsize=(15,4))
    #fs=5.0 
    t = linspace(-1,1,100)
    t1 = linspace(-anz_p/2,anz_p/2,anz_p*50)
    k=np.array(sorted(set((t1*fS).astype(int))))
    ax1 = fig.add_subplot(111)
    ax1.plot(t,(np.sin(2*np.pi*(k[:,None]/fS))*np.sinc(k[:,None]-fS*t)).T,'--', t,
        (np.sin(2*np.pi*(k[:,None]/fS))*np.sinc(k[:,None]-fS*t)).sum(axis=0),'k-', k/fS,
        np.sin(2*np.pi*k/fS),'ob')
    ax1.set_xlabel('Zeit in s')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Sinusrekonstruktion mit Spaltfunktionen')
    ax1.axis((-1.1,1.1,-1.1,1.1))
    ax1.grid(True)
   
   
def demo_aliasing():
    fig = plt.figure(figsize=(15,4))
    t = np.linspace(0,1,1000)
    t1 = np.linspace(0,1,7)
    x_samp = np.sin(2*np.pi*t1)
    stem(t1,x_samp,'k')
    freq = 6 * randrange(-4, 4) + 1
    x1 = np.sin(2*np.pi*t)
    x2 = np.sin(freq*2*np.pi*t)
    plot(t,x1,label='1 Hz')
    plot(t, x2,'--',label='%s Hz' % freq)
    legend()
    xlabel('Zeit in s')
    title('Sinusschwingungen zu einer Abtastwertefolge')
    grid(True)
    
def show_exp(k, N):
    plt.figure(figsize=(15,5))
    t = np.arange(0,N,0.01)
    y = np.cos(2*np.pi*t/N*k)
    plt.plot(t,y, 'g:')
    n = np.arange(0,N+0.1)
    y_n = np.cos(2*np.pi*n*k/N)
    plt.stem(n, y_n,'r', basefmt=" ", markerfmt='ro')
    plt.xlabel('Abtastwerte')
    plt.axis([-0.2, 8.2, -1.1, 1.1])
    plt.grid()
    plt.show()
