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
age = input('Digite sua idade: ')





if not(nome == '') and not(age ==''):
    idade = int(age)  
    if type(nome) == str and type(idade) == int:
        print(60* '=')
        letras = len(nome.replace(" ", ""))
        if " " in nome:
            espaco = 'tem' 
        else:
            espaco = 'não tem'            
        print(f' Seu nome é {nome}'
              f'\nSeu nome invertido é {nome[::-1][:len(nome)+1]}'
              f'\nSeu nome {espaco} espaços'
              f'\nSeu nome tem {letras} letras'
              f'\nA primeira letra do seu nome é {nome[0]}'
              f'\nA ultima letra do seu nome é {nome[len(nome) - 1]}'
              )
    else: 
        print('Alguma das variáveis não está com o tipo certo')
        
else:
    print(60* '=')
    print('Você deixou campos vazios')   
