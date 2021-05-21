num_alunos = int(input("Digite o número de alunos: "))

idade = int(input("Digite a idade: "))

maior = idade
menor = idade
for i in range (num_alunos - 1):
    idade = int(input("Digite a idade: "))
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

print("A maior idade é %d e a menor é %d." %(maior, menor))
