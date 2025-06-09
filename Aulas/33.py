# else no while


string = input('Escreva algo ')

i = 0

while i < len(string):

    letra = string[i]

    if letra == ' ':
        break


    print(letra)

    i += 1

else:
    print('Não achei espaços na string definida ')

print('fora do while')    

# Básicamente o else do while é satisfeito quando a condição do while é falsa
# se por algum motivo o leitor do python sair do while sem fazer a comparação
# o else não será executado, como é o caso da utilização do break