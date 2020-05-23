import numpy as np 
import matplotlib.pyplot as plt 


def F(x,y,z):
    return np.array([
        x**2 + y**2 + y**2,
        x*y*z,
        z**2
    ])


plt