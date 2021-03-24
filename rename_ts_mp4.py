# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:28:16 2020

@author: vagmark
"""

import os

startPart=0
#depends for every content
endPart=475

for i in range(startPart,endPart):
    os.rename(r'C:\Users\---ADD-YOUR USERNAME---\Downloads\media_'+str(i)+'.ts',r'C:\Users\vagmark\Downloads\media_'+str(i)+'.mp4')