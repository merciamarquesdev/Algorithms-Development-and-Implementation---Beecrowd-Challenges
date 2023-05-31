C = []
P = []

def geraCrivo(n,C):
    for i in range(1,n+1):
        C[i] = i
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
            P[np] = i
    return P

def contador(n,P):
    total = 0
    inicio = 1
    final = 1
    aux = P[inicio]
    while(P[final] <= n):
        if(aux == n):
            total += 1
        if(aux <= n):
            final += 1
            aux += P[final]
        else:
            aux -= P[inicio]
            inicio += 1
    return total

def ganhador(total):
    if(total % 2 != 0):
        return 'Joana'
    else:
        return 'Bruno'

def fracoesIrredutiveis(C,P):
    tamCrivo = int(abs((10**12)**(1/2))) + 3

    for i in range(tamCrivo):
        C.append(0)
        P.append(0)

    np = 0
    crivo = geraCrivo(tamCrivo-2,C)
    primos = geraPrimos(tamCrivo-2,crivo,P,np)
    nCasos = int(input())

    while(nCasos > 0):
        n = int(input())
        total = contador(n,primos)
        resultado = ganhador(total)
        print(resultado)
        nCasos -= 1

fracoesIrredutiveis(C,P)