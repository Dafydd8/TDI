# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:50:03 2022

@author: dafyd
"""

def suma_pos(xs):
    if len(xs) == 0:
        return 0
    elif len(xs) == 1:
        if xs[0] > 0:
            return xs[0]
        else:
            return 0
    else:
        if xs[0] >0:
            return xs[0] + suma_pos(xs[1:])
        else:
            return suma_pos(xs[1:])
        
print(suma_pos([1,2,-3,-4,4,-5]))
        
            