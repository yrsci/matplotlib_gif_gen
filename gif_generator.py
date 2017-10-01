#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import imageio

def func(func_name, x, *args, **kwargs):
    """
    Generates one of a selection of functions depending on input 
    func_name, using the input x as the independent variable(s). Can also
    take more arguments to use as coefficients in the function formulae.
    """
    
    def line(x, m=1.0, c=0.0):
        line_yval = m * x + c
        return line_yval
    
    def quad(x, a=1.0, b=1.0, c=0.0):
        quad_yval = a*(x**2) + b*x + c
        return quad_yval
    
    if func_name == "line":
        return line(x, *args, **kwargs)
    if func_name == "quad":
        return quad(x, *args, **kwargs)
    else:
        return None

# Generate an array of x values:
xvals = np.arange(0.0, 20.0, 1.0)
yvals = []

func_type = "line"

filenames = []

for i, x in enumerate(xvals):
    fig = plt.figure()
    y = func(func_type, x)
    yvals.append(y)
    plt.plot(xvals[:i+1], yvals, "*")
    plt.title("Generating a " + func_type + " using matplotlib")
    
    # Generate axis values based on the xvals array
    plt.xlim(xvals[0]-1,xvals[-1]+1)
    plt.ylim(func(func_type, np.sort(abs(xvals))[0]-1), func(func_type, np.sort(abs(xvals))[-1]+1))
    
    # Save current plot as .png file (in the same directory) & append its name 
    # to a list of image filenames:
    filename = func_type + "_" + str(i) + ".png"
    plt.savefig(filename)
    filenames.append(filename)
    
    # Close the current plot before generating the next one (to save resources)
    plt.close()

# Generate a .gif using the plots exported by matplotlib
frames = []

for file in filenames:
    frames.append(imageio.imread(file))
imageio.mimsave(func_type + ".gif", frames)
