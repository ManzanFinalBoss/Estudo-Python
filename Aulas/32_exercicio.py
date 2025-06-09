# =========================[CABEÇALHO]=========================

# PROJETO:        Aula
# AUTOR:          Felipe Manzan
# DATA:           02/06/2025
# DESCRIÇÃO:      Estudando While
# VERSÃO:         1.0
# PYTHON:         3.13

#Atividade de uma calculadora com while

# ====================[PROGRAMA PRINCIPAL]=======================

operadores_permitidos = '+-/*'

while True:

    numero_1 = input('Digite um número ')
    numero_2 = input('Digite um número ')
    operador = input('Digite um operador [+-/*] ')
    
    numeros_validos = None

    try:

        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        print('Apenas números são válidos')
        continue 

    if operador not in operadores_permitidos:
        print('Operador invalido ')
        continue

    if len(operador) > 1:
        print('Operador invalido, escolha apenas um ')
        continue
    

    print('O resultado é:')

    if operador == '+':
        print(numero_1 + numero_2)
        
    elif operador == '-':
        print(numero_1 - numero_2)
        
    elif operador == '/':
        print(numero_1 / numero_2)

    elif operador == '*':
        print(numero_1 * numero_2)

    else:
        print('saporra n deveria acontecer')

    sair = input('Quer sair? ').lower().startswith('s')

    if sair is True:
        break

# ========================[EXECUÇÃO]=============================
if __name__ == '__main__':
    # Chamada da função principal ou lógica principal aqui
    pass
