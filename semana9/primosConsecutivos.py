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
    
def geraPrimos(n,crivo,P,np):
    for i in range(2,n+1):
        if(crivo[i] == i):
            np += 1
            P.insert(np,i)
    return P

def ganhador(n,tabelaPrimos,np):
    if(sum(tabelaPrimos) == n):
        if(np % 2 != 0):
            return 'Joana'
        else:
            return 'Bruno'

def fracoesIrredutiveis(C,P):
    n = 10**7
    np = 0
    crivo = geraCrivo(n,C)
    tabelaPrimos = geraPrimos(n,crivo,P,np)
    np = len(tabelaPrimos)
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        resultado = ganhador(n,tabelaPrimos,np)
        print(resultado)
        nCasos -= 1

fracoesIrredutiveis(C,P)