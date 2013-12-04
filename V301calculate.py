# -*- coding: utf-8 -*-
"""
V301, Durchführung am 28.11.13
Martin Bieker, Julian Surmann.
"""
from scipy import *
from uncertainties import *
import matplotlib.pyplot as plt


# Messwerte wie aufgenommen, U in Volt und I in mA:

U2=array([1.42, 1.395, 1.37, 1.32, 1.30, 1.23, 1.16, 1.04, 0.86, 0.61, 0.082])
vI2=array([23, 25.9, 28.5, 31.9, 33.5, 39.5, 45, 56, 72, 93, 139])
U3=array([2.07, 2.09, 2.15, 2.19, 2.26, 2.35, 2.42, 2.58, 2.718, 2.91, 3.73])
vI3=array([34.5, 36, 40, 43, 48.5, 55.5, 63, 77.5, 93.5, 125, 195])
U4=array([0.395, 0.39, 0.3825, 0.375, 0.3625, 0.3475, 0.3275, 0.3, 0.2525, 0.19, 0.105])
vI4=array([1.4, 1.46, 1.61, 1.75, 1.97, 2.25, 2.62, 3.05, 3.6, 4.7, 6.2])
U5=array([1.525, 1.5125, 1.5, 1.48, 1.455, 1.42, 1.37, 1.28, 1.13, 0.84, 0.5])
vI5=array([0.230, 0.245, 0.2725, 0.296, 0.305, 0.361, 0.44, 0.57, 0.81, 1.13, 1.64])
# Umwandlung von I in SI-Einheit.
I2=vI2/1000.0
I3=vI3/1000.0
I4=vI3/1000.0
I5=vI5/1000.0

plt.plot(I2,U2,'x')
plt.title('$U_K = f(I)$ fuer die Monozelle')
plt.xlabel('I[A]')
plt.ylabel('U[V]')
plt.show()

