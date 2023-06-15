def metodo1(a,b):        
    if (a >= b):
        resultado = b//2 
    else:
        resultado = a//2
    return resultado


def metodo2(a,b):
    if (a >= b):
        while (b > 0):
            if (b*4 <= a):
                resultado = b
                break
            else:
                b -= 1
                    
    else:
        while (a > 0):
            if (a*4 <= b):
                resultado = a
                break
            else:
                a -= 1
    return resultado


def origami():
    nCasos = int(input())
    
    while (nCasos > 0):
        entrada = input().split(" ")
        a = int(entrada[0])
        b = int(entrada[1])

        m1 = metodo1(a,b)
        m2 = metodo2(a,b)
        
        if (m1 >= m2):
            print(m1)
        else:
            print(m2)
        
        nCasos -= 1
        
origami()
