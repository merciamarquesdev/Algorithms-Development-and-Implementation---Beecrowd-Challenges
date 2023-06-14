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

def hornerMetodoA(n,d):
    m = 0
    for i in range(len(d)-1,-1,-1):
        m = (m*10 + d[i]) % n
    return m

def hornerMetodoC(n,d,a):
    m = 1
    for i in range(len(d)-1,-1,-1):
        m = (exp(m,10,n) * exp(a,d[i],n)) % n
    return m

def potenciacao():
    nCasos = int(input())
    while(nCasos > 0):
        a = input()
        B = []
        for i in range(len(a)-1,-1,-1):
            B.append(int(a[i]))

        b = input()
        E = []
        for i in range(len(b)-1,-1,-1):
            E.append(int(b[i]))

        n = int(input())

        a = hornerMetodoA(n,B)
        resultado = hornerMetodoC(n,E,a)
        print(resultado)
        nCasos -= 1

potenciacao()