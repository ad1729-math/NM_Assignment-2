import numpy as np 
from Q2_a_Lagrange import F,X,Y
import matplotlib.pyplot as plt

def Integral(x):
    a,b=0,x #These are the given limits for the interpolated funtion

    n=200   #Number of bins used for the intergration 
    D=(b-a)/(3*n)
    h=(b-a)/n
    sum_simps=(F(a)+F(b))*D

    for i in range(1,n):
       w=(3-(-1)**i)
       sum_simps=sum_simps+D*F(a+i*h)*w

    return sum_simps 


print("The value of the integral at x=4 is=",Integral(4))
#The plot of the funtion "Integral(x)" that we get by integrating the interpolated polynomial form 0 to x

x=np.linspace(0,X[0],100)
plt.plot(x,Integral(x),'r',label="Intergral")
plt.plot(x,x*0+5,'b',label="y=5")
plt.legend()
plt.show()

#Now to find where the function Integral becomes 5 we use Newton-Rhapson method  
#s=4 (initial guess), as from the graph we seen the root is a little lesser than 4.

print("Hold tight, it will take quite a bit of time")

s=4
for i in range(0,25):
   s=s-(Integral(s)-5)/F(s) 

print("The value of x where the integral is 5 is=",s)
