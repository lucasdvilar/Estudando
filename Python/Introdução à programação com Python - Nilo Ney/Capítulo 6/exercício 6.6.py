#6.6
ultimo = 0
fila1 = []
fila2 = []

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    op = input("Operação F, G, A, B ou S: ")

    x = 0
    sair = False
    while x < len(op):
        if op[x] == 'A' or op[x] == 'F':
            fila = fila1
        else:
            fila = fila2
        if op[x] == 'A' or op[x] == 'B':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia!")
        elif op[x] == 'F' or op[x] == 'G':
            ultimo += 1
            fila.append(ultimo)
        elif op[x] == 'S':
            sair = True
            break
        else:
            print("Operação inválida!")
        x += 1
    if sair == True:
        break
