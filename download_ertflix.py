# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:16:57 2020

@author: vagmark
"""
import time

startPart=0
#depends for every content
endPart=475

import webbrowser
for i in range (startPart,endPart):
    #your link
    webbrowser.open('https://mediastream.ert.gr/vodedge/_definst_/mp4:dvrorigingr/2021/movies/TAKEN.mp4/media_'+str(i)+'.ts')  
    time.sleep(0.3)