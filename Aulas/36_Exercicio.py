"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

tentativas = 0
letras_descobertas = ''
  
while True:
    palavra_secreta = input('digite a palavra secreta ').lower()
    os.system('cls')
    
    while True:

        letra_digitada = input('Digite uma letra da palavra secreta ').lower()

        if len(letra_digitada) > 1:
            print('Digite apenas 1 letra')
            continue

        tentativas += 1

        if letra_digitada in palavra_secreta:
            print(f'A letra {letra_digitada} está na palavra')
            letras_descobertas += letra_digitada
        else:
            print('A letra digitada não está na palavra secreta')

        resultado = ''    

        for letra_it in palavra_secreta:

            if letra_it in letras_descobertas:
                resultado += letra_it

            else:
                resultado += '*'    

        print(f'palavra secreta= {resultado}')        
        
        
        if resultado == palavra_secreta:
            os.system('cls')
            print('=' * 40)
            print(f'Parabens vc acertou a palavra secreta, com {tentativas} tentativas')
            print(f'A palavra era: {palavra_secreta}')
            break

    letras_descobertas = ''    
    tentativas = 0

    sair = input('deseja sair? ')
    if sair.lower().startswith('s'):
        print('saindo...')
        os.system('cls')
        break
            