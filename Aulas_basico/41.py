# for in com listas

lista = ['Felipe', 'Maria', 'Nathan']

for nome in lista:

    print(nome,type(nome))




lista_nome = ['Felipe', 'Maria', 'Nathan']

lista.append('Jefferesonf')
lista.append('Silva')

indices = range(len(lista))

for indice in indices:
    print(f'{indice} {lista[indice]} {type(lista[indice])}')