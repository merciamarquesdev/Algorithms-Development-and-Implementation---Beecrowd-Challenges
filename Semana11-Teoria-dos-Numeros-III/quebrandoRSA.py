C = []
F = []
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

def fatora(n,P,np,F,nf):
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

def MDCE(a,b):
    t = 0
    x = 1
    y = 0
    Pa = [0]*100
    Pb = [0]*100
    while(b != 0):
        t += 1
        Pa[t] = a
        Pb[t] = b
        f = a%b
        a = b
        b = f
    for i in range(t,0,-1):
        f = y
        y = x - (Pa[i]//Pb[i])*y
        x = f
    return a,x,y

def invMod(b,n):
    a,x,y = MDCE(b,n)
    return (x+n)%n

def multMod(a,b,n):
    mod = a*b%n
    return mod

def exp(a,b,n):
    if(b == 0):
        return 1
    elif(b%2 != 0):
        return multMod(exp(a,b-1,n),a,n)
    else:
        x = exp(a,b/2,n)
        return multMod(x,x,n)

def quebrandoRSA(C,F,P):
    crivoTamanho = int((10**8)**(1/2))
    np = 0
    crivo = geraCrivo(crivoTamanho,C)
    primos = geraPrimos(crivoTamanho,crivo,P,np)
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        e = int(entrada[0])
        n = int(entrada[1])
        cifrada = int(input())
        nf = 0
        np = len(primos)
        for i in range(0,3):
            F.append(0)
        fatores = fatora(n,P,np,F,nf)
        p = int(fatores[1])
        q = int(fatores[2])
        t = (p-1)*(q-1)
        d = invMod(e,t)
        decifrada = exp(cifrada,d,n)
        print(decifrada)

        nCasos -= 1

quebrandoRSA(C,F,P)