#exercício 5.11
dep_inicial = float(input("Depósito inicial: "))
taxa_juros = float(input("Taxa de juros: "))

mes = 1
saldo = dep_inicial
while mes <= 24:
    saldo = saldo + (saldo * (taxa_juros / 100))
    print("O saldo do mês é: R$%.2f" %saldo)
    mes = mes + 1

print("O total ganho com juros foi de R$%.2f" %(saldo - dep_inicial))
