C = [0]*200010

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

def geraCrivo(n,C):
    for i in range(1,n+1):
        C[i] = i
    t = 2
    for i in range(1,int(n/2)+1):
        C[t] = 2
        t += 2
    s = int(abs((n)**(1/2)))+1
    for i in range(3,s):
        if(C[i] == i):
            t = i*i
            d = i+i
            while(t <= n):
                if(C[t] == t):
                    C[t] = i
                t += d
    return C 

def carmichael(n, crivo, carm):
    for i in range(2, n + 1):
        carm[i] = carm[i - 1]
        if(crivo[i] != i):
            aux = False
            for j in range(2, i):
                if(j != exp(j, i, i)):
                    aux = True
                    break
            if(not aux):
                carm[i] += 1
    return carm


def primoConsideracao(C):
    crivoTamanho = 200000
    crivo = geraCrivo(crivoTamanho,C)
    carm = [0]*200010
    carm = carmichael(200000,crivo,carm)
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        p = int(entrada[0])
        q = int(entrada[1])
        print(carm[q]-carm[p])

        nCasos -= 1

primoConsideracao(C)