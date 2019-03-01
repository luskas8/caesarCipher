def cifrador(cifra, key):
    cifra.lower()
    new_char = ''

    for char in cifra:
        if char == ' ':
            new_char += ' '
        else:
            if ord(char)+key > 122:
                char = chr(((ord(char) + key) - 122) + 96)
            else:
                char = chr(ord(char) + key)

            new_char += char

    return new_char

def decriptar(cifra):
    cifra.lower()
    new_char = ''
    key = 1
    lista = []

    while True:
        for char in cifra:
            if char == ' ':
                new_char += ' '
            else:
                if ord(char) - key < 97:
                    char = chr(((ord(char) - key) - 97) + 123)
                else:
                    char = chr(ord(char) - key)
        
            new_char += char
        new_char += '\n'
        lista.append(new_char)
        new_char = ''
        if key >= 26:
            break
        else:
            key += 1

    wordlist = open("wordlistPortugues.txt", "r")
    listWord = wordlist.readlines()
    for word in lista:
        if word in listWord:
            return word
    else:
            return 'Palavra não semelhante a nada no portugues'
            exit()        

def decriptar_key(cifra, key):
    cifra.lower()
    new_char = ''
    
    for char in cifra:
        if char == ' ':
            new_char += ' '
        else:
            if ord(char) - key < 97:
                char = chr(((ord(char) - key) - 97) + 123)
            else:
                char = chr(ord(char) - key)
        
        new_char += char

    return new_char

def main():
    try:
        op = int(input('Digite a opção desejada: \n1 - Encriptacao \n2 - Decriptacao\n'))
        if op == 1:
            palavra = input('Digite o texto para ser cifrado: ')
            key = int(input('Digite a chave: '))
            print('Sua palavra cifrada ficou:',cifrador(palavra,key))
        elif op == 2:
            op = int(input('Deseja utilizar qual metodo\n 1 - brute force \n 2 - sabendo a chave \n'))
            if op == 1:
                palavra = input('Digite o texto para ser decriptado: ')
                print(decriptar(palavra))
            elif op == 2:
                palavra = input('Digite o texto para ser decriptado: ')
                key = int(input('Digite a chave: '))
                print(decriptar_key(palavra, key))
        else:
            print('Opcao digitada não existente, saindo do programa...')
            exit()
    except Exception as error:
        print('Ocorreu um erro:', error)

main()
