def calculaMedia(notas):
    #caso em que o aluno so fez 1 avaliacao
    if(len(notas) == 1):
        notas.append(0.0)

    #caso em que o aluno fez 4 avaliacoes e descarta-se a menor nota
    elif(len(notas) == 4):
        menorNota = min(notas)
        notas.remove(menorNota)

    #calculando a media
    somatorioNotas = sum(notas)
    quantidadeNotas = len(notas)
    media = somatorioNotas/quantidadeNotas
    return media

def avaliacoesAlgoritmos():
    n = int(input())
    while(n > 0):
        #entradas
        nome = input()
        notas = input().split(" ")
        for i in range(len(notas)):
            notas[i] = float(notas[i])

        #calcula media do aluno
        media = calculaMedia(notas)
        
        #saida
        print(nome + ": %.1f" % media)

        #decrementa numero de alunos
        n -= 1

avaliacoesAlgoritmos()