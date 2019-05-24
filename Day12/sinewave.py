# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:48:10 2019

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 0 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('A nice sine wave')
plt.grid(True)
#plt.savefig('data/sinewave.png')
plt.show()
