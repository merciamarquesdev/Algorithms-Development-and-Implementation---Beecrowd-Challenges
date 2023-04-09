  
def C(p0, p1, arvores, n):
    if (n == -1):
        area = (p1[0]-p0[0])*(p0[1]-p1[1])
        return area
    if (not arvoreDentro(p0,p1,arvores[n])):
        return C(p0,p1,arvores,n-1)
    else:
        n1Ponto = [p0[0],arvores[n][1]]
        n2Ponto = [arvores[n][0],p0[1]]
        n3Ponto = [arvores[n][0],p1[1]]
        n4Ponto = [p1[0],arvores[n][1]]
        a1 = C(n1Ponto,p1,arvores,n-1)
        a2 = C(n2Ponto,p1,arvores,n-1)
        a3 = C(p0,n3Ponto,arvores,n-1)
        a4 = C(p0,n4Ponto,arvores,n-1)
        return max(a1,a2,a3,a4)
      
def brincadeiraEscadaria():
    nCasos = int(input())
    
    while (nCasos > 0):
        entrada = input().split(" ")
        n = int(entrada[0])
        contador = n
        k = int(entrada[1])
        escada = []
        while (contador > 0):
            degrau = input().split(" ")
            escada.append(degrau)
            contador -= 1
            
        nCasos -= 1

brincadeiraEscadaria()
