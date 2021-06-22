#5.22
while True:
    opcao = input("Digite uma opção (+, -, /, * ou sair): ")
    if opcao == 'sair':
        break
    elif opcao == '+' or opcao == '-' or opcao == '/' or opcao == '*':
        num = int(input("Digite um número: "))
        x = 1
        while x <= 10:
            if opcao == '+':
                print(f"{num} + {x} = {num + x}")
            elif opcao == '-':
                print(f"{num} - {x} = {num - x}")
            elif opcao == '/':
                print(f"{num} / {x} = {num / x}")
            elif opcao == '*':
                print(f"{num} * {x} = {num * x}")
            x += 1
    else:
        print("Função inválida!")
