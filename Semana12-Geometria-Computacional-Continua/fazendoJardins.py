import math

def area(a,b,c):
    s = (a+b+c)/2.0
    aux = (s*(s-a)*(s-b)*(s-c))
    areaTriang = math.sqrt(aux)
    r = aux/(s**2)
    R = ((a*b*c)**2)/(16*aux)

    areaVermelha = math.pi*r
    areaVioleta = areaTriang - areaVermelha
    areaAmarela = (math.pi*R) - areaVioleta
    
    return areaAmarela,areaVioleta,areaVermelha

def jardins():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        a = int(entrada[0])
        b = int(entrada[1])
        c = int(entrada[2])
        resultado = area(a,b,c)
        print("%.2f %.2f %.2f" %(resultado))
        nCasos -= 1

jardins()
