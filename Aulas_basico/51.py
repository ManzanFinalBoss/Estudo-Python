# Verificador de CPF

import re
import sys

cpf = input('Digite o CPF para verificação ou criação ')

cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
)

cpf_final = ''
cpf_final_com_pontos= ''
nove_digitos = cpf[0:9]
soma_digitos = 0
mult = 10
primeiro_digito = '' 
segundo_digito = ''

cpf_repetido = cpf == cpf[0] * 11
if cpf_repetido:
    print('Você digitou um CPF com números repetidos')
    sys.exit()



for i in nove_digitos:
    soma_digitos += (int(i) * mult) 
    mult -= 1

primeiro_digito = str((soma_digitos * 10) % 11)

primeiro_digito = '0' if int(primeiro_digito) > 9 else primeiro_digito

cpf_final = nove_digitos + primeiro_digito

soma_digitos = 0
mult = 11

for i in cpf_final:
    soma_digitos += (int(i) * mult) 
    mult -= 1

segundo_digito = str((soma_digitos * 10)%11)

segundo_digito = '0' if int(segundo_digito) > 9 else segundo_digito

cpf_final += segundo_digito


if cpf_final == cpf:
    print('o CPF é Válido')
elif len(cpf) == len(cpf_final):
    print('O CPF não é válido')    
else:
    count = 0
    for i in cpf_final:
        if count == 3 or count ==6:
            cpf_final_com_pontos += '.'
        elif count == 9:
            cpf_final_com_pontos += '-'   
        cpf_final_com_pontos += i
        count +=1

    print(f'O novo CPF gerado foi {cpf_final_com_pontos}')

