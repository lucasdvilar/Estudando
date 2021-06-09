#exercício 3.9
dias = float(input("Digite o número de dias: "))
horas = float(input("Digite o número de horas: "))
minutos = float(input("Digite o número de minutos: "))
segundos = float(input("Digite o número de segundos: "))

dias_s = 86400 * dias
horas_s = 3600 * horas
minutos_s = 60 * minutos
total_s = dias_s + horas_s + minutos_s + segundos

print("O total de segundos é %2f." %total_s)
