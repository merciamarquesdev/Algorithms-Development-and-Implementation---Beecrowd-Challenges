def mochila(n,d,p,k):
    k[0] = 0
    for q in range(1,(n*2)+1,2):
        for j in range(d,-1,-1):
            if (k[j] >= 0):
                if (j+p[q] <= d):
                    if (k[j+p[q]] == -1):
                        k[j+p[q]] = q
                if (j+p[q+1] <= d):
                    if (k[j+p[q+1]] == -1):
                        k[j+p[q+1]] = q
    #completei k
    if (k[d] != -1):
        maiorValor = 'S'
    return maiorValor

def cobrancas():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        d = int(int(entrada[1])/2) #considerar a distancia para voltar para casa
        p = input().split(" ")
        #transformando p em vetor de inteiros
        p.insert(0,0)
        for i in range((2*n)+1):
            p[i] = int(p[i])
        #criando vetor k
        k = []
        for i in range(0,d+1):
            k.append(-1)
        #exibindo resultado
        resultado = mochila(n,d,p,k)
        print(resultado)
        
        nCasos -= 1
        
cobrancas()
