from math import *
def integrand(x):
    x=float(x)
    return sin(x)*cos(x)
def trap(i,f,d):
    i,f,d=float(i),float(f),int(d)
    f_i,f_f=integrand(i),integrand(f)
    dx=(f-i)/float(d)
    x=i
    s=0.0
    for k in range(1,d):
        x=x+dx
        s+=integrand(x)
    s*=dx
    trap=(f_i+f_f+s)*dx/2.0
    trap+=s
    return trap
xi,xf,division=(0.0,1.0,1000)
print trap(xi,xf,division)
