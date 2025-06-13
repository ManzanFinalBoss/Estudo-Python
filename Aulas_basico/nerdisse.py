table = iter(['Felipe','Manzan'])
texto = iter(next(table))


print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

texto = iter(next(table))
print('\n =============================================================\n')
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))


iteratador = iter(texto)  # iterator

while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration:
         break

for letra in texto:
    print(letra)








