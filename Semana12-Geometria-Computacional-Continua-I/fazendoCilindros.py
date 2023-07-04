import math

def volumeMetodo1(c,l):
    r = c/(2*math.pi)
    v = (math.pi*(r)**2)*(l-(2*r))
    return v

def volumeMetodo2(c,l):
    x = l/(2*(math.pi+1))
    r = min(c/2,x)
    v = math.pi*(r**2)*c
    return v

def fazendoCilindros():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        c = int(entrada[0])
        l = int(entrada[1])
        if(c > l):
            volume1 = volumeMetodo1(l,c)
            volume2 = volumeMetodo2(l,c)
        else:
            volume1 = volumeMetodo1(c,l)
            volume2 = volumeMetodo2(c,l)
        maior = max(volume1,volume2)
        print("%.2f" %(maior))

        nCasos -= 1

fazendoCilindros()