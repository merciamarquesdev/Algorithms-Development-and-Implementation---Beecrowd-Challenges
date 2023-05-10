def tipoInteiro():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    lista = [n1,n2,n3,n4,n5]
    par = 0
    impar = 0
    positivo = 0
    negativo = 0
    for i in lista:
        if i%2 == 0:
            par += 1
        if i%2 != 0:
            impar += 1
        if i > 0:
            positivo += 1
        if i < 0:
            negativo += 1
    print("{} valor(es) par(es)".format(par))
    print("{} valor(es) impar(es)".format(impar))
    print("{} valor(es) positivo(s)".format(positivo))
    print("{} valor(es) negativo(s)".format(negativo))
tipoInteiro()
