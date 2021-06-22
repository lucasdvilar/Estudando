#5.27
pal = input("Digite um número: ")

cont_i = 0
cont_f = -1
check = 0
while cont_i + 1 <= len(pal):
    if pal[cont_i] == pal[cont_f]:
        check += 1
    cont_i += 1
    cont_f -= 1

print(check), print(len(pal))
if check == len(pal):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")
        
