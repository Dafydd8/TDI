# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:05:04 2022

@author: dafyd
"""
from typing import List
import time
time.time()

import matplotlib.pyplot as plt

def sumatoria(n):
    vr = 0
    i = 1
    while i <= n:
        vr = vr + i
        i = i + 1
    return vr

def lista_sumatorias_v1(n):
    vr = []
    i = 1
    while i<=n:
        vr.append(sumatoria(i))
        i = i + 1
    return vr

def lista_sumatorias_v2(n):
    vr = []
    i = 1
    s = 1
    while i<n:
        vr.append(s)
        i = i + 1
        s = s + 1
    return vr   

n:int = 0
ns:List[int] = []
ts:List[float] = []
while n<=2000:
    comienzo:float = time.time()
    lista_sumatorias_v1(n)
    t:float = time.time() - comienzo
    ns.append(n)
    ts.append(t)
    n = n + 10
plt.plot(ns, ts)
plt.xlabel('n')
plt.ylabel('tiempo')
plt.show


