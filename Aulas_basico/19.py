# ==============================[Operadores lógicos]===============================

'''

Operadores lógicos
and - ambos True
or - pelo menos um True
not - "inverso"
none - valor nulo 

'''

# ==========================[or]===================================

'''
Tabela verdade:

A | B | A OR B
--+---+--------
0 | 0 |   0
0 | 1 |   1
1 | 0 |   1
1 | 1 |   1

'''

entrar = input('Digite E ou S ')

if entrar == 'E' or entrar == 'e':
    print('Vc entrou')
else:
    print('Vc saiu')    

# ===============================[and]===================    

'''
Tabela verdade:

A | B | A AND B
--+---+--------
0 | 0 |   0
0 | 1 |   0
1 | 0 |   0
1 | 1 |   1

'''

entrar_2 = input('Digite a senha ')

if (entrar == 'E' or entrar == 'e') and entrar_2 == '1234':
    print('Acesso concedido')
else:
    print('Acesso negado')    


# ===============================[not]===================    

'''
Tabela verdade:

 A | NOT A
---+--------
 0 |   1
 1 |   0

'''
if (not(entrar == 'E' or entrar == 'e') and entrar_2 == '1234'):
    print('Acesso concedido parte 2')
else:
    print('Acesso negado parte 2')  