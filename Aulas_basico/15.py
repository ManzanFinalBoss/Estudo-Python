# ==========================[Função input]==================================

# input coleta dados pelo terminal
# input sempre pega as informações escritas como string

#=============================[Testes]========================

# teste de input com string
nome = input('Qual seu nome? ')

print(f'O seu nome é {nome}')

# testando a concatenação de numeros string
numero_1 = input('Digite um número ')
numero_2 = input('Digite um número ')

print(f'A soma dos numeros em teste é {numero_1 + numero_2}')

# testando operadores com numeros após coerção
n1 = float(numero_2)
n2 = float(numero_1)

print(f'A soma dos números é {n1 + n2:.0f}')

  