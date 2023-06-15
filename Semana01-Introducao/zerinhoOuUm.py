def zerinhoOuUm():
    nCasos = int(input())
    
    while (nCasos > 0):
        valores = input().split(" ")

        if (valores[0] != valores [1] and valores[0] != valores[2]):
            print(1) #primeiro jogador venceu
        elif (valores[1] != valores[0] and valores[1] != valores[2]):
            print(2) #segundo jogador venceu
        elif (valores[2] != valores[0] and valores[2] != valores[1]):
            print(3) #terceiro jogador venceu
        elif (valores[0] == valores[1] and valores[0] == valores[2]):
            print(0) #empate
        nCasos = nCasos - 1

zerinhoOuUm()