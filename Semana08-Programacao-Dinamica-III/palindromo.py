def criaMatriz(n):
    T = []
    for i in range(n):
        T.append([])
        for j in range(n):
            T[i].append(0)
    return T

def palMax(n,S,T):
    maxP = 1
    for i in range(0,n-1): #pode ser n-1
        T[i][i] = 1
        if(S[i] == S[i+1]):
            T[i][i+1] = 1
            maxP = 2
    T[n-1][n-1] = 1
    for d in range(2,n): #pode ser n-1
        for i in range(0,n-d): #pode ser n-d
            j = i+d
            if(S[i] == S[j] and T[i+1][j-1] == 1):
                T[i][j] = 1
                maxP = max(maxP,j-i+1)
    #imprimindo matriz
    #for i in range(n):
    #    print(T[i])
    return maxP

def palindromo():
    nCasos = int(input())
    while(nCasos > 0):
        S = input()
        n = len(S)
        T = criaMatriz(n)
        resultado = palMax(n,S,T)
        print(resultado)
        nCasos -= 1

palindromo()
