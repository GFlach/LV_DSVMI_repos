# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:02:01 2016

@author: Flach
"""

import numpy as np

# Funktion zur LDA-Analyse
# k_anz: Klassenanzahl
# m_anz: Merkmalanzahl
# m: Liste der Musterbeschreibungen (Merkmal, Klasse)


def lda(m_anz, k_anz, m):
    # Klassenmittelwerte berechnen
    mw = np.zeros((k_anz, 2))
    for i in range(k_anz):
        data = np.append(m[:, 0][m[:, 2] == i+1], m[:, 1][m[:, 2] == i+1])
        data = np.reshape(data, (2, m_anz[i]))
        mw[i] = np.mean(data, axis=1)
    # Gesamtmittelwerrt berechnen
    data = np.reshape(np.append(m[:, 0], m[:, 1]), (2, len(m)))
    mw_ges = np.mean(data, axis=1)
    # Scattermatrix (within-class) berechnen
    S_W = np.zeros((2, 2))
    for cl, mv in zip(range(1, 3), mw):
        s = np.zeros((2, 2))
        data = np.append(m[:, 0][m[:, 2] == cl], m[:, 1][m[:, 2] == cl])
        data = np.reshape(data, (2, m_anz[cl-1])).T
        for row in data:
            row, mv = row.reshape(2, 1), mv.reshape(2, 1)
            s += (row-mv).dot((row-mv).T)
            S_W += s
    # Scattermatrix (between-class) berechnen
    S_B = np.zeros((k_anz, k_anz))
    for i, mean_vec in enumerate(mw):
        n = m_anz[i]
        mean_vec = mean_vec.reshape(2, 1)         # make column vector
        mw_ges = mw_ges.reshape(2, 1)             # make column vector
        S_B += n * (mean_vec - mw_ges).dot((mean_vec - mw_ges).T)

    eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
#    for i in range(len(eig_vals)):
#        eigvec_sc = eig_vecs[:, i].reshape(2,1)
    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
    # Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)

    k = 2
    W = eig_pairs[0][1].reshape(2, 1)
    for i in range(1, k):
        W = np.hstack((W, eig_pairs[i][1].reshape(2, 1)))
    # Transformation der Daten in den neuen Unterraum
    d = m[:, :2]
    data_lda = d.dot(W)
    data_lda = np.append(data_lda.T, m[:, 2])
    data_lda = data_lda.reshape(3, sum(m_anz))
    data_lda = data_lda.T

    return data_lda

# Funktion zur PCA-Analyse
# m_anz: Merkmalanzahl
# k_anz: Klassenanzahl
# m: Liste der Musterbeschreibungen (Merkmal, Klasse)


def pca(m_anz, k_anz, m):
    S_all = np.zeros((k_anz, k_anz))
    data = np.reshape(np.append(m[:, 0], m[:, 1]), (2, len(m))).T
    # Gesamtmittelwert berechnen
    mw_ges = np.mean(data, axis=0)
    mv = mw_ges.reshape(2, 1)
    for row in data:
        row = row.reshape(2, 1)
        S_all += (row-mv).dot((row-mv).T)
    # Berechnung der Eigenwerte
    eig_vals, eig_vecs = np.linalg.eig(S_all)
    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
    # Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
    k = 2
    W1 = eig_pairs[0][1].reshape(2, 1)
    for i in range(1, k):
        W1 = np.hstack((W1, eig_pairs[i][1].reshape(2, 1)))

    d = m[:, :2]
    data_pca = d.dot(W1)
    data_pca = np.append(data_pca.T, m[:, 2])
    data_pca = data_pca.reshape(3, sum(m_anz))
    data_pca = data_pca.T

    return data_pca
