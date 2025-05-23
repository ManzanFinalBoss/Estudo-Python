#==================================[Exercício]===========================

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."

"""

# =============================[Resolução]==============================

# =============================[Variaveis]==============================

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espaco = 'tem'
letras = len(nome)



if not(nome == '') and not(idade ==''):
    if type(nome) == str and type(idade) == int:
        print(f' Seu nome é {nome}'
              '\nSeu nome invertido é {nome[-1:-2000]}'
              '\nSeu nome {espaco} espaços'
              '\nSeu nome tem {letras}'
              )
        
        
else:
    print('Você deixou campos vazios')    