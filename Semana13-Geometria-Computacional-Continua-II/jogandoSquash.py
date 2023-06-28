def pontosParaReta(p1,p2):
    reta = [0,0,0]
    if (p1[0] == p2[0]):
        reta[0] = 1
        reta[1] = 0
        reta[2] = -p1[0]
    else:
        reta[1] = 1
        reta[0] = -(p1[1]-p2[1])/(p1[0]-p2[0])
        reta[2] = -(reta[0]*p1[0])-(reta[1]*p1[1])
    return reta

def pontoTangenteParaReta(p,tang):
    r = [0,0,0]
    r[0] = - tang
    r[1] = 1.0
    r[2] = - ((r[0]*p[0])+(r[1]*p[1]))
    return r

def paralelas(r1,r2):
    QZERO = 0.000000001
    return ((abs(r1[0]-r2[0]) <= QZERO) and (abs(r1[1]-r2[1]) <= QZERO))

def mesmaReta(r1,r2):
    QZERO = 0.000000001
    return (paralelas(r1,r2) and (abs(r1[2]-r2[2]) <= QZERO))

def pontoIntersecao(r1,r2):
    QZERO = 0.000000001
    bp = [False,[0,0]]
    bp[0] = True
    if (paralelas(r1,r2) or mesmaReta(r1,r2)):
        bp[0] = False
    else:
        bp[1][0] = (r2[1]*r1[2]-r1[1]*r2[2])/(r2[0]*r1[1]-r1[0]*r2[1])
        if (abs(r1[1]) > QZERO):
            bp[1][1] = -(r1[0]*bp[1][0] + r1[2])/r1[1]
        else:
            bp[1][1] = -(r2[0]*bp[1][0] + r2[2])/r2[1]
        if (abs(bp[1][0]) < QZERO):
            bp[1][0] = 0 #Para evitar -0.00
        if (abs(bp[1][1]) < QZERO):
            bp[1][1] = 0 #Para evitar -0.00   
    return bp

def pontoMaisProximo(p1,r1):
    QZERO = 0.000000001
    p2 = [0,0]
    bp = [False,[0,0]]
    r2 = [0,0,0]
    if(abs(r1[1]) <= QZERO):
        p2[0] = -r1[2]
        p2[1] = p1[1]
    elif(abs(r1[0]) <= QZERO):
        p2[0] = p1[0]
        p2[1] = -r1[2]
    else:
        r2 = pontoTangenteParaReta(p1,(1.0/r1[0]))
        bp = pontoIntersecao(r1,r2)
        if (not bp[0]):
            print("Erro")
        p2[0] = bp[1][0]
        p2[1] = bp[1][1]
    return p2

def jogandoSquash():
    nCasos = int(input())
    while(nCasos > 0):
        pontos = input().split(" ")
        for i in range(len(pontos)):
            pontos[i] = float(pontos[i])

        p1 = pontos[:2]
        p2 = pontos[2:4]
        pb = pontos[4:6]
        ph = pontos[6:]
        
        r1 = pontosParaReta(p1,p2)
        pm = pontoMaisProximo(ph,r1)
        ps = [0,0]
        ps[0] = 2*pm[0] - ph[0]
        ps[1] = 2*pm[1] - ph[1]
        r3 = pontosParaReta(pb,ps)
        pMira = pontoIntersecao(r1,r3)
        if((pMira[1][0] < 0) or (pMira[1][1] < 0)):
            print("Impossivel")
        else:
            print("%.2f %.2f" %(pMira[1][0],pMira[1][1]))

        nCasos -= 1

jogandoSquash()