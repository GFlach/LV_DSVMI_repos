# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:51:59 2016

@author: Admin_1
"""

    
def protokoll(nb_in,nb_out):
    f1 = open(nb_in)
    f2 = open(nb_out, 'w')
    liste = []
    new_list = []

    mdc = 1
    mdc_count = 0
    start = []
    stop = []
    j = 0
    for line in f1:
        if line == '   "cell_type": "markdown",\n':
            if (mdc == 0):
                liste.append('  {\n')
                j = j + 1

            mdc = 1

        if line == '   "cell_type": "code",\n':
            if (mdc == 1):
                mdc = 0
                j = j - 1
                liste.pop()

        if line == ' ],\n':
            liste.pop()
            liste.append('  }\n')
            mdc = 1

        if mdc == 1:
            liste.append(line)
            j = j + 1

    for i in range(j):
        if liste[i] == '  {\n':
            start.append(i)
            mdc_count = mdc_count + 1

        if liste[i] == '  },\n':
            stop.append(i)

        if liste[i] == '  }\n':
            stop.append(i)
            break

    for k in range(start[0]):
        new_list.append(liste[k])

    for i in range(mdc_count):
        for ln in range(start[i], stop[i]):
            if  '##### Protokoll' in liste[ln]:
                liste[ln] = ''
                for ln in range(start[i], stop[i]):
                    new_list.append(liste[ln])

                new_list.append('  },\n')

    new_list.pop()

    for k in range(stop[mdc_count-1],len(liste)):
        new_list.append(liste[k])

    for k in range(len(new_list)):
        print(new_list[k], file=f2)

    f1.close()
    f2.close()