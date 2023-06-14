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

def quebrandoRSA(C,F):
    nCasos = int(input())
    nf = 0
    while(nCasos > 0):
        entrada = input().split(" ")
        e = int(entrada[0])
        n = int(entrada[1])
        cifrada = int(input())
        crivo = geraCrivo(n,C)
        fatores = fatora(n,crivo,F,nf)
        print(fatores)
        p = fatores[0]
        q = fatores[1]
        t = (p-1)*(q-1)
        d = invMod(e,t)
        print(d)
        decifrada = exp(cifrada,d,n)
        print(decifrada)

        nCasos -= 1

quebrandoRSA(C,F)