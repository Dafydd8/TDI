# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:40:37 2022

@author: dafyd
"""

import turtle as t
t.clearscreen()
t.speed(0)

#a)
def poligono(d:float, n:int):
    for i in range(n):
        t.forward(d)
        t.left(360/n)

#poligono(0.1,10000)

#b)
def espiral(d:float, n:int, incr:float):
    if d <= 0:
        pass
    else:
        t.forward(d)
        t.left(360/n)
        espiral(d-incr, n, incr)
        
espiral(110, 8,0.5)

 
t.mainloop()
t.bye()