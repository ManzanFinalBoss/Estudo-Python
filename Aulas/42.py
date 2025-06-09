# desempacotamento


nome1, nome2, nome3 = ['Felipe', 'Gabriel', 'João']

print(nome1, nome2, nome3)


nome_1, *resto = ['Felipe', 'Gabriel', 'João', 'Frederico']

print(nome_1)
print(resto)

# o _ pula o próximo indice presente na lista
_, _, nome_2, *resto_2 = ['Felipe', 'Gabriel', 'João', 'Frederico']

print(nome_2)
print(resto_2)

