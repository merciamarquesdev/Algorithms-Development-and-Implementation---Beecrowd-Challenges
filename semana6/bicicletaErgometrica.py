def somaMod(a,b):
    num = 1000000007
    return (a+b)%num

def T(i,j,m,n):
    if (j == 1 and i >= m and i <= n):
        return 1
    elif (i < m or i > n):
        return 0
    elif (j > 1 and i >= m and i <= n):
        return somaMod(T(i-1,j-1,m,n),T(i+1,j-1,m,n))

def bicicletaErgonometrica():
    nCasos = int(input())
    while (nCasos > 0):
        entrada = input().split(" ")
        t = int(entrada[0])
        m = int(entrada[1])
        n = int(entrada[2])
        niveis = []
        for i in range(m,n+1):
            niveis.append(i)
        j = t
        total = 0
        for i in range(m,n):
            total += T(i,j,m,n)
        print(total)       
        
        nCasos -= 1

bicicletaErgonometrica()
