def somaMod(a,b):
    num = 1000000007
    return (a+b)%num

def multMod(a,b):
    num = 1000000007
    return (a*b)%num

def matrizIdentidade(k):
    identidade = [[1 if i == j else 0 for i in range(0,k)] for j in range(0,k)] 
    return identidade

def multiplicaMatrizes(a,b):
    k = 3
    r = [[0 for i in range(k)]for j in range(k)]
    for i in range(0,k):
        for j in range(0,k):
            for z in range(0,k):
                r[i][j] = somaMod(r[i][j],multMod(a[i][z],b[z][j]))
    return r

def exp(matrizA,n):
    k = 3
    b = matrizA
    if(n <= 0):
        return matrizIdentidade(k)
    elif (n%2 != 0):
        a = exp(b,n-1)
        return multiplicaMatrizes(a,b)
    else:
        x = exp(b,n/2)
        return multiplicaMatrizes(x,x)

def T(n,matrizA,linha3):
    if(n == 2):
        return linha3[0]
    if(n == 1):
        return linha3[1]
    if(n == 0):
        return linha3[2]
    k = 3
    a = exp(matrizA,n-(k-1))
    b = linha3
    resultado = 0
    for i in range(k):
        resultado = somaMod(resultado,multMod(a[0][i],b[i]))
    return resultado

def recorrenciaLinearI():
    nCasos = int(input())
    while (nCasos > 0):
        n = int(input())
        linha2 = input().split(" ")
        a = int(linha2[0])
        b = int(linha2[1])
        c = int(linha2[2])
        linha3 = input().split(" ")
        for i in range(len(linha3)):
            linha3[i] = int(linha3[i])
        linha3 = linha3[::-1]
        k = 3
        matrizI = matrizIdentidade(k)
        matrizA = [[a,b,c]]
        for i in range(k-1):
            matrizA.append(matrizI[i])
        
        print(T(n,matrizA,linha3))
            
        nCasos -= 1

recorrenciaLinearI()        
