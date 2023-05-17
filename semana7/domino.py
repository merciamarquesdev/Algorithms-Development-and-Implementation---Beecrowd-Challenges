def mochila(n,s,p,k):
    k[0] = 0
    for q in range(1,(n*2)+1,2):
        for j in range(s,-1,-1):
            if (k[j] >= 0):
                if (j+p[q] <= s):
                    if (k[j+p[q]] == -1):
                        k[j+p[q]] = q
                if (j+p[q+1] <= s):
                    if (k[j+p[q+1]] == -1):
                        k[j+p[q+1]] = q
    #completei k
    if (k[s] != -1):
        acomodaTodos = 'S'
    else:
        acomodaTodos = 'N'
    return acomodaTodos

def superdominos():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        s = int(entrada[1])
        p = input().split(" ")
        #transformando p em vetor de inteiros
        p.insert(0,0)
        for i in range((2*n)+1):
            p[i] = int(p[i])
        #criando vetor k
        k = []
        for i in range(0,s+1):
            k.append(-1)
        #exibindo resultado
        resultado = mochila(n,s,p,k)
        print(resultado)
        
        nCasos -= 1
        
superdominos()
