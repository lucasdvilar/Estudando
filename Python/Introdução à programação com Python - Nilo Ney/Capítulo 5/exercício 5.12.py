#exercício 5.12
dep_inicial = float(input("Depósito inicial: "))
taxa_juros = float(input("Taxa de juros: "))
investimento = float(input("Investimento mensal: "))

mes = 1
saldo = dep_inicial
while mes <= 24:
    saldo = saldo + (saldo * (taxa_juros / 100)) + investimento
    print("O saldo do mês é: R$%.2f" %saldo)
    mes = mes + 1
total_juros = saldo - dep_inicial - investimento * 24

print("O total ganho com juros foi de R$%.2f" %total_juros)
