def igual(a,b):
    z = 0.000000001
    return abs(a-b) <= z

def menorIgual(a,b):
    return (a<b) or igual(a,b)

def area(a,b,c):
    area = (a[0]*(b[1]-c[1])) - (b[0]*(a[1]-c[1])) + (c[0]*(a[1]-b[1]))
    return abs(area)

def contandoTriangulos():
    casos = int(input())
    while(casos > 0):
        n = int(input())
        pontos = input().split(" ")
        for i in range(len(pontos)):
            pontos[i] = int(pontos[i])
            
        a = pontos[:2]
        b = pontos[2:4]
        c = pontos[4:6]
        p = pontos[6:]

        area1 = area(a,b,p)
        area2 = area(a,c,p)
        area3 = area(b,c,p)
                    
        casos -= 1
contandoTriangulos()
