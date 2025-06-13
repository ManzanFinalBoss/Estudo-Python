# iterando strings com while

# frase = '''

# d2d2d2d2d2d2d2d2d2d2d2d2d2d2ichiwjvwkjvbalfkabvajfabviafkavvihhfiuhvuysbf8hqivbwuibviwubfiubcisbviuwbdk
# '''.upper()


# print(frase.count('d'))

frase = 'aaaooocccgggc'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
string_final = letra_apareceu_mais_vezes

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < qtd_atual:

        apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
        string_final = letra_atual
        
    elif letra_apareceu_mais_vezes == letra_atual:

        i += 1
        continue

    elif apareceu_mais_vezes == qtd_atual:
       string_final = string_final + letra_atual
       letra_apareceu_mais_vezes = letra_atual
    i += 1
else:
    print(
        f'A letra "{string_final}" ' 
        f'foi a que apareceu mais vezes,'
         f' apareceu {apareceu_mais_vezes}x'
         )    
