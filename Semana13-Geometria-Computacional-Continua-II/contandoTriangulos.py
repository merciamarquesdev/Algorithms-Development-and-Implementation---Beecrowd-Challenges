import math

def igual(a,b):
    z = 0.000000001
    return abs(a-b) <= z

def menor(a,b):
    return (a<b)

def area(a,b,c):
    area = (a[0]*(b[1]-c[1])) - (b[0]*(a[1]-c[1])) + (c[0]*(a[1]-b[1]))
    return abs(area)

def ladosTriangulo(x,y,z):
    a = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    b = math.sqrt((y[0]-z[0])**2 + (y[1]-z[1])**2)
    c = math.sqrt((z[0]-x[0])**2 + (z[1]-x[1])**2)
    temp = max(a,b,c)
    if (temp == a):
        a = c
        c = temp
    elif (temp == b):
        b = c
        c = temp
    return c,a,b

def tipoTriangulo(c,a,b,nr,na,no):
    if(igual(c**2,(a**2 + b**2))):
        nr += 1
    elif(menor(c**2,(a**2 + b**2))):
        na += 1
    else:
        no += 1
    return nr,na,no

def contandoTriangulos():
    casos = int(input())
    while(casos > 0):
        nr = 0
        na = 0
        no = 0

        n = int(input())
        entrada = input().split(" ")
        pontos = []

        for i in range(0,2*n,2):
            pontos.append([float(entrada[i]),float(entrada[i+1])])

        for x in range(0,n-2):
            for y in range(x+1,n-1):
                for z in range(y+1,n):
                    if(area(pontos[x],pontos[y],pontos[z]) != 0):#teste de nao-colinearidade
                        c,a,b = ladosTriangulo(pontos[x],pontos[y],pontos[z])
                        nr,na,no = tipoTriangulo(c,a,b,nr,na,no)                   
        print(nr,na,no)

        casos -= 1

contandoTriangulos()
