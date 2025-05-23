# ========================================[interpolação de string]========================================

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
o - octal

"""

# ========================================[teste]========================================
nome = 'Felipe'
preco = 112233.554456655
variavel = '%s, o valor da compra é de R$%.2f' %(nome, preco)
print(variavel)

tipo = input('Qual tipo de número? '
             '\n [1] - Decimal'
             '\n [2] - Hexadecimal'
             '\n [3] - Octal'
             '\n [4] - Binário\n')

if tipo == '1' or tipo.lower() == 'decimal':
    num = int(input('Digite um valor inteiro (decimal): '))
elif tipo == '2' or tipo.lower() == 'hexadecimal':
    num = int(input('Digite um valor em hexadecimal (ex: 2A): '), 16)
elif tipo == '3' or tipo.lower() == 'octal':
    num = int(input('Digite um valor em octal (ex: 52): '), 8)
elif tipo == '4' or tipo.lower() == 'binário' or tipo.lower() == 'binario':
    num = int(input('Digite um valor em binário (ex: 101010): '), 2)
else:
    print('Tipo inválido!')

print(20*'=','[Conversão',20*'=')
print('Decimal: %i \n'
'Hexadecimal: %X \n' 
'Octal: %o \n'
'Binário: %s '
% (num,num,num,bin(num)[2:])) # [2:] diz "pegue do iíndice 2 em diante", isso retira o 0b antés do número
