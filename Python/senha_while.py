senha = input("Digite a senha: ")

cont = 1
while senha != 'XYZ':
    if cont >= 3:
        print("Senha bloqueada!")
        break

    cont += 1
    senha = input("Senha incorreta. Digite novamente: ")
