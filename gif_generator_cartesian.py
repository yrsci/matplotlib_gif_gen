#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:03:55 2017

@author: Yv
"""

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
    
    def expon(x, A=1.0):
        exp_yval = A * (np.e**x)
        return exp_yval
    
    if func_name == "line":
        return line(x, *args, **kwargs)
    if func_name == "quad":
        return quad(x, *args, **kwargs)
    if func_name == "exp":
        return expon(x, *args, **kwargs)
    else:
        return None

# Generate an array of x values:
xvals = np.arange(-10.0, 20.0, 1.0)
yvals = []

# Change the desired type of function to generate by attributing either "line"
# or "quad" to func_type:
func_type = "line"

function_names = {
        "quad" : "a quadratic function",
        "line" : "a linear function",
        "exp" : "an exponential function"
        }

filenames = []

for i, x in enumerate(xvals):
    fig = plt.figure()
    y = func(func_type, x)
    yvals.append(y)
    plt.plot(xvals[:i+1], yvals, "*")
    plt.title("Generating " + function_names[func_type] + " using matplotlib")
    
    # Generate axis values based on the xvals array
    plt.xlim(xvals[0]-1,xvals[-1]+1)
    if func_type == "line":
        plt.ylim(func(func_type,xvals[0]-1), func(func_type, xvals[-1]+1))
    else:
        plt.ylim(func(func_type, np.sort(abs(xvals))[0]-1), func(func_type, np.sort(abs(xvals))[-1]+1))
    
    # Save current plot as .png file (in the same directory) & append its name 
    # to a list of image filenames:
    filename = func_type + "_" + str(i) + ".png"
    plt.savefig(filename)
    filenames.append(filename)
    
    # Close the current plot before generating the next one (to save memory)
    plt.close()

# Generate a .gif using the plots exported by matplotlib
frames = []

for file in filenames:
    frames.append(imageio.imread(file))
imageio.mimsave(func_type + ".gif", frames)
