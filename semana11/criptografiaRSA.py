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

def criptografiaRSA():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        p = int(entrada[0])
        q = int(entrada[1])
        e = int(entrada[2])
        msg = int(input())
        t = (p-1)*(q-1)
        n = p*q
        d = invMod(e,t)
        decodificacao = exp(msg,d,n)
        print(decodificacao)

        nCasos -= 1
    
criptografiaRSA()