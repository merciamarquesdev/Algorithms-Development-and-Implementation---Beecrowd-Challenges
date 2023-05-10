def areaCirculo():
    pi = 3.14159
    raio = float(input())
    A = round((raio**2)*pi,4)
    print('A={:.4f}'.format(A))

areaCirculo()
