def somaDePares():
    nCasos = int(input())
    
    while (nCasos > 0):
        entrada = input().split(" ")
        tamanhoVetor = int(entrada[0])
        soma = int(entrada[1])
        vetor = input().split(" ")
        contPares = 0
        posInicial = 0
        posFinal = tamanhoVetor-1
        
        while (posFinal > posInicial):
            tentativa = int(vetor[posInicial]) + int(vetor[posFinal])
            
            if(tentativa == soma):
                contPares += 1

            if (tentativa > soma):
                posFinal -= 1
            else:
                posInicial += 1
        
        print(contPares)

        nCasos = nCasos - 1

somaDePares()