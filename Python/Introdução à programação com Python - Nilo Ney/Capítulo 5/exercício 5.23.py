#5.23
num = int(input("Digite um número: "))

if num == 2:
    print("É primo!")
elif num == 0 or num == 1:
    print("Não é primo!")
else:
    cont = 2
    existe = 0
    while cont < num:
        if num % cont == 0:
            print("Não é primo!")
            break
        else:
            existe += 1
        cont +=1
    if existe == (num - 2):
        print("É primo!")

#print(existe)
#if existe == (num - 2):
#    print("É primo!")
