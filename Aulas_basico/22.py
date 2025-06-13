# =======================[Formatações com f-string]=============================

"""
Formatação básica de strings
s - string
d - int
f - float
x ou X - Hexadecimal
.<número de dígitos>f
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
print(f'{variavel:0>10}')    
Conversion flags - !r !s !a 

"""
# ====================================[Testes]=================================

variavel = 'ABCDEFG'
hexa = 12
 
print(f'{variavel}')
print(f'{variavel:0>10}')    
print(f'{variavel:0<10}')  
print(f'{variavel:0^10}')
print(f'{10000000.92848247274:_=+30,.3f}')
print(f'O exadecimal de {hexa} é {hexa:X}')
