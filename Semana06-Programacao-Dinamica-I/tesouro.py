def buscaTesouro(matriz,n,m):
    #criando matriz auxiliar
    aux = []
    for i in range(n):
        aux.append([])
        for j in range(m):
            aux[i].append(0)

    #atualizando matriz com valores corretos
    for i in range(n):
        for j in range(m):
            if(i == 0 and j == 0):
                aux[i][j] = matriz[i][j]
            elif(i == 0 and j > 0):
                aux[i][j] = matriz[i][j] + aux[i][j-1]
            elif(i > 0 and j == 0):
                aux[i][j] = matriz[i][j] + aux[i-1][j]
            else:
                aux[i][j] = max(aux[i][j-1],aux[i-1][j]) + matriz[i][j]
    return aux[n-1][m-1]

def criaMatriz(n,m):
    matriz = []
    for i in range(n):
        entrada = input().split(" ")
        matriz.append(entrada)
    for i in range(n):
        for j in range(m):
            matriz[i][j] = int(matriz[i][j])
    return matriz

def tesouro():
    nCasos = int(input())
    while (nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        m = int(entrada[1])
        matriz = criaMatriz(n,m)
        resultado = buscaTesouro(matriz,n,m)
        print(resultado)
        
        nCasos -= 1

tesouro()
