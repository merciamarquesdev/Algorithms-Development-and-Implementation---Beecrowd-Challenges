import math

def area(a,b,c):
    s = (a+b+c)/2
    areaVioleta = math.sqrt(s*(s-a)*(s-b)*(s-c))
    r = a/s
    R = (a*b*c)/(4*A)
    areaVermelha = math.pi*(r**2)
    areaAmarela = math.pi*(r**2)
    return areaAmarela,areaVioleta,areaVermelha


def jardins():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        a = int(entrada[0])
        b = int(entrada[1])
        c = int(entrada[2])

        nCasos -= 1

jardins()