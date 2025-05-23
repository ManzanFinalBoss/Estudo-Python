# ===============================[if, else, elif ]==============================

# Os blocos vão de if a if ou de if a else, com elif no meio
 
# ============================[Testando parte 1 ]=============================

teste = input('Escolha 1 ou 2 ')

if teste == '1':
    print(f'O teste funcionou {teste}')
elif teste == '2':
    print(f'O teste funcionou parte 2. {teste}')    
else:
    print(f'A opção {teste} não existe')
         
# ============================[Testando parte 2]=============================

cond_2 = input('Escolha um número ')


if cond_2 in ['1','2','3','4','5','6']:
    print(f' O número {cond_2} existe')

else:
    print(f'O número {cond_2} não existe')
