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

def ehPrimo(n,tabelaPrimos,np):
    for i in range(0,np):
        if(n%tabelaPrimos[i] == 0):
            if(n != tabelaPrimos[i]):
                return False
            else:
                return True
    return True

def ehComposto(primo):
     if(primo):
         return 'N'
     else:
         return 'S'

def numeroComposto(C,P):
    n = 10**7
    np = 0
    crivo = geraCrivo(n,C)
    tabelaPrimos = geraPrimos(n,crivo,P,np)
    np = len(tabelaPrimos)
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        primo = ehPrimo(n,tabelaPrimos,np)
        resultado = ehComposto(primo)
        print(resultado)
        nCasos -= 1

numeroComposto(C,P)
