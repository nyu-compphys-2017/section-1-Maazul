# This is a python file! The '#' character indicates that the following line is a comment.
from __future__ import division
import numpy as np

#Implement the Riemann Sum approximation for integrals.

def riemann(a, b, N, y):

    w = (b - a) / N 
    #Defines width of the function

    x_vals = np.arange(a + w, b + w, w) 
    #Assigns all right end x values of all intervals to x_vals

    y_values = y(x_vals)
    #Assigns all y values to fn_values

    result = np.sum(w * y_values)
    #sums the area of all intervals and stores into result

    return result

# Note: Use lambda to input a function in the y argument of riemann(a, b, N, y).
