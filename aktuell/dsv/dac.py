# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:57:37 2016

@author: Admin_1
"""

import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def analog_sig(f1=0, f2=0, f3=0):
    t = np.linspace(-511, 512, 1024)
    y1 = np.sin(2*np.pi*f1*t/1024)
    y2 = np.sin(2*np.pi*f2*t/1024)
    y3 = np.sin(2*np.pi*f3*t/1024)
    y = y1 + y2 + y3
    return y

def analog_t(f1=0, f2=0, f3=0):
    t = np.linspace(-511, 512, 1024)
    if f1 != 0:
        y1 = np.cos(2*np.pi*f1*t/1024)
    else:
        y1 = np.zeros(1024)
    if f2 != 0:
        y2 = np.cos(2*np.pi*f2*t/1024)
    else:
        y2 = np.zeros(1024)
    if f3 != 0:
        y3 = np.cos(2*np.pi*f3*t/1024)
    else:
        y3= np.zeros(1024)
    y = y1 + y2 + y3
    plt.figure(figsize=(15,4))
    ax1 = plt.subplot2grid((2,2), (0,0), rowspan=2)
    ax1.plot(t/1024,y)
    ax1.set_title('analoge Funktion im Zeitbereich')
    ax1.set_xlabel('t in s')
    ax1.axis([-0.5,0.5,-3,3])
    ax1.grid(True)
    return y

def analog_f(data, fmax=512):
    data = np.append(data[512:1024], data[0:512])
    y = np.fft.fft(data)/len(data)
    y[np.abs(y)<0.1]=0+0j
    y[np.imag(y)<0.1]=np.real(y)+0j
    y1 = np.abs(np.fft.fftshift(y))
    y2 = np.angle(np.fft.fftshift(y))
    f = np.linspace(-512,511,1024)
    ax2 = plt.subplot2grid((2,2),(0,1))
    ax3 = plt.subplot2grid((2,2),(1,1))
    ax2.stem(f,y1,markerfmt='.')
    ax2.set_title('Betrags- und Phasenspektrum')
    ax2.set_xlabel('f in Hz')
    ax2.axis([-fmax,fmax,0,1])
    ax2.grid(True)
    ax3.stem(f,y2,markerfmt='.')
    ax3.set_xlabel('f in Hz')
    ax3.axis([-fmax,fmax,-3,3])
    ax3.grid(True)
    
def digital_t(f1=0, f2=0, f3=0, fS=1024):
    y1 = [0]
    if max(f1,f2,f3) >= fS/2:
        print('Abtasttheorem verletzt')
        return y1
    t = np.linspace(-fS/2+1, fS/2, fS)
    if f1 != 0:
        y1 = np.cos(2*np.pi*f1*t/fS)
    else:
        y1 = np.zeros(fS)
    if f2 != 0:
        y2 = np.cos(2*np.pi*f2*t/fS)
    else:
        y2 = np.zeros(fS)
    if f3 != 0:
        y3 = np.cos(2*np.pi*f3*t/fS)
    else:
        y3 = np.zeros(fS)
    y = y1 + y2 + y3
    plt.figure(figsize=(15,4))
    ax1 = plt.subplot2grid((2,2), (0,0), rowspan=2)
    ax1.stem(t/fS,y, markerfmt='.')
    ax1.set_title('digitale Funktion im Zeitbereich')
    ax1.set_xlabel('t in s')
    ax1.axis([-0.5,0.5,-3,3])
    ax1.grid(True)
    y1 = np.append(y[len(y)/2-1:len(y)], y[0:len(y)/2-1])
    return y1

def digital_f(data, fmax=512):
    y = np.fft.fft(data)/len(data)
    y[np.abs(y)<0.1]=0+0j
    y[np.imag(y)<0.1]=np.real(y)+0j
    y1 = y
    i = 0
    if len(data) < 1024:
        for i in range(1,int(1024/len(data))):
            #print(i)
            y1 = np.append(y1,y)
    yb = np.abs(np.fft.fftshift(y1))
    yp = np.angle(np.fft.fftshift(y1))
    f_h = (i+1)*len(data)
    f = np.linspace(-f_h/2,f_h/2-1,f_h)
    ax2 = plt.subplot2grid((2,2),(0,1))
    ax3 = plt.subplot2grid((2,2),(1,1))
    ax2.stem(f,yb,markerfmt='.')
    ax2.set_title('Betrags- und Phasenspektrum')
    ax2.axis([-fmax,fmax,0,1])
    ax2.grid(True)
    ax3.stem(f,yp,markerfmt='.')
    ax3.set_xlabel('f in Hz')
    ax3.axis([-fmax,fmax,-3,3])
    ax3.grid(True)

def generate_dig_sig(f1=[0,0], f2=[0,0], f3=[0,0], fS=16, anz_spek=1):
    t = np.linspace(-511, 512, 1024)
    z = np.zeros(1024)
    for i in range(0, anz_spek):
        #y11 = f1[0]/anz_spek*np.sin(2*np.pi*(i*fS+f1[1])*t/1024)
        #y12 = -f1[0]/anz_spek*np.sin(2*np.pi*(i*fS-f1[1])*t/1024)
        #y1 = y11 + y12
        #y21 = f2[0]/anz_spek*np.sin(2*np.pi*(i*fS+f2[1])*t/1024)
        #y22 = -f2[0]/anz_spek*np.sin(2*np.pi*(i*fS-f2[1])*t/1024)
        #y2 = y21 + y22
        #y31 = f3[0]/anz_spek*np.sin(2*np.pi*(i*fS+f3[1])*t/1024)
        #y32 = -f3[0]/anz_spek*np.sin(2*np.pi*(i*fS-f3[1])*t/1024)
        #y3 = y31 + y32
        y11 = f1[0]/anz_spek*np.cos(2*np.pi*(i*fS+f1[1])*t/1024)
        y12 = f1[0]/anz_spek*np.cos(2*np.pi*(i*fS-f1[1])*t/1024)
        y1 = y11 + y12
        y21 = f2[0]/anz_spek*np.cos(2*np.pi*(i*fS+f2[1])*t/1024)
        y22 = f2[0]/anz_spek*np.cos(2*np.pi*(i*fS-f2[1])*t/1024)
        y2 = y21 + y22
        y31 = f3[0]/anz_spek*np.cos(2*np.pi*(i*fS+f3[1])*t/1024)
        y32 = f3[0]/anz_spek*np.cos(2*np.pi*(i*fS-f3[1])*t/1024)
        y3 = y31 + y32
        z = z + y1 + y2 + y3
    subplot(122)
    plt.plot(t/1024,z)
    plt.title('analoge Funktion im Zeitbereich -> Abtastwertefolge')
    plt.xlabel('t in s')
    plt.axis([-0.5,0.5,-3,3])
    plt.grid(True)
    
def generate_analog_sig(f1=[0,0], f2=[0,0], f3=[0,0]):
    t = np.linspace(-511, 512, 1024)
    #y11 = f1[0]*np.sin(2*np.pi*f1[1]*t/1024)
    #y12 = -f1[0]*np.sin(2*np.pi*(-f1[1])*t/1024)
    #y21 = f2[0]*np.sin(2*np.pi*f2[1]*t/1024)
    #y22 = -f2[0]*np.sin(2*np.pi*(-f2[1])*t/1024)
    #y31 = f3[0]*np.sin(2*np.pi*f3[1]*t/1024)
    #y32 = -f3[0]*np.sin(2*np.pi*(-f3[1])*t/1024)
    y11 = f1[0]*np.cos(2*np.pi*f1[1]*t/1024)
    y12 = f1[0]*np.cos(2*np.pi*(-f1[1])*t/1024)
    y21 = f2[0]*np.cos(2*np.pi*f2[1]*t/1024)
    y22 = f2[0]*np.cos(2*np.pi*(-f2[1])*t/1024)
    y31 = f3[0]*np.cos(2*np.pi*f3[1]*t/1024)
    y32 = f3[0]*np.cos(2*np.pi*(-f3[1])*t/1024)
    y = y11 + y12 + y21 + y22 + y31 + y32
    plt.figure(figsize=(15,4))
    subplot(121)
    plt.plot(t/1024,y)
    plt.title('analoge Funktion im Zeitbereich')
    plt.xlabel('t in s')
    plt.axis([-0.5,0.5,-3,3])
    plt.grid(True)
    
def sample_hold(data, fS=1024):
    if fS in [1,2,4,8,16,32,64,128,256,512,1024]:
        t = np.linspace(-511, 512, 1024)
        plt.figure(figsize=(15,4))
        plt.plot(t, data, label='kontinuierliches Signal')
        t1 = range(-511, 513, int(1024/fS))
        y_sample = data[np.array(range(0,1024, int(1024/fS)))]
        plt.stem(t1,y_sample, markerfmt='.', label='Abtastfolge')
        y_sh = np.repeat(y_sample,int(1024/fS))
        plt.plot(t, y_sh, label='sample&hold Signal')
        plt.grid(True)
        plt.legend(loc=4)
        plt.axis([-511, 512, min(data)-0.1, max(data)+0.1])
        return y_sh
    else:
        print('fS muss Zweierpotenz sein')
    
def sample_hold_audio(data, fS=2000):
    y_sample = data[np.array(range(0,16000, int(16000/fS)))]
    y_sh = np.repeat(y_sample,int(16000/fS))
    return y_sh
    
def analog_reko(f1=1, f2=0, f3=5, fS=30):
    if fS in [1,2,4,8,16,32,64,128,256,512,1024]:
        y = analog_sig(f1=f1, f2=f2, f3=f3)
        y1 = y
        y = np.append(y1,y)
        y = np.append(y1,y)
        fS = 3*fS
        plt.figure(figsize=(15,8))
        plt.grid(True)
        t = np.linspace(-1.5, 1.5, 3*1024)
        subplot(311)
        plt.plot(t,y, label='Originalsignal')
        plt.title('kontinuierliches Signal')
        plt.axis([-1.5,1.5,min(y),max(y)])
        t1 = np.linspace(-1.5, 1.5, fS)
        y_sample = y[np.array(range(0,3*1024, int(3*1024/fS)))]
        subplot(312)
        plt.stem(t1,y_sample, markerfmt='.')
        plt.title('Abtastwertefolge')
        plt.axis([-1.5,1.5,min(y),max(y)])
        plt.grid(True)
        subplot(313)
        y_reko = np.zeros(3072)
        for k in range(-int(len(t1)/2),int(len(t1)/2)):
            delta_reko = y_sample[k+int(len(t1)/2)]*sinc(k - fS/3 *np.array(t))
            y_reko = y_reko + delta_reko
            plt.plot(t,delta_reko)
        plt.axis([-1.5,1.5,min(y),max(y)])
        plt.title('gewichtete Spaltfunktionen')
        plt.grid(True)
        plt.xlabel('t in s')
        subplot(311)
        plt.plot(t,y_reko, label='rekonstruiertes Signal')
        plt.legend()
        plt.grid(True)
    else:
        print('fS muss Zweierpotenz sein')

    

    
#analog_reko()
#generate_analog_sig(f1=[0.5,1])
#generate_dig_sig(f1=[0.5,1], f2=[0.5,3],anz_spek=1000)
#y = analog_t(f1=1, f2=0, f3=0)
#analog_f(y, fmax=64)
#y = digital_t(f1=8, f2=0, f3=0, fS=32)
#if len(y) > 1:
#   digital_f(y)
#y = analog_sig(f1=1, f2=15)
#sample_hold(y, fS=32)
#y_kont= generate_audio(y)