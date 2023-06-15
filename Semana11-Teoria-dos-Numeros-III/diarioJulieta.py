def chaveCesar(cifrada,parteDecifrada):
    limite = ord('z')-ord('a')+1
    convertida = cifrada
    for chave in range(0,limite):
        for i in range(len(cifrada)):
            if(convertida[i] == 'a'):
                convertida = convertida[:i] + chr(ord(convertida[i])+25) + convertida[i+1:]
            else:
                convertida = convertida[:i] + chr(ord(convertida[i])-1) + convertida[i+1:]
        if (parteDecifrada in convertida):
            return convertida

def diarioJulieta():
    nCasos = int(input())
    while(nCasos > 0):
        cifrada = input()
        parteDecifrada = input()
        resultado = chaveCesar(cifrada,parteDecifrada)
        print(resultado)
        nCasos -= 1

diarioJulieta()
