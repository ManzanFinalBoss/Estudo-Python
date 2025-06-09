# Aprendendo for

texto = 'P'
novo_texto = ''

for letra in texto:
    print(letra)
    novo_texto += f'*{letra}'
    
print(f'{novo_texto}*')    

# for + range
multiplos = 0

while True:
    try:
        a= int(input('start '))
        b= int(input('stop '))
        c= int(input('step '))
        break
    except:
        print('digite apenas numeros inteiros ')
        continue

for numero in range(a, b + 1, c):
    print(numero)
    multiplos += 1

print(f'De {a} até {b} existem {multiplos - 1} multiplos de {c} ')    

# else, coninue, brek, funcionam igual ao while