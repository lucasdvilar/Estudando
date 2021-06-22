#6.5
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    op = input("Operação F (adicionar à fila), A (atender) ou S (sair): ")

    x = 0
    sair = False
    while x < len(op):
        if op[x] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia!")
        elif op[x] == 'F':
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
