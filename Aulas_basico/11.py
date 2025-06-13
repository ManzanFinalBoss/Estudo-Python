# =========================[Precedencia dos operadores]==================================

# Aprendendo a Precedencia dos operadores

ordem ='''
ordem de precedencia:
1 - (n + n)
2 - **
3 - *, /, //, %
4 - +, -
'''
# =============================[Variáveis]===============================================

conta_1 = 1 + 1 ** 5 + 5 
conta_2 = (1 + 1) ** (5 + 5) # 2^10
conta_3 = (1+(205 - 204)) ** (5 + (3 + 2)) # mesma coisa que conta_2

# ==============================[functions]================================================

print(ordem)
print('====================================[testes]================================')
print(conta_1)
print(conta_2)
print(conta_3)
