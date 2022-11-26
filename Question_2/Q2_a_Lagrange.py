import numpy as np 
import math as m 
import matplotlib.pyplot as plt 

Data=np.loadtxt("Data file.dat",unpack=True)

X=Data[0]
Y=Data[1]

def F(x):
    sum=0 
    for i in range(len(X)):
        prod=1
        for j in [h for h in range(len(X)) if h!=i]:
                prod=prod*(x-X[j])/(X[i]-X[j])
        sum=sum+Y[i]*prod
    return sum

def F1(x):
    sum=0
    for i in range(len(X)):
       g=1 
       sum1=0
       for j in range(len(X)):
            if j==i:
                continue
            g=g*(X[i]-X[j])       
            prod=1
            for r in range(len(X)):
                if r==i or r==j:
                    continue
                prod=prod*(x-X[r])
            sum1=sum1+prod 
       sum=sum+Y[i]*sum1/g
    return sum



