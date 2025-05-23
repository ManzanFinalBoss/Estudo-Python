from time import sleep

while True:
    print('\nEscolha o tipo de número ou digite "sair" para encerrar.')

    tipo = input('Qual tipo de número? '
                 '\n [1] - Decimal'
                 '\n [2] - Hexadecimal'
                 '\n [3] - Octal'
                 '\n [4] - Binário\n'
                 '> ')

    if tipo.lower() == 'sair':
        print('Encerrando o programa...')
        break

    try:
        if tipo == '1' or tipo.lower() == 'decimal':
            num = int(input('Digite um valor inteiro (decimal): '))
        elif tipo == '2' or tipo.lower() == 'hexadecimal':
            num = int(input('Digite um valor em hexadecimal (ex: 2A): '), 16)
        elif tipo == '3' or tipo.lower() == 'octal':
            num = int(input('Digite um valor em octal (ex: 52): '), 8)
        elif tipo == '4' or tipo.lower() in ['binario', 'binário']:
            num = int(input('Digite um valor em binário (ex: 101010): '), 2)
        else:
            print('⚠️ Tipo inválido! Tente novamente.')
            continue

        print('='*20, '[ Conversão ]', '='*20)
        print('Decimal:     %i' % num)
        print('Hexadecimal: %X' % num)
        print('Octal:       %o' % num)
        print('Binário:     %s' % bin(num)[2:])
        input('Pressione ENTER para continuar')
        sleep(1)

        
    except ValueError:
        print('❌ Número inválido para essa base. Tente novamente.')
