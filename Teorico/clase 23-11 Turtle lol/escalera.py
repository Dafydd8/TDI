# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:28:05 2022

@author: dafyd
"""
import turtle as t
t.shape('arrow')

def escalera(d:float, n:int):
    if n == 0:
        pass
    else:
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.right(90)
        escalera(d, n-1)
        
def escalera2(d:float, k:float):
    if d <= 0:
        pass
    else:
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.right(90)
        escalera(d - k, k)
        
def espiral(d:float, k:float):
    if d<=0:
        pass
    else:
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        espiral(d-k, k)
      
       
def copito(d:int, k:int):
    if k == 0:
        t.forward(d)
    else:
        copito(d/3, k-1)
        t.left(60)
        copito(d/3, k-1)
        t.right(120)
        copito(d/3, k-1)
        t.left(60)
        copito(d/3, k-1)

def copito_completo(d, k):
    t.speed(0)
    for i in range(3):
        copito(d, k)
        t.right(120)
    
copito_completo(200,3)
t.penup()
t.goto(-200,200)
t.pendown()
copito_completo(150,3)
#espiral(200, 10)
t.mainloop()
t.bye()