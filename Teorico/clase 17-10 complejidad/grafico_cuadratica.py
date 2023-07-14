# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:05:04 2022

@author: dafyd
"""

import time
time.time()

import matplotlib.pyplot as plt

def cuadratica(dominio):
    
    equis:float = 0
    x=[]
    y=[]
    while equis <= dominio:
        x.append(equis)
        y.append(equis*equis)
        equis= equis + 0.1
    plt.plot(x, y)
    plt.show()
    
print(cuadratica(100.0))

