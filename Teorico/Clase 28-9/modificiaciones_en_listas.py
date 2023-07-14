# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:21:12 2022

@author: dafyd
"""
from typing import List

a = [1, 2]
b = a
a.append(3)

print(a, b)
c = a + b + [4]
print(a, b, c)

e = [1, 2, 3]
f = e
e = e + [4]
print(e, f)  
