#exercício 3.15
cigarros_dia = int(input("Quantidade de cigarros por dia: "))
anos_fumando = float(input("Anos fumando: "))

reducao_min = cigarros_dia * 365 * anos_fumando * 10
reducao_dias = reducao_min / (24 * 60)

print("A redução do tempo de vida em dias é %.2f." %reducao_dias)
