# inserir itens em qualquer local da lista

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

lista.append('Felipe')

print(f'Foi adicionado ao final {lista[-1]}')

nome = lista.pop()

print(f'Foi retirado da lista o último indice {nome}')

del lista[-1]

print(lista)

lista.insert(0, 888)

print(lista)