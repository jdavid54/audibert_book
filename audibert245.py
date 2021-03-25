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
    print(X)
    for k in range(0,N):
        Y[k+1] = Y[k]+h*F(X[k],Y[k])
    print(Y)
    return (X, Y)

F1 = lambda t, y : -0.5*y    #fonction dérivée de y(t) ou pente de y(t)
t0 = 0
y0 = 1
T = 7

for k in range(1,10,2):
    print(t0,y0,T,k)
    X, Y = Euler(F1, t0, y0, T, 10*k)
    pl.plot(X,Y, color='black', linewidth=2)

    Z = np.exp(-0.5*X)
    pl.plot(X,Z, color='red')
    pl.show()
    pl.close()

def main():
    pass

if __name__ == '__main__':
    main()
