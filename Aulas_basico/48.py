"""
Lista de listas e seus índices
"""

salas = [

    ['Maria', 'Felipe'],
    ['José', 'Pedro'],
    ['Helena', 'Roberto', 'Pedrini', ['Felipe', 'Jose', 'Paulo']]


]

#print(salas[2][3][2])

for sala in salas:
    print(sala)

    for item in sala:
        print(item)

        for iter in item:
            print(iter)

            if len(iter) > 1:
                for iter_2 in iter:
                    print(iter_2)



