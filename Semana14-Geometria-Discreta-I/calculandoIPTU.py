def areaPoligono(poligono,n):
    poligono[n] = poligono[0]
    c = 0
    for i in range(0,n):
        c = c + (poligono[i][0]*poligono[i+1][1]) - (poligono[i+1][0]*poligono[i][1])
    return c/2.0

def calculandoIPTU():
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        pontos = input().split(" ")
        impostoPorMetroQuadrado = int(input())
        poligono = [0]*((2*n)+2)

        for i in range(2*n):
            poligono[i] = int(pontos[i])
        
        for i in range(n):
            poligono[i:i+2] = [poligono[i:i+2]]
        
        area = abs(areaPoligono(poligono,n))
        valor = area*impostoPorMetroQuadrado
        print("R$ %.2f" %(valor))

        nCasos -= 1

calculandoIPTU()