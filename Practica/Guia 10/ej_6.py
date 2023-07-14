# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:27:01 2022

@author: dafyd
"""

import turtle as t

t.left(90)

def arbol ( altura : float , nivel : int ) :
    if -1< nivel <1:
        t.pensize(1)
        t.pencolor('red')
    elif 0<nivel<4:
        t.pensize(2)
        t.pencolor('green')
    else:
        t.pensize(3)
        t.pencolor('brown')
    t . forward ( altura )
    if nivel >0 and altura >1:
        t . left (30)
        arbol ( altura /2 , nivel -1)
        t . right (30)
        arbol ( altura /2 , nivel -1)
        t.right(30)
        arbol ( altura /1.8 , nivel -1)
        t . left (30)
    t.penup()
    t . backward ( altura )
    t.pendown()
    
arbol(100,5)

t.mainloop()
t.bye()