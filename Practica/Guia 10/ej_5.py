# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:58:48 2022

@author: dafyd
"""
import turtle as t
t.clearscreen()
t.speed(0)

def cuadrado(d):
    for i in range(4):
        t.forward(d)
        t.left(90)

def espiral_cuadrados_rec(d:float, n:int, incr:float):
    if d<=0:
        pass
    elif n == 1:
        cuadrado(d)
    else:
        cuadrado(d)
        t.right(360/n)
        espiral_cuadrados_rec(d-incr, n, incr)
        
espiral_cuadrados_rec(200, 4, 1)

def espiral_cuadrados_iter(d:float, n:int, incr:float):
    i:float = d
    while i > 0:
        cuadrado(i)
        t.right(360/n)
        i = i-1
        n = n - 1
        
#espiral_cuadrados_iter(200, 100, 2)

t.mainloop()
t.bye()
    