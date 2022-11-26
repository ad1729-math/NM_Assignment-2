import numpy as np 
from Q2_a_Lagrange import F,F1,X,Y
import matplotlib.pyplot as plt


#Intial guessed values of to find the roots are taken to be 1 and 2.5 based on our observation from the data points.
#We use Netwon-Rhapson method to find the roots, 
s1=1
s2=2.5

for i in range(0,10):
    s1=s1-F(s1)/F1(s1)
    s2=s2-F(s2)/F1(s2)

print("The value of the interpolated funtion at x=2.5 is",F(2.5))
print("The roots of the interpolated funtion is",s1,s2)


