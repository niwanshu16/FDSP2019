# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:17:17 2019

@author: KIIT
"""

# Making gif file

import os
import imageio
images =[]
path = os.getcwd()
files = os.listdir(path)
file =[]
for i in files:
    if i.endswith('.png'):
        file.append(i)


for filename in file:
    images.append(imageio.imread(filename))
imageio.mimsave('image.gif',images,duration = 0.40)

