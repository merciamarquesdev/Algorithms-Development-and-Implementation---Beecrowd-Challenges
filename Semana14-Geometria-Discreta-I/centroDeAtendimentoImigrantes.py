def calculaArea(iareaIntersecao):
    ladoX = abs(iareaIntersecao[1][0]-iareaIntersecao[0][0])
    ladoY = abs(iareaIntersecao[1][1]-iareaIntersecao[0][1])
    iarea = ladoX*ladoY
    return iarea

def intersecaoDoisRetangulos(r1, r2):
    x1 = max(r1[0][0],r2[0][0])
    y1 = max(r1[0][1],r2[0][1])
    x2 = min(r1[1][0],r2[1][0])
    y2 = min(r1[1][1],r2[1][1])
    return [[x1,y1],[x2,y2]]

def centroDeAtendimentoImigrantes():
    nCasos = int(input())
    while(nCasos > 0):
        n = int(input())
        area = input().split(" ")
        iarea = []

        for i in range(4*n):
            iarea.append(int(area[i]))
        
        for i in range(0,2*n):
            iarea[i:i+2] = [iarea[i:i+2]]

        for i in range(0,n):
            iarea[i:i+2] = [iarea[i:i+2]]

        areaIntersecao = iarea[0]
        semIntersecao = False
        for i in range(1,len(iarea)):
            areaIntersecao = intersecaoDoisRetangulos(iarea[i], areaIntersecao)

            x1 = areaIntersecao[0][0]
            y1 = areaIntersecao[0][1]
            x2 = areaIntersecao[1][0]
            y2 = areaIntersecao[1][1]

            if((x1 >= x2) or (y1 >= y2)):
                semIntersecao = True
                break

        if(semIntersecao):
            print(0)
        else:
            resultado = calculaArea(areaIntersecao)
            print(resultado)
        
        nCasos -= 1

centroDeAtendimentoImigrantes()
