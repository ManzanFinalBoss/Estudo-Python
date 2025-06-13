"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


def escrita(a, b, c):
    print(f'a= {a} | b= {b} | c= {c}')

'''
Argumentos nomeados e não nomeados
chamando com a ',' atribue ao parametrô em ordem, usando o argumento nomeado, não precisa estar em ordem
porém, a partir do 1° argumento nomeado, os proximos precisam ser também
'''
x = 1
y = 2
z = 4

escrita(1, 2, 4)
escrita(2, 4, 1)
escrita(c=4, b=2, a=1)
escrita(a=x,b=y,c=z)

print(escrita)