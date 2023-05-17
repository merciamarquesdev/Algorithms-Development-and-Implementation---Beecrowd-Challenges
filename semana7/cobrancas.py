def mochila(n,d,distancias,valores):
    #criando vetor k, da mochila, e vetor auxiliar
    k = []
    aux = []
    k.append(0)
    aux.append(0)
    for i in range(0,d):
        k.append(-1)
        aux.append(-1)
    #comparacoes
    for i in range(n):
        for j in range(d,distancias[i]-1,-1):
            if (k[j-distancias[i]] >= 0):
                if (aux[j-distancias[i]] + valores[i] > aux[j]):
                    k[j] = i + 1
                    aux[j] = aux[j-distancias[i]] + valores[i]
    #achando maior valor
    maiorValor = 0
    for i in range(d+1):
        if (aux[i] > maiorValor):
            maiorValor = aux[i]
    return maiorValor
    

def cobrancas():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        d = int(entrada[1]) #considerar a distancia para voltar para casa
        p = input().split(" ")
        #transformando p em vetor de inteiros
        for i in range(2*n):
            p[i] = int(p[i])
        #criando vetor das distancias
        distancias = []
        for i in range(0,(2*n),2):
            distancias.append(p[i]*2)
        #criando vetor dos valores
        valores = []
        for i in range(1,(2*n),2):
            valores.append(p[i])
        #exibindo resultado
        resultado = mochila(n,d,distancias,valores)
        print(resultado)
        
        nCasos -= 1
        
cobrancas()
