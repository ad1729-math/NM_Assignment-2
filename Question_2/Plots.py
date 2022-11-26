import matplotlib.pyplot as plt 
import numpy as np 
from Q2_a_Lagrange import F,F1,X,Y
from Q2_e_Estimate import a,b,c,w

def F0(x):
    return (a*x**2+b*x+c)*np.exp(w*x)

x=np.linspace(-4,X[0],1000)
plt.plot(x,F(x),'r',label="Interpolated curve")
plt.plot(X,Y,'k+',label="Given data points")
plt.plot(x,F1(x),'b',label="Derivative of the interpolated funtion")
plt.plot(x,F0(x),'g',label="Generating funtion")
plt.ylim(-5,25)
plt.legend()
plt.show()

