# -*- coding: utf-8 -*-
"""
Time series tools

Created on Fri Jun  9 16:28:18 2017

@author: Pablo Rodríguez-Sánchez
"""

#%% Load dependencies
from math import sqrt
from numpy import zeros, append


#%% Methods
def mean(x):
    """
    Mean value of x
    
    Returns the mean value of a row-shaped array.

    Args:
        x: a row-shaped numeric array.

    Returns:
        A float containing the mean value.

    Raises:
        This function raises no custom exceptions.
    """    
    return sum(x)/len(x)
    
def cov(x,y):
    """
    Covariance of x and y   
    
    Returns the covariance of two row-shaped arrays.
    
        Args:
        x: a row-shaped numeric array.
        y: a row-shaped numeric array.
        
    Returns:
        A float containing the covariance value.

    Raises:
        This function raises no custom exceptions.
    """
    dx = x - mean(x)
    dy = y - mean(y)
    return mean(dx*dy)

def var(x):
    """
    Variance of x
    
    Returns the variance of a row-shaped array.

    Args:
        x: a row-shaped numeric array.

    Returns:
        A float containing the variance value.

    Raises:
        This function raises no custom exceptions
    """
    return cov(x,x)

def sd(x):
    """
    Standard deviation of x
    
    Returns the standard deviation of a row-shaped array.

    Args:
        x: a row-shaped numeric array.

    Returns:
        A float containing the standard deviation value.

    Raises:
        This function raises no custom exceptions
    """
    return sqrt(var(x))

def corr(x,y):
    """
    Returns correlation of arrays x and y
    
    Returns the correlation of two row-shaped arrays
    
        Args:
        x: a row-shaped numeric array.
        y: a row-shaped numeric array.
        
    Returns:
        A float containing the correlation value.

    Raises:
        This function raises no custom exceptions.
    """
    return cov(x,y)/(sd(x)*sd(y))