import numpy as np 
import math as m 
from Q2_a_Lagrange import X,Y 
import matplotlib.pyplot as plt 

Sgm=1/X #Reciprocals
n=len(X)

Prod=1
for i in range(n):
    Prod=Prod*X[i]

S=0 
for i in range(n):
    S=S+Sgm[i]

S2=0 
for i in range(n):
    S2=S2+Sgm[i]**2 

S3=0 
for i in range(n):
    S3=S3+Sgm[i]**3 

def g(i):
    p=1
    for j in range(n):
        if j!=i:
            p=p*(X[i]-X[j])
    return p 


A1=0
for i in range(n):
    A1+=Y[i]/g(i)/X[i]
A1=A1*Prod*(-1)**(n-1)

A2=0
for i in range(n):
    A2+=Y[i]/g(i)*(S-Sgm[i])/X[i]
A2=A2*Prod*(-1)**(n-2)

A3=0
for i in range(n):
    A3+=(Y[i]/g(i))*((S-Sgm[i])**2-(S2-Sgm[i]**2))/X[i]
A3=A3*Prod/2*(-1)**(n-3)

A4=0
for i in range(n):
    A4+=Y[i]/(g(i)*X[i])*((S-Sgm[i])**3-3*(S2-Sgm[i]**2)*(S-Sgm[i])+2*(S3-Sgm[i]**3))
A4=A4*Prod*1/6*(-1)**(n-4)

def f(x):
    return A1*x**3/6-A2*x**2/2+A3*x-A4
def f1(x):
    return A1*x**2/2-A2*x+A3

#x=np.linspace(0,0.5,1000)
#plt.plot(x,f(x),'r')
#plt.ylim(-0.5,0.5)
#plt.show()

#From this graph we fin there is a solution of x/w in the interval of 0,0.5. We find it using Newton-Rhapson method.
s=0.3 #Intitial guess 

for i in range(20):
    s=s-f(s)/f1(s)

w=s #This is the value of w
a=A1*w**2/2-A2*w+A3 
b=-(A1*w-A2) 
c=A1

print("The values of a,b,c,w are reespectively",a,b,c,w)