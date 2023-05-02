def avaliacaoPolinomios(nInvertido,indice,base):
    i = 0
    b = 1
    r = int(nInvertido[0])
    while (i != indice):
        b = b*base
        i += 1
        r = r + (int(nInvertido[i])*b)
    return r

def brigasEntreIrmaos():
    nCasos = int(input())
    while (nCasos > 0):
        n = input()
        k = int(input())
        
        nInvertido = n[::-1]
        indice = len(n)-1
        base = 10

        if (avaliacaoPolinomios(nInvertido,indice,base)%k == 0):
            print("S")
        else:
            print("N")
            
        nCasos -= 1

brigasEntreIrmaos()        
