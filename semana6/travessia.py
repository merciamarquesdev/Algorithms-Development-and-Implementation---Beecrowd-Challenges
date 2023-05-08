def particao(n,k,tempos):
    melhoresTempos = []
    for i in range(n):
        melhoresTempos.append(10000)
    melhoresTempos[0] = tempos[0]
    for i in range(1,n):
        maximo = tempos[i]
        possibilidade = 10000
        for j in range(k):
            maximo = max(maximo,tempos[i-j])
            if (i >= k):        
                if (maximo + melhoresTempos[i-(j+1)] < possibilidade):
                    possibilidade = maximo + melhoresTempos[i-(j+1)]
            else:
                possibilidade = max(tempos[:(i+1)])
                break          
        melhorOpcao = possibilidade
        melhoresTempos[i] = melhorOpcao
    return(melhoresTempos[-1])


        
def travessia():
    nCasos = int(input())
    while (nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        k = int(entrada[1])
        tempos = input().split(" ")
        for i in range(n):
            tempos[i] = int(tempos[i])
        resultado = particao(n,k,tempos)
        print(resultado)

        nCasos -= 1

travessia()
