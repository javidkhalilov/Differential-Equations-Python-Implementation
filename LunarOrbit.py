# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:57:11 2016

@author: Javid
"""

import math
import numpy
import matplotlib.pyplot

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    for step in range(num_steps+1):
        x[step,0]=moon_distance*math.cos(step*2.0*math.pi/num_steps)
        x[step,1]=moon_distance*math.sin(step*2.0*math.pi/num_steps)
    return x

x = orbit()

matplotlib.pyplot.axis('equal')
matplotlib.pyplot.plot(x[:, 0], x[:, 1])
axes = matplotlib.pyplot.gca()
axes.set_xlabel('Longitudinal position in m')
axes.set_ylabel('Lateral position in m')