# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:20:04 2022

@author: dafyd
"""

import turtle as t

t.forward(100)

def cuadrado(d:float):
    for i in range(4):
        t.forward(d)
        t.left(90)

def montana(d:float):
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)
    t.right(120)
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)
    
t.mainloop()
t.bye()