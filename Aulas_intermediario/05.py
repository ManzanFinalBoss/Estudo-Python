'''
args - Argumentos não nomeados
* - *args (empacotameno e desempacotamnto)
'''

# lembrete de desempacotamento

x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8

print(x, y, resto, sep='; ')


def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total)
    return total


numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(soma(*numeros))
