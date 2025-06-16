# Retorno de valores das funções (return)

def somar(x, y):
    if x > 10:
        return 10
    return x + y


soma1 = somar(int(input('Número 1 ')), int(input('Número 2 ')))

print(soma1)

soma2 = somar(int(input('Número 1 ')), int(input('Número 2 ')))

print(soma2)

soma3 = somar(soma1, soma2)

print(soma3)
