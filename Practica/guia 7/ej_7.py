# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:06:35 2022

@author: dafyd
"""
from typing import List
def bubble_sort(ls:List[int]) -> List[int]:
    for i in range(len(ls)):
        for j in range(len(ls)-1):
            print(j)
            if ls[j] > ls[j + 1]:
                (ls[j], ls[j+1]) = (ls[j+1], ls[j])
    return ls
print(bubble_sort([3,8,1,9,6,8,2,3,4,5]))
                        
                        