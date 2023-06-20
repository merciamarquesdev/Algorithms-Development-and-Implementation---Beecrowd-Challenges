def somaPar(n):
    k = int((n/2)-1)
    soma = []
    for i in range(1,k+1,2):
        soma.append(i)
    return sum(soma)

def somaImpar(n):
    k = int((n/2)-1)
    soma = []
    for i in range(2,(2*k)+1,2):
        soma.append(i)
    return sum(soma)

def T(n):
    if(n == 4):
        return 1
    elif (n%2 == 0): #se n for par
        return T(n-1) + somaPar(n)
    else: #se n for impar
        return T(n-1) + somaImpar(n)

def fazendoTriangulos():
    casos = int(input())
    while(casos > 0):
        n = int(input())
        resultado = T(n)
        print(resultado)

        casos -= 1

fazendoTriangulos()

#biblioteca em C++: include <bits/stdc++.h>

# T[1,2,3,4] = 1 (2,3,4)
# T[1,2,3,4,5] = 3 (2,3,4) (5,4,2) (5,4,3)
# T[N] = T[N=1] + (triangulos com lado = N)

# N par = 10 por exemplo
# Outros lados poderao ser:
# 9 2          8 3           7 4       6 5
# 9 3          8 4           7 5       
# .
# .
# .
# 9 8          8 7           7 6
# ----       -------       ------     -----
# 7 total     5 tot          3 tot     1 tot 

# N impar = 11 por exemplo
# Outros lados poderao ser:
# 10 2          9 3           8 4       7 5
# 10 3          9 4                     7 6      
# .
# .
# .
# 10 9          9 8           8 7
# ----       -------       ------     -----
# 8 total     6 tot          4 tot     2 tot 

