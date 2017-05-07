# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:34:08 2016

@author: Javid
"""
import numpy

earth_mass=5.97e24 #kg
moon_mass=7.35e22 #kg
gravitational_constant=6.67e-11 #Nm2/kg

def acceleration(moon_position,spaceship_position):
    #nonsense=numpy.linalg.norm(moon_position)*spaceship_position
    vector_to_moon=moon_position-spaceship_position
    vector_to_earth=-spaceship_position
    return gravitational_constant*(earth_mass/numpy.linalg.norm(vector_to_earth)**3*vector_to_earth
                                    +moon_mass/numpy.linalg.norm(vector_to_moon)**3*vector_to_moon)

acc=acceleration(2500,4500)
print(acc)

