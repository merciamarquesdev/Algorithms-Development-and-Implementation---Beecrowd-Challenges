def salarioComBonus():
    nome = input()
    salario = float(input())
    totalVendas = float(input())
    comissao = 0.15*totalVendas
    salarioFinal = salario+comissao
    print("TOTAL = R$ {:.2f}".format(salarioFinal))
    
salarioComBonus()

