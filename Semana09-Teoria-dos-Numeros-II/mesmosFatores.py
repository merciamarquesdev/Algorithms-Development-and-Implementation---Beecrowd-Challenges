C = []
F = []

def geraCrivo(n,C):
    C.append(0)
    for i in range(1,n+1):
        C.append(i)
    t = 2
    for i in range(1,int(n/2)+1):
        C[t] = 2
        t += 2
    for i in range(3,int(abs((n)**(1/2)))+1):
        if(C[i] == i):
            t = i*i
            d = i+i
            while(t <= n):
                if(C[t] == t):
                    C[t] = i
                t += d
    return C 

def fatora(n,crivo,F,nf):
    if(n == 1):
        F = [0]
    else:
        while(n != 1):
            F.insert(nf,crivo[n])
            nf += 1
            n = int(n/crivo[n])
    return F

def mesmosFatores(C,F):
    n = 10**7
    nf = 0
    crivo = geraCrivo(n,C)
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        fatores = fatora(n,crivo,F,nf)
        print(n*fatores[0])
        nCasos -= 1

mesmosFatores(C,F)
