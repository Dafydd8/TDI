# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:25:37 2022

@author: dafyd
"""

def fibonacci(n:int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(7))