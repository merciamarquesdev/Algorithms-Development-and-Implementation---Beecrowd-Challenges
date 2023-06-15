C = []

def geraCrivo(n,C):
    C.append(0)
    for i in range(1,n+1):
        C.append(i)
    t = 2
    for i in range(1,int(n/2)+1):
        C[t] = 2
        t += 2
    rq = int(abs((n)**(1/2)))
    for i in range(3,rq+1):
        if(C[i] == i):
            t = i*i
            d = i+i
            while(t <= n):
                if(C[t] == t):
                    C[t] = i
                t += d
    return C 

def geraPrimos(n,crivo,P,np):
    for i in range(2,n+1):
        if(crivo[i] == i):
            np += 1
            P.insert(np,i)
    return P

def fatora(n,crivo,F,nf):
    if(n == 1):
        F = [0]
    else:
        while(n != 1):
            F.insert(nf,crivo[n])
            nf += 1
            n = int(n/crivo[n])
    return F
    # rq = int(abs((n)**(1/2)))+1
    # if(n == 1):
    #      F = [0]
    # else:
    #     for i in range(1,np+1):
    #         while(n%P[i] == 0):
    #             nf += 1
    #             F.insert(nf,P[i])
    #             n = int(n/P[i])
    #         if(n == 1 or P[i] >= rq):
    #             break
    #     if(n != 1):
    #         nf += 1
    #         F.insert(nf,n)
    # return F

def totienteEuler(fatores):
    fatores.sort()
    i = 0
    exp = 0
    fator = 1
    total = 1
    size = len(fatores)
    if(fatores[i] != 0):
        while(i < size):
            exp = fatores.count(fatores[i])
            fator = (fatores[i]**exp) - (fatores[i]**(exp-1))
            total *= fator
            i += exp
    else:
        total = 0
    return total

def fracoesIrredutiveis(C):
    n = 10**7
    crivoTamanho = (10**7) + 3
    np = 0
    P = []
    crivo = geraCrivo(crivoTamanho-2,C)
    primos = geraPrimos(crivoTamanho-2,crivo,P,np)
    nCasos = int(input())
    while(nCasos > 0):
        nf = 0
        F = []
        n = int(input())
        fatores = fatora(n,crivo,F,nf)
        print(fatores)
        resultado = totienteEuler(fatores)
        print(resultado)
        nCasos -= 1

fracoesIrredutiveis(C)
