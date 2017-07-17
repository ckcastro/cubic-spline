#  Natural Cubic  Spline 
from numpy import *
from pylab import *
from scipy import *
from math import *

x=np.array([0.5,1.0,1.5,2.0])
a=np.array([6.8,3.00,1.5,0.75])

n=len(x) #n+1
h=np.array(zeros((n-1,1)))
alfa=np.array(zeros((n,1)))
l=np.array(zeros((n,1)))
mu=np.array(zeros((n,1)))
z=np.array(zeros((n,1)))
b=np.array(zeros((n,1)))
c=np.array(zeros((n,1)))
d=np.array(zeros((n,1)))

for i in range(0,n-1,1):
	h[i]=x[i+1]-x[i]

print "h=",h.T

for i in range(1,n-1,1):
	alfa[i]=(3/h[i])*(a[i+1]-a[i])-(3/h[i-1])*(a[i]-a[i-1])
print "alfa=", alfa.T

l[0]=1.0
mu[0]=0.0
z[0]=0.0

for i in range(1,n-1,1):
	l[i]=(2.0*(x[i+1]-x[i-1]))-((h[i-1])*mu[i-1])
	mu[i]=h[i]/l[i]
	z[i]=(alfa[i]-(h[i-1]*z[i-1]))/l[i]

l[n-1]=1.0
z[n-1]=0.0
print "l=",l.T,"\nz=",z.T,"\nmu=",mu.T
#c[n-1]=0.0

A=matrix(zeros((n,n)))
A[0,0]=1
A[-1,-1]=1
for i in range(1,n):
	A[i,i-1]=h[i-1]
        A[i,i]=2.0*(h[i-1]+h[i])
        A[i,i+1]=h[i]

b=matrix(zeros((n+1,1)))
for i in range(1,n):
	b[i]=((3/(h[i]))*(a[i+1]-a[i]))-((3/(h[i-1]))*(a[i]-a[i-1]))

c=linalg.solve(A,b)

#for i in range(n-1,0,-1):
#	c[i]=z[i]-mu[i]*c[i+1]
#	b[i]=(a[i+1]-a[i])/h[i] - h[i]*(c[i+1]+(2.0*c[i]))/3.0
#	d[i]=(c[i+1]-c[i])/(3.0*h[i])

#print "a=%s, \nb=%s ,\nc=%s,\nd=%s" %(a,b.T,c.T,d.T)

#def S(x,i):
#	return[i]+b[i]*(x-t[i])+c[i]*(x-t[i])**2+d[i]*(x-t[i])**3

#for i in range(0,1):
#	xi=linspace(t[i],t[i+1],10**-3)
#	yi=S(xi,i)
#	plot(xi,yi)
#	hold(True)
#show()
	

