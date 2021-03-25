# audibert page 195
import numpy as np
import time as t

def H1(n):
    s = 0
    for k in range(1, n+1):
        s += (-1)**(k-1)/k
    return s

def H2(n):
    s = 0
    for k in range(1, n+1):
        s += 1 / ((2*k-1)*k)
    return s/2

n = 1000

def calcul(n):
    for p in range(n, n+2):
        t0 = t.time()
        print(p, H1(2*p), H2(p), H1(2*p+1), np.log(2), t.time()-t0)
        print('--------------------------------')

calcul(n)

'''
H1(2*p+1) s'approche mieux de ln(2)
1000 0.6928972430599403 0.6928972430599386 0.6933969931848778 0.6931471805599453 0.003312349319458008
--------------------------------
1001 0.6928974926853773 0.6928974926853756 0.6933967438086923 0.6931471805599453 0.0033833980560302734
--------------------------------
100000000 0.6931471780606475 0.6931471773731642 0.6931471830606475 0.6931471805599453 533.0700035095215
'''

# n = 100000000
# temps de calcul  : 533.0700035095215 sec soit presque 10 mn