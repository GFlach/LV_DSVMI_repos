# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:34:46 2016

@author: Admin_1
"""

import numpy as np
import matplotlib.pyplot as plt


def pca(x):
    print(x.shape)
    mu = np.mean(x, axis=1)
    print(mu)
    xmf = np.vstack(mu) - x
    xcov = 1/x.shape[1]*np.dot(xmf, np.transpose(xmf))
    w, v = np.linalg.eigh(xcov)
    w_sorted = np.sort(w)[::-1]
    v_sorted = v[:, w_sorted.argsort()]


    return mu, xmf, xcov, w_sorted, v_sorted

num1 = np.array([0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,0,
             1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,
             0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,
             1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,
             1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,
             1,1,1,1,0,1,1,0,1,1,0,1,1,1,1]).reshape((10 ,15))

plt.figure(1)
for i in range(num1.shape[0]):
    plt.subplot(2, 5, i+1)
    # b1 = np.flipud(np.transpose(num[i,:].reshape((5,3))))
    b1 = np.flipud(np.transpose(num1[i, ::-1].reshape((5, 3))))
    plt.imshow(b1.T, origin='lower', cmap=plt.cm.gray_r,
               interpolation='nearest')
    plt.xticks([])
    plt.yticks([])

plt.subplot(2, 5, 3)
plt.title('Ziffernmuster')

mu, xmf, xcov, w, v = pca(np.transpose(num1))

plt.figure(2)
plt.imshow(np.flipud(np.transpose(mu[::-1].reshape((5, 3)))).T, origin='lower',
           cmap=plt.cm.gray_r, interpolation='nearest')
plt.xticks([])
plt.yticks([])
plt.title('Mittelwertbild')

plt.figure(3)
for i in range(v.shape[1]):
    plt.subplot(3, 5, i+1)
    b1 = np.flipud(np.transpose((-1)*v[::-1, i].reshape((5, 3))))
    plt.imshow(b1.T, origin='lower', cmap=plt.cm.gray_r,
               interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
V = v[:, 0:14]
X1 = np.dot(np.transpose(V), xmf)
rec = np.vstack(mu)+np.dot(V, X1)

plt.figure(4)
for i in range(rec.shape[1]):
    plt.subplot(2, 5, i+1)
    # b1 = np.flipud(np.transpose(num[i,:].reshape((5,3))))
    b1 = np.flipud(np.transpose(rec[::-1, i].reshape((5, 3))))
    plt.imshow(b1.T, origin='lower', cmap=plt.cm.gray_r,
               interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
