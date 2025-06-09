# Listas
import os

lista_1 = [123, True, 'Felipe Manzan', 1.7]

print(lista_1)

lista_1[-3] = 'siii'

print('Indice 2: ', lista_1[2])

print('Indice -3: ', lista_1[-3]) 

#Básicamente dá pra alterar todos os itens da lista

os.system('cls')

lista_2 = [10, 20, 30, 40]

lista_2[2] *= 10

print(lista_2) 
print(lista_2[2]) 


del lista_2[2] # deleta o iten 2 da lista 

print(lista_2)
print(lista_2[2]) 

lista_2.append(50)
lista_2.append(60)
lista_2.append(70)
lista_2.append(80)
lista_2.append('Manzan')

print(lista_2)


ultimo_valor = lista_2.pop() # pop() deleta e  retorna o ultimo valor da lista

valor_da_lista = lista_2.pop(-4) # pop(3) deleta e  retorna o indice(x) da lista

print(ultimo_valor)
print(valor_da_lista)
print(lista_2)