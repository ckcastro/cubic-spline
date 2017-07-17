# Natural cubic spline
# Claudia Castro @ CIMAT
# Fall 2011

from numpy import *
from pylab import *
from scipy import *
from math import *

#Set input points
t=np.array([0.5,1.0,1.5,2.0])
y=np.array([6.8,3.00,1.5,0.75])

#PAJARO
#t = np.array([0.9, 1.3, 1.9 , 2.1, 2.6, 3.0, 3.9, 4.4 , 4.7 , 5.0, 6.0 , 7.0, 8.0 , 9.2 , 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
#y = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4 , 0.9 , 0.7 , 0.6 , 0.5 , 0.4 , 0.25])

n=len(t)-1 
b=np.array(zeros((n,1)))
d=np.array(zeros((n+1,1)))
h=np.array(zeros((n,1)))

for i in range(0,n,1):
	h[i]=t[i+1]-t[i]

A=np.array(zeros((n+1,n+1)))
A[0,0]=1
A[-1,-1]=1
for i in range(1,n):
	A[i,i-1]=h[i-1]
        A[i,i]=2.0*(h[i-1]+h[i])
        A[i,i+1]=h[i]

b=np.array(zeros((n+1,1)))
for i in range(1,n):
	b[i]=((3/(h[i]))*(y[i+1]-y[i]))-((3/(h[i-1]))*(y[i]-y[i-1]))

#SPLINE CUBICO NATURAL
c=linalg.solve(A,b)

for i in range(n):
	b[i]=((y[i+1]-y[i])/h[i])-(h[i]*(c[i+1]+2.0*c[i]))/3.0
        d[i]=(c[i+1]-c[i])/(3*h[i])

print "h=",h.T,"\na=",y.T,"\nb=",b.T,"\nc=",c.T,"\nd=",d.T

def S(x,i):
	return y[i]+b[i]*(x-t[i])+c[i]*(x-t[i])**2+d[i]*(x-t[i])**3

for i in range(n):
	xi=linspace(t[i],t[i+1],1000)
	yi=S(xi,i)
	plot(xi,yi)
	hold(True)

plot(t,y,"*")
xlabel(r"$t-axis$"); ylabel(r"$y-axis$")
title(r"$Cubic$ $Spline$  $(natural) $"); show()
