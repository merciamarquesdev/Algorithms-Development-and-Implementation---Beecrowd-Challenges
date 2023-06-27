def igual(a,b):
    z = 0.000000001
    return abs(a-b) <= z

def menor(a,b):
    return (a<b)

def area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return abs(area)

def tipoTriangulo(a,b,c,nr,na,no):
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
        pontos = input().split(" ")
        for i in range(len(pontos)):
            pontos[i] = int(pontos[i])

        for x in range(len(pontos)):
            for y in range(len(pontos)):
                for z in range(len(pontos)):
                    a = y-x
                    b = z-y
                    c = x-z
                    if(area(a,b,c) != 0):#teste de nao-colinearidade
                        nr,na,no = tipoTriangulo(a,b,c,nr,na,no)                   
        print(nr,na,no)

        casos -= 1
contandoTriangulos()
