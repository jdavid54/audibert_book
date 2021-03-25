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

def yprime(t,y):
    r = 0.1
    #K = 1000
    return r*y*(1-y/K)

t0 = 0
y0 = 1
T = 12
K = 1000

for j in range(0,9):
    N = 2000
    y0 = 250*j
    X,Y = Euler(yprime, t0, y0, T, N)
    if y0==1000:
        pl.plot(X,Y, 'r', linewidth=2)
    else:
        pl.plot(X,Y, 'b', linewidth=2)

#pl.plot(X,K*np.ones(N+1), color='red', linewidth=2)
pl.show()
pl.close()

def main():
    pass

if __name__ == '__main__':
    main()
