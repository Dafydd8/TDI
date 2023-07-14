# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:58:48 2022

@author: dafyd
"""
from typing import Set
#a)
def indice_jaccard(c:Set[type], d:Set[type]) -> float:
    a:Set[type] = c | d
    b:Set[type] = c & d
    return len(b) / len(a)
#print(indice_jaccard({1,2,3}, {3,4}))

#b)
def k_shingles(t:str, x:int) -> set:
    res:Set[str] = set()
    for i in range(len(t)-x+1):
       res.add(t[i:i + x]) 
    return res
#print(k_shingles('hola mundo', 5))

#c)
def similitud_textos(t1:str, t2:str, k:int) -> float:
    ct1:Set[str] = k_shingles(t1, k)
    ct2:Set[str] = k_shingles(t2, k)
    return indice_jaccard(ct1, ct2)
print(similitud_textos("hola mundo", 'hola mu', 5))