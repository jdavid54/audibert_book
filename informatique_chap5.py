import numpy as np

def conv10to2Int(n):
    v = abs(n)
    L, p = list([]), 0
    if v==0:
        L.append(0)
    else:
        while v>0:
            v,r = divmod(v,2)
            L.insert(0,r)
        if n<0:
            L.insert(0,'-')
    return L

def conv10to2Frac(f, eps):
    '''
    si 2f <1, chiffre =0, f=2f
    sinon chiffre=1, f=2f-1
    '''
    p,g = 0,f
    L = list(['.'])
    while 2**(-p) > eps:
        #print(f)        
        p += 1
        if 2*f<1:
            L.append(0)
            f = 2*f
        else:
            L.append(1)
            f = 2*f-1
        if f==0: break        
    return L

def conv10to2(x, eps):
    v = abs(x)
    e,f = int(v), v-int(v)
    eps1 = min(eps, .5)
    
    L1 = conv10to2Int(e)
    if f != 0:
        L2 = conv10to2Frac(f, eps)
        L1.extend(L2)
    if x<0:
        L1.insert(0,'-')  # position 0
    return L1

n = -5
print(n,conv10to2Int(n))
# nombres dyadiques
n = 2**(-2)
print(n,conv10to2Frac(n,2**(-5)))
n = 0.1
eps = 2**(-10)
print(n,conv10to2Frac(n,eps))
n= -5.125
print(n,conv10to2(n,eps))

