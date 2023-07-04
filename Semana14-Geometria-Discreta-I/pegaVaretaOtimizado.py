def sentidoPercurso(p1, p2, p3):
    a = p2[0] - p1[0]
    b = p3[1] - p1[1]
    c = p3[0] - p1[0]
    d = p2[1] - p1[1]
    a = (a*b)-(c*d)
    if (a > 0):
        return 1
    elif (a < 0):
        return -1
    else:
        return 0

def intercepta(s1, s2):
    x1, y1 = s1[0]
    x2, y2 = s1[1]
    x3, y3 = s2[0]
    x4, y4 = s2[1]
    if (max(x1, x2) >= min(x3, x4) and
        max(x3, x4) >= min(x1, x2) and
        max(y1, y2) >= min(y3, y4) and
        max(y3, y4) >= min(y1, y2) and
        sentidoPercurso(s1[0], s1[1], s2[0]) * sentidoPercurso(s1[0], s1[1], s2[1]) <= 0 and
        sentidoPercurso(s2[0], s2[1], s1[0]) * sentidoPercurso(s2[0], s2[1], s1[1]) <= 0):
        return 1
    else:
        return 0

def vencedor(pontosJoao, pontosAdversario):
    if pontosJoao > pontosAdversario:
        print('+')  # João vencedor
    elif pontosAdversario > pontosJoao:
        print('-')  # Adversário vencedor
    else:
        print('x')  # Empate

def pegaVareta():
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        vezJoao = input().split(" ")
        vezAdversario = input().split(" ")
        
        for i in range(4*n):
            vezJoao[i] = int(vezJoao[i])
            vezAdversario[i] = int(vezAdversario[i])
        
        for i in range(0,2*n):
            vezJoao[i:i+2] = [vezJoao[i:i+2]]
            vezAdversario[i:i+2] = [vezAdversario[i:i+2]]

        for i in range(0,n):
            vezJoao[i:i+2] = [vezJoao[i:i+2]]
            vezAdversario[i:i+2] = [vezAdversario[i:i+2]]

        pontosJoao = 0
        pontosAdversario = 0
        for i in range(0,len(vezJoao)):
            for j in range(i+1,len(vezJoao)):
                pontosJoao += intercepta(vezJoao[i], vezJoao[j])
                pontosAdversario += intercepta(vezAdversario[i], vezAdversario[j])
                
        vencedor(pontosJoao,pontosAdversario)

        nCasos -= 1

pegaVareta()
