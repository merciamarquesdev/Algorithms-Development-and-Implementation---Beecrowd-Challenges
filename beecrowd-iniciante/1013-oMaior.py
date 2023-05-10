def oMaior():
    entrada = input().split(" ")
    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])
    maiorAB = (a+b+abs(a-b))/2
    maiorABC = (maiorAB+c+abs(maiorAB-c))/2
    print("{:.0f} eh o maior".format(maiorABC))
oMaior()
