#cifra de césar
from os import write

def cod_cesar(texto, chave):
    min = 32
    max = 126
    encript = ""

    for c in texto:
        numtexto = ord(c)
        numtexto_encript = numtexto + chave
        if numtexto_encript > max:
            encript = (min - 1) + (numtexto_encript % max)
            return chr(encript)
        encript += chr(numtexto_encript)
    return encript

def decod_cesar (texto, chave):
    min = 32
    max = 126
    decript = ""

    for c in texto:
        numtexto = ord(c)
        numtexto_decript = numtexto - chave
        if numtexto_decript < min:
            numtexto_decript = max - (min - numtexto_decript)
        decript += chr(numtexto_decript)
    return decript

opcao = input("1 para criptografar e 2 para descriptografar: ")
chave = int(input("Digite a chave: "))

if opcao == 1:
    filename = "test.txt"
    filecript = open("testcript.txt", "w")
    with open(filename, 'r', errors = 'ignore') as file:
        for line in file:
            print(line)
            cript_line = cod_cesar(line, chave)
            print(cript_line)
            filecript.writelines("%s\n\n" %cript_line)
    filecript.close()
elif opcao == 2:
    filename = "testcript.txt"
    filedecript = open("testdecript.txt", "w")
    with open (filename, 'r', errors = 'ignore') as file:
        for line in file:
            print(line)
            cript_line = decod_cesar(line, chave)
            print(cript_line)
            filedecript.writelines("$s\n\n" %cript_line)
    filedecript.close()
