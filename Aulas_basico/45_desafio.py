"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []


while True:
    os.system('cls')
    print('Selecione uma opção')
    opção = input('[i]nserir [a]pagar l[istar] ').lower()

    if opção.startswith('i'):
        os.system('cls')
        novo_iten = input('Que iten deseja inserir? ')
        lista_de_compras.append(novo_iten)
        input('pressione enter para continuar ')
        continue
    elif opção.startswith('a'):
        os.system('cls')
        if lista_de_compras == []:
            print('Não existem itens para apagar')
            input('pressione enter para continuar ')
            continue
        else:
            
            for indice, iten in enumerate(lista_de_compras):
                print(indice, iten)

            try:
                indice_delete =  int(input('Escolha o indice do iten que está na lista '))   

            except:
                print('Você não escolheu um número ')    
                input('Pressione enter para continuar')
                continue

            for indice, iten in enumerate(lista_de_compras):

                if indice == indice_delete:
                    lista_de_compras.pop(indice)
                    break

            else:
                print('Esse indice não existe na lista')
                input('Pressione enter para continuar ')
                
    elif opção.startswith('l'):
        os.system('cls')
        if lista_de_compras == []:
            print('Não existem itens para listar')
            input('pressione enter para continuar')
            continue

        for indice, iten in enumerate(lista_de_compras):
                print(indice, iten)

        input('Pressione enter para continuar ')        

    else:
        print('Essa opção não existe')    
        input('pressione enter para continuar ')
