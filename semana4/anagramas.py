import sys 
sys.setrecursionlimit(100000)

def multMod(a,b):
    num = 1000000007
    return (a*b)%num

def MDCE (a,b):
    if (b == 0):
        x = 1
        y = 0
        return a, x, y
    else:
        d,xl,yl = MDCE(b,a%b)
        x = yl
        y = xl - ((a//b) * yl)
        return d, x , y

def invMod(b):
    z = 1000000007
    d, x, y = MDCE(b,z)
    return (x+z)%z

def fatorial(k):
    fat = 1
    for i in range(1,k+1):
        fat = multMod(fat,i)
    return fat
        
def N(k):
    return fatorial(k)

def Q(lista):
    total = 1
    for i in range(0,len(lista)):
        total = multMod(total,fatorial(lista[i]))
    return total
        
def totalAnagramas(k,lista):
    return multMod(N(k),invMod(Q(lista)))
    
def anagramas():
    nCasos = int(input())    
    while (nCasos > 0):
        entrada = input().split(" ")
        n = 0
        for i in range(0,len(entrada)):
           entrada[i] = int(entrada[i])
           n += entrada[i]
        n -= entrada[0]
        resultado = totalAnagramas(n,entrada[1:])
        print(resultado)
        nCasos -= 1
        
anagramas()


