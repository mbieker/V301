# -*- coding: utf-8 -*-
"""
V301, Durchführung am 28.11.13
Martin Bieker, Julian Surmann.
"""
from scipy import *
from uncertainties import *
import matplotlib.pyplot as plt

def lin_reg(x,y):
    N = len(x)
    sumx = x.sum()
    sumy = y.sum()
    sumxx = (x*x).sum()
    sumxy = (x*y).sum()
    m = (sumxy -  sumx*sumy/N)/(sumxx- sumx**2/N)
    b = sumy/N - m*sumx/N
    
    sy = sqrt(((y - m*x - b)**2).sum()/(N-1))
    m_err = sy *sqrt(N/(N*sumxx - sumx**2))
    b_err= m_err * sqrt(sumxx/N)
    return ufloat(m,m_err), ufloat(b,b_err)

# Messwerte wie aufgenommen, U in Volt und I in mA:

U_k= 1.68
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
I4=vI4/1000.0
I5=vI5/1000.0

print "Monozelle:"
m,b = lin_reg(I2,U2)
print "-Innenwiederstand:"
print m
print "Leerlaufspannung:"
print b
Mono_Ri = - m
Mono_U0 = b
x = linspace(0.02,0.16)
plt.plot(x, m.n*x+b.n, label = "Lineare Regression" )
plt.plot(I2,U2,'x', label = "Messwerte")
plt.xlabel('I[A]')
plt.ylabel('U[V]')
plt.xlim(0.02,0.16)
plt.legend()
plt.savefig('Plot1.png')
plt.close()


print "Rechteckausgang:"
m,b = lin_reg(I4,U4)
print "-Innenwiederstand:"
print m
print "Leerlaufspannung:"
print b

x = linspace(0,0.008)
plt.ylim(0,0.5)
plt.plot(x, m.n*x+b.n, label = "Lineare Regression" )
plt.plot(I4,U4,'x', label = "Messwerte")
plt.xlabel('I[A]')
plt.ylabel('U[V]')
plt.legend()
plt.savefig('Plot2.png')
plt.close()

print "Sinusausgang:"
m,b = lin_reg(I5,U5)
print "-Innenwiederstand:"
print m
print "Leerlaufspannung:"
print b

x = linspace(0,0.002)
plt.plot(x, m.n*x+b.n, label = "Lineare Regression" )
plt.xlim(0,0.002)
plt.plot(I5,U5,'x', label = 'Messwerte')
plt.xlabel('I[A]')
plt.ylabel('U[V]')
plt.legend()
plt.savefig('Plot3.png')

print('Fehler der direkten Messung')
print("U_0 = %s"% str(U_k *(1+ Mono_Ri/10e6)) )
print('Delta_U = %s' % str(U_k*Mono_Ri/10e6))  
plt.close()

print('Leistung der Monozelle')
P = U2*I2
R_a = U2/I2

plt.plot(R_a, P ,'x', label = 'Messwerte')
R= linspace(0,100,100)
P_th = Mono_U0.n**2 *R /(R+Mono_Ri.n)**2 
plt.plot(R,P_th, '-' ,label = "Erwarteter Leistungsverlauf") 
plt.xlabel(r"$R_a [\Omega]$")
plt.ylabel(r"$N [W]$")
plt.legend()
plt.savefig('Plot4.png')
plt.show()
 