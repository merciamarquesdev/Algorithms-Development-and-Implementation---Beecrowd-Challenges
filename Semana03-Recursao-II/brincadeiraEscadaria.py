import sys 
sys.setrecursionlimit(10000)

def Pontuacao(i):
    if (i == n-1):
        resultado = escada[i]
        vMax[i] = resultado
    else:
        resultado = []
        for j in range(1,k+1):
            if ((i+j) < n):
                if (vMax[i+j] != -999999):
                    resultado.append(vMax[i+j]) #adiciona pontuacao maxima degrau por degrau
                else:
                    Pontuacao(i+j)
                    resultado.append(vMax[i+j]) #adiciona pontuacao maxima degrau por degrau
        vMax[i] = max(resultado)+escada[i]
    
    

nCasos = int(input())    
while (nCasos > 0):
    entrada = input().split(" ")
    n = int(entrada[0])
    k = int(entrada[1])
    escada = input().split(" ")
    for i in range(n):
        escada[i] = int(escada[i])
        
    vMax = [-999999 for i in range(n)]

    Pontuacao(0)
    print(vMax[0])
    
    nCasos -= 1
