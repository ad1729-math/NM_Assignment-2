import numpy as np 
import math as m 

def f(x):
    return x*m.log(x)-x
a,b=1,3 
#Trapizoidal method 

n1=100 
h=(b-a)/n1
sum_trap=(f(a)+f(b))*h/2

for i in range(1,n1):
    sum_trap=sum_trap+f(a+h*i)*h

print("Integration from 1 to 3 using Trapizoidal MEthod is ",sum_trap)

#Simpson's method 
n2=100
D=(b-a)/(3*n2)
sum_simps=(f(a)+f(b))*D

for i in range(1,n2):
    w=(3-(-1)**i)
    sum_simps=sum_simps+D*f(a+i*h)*w

print("The integration using Simmpson's 1-3rd method is ",sum_simps) 

