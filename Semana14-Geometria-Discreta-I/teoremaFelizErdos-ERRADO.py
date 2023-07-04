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
    
def poligonoConvexo(poligono,n):
    s = sentidoPercurso(poligono[n-2], poligono[n-1], poligono[0])
    if (s != sentidoPercurso(poligono[n-1], poligono[0], poligono[1])):
         return 0
    for i in range(0,n-2):
        if (s != sentidoPercurso(poligono[i], poligono[i+1], poligono[i+2])):
            return 0
    return 1

def areaPoligono(poligono,n):
    poligono[n] = poligono[0]
    c = 0
    for i in range(0,n):
        c = c + ((poligono[i][0]*poligono[i+1][1]) - (poligono[i+1][0]*poligono[i][1]))
    return c/2.0

def teoremaFelizErdos():
    nCasos = int(input())
    while(nCasos > 0):
        pontos = input().split(" ")
        poligono = [0]*(10+1)

        for i in range(10):
            poligono[i] = int(pontos[i])
        
        for i in range(5):
            poligono[i:i+2] = [poligono[i:i+2]]

        maneiras = [[poligono[0],poligono[0],poligono[1],poligono[2],poligono[3]],
                   [poligono[0],poligono[0],poligono[1],poligono[3],poligono[2]],
                   [poligono[0],poligono[0],poligono[2],poligono[1],poligono[3]],
                   [poligono[0],poligono[0],poligono[2],poligono[3],poligono[1]],
                   [poligono[0],poligono[0],poligono[3],poligono[1],poligono[2]]]
        
        area = 0

        ponto = [0,0]
        for i in range(5):
            ponto = [[maneiras[i][0],maneiras[i][0],maneiras[i][1],maneiras[i][2],maneiras[i][3]],
                   [maneiras[i][0],maneiras[i][0],maneiras[i][1],maneiras[i][3],maneiras[i][2]],
                   [maneiras[i][0],maneiras[i][0],maneiras[i][2],maneiras[i][1],maneiras[i][3]],
                   [maneiras[i][0],maneiras[i][0],maneiras[i][2],maneiras[i][3],maneiras[i][1]]]
            if(poligonoConvexo(ponto,4)):
                areaPoligono = abs(areaPoligono(ponto[i],4))
                area = max(area,areaPoligono)
        
        print(area)
        nCasos -= 1

teoremaFelizErdos()