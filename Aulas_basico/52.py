# Gerador de CPF

import random

while True:
    try:
        qtd_cpf = int(input('Quantos CPFs gostaria de gerar? '))
        break
    except:
        print('Coloque uma quantidade válida ')
        continue

for a in range(0, qtd_cpf):

    cpf = ''
    for i in range(0, 9):
        
        cpf += str(random.randint(0,9))

    cpf_final = ''
    cpf_final_com_pontos = ''
    nove_digitos = cpf[0:9]
    soma_digitos = 0
    mult = 10
    primeiro_digito = ''
    segundo_digito = ''



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

    segundo_digito = str((soma_digitos * 10) % 11)

    segundo_digito = '0' if int(segundo_digito) > 9 else segundo_digito

    cpf_final += segundo_digito


    count = 0
    for i in cpf_final:
        if count == 3 or count == 6:
            cpf_final_com_pontos += '.'
        elif count == 9:
            cpf_final_com_pontos += '-'
        cpf_final_com_pontos += i
        count += 1
    else:
        print(f'O novo CPF gerado foi {cpf_final_com_pontos}')

        