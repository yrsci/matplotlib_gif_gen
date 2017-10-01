#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:42:42 2017

@author: Yv
"""

"""
Trying out polar plots using matplotlib.pyplot.polar.
"""

import matplotlib.pyplot as plt
import numpy as np
import imageio

theta_vals = np.arange(0.0,2*np.pi,0.075)

filenames = []

r_big_vals = []
r_small_vals = []
for i, val in enumerate(theta_vals):
    fig = plt.figure()
    r_big = 3.2 + np.sin(5*theta_vals[i] + np.pi/6)
    r_big_vals.append(r_big)
    r_small = 0.6 + np.sin(5*theta_vals[i] + np.pi/6)
    r_small_vals.append(r_small)
    plt.polar(theta_vals[:i+1], r_big_vals, "-")
    plt.polar(theta_vals[:i+1], r_small_vals, "-")
    
    # Save current plot as .png file (in the same directory) & append its name 
    # to a list of image filenames:
    filename = "cardioid" + str(i) + ".png"
    plt.savefig(filename)
    filenames.append(filename)
    
    # Close the current plot before generating the next one (to save memory)
    plt.close()

# Generate a .gif using the plots exported by matplotlib
del filenames[::2]
frames = []

for file in filenames:
    frames.append(imageio.imread(file))
imageio.mimsave("cardioid.gif", frames)
