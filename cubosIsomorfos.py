       
#girando pra esquerda com as posiçoes 1 e 6 fixas (eixo z fixo)
def giraParaEsquerdaEixoZFixo(cubo1):
    cubo1 = cubo1[0]+cubo1[2]+cubo1[4]+cubo1[1]+cubo1[3]+cubo1[5]
    return cubo1

#girando pra direita com as posiçoes 1 e 6 fixas (eixo z fixo)
def giraParaDireitaEixoZFixo(cubo1):
    cubo1 = cubo1[0]+cubo1[3]+cubo1[1]+cubo1[4]+cubo1[2]+cubo1[5]
    return cubo1

#girando pra esquerda com as posiçoes 2 e 5 fixas (eixo y fixo)
def giraParaEsquerdaEixoYFixo(cubo1):
    cubo1 = cubo1[3]+cubo1[1]+cubo1[0]+cubo1[5]+cubo1[4]+cubo1[2]
    return cubo1

#girando pra direita com as posiçoes 2 e 5 fixas (eixo y fixo)
def giraParaDireitaEixoYFixo(cubo1):
    cubo1 = cubo1[2]+cubo1[1]+cubo1[5]+cubo1[0]+cubo1[4]+cubo1[3]
    return cubo1

#girando pra cima com as posiçoes 3 e 4 fixas (eixo x fixo)
def giraParaCimaEixoXFixo(cubo1):
    cubo1 = cubo1[1]+cubo1[5]+cubo1[2]+cubo1[3]+cubo1[0]+cubo1[4]
    return cubo1

#girando pra baixo com as posiçoes 3 e 4 fixas (eixo x fixo)
def giraParaBaixoEixoXFixo(cubo1):
    cubo1 = cubo1[4]+cubo1[0]+cubo1[2]+cubo1[3]+cubo1[5]+cubo1[1]
    return cubo1

#giros possiveis e comparaçoes
def cubosIsomorfos():
    nCasos = int(input())
    
    while (nCasos > 0):
        cubo1 = input()
        cubo2 = input()
        auxiliar = ""
        for i in range(0,4):
            auxiliar = giraParaEsquerdaEixoZFixo(cubo1)
            auxiliar = giraParaDireitaEixoZFixo(auxiliar)
            for j in range(0,4):
                auxiliar = giraParaEsquerdaEixoYFixo(auxiliar)
                auxiliar = giraParaDireitaEixoYFixo(auxiliar)
                for k in range(0,4):
                    auxiliar = giraParaCimaEixoXFixo(auxiliar)
                    auxiliar = giraParaBaixoEixoXFixo(auxiliar)
        print(auxiliar)
        
        if (auxiliar == cubo2):
            print("S")
        else:
            print("N")
        nCasos -= 1

cubosIsomorfos()

        