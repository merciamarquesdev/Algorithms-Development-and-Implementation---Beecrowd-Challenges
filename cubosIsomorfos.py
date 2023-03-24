       
#girando com as posiçoes 1 e 6 fixas (eixo z fixo)
def giraComEixoZFixo(cubo1):
    return cubo1[0]+cubo1[2]+cubo1[4]+cubo1[1]+cubo1[3]+cubo1[5]

#girando com as posiçoes 2 e 5 fixas (eixo y fixo)
def giraComEixoYFixo(cubo1):
    return cubo1[3]+cubo1[1]+cubo1[0]+cubo1[5]+cubo1[4]+cubo1[2]

#girando com as posiçoes 3 e 4 fixas (eixo x fixo)
def giraComEixoXFixo(cubo1):
    return cubo1[1]+cubo1[5]+cubo1[2]+cubo1[3]+cubo1[0]+cubo1[4]

#giros possiveis e comparaçoes
def cubosIsomorfos():
    nCasos = int(input())
    
    while (nCasos > 0):
        cubo1 = input()
        cubo2 = input()
        iguais = False
        
        for i in range(0,4):
            cubo1 = giraComEixoZFixo(cubo1)
            for j in range(0,4):
                cubo1 = giraComEixoYFixo(cubo1)
                for k in range(0,4):
                    cubo1 = giraComEixoXFixo(cubo1)
                    if (cubo1 == cubo2):
                        iguais = True
  
        if (iguais):
            print("S")
        else:
            print("N")
        nCasos -= 1

cubosIsomorfos()

        