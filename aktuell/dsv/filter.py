# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:52:40 2016

@author: Admin_1
"""

from scipy.signal import butter, freqz, lfilter
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from pylab import *
import data_resample as dr

fig = plt.figure(figsize=(12,4))
fS = 1600
fgo = 200
high = 2*fgo/fS

order = 5
b,a = butter(order,[high])
w,h = freqz(b,a)
plt.plot((fS/(2*np.pi))*w, abs(h),label='ord='+str(order))
h_flip = h[::-1]
plt.plot((fS/(2*np.pi))*w, abs(h_flip),'--', label='ord='+str(order)+' alias')

order = 1
b,a = butter(order,[high])
w,h = freqz(b,a)
plt.plot((fS/(2*np.pi))*w, abs(h),label='ord='+str(order))
h_flip = h[::-1]
plt.plot((fS/(2*np.pi))*w, abs(h_flip),'--',label='ord='+str(order)+' alias')

plt.plot([0,fS/2],[np.sqrt(0.5),np.sqrt(0.5)])
plt.legend()
plt.grid(True)
plt.title('Antialiasing-Tiefpassfilter')
plt.xlabel('f in Hz')
plt.ylabel('Verstärkung')


fig = plt.figure(figsize=(12,4))
file_name = 'C:\\WinPython\\notebooks\\sound\\mischton_8000.wav'
fS, data_in = wavfile.read(file_name)
data_in = data_in/max(max(data_in),abs(min(data_in)))
data_out = lfilter(b, a, data_in)
f = np.linspace(0,4000,len(data_out)/2)
plt.plot(f,1/len(data_in)*np.abs(fft(data_in))[0:len(data_in)/2], label='ungefiltert')
plt.plot(f,1/len(data_out)*np.abs(fft(data_out))[0:len(data_out)/2], label='gefiltert')
plt.legend()
plt.grid(True)
plt.title('Betragsspektrum')
plt.xlabel('f in Hz')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.title('Betragsspektrum')
plt.xlabel('f in Hz')
plt.ylabel('Amplitude')

dr.resample_file(data_out)
fig = plt.figure(figsize=(12,4))

file_name = 'C:\\WinPython\\notebooks\\sound\\mischton_800.wav'
fS, data_in = wavfile.read(file_name)
data_in = data_in/max(max(data_in),abs(min(data_in)))
data_out = lfilter(b, a, data_in)
f = np.linspace(0,400,len(data_out)/2)
plt.plot(f,1/len(data_in)*np.abs(fft(data_in))[0:len(data_in)/2], label='abgetastet')
plt.legend()
plt.grid(True)
plt.title('Betragsspektrum')
plt.xlabel('f in Hz')
plt.ylabel('Amplitude')
