import sys 
sys.setrecursionlimit(10000)

def ranking():
    nCasos = int(input())    
    while (nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        k = int(entrada[1]) 
        resultado = fatorial(n,k)
        print(resultado)
        
        nCasos -= 1

def multMod(a,b):
    num = 1000000007
    return (a*b)%num

def fatorial(n,k):
    if(n == k):
        return 1    
    else:
        return multMod(n,fatorial(n-1,k))

ranking()
