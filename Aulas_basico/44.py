# enumerate - enumera ieráveis



lista = ['Maria', 'Felipe', 'João']

lista.append('Pedro')

lista_enumerada = enumerate(lista) # a variável lista_enumerada só pode ser consumida 1 única vez sua iteração em for

for item in lista_enumerada:
    print(item)

    for nome in item:
        print(nome)
        if type(nome) is int:
            continue
        for algo in nome:
            print(algo)

print('=' * 50)

for indice, nome in enumerate(lista):
    print(indice, nome, '|', lista[indice])


print('=' * 50)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)