import math 

C = []
P = []

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

def geraPrimos(n,crivo,P):
    np = 0
    P.insert(0,0)
    for i in range(2,n+1):
        if(crivo[i] == i):
            np += 1
            P.insert(np,i)
    return P

def fatora(n,P,np,F):
    nf = 0
    for i in range(1,np):
        while(n%P[i] == 0):
            nf += 1
            F[nf] = P[i]
            n = n/P[i]
        if(n == 1 or P[i] >= int(abs((n)**(1/2)))):
            break
    if(n != 1):
        nf += 1
        F[nf] = n
    return F

def getValoresUnicos(fatores):
    unicos = []
    for num in fatores:
        if num not in unicos:
            unicos.append(num)
    unicos.remove(0)
    return unicos

def triangulosRetangulos(C):
    
    n = int(math.sqrt(10**8) + 5)
    crivo = geraCrivo(n,C)
    primos = geraPrimos(n,crivo,P)
    np = len(primos)

    casos = int(input())
    while(casos > 0):
        n = int(input())

        F = []
        for i in range(1000):
            F.append(0)
        fatores = fatora(n,P,np,F)

        valoresUnicos = getValoresUnicos(fatores)
        m = 1
        for i in valoresUnicos:
            exp = fatores.count(i)
            m *= i**(math.ceil(exp/2))
        if(m != 0):
            r = int(abs(n/m) - 1)
        else:
            r = 0
        solucao = 8*r
        
        print(solucao)

        casos -= 1

triangulosRetangulos(C)