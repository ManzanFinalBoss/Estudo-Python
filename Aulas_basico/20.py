# ===========================[Operadores in e not in]============================

#string em python são iteráveis, o que significa que dá para navegar como uma lista

# ================================[testes]======================================

nome= 'Manzan'

print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])

print(20*'=', '[in]', 20*'=',sep='')

print('1-', 'n' in nome)
print('2-','j' in nome)
print('3-','n' in nome[1])
print('4-','n' in nome[2])
print('5-','n' not in nome[1])
print('6-','zan' in nome )
print('7-','zan' not in nome )
print(f'8- {'Man' not in nome}')
