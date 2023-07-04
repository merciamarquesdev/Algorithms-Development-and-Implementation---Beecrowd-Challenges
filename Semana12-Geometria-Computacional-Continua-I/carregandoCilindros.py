def carregandoCilindros():
    nCasos = int(input())
    while(nCasos > 0):
        entrada = input().split(" ")
        c = int(entrada[0])
        l = int(entrada[1])
        r1 = int(entrada[2])
        r2 = int(entrada[3])

        diametro1 = r1*2
        diametro2 = r2*2
        maiorDiametro = max(diametro1,diametro2)
        menorLado = min(c,l)

        cateto1 = l-(r1+r2)
        cateto2 = c-(r1+r2)
        hipotenusa = (cateto1**2) + (cateto2**2)
        somaRaios = (r1+r2)**2

        if((maiorDiametro <= menorLado) and (somaRaios <= hipotenusa)):
            print('S')
        else:
            print('N')

        nCasos -= 1

carregandoCilindros()