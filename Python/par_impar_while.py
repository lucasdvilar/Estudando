#sem break
num = int(input("Digite um número inteiro (-1 para sair): "))

while num != -1:
    if num % 2 == 0:
        print("Par.")
    else:
        print("Ímpar.")
    num = int(input("Digite um número inteiro (-1 para sair): "))
