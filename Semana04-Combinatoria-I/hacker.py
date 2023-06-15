import sys 
sys.setrecursionlimit(10000)

def multMod(a,b):
    num = 1000000007
    return (a*b)%num

def arranjo(n,k):
    if (n == 1):
        return k
    if (n%2 == 0):
        result = arranjo(n/2,k)
        return multMod(result,result)
    else:
        return multMod(k,arranjo(n-1,k))

def hacker():
    nCasos = int(input())    
    while (nCasos > 0):
        entrada = input().split(" ")
        k = int(entrada[0])
        n = int(entrada[1])
        resultado = arranjo(n,k)
        print(resultado)
        nCasos -= 1
        
hacker()


