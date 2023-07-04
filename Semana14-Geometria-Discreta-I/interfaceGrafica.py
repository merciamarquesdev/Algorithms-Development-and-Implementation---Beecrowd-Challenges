def sentidoPercurso(p1,p2,p3):
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

def intercepta(s1,s2):
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

def pontoNoSegmento(p1,p2,p3):
    resultado = (sentidoPercurso(p1,p2,p3) == 0) and (p1[0] >= min(p2[0], p3[0])) and (p1[0] <= max(p2[0], p3[0])) and (p1[1] >= min(p2[1], p3[1])) and (p1[1] <= max(p2[1], p3[1]))
    return resultado

def pontoInterior(poligono,n,q):
    maxx = poligono[0][0]
    s1 = [[0,0],[0,0]]
    s2 = [[0,0],[0,0]]
    poligono[n] = poligono[0]

    for i in range(1,n+1):
        if(pontoNoSegmento(q,poligono[i-1],poligono[i])):
            return 5
        if(poligono[i][0] > maxx):
            maxx = poligono[i][0]

    s2[0] = q
    s2[1][0] = maxx+1
    s2[1][1] = q[1]
    cont = 0
    
    for i in range(1,n+1):
        s1[0] = poligono[i-1]
        s1[1] = poligono[i]
        if ((((poligono[i][1] > q[1]) and (poligono[i-1][1] <= q[1])) or ((poligono[i-1][1] > q[1]) and (poligono[i][1] <= q[1]))) and (intercepta(s1,s2))):
            cont += 1   
    return cont%2

def saida(interior):
    if(interior == 5):
        return '/'
    elif(interior == 1):
        return '!'
    else:
        return '-'

def interfaceGrafica():
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        pontosPoligono = input().split(" ")
        c = int(input())
        pontosClique = input().split(" ")
        poligono = [0]*((2*n)+1)
        cliques = [0]*((2*c)+1)

        for i in range(2*n):
            poligono[i] = int(pontosPoligono[i])
        
        for i in range(2*c):
            cliques[i] = int(pontosClique[i])
        
        for i in range(n):
            poligono[i:i+2] = [poligono[i:i+2]]

        for i in range(c):
            cliques[i:i+2] = [cliques[i:i+2]]

        output = ''
        for i in range(c):
            interior = pontoInterior(poligono,n,cliques[i])
            output += saida(interior)

        print(output)
        nCasos -= 1

interfaceGrafica()