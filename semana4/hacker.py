import sys 
sys.setrecursionlimit(10000)

def hacker():
    nCasos = int(input())    
    while (nCasos > 0):
        entrada = input().split(" ")
        k = int(entrada[0])
        n = int(entrada[1])
        var = n - k
        resultado = arranjo(n,k)
        print(resultado)
        
        nCasos -= 1

def multMod(a,b):
    num = 1000000007
    return (a*b)%num


def arranjo(n,k):
    result = 1
    for i in range(1,n+1):
        result *= multMod(result,k)
    return result
    #if(n == var):
     #   return 1    
    #else:
     #   return multMod(n,arranjo(n-1,var))

hacker()
