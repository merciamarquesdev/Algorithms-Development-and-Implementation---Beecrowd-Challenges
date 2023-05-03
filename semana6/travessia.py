#ideia da particao (ao inves de usar maximo, usar minimo)
#tempo minimo é o tempo do carro mais lento



def T(n,k):
    if (n < 0 or (n > 0 and p == 0)):
        return 0
    elif (n == 0):
        return 1
    else:
        return T(p,n-p) + T(p-1,n)

def particao(nInteiros,n):
    T[0] = val(nInteiros[0])            
    P[0] = 1
    T[1] = 10*val(nInteiros[0]) + val(nInteiros[1])
    P[1] = 2
    for i in range(2,n-1):
        T[i] = T[i-1] + val(nInteiros[i]) 
        P[i] = 1
        if (T[i-2] + 10*val(nInteiros[i-1]) + val(nInteiros[i]) > T[i]):
            T[i] = T[i-2] + 10*val(nInteiros[i-1]) + val(nInteiros[i])   
            P[i] = 2

def gerar(i,j,k):
    if (k > 0):
        if (a[i] == b[j]):
            c[k] = a[i]
            gerar(i-1,j-1,k-1)
        elif (T[i-1][j] == k):
            gerar(i-1,j,k)
        else:
            gerar(i,j-1,k)

def scm(n,m):
    for i in range(n+1):
        T[i][0] = 0
    for j in range(m+1):
        T[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (a[i] == b[j]):
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j],T[i][j-1])

def travessia():
    nCasos = int(input())
    while (nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        k = int(entrada[1])
        print(n)
        print(k)
        nInteiros = input().split(" ")
        for i in range(len(nInteiros)):
            nInteiros[i] = int(nInteiros[i])
        print(nInteiros)

        gerar(n,m,T[n][m])
        print(c)
        
        
        nCasos -= 1

travessia()
