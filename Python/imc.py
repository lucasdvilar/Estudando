#imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

if imc < 18.5:
    indice = 'Magreza.'
elif imc < 25:
    indice = 'Peso normal.'
elif imc < 30:
    indice = 'Sobrepeso.'
elif imc < 35:
    indice = 'Obesidade de grau I.'
elif imc < 40:
    indice = 'Obesidade de grau II.'
else:
    indice = 'Obesidade de grau III.'

print("\nO seu IMC é %.1f." %imc)
print(indice)
