"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Uma Frase bem grande, e aleatória'
lista_frases_crua = frase.split(',') # se não colocar nada dentro, splita no " "
lista_frases_tratadas = []
frases_unidas = ' '


for i, frase in enumerate(lista_frases_crua):
    lista_frases_tratadas.append(lista_frases_crua[i].strip())
else:
    print(lista_frases_tratadas)

frases_unidas = frases_unidas.join(lista_frases_tratadas)

print(frases_unidas)