# ==========================[Exercicio]===============================================

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# =============================[E1]============================================

try:
    
    numero_digitado = int(input('Digite um número inteiro '))

    numero_par = numero_digitado % 2 == 0
    
    if numero_par:
        print(f'O número {numero_digitado} é par')

    else:    
        print(f'O número {numero_digitado} é ímpar')

except:
    print('Você não digitou um número inteiro') 

# =============================[E2]============================================      

try: 
    horario = int(input('Que horas são? (Apenas as Hóras sem minutos) '))
    dia = horario >= 0 and horario <= 11
    tarde = horario > 11 and horario <= 17
    noite = horario > 17 and horario <= 23

    if tarde:
        print('Boa tarde')

    if dia:
        print('Bom dia')    
    if noite:
        print('Boa noite')

except:
    print('Vc n digitou um horário válido')        


# =============================[E3]============================================  


nome = input('Qual seu primeiro nome? ')

try:
    float(nome)
    print('Você não digitou um nome válido')

except:

    if (len(nome)) <= 4 and (len(nome)) != 0:
        print('Seu nome é muito curto') 
    elif (len(nome)) >= 5 and  (len(nome)) <= 6:
        print('Seu nome é normal')
    elif not nome:
        print('Você não digitou nada')    
    else:
        print('Seu nome é muito grande')   



