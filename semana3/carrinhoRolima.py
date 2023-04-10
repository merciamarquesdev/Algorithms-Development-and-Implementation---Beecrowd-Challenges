import sys 
sys.setrecursionlimit(10000)

def D(i,j):
    resultado = []
    if (i+1<n):
        if (altura[i][j] > altura[i+1][j]):
            if (vMax[i+1][j] == -1):
                D(i+1,j)
            resultado.append(vMax[i+1][j])
            
    if (i-1>=0):
        if (altura[i][j] > altura[i-1][j]):
            if (vMax[i-1][j] == -1):
                D(i-1,j)
            resultado.append(vMax[i-1][j])
            
    if (j+1<m):
        if (altura[i][j] > altura[i][j+1]):
            if (vMax[i][j+1] == -1):
                D(i,j+1)
            resultado.append(vMax[i][j+1])

    if (j-1>=0):
        if (altura[i][j] > altura[i][j-1]):
            if (vMax[i][j-1] == -1):
                D(i,j-1)
            resultado.append(vMax[i][j-1])

    if (resultado == []):
        vMax[i][j] = 1
    else:
        vMax[i][j] = max(resultado)+1

    
nCasos = int(input())    
while (nCasos > 0):
    entrada = input().split(" ")
    n = int(entrada[0])
    m = int(entrada[1])
    altura = []
    for i in range(n):
        altura.append(input().split(" "))
        
    for i in range(n):
        for j in range(m):
            altura[i][j] = int(altura[i][j])
            
    vMax = [[-1 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if (vMax[i][j] == -1):
                D(i,j)

    maior = 0
    for i in range(n):
        for j in range(m):
            if (vMax[i][j] > maior):
                maior = vMax[i][j]
    print(maior)
        
    nCasos -= 1
