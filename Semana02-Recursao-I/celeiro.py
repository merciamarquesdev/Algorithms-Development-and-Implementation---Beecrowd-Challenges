def arvoreDentro(p0,p1,arvore):
    return p0[0] <= arvore[0] and arvore[0] <= p1[0] and p1[1] <= arvore[1] and arvore[1] <= p0[1]
    
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
        if (a1 >= a2 and a1 >= a3 and a1 >= a4):
            return a1
            
        elif (a2 >= a1 and a2 >= a3 and a2 >= a4):
            return a2
            
        elif (a3 >= a1 and a3 >= a2 and a3 >= a4):
            return a3
            
        return a4
def celeiro():
    nCasos = int(input())
    
    while (nCasos > 0):
        L, A = input().split(" ")
        p0 = [0,int(A)]
        p1 = [int(L),0]
        vet = input().split(" ")
        n = int(vet[0])
        arvores = [] 
        for i in range(1, n*2, 2):
            arvores.append((int(vet[i]), int(vet[i+1])))
        print(C(p0,p1,arvores,n-1))
        nCasos -= 1

celeiro()
