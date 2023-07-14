# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:04:07 2022

@author: dafyd
"""

from typing import TextIO
f:TextIO = open('20primeros.txt', 'w')
for i in range(1,21):
    f.write(str(i) + '\n')
f.close()
