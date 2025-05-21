# ======================================[Funções Matemáicas]=======================================

# Testando funções matemáticas

# ==================================[Operadores]=======================================

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicão', multiplicacao)

divisao = 10 / 3  # Gera um float
print('Divisão', divisao)

# Gera inteiro se o dividendo e o divisor forem inteiros, caso um seja float, gera float
# essa operação ignora o que vem depois da vírgula
divisao_inteira = 10 // 3
print('Divisão Inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciaçao', exponenciacao)

modulo = 55 % 5  # Apresenta o resto da divisão
print('Módulo', modulo)

# ========================[Um pequeno teste]=========================================

print(
    '\n========================[Teste1]===================\n'
    'Divisão de 10/8 é:\n',
    10//8,
    '\nTem resto:\n',
    10 % 8
)

print(
'\n',
'=================[Teste2]================================\n'
'Divisão de 10 por 8:', str(10//8),'|', 'Resto:', str(10%8)
)