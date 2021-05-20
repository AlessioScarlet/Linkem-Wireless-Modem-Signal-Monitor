# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:40:57 2021

@author: alessiosca
"""

with open('logs.txt', mode='r') as f:
    f=f.readlines()

cont=0
tot=0
for r in f:
    tot+=int(f[cont][9])
    cont+=1

media=tot/cont
print('Total signals: ', cont)
print('Signals average: ', media)
