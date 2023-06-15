def criaVetor(n):
    A = []
    for i in range(n):
        A.append(0)
    return A

def criaMatriz(n):
    T = []
    for i in range(n):
        T.append([])
        for j in range(n):
            T[i].append(0)
    return T

def jogo(n,V,A,T):
    A[0] = V[0]
    for k in range(1,n):
        A[k] = A[k-1]+V[k]
    for k in range(n):
        T[k][k] = V[k]
    for d in range(1,n):
        for i in range(0,n-d):
            j = i + d
            T[i][j] = A[j]
            if (i > 0):
                T[i][j] = T[i][j] - A[i-1] 
            for k in range(i,j):
                aux = A[k] - T[k+1][j]
                if (i > 0):
                    aux = aux - A[i-1]
                if(T[i][j] < aux):
                    T[i][j] = aux
            for k in range(j,i,-1):
                aux = A[j]-A[k-1]-T[i][k-1]
                if(T[i][j] < aux):
                    T[i][j] = aux

    return T[0][n-1]

def jogoDaSoma():
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        V = input().split(" ")
        A = criaVetor(n)
        T = criaMatriz(n)
        for i in range(n):
            V[i] = int(V[i])
        resultado = jogo(n,V,A,T)
        print(resultado)

        nCasos -= 1

jogoDaSoma()
