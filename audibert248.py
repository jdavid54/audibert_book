#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     01/03/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import pylab as pl

def Euler(F, t0, y0, T, N):
    h = T/N
    X = np.linspace(t0, T, N+1)
    Y = np.zeros(N+1)
    Y[0]= y0
    #print(X)
    for k in range(0,N):
        Y[k+1] = Y[k]+h*F(X[k],Y[k])
    #print(Y)
    return (X, Y)

def yprime(t,y):                # ou encore yprime = lambda t,y : np.sin(t*y)
    return np.sin(t*y)

t0 = 0
#y0 = 4
T = 2*np.pi
min = 0
max = T
#K = 1000
N = 2000
#for y0 in np.linspace(-1, 1, 10):
for y0 in (0.2,0.3,0.4,0.5,1,1.5,2,2.5,3,-1,-2,-3):
#for y0 in (1,1.5,2,3,4,5):
    X,Y = Euler(yprime, t0, y0, T, N)
    Xm,Ym = Euler(yprime, t0, y0, -T, N)
    pl.plot(X,Y,'b',Xm,Ym,'b',  linewidth=2)
pl.show()
pl.close()

def main():
    pass

if __name__ == '__main__':
    main()
