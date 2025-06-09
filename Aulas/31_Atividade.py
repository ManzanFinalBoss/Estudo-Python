# =========================[CABEÇALHO]=========================

# PROJETO:        Aula
# AUTOR:          Felipe Manzan
# DATA:           02/06/2025
# DESCRIÇÃO:      Estudando While
# VERSÃO:         1.0
# PYTHON:         3.13

# =====================[VARIÁVEIS GLOBAIS]=======================

nome = None
tamanho_nome = None
indice = 0
string_final = ''
string_final_2 = ''

# ====================[PROGRAMA PRINCIPAL]=======================

nome = input('Qual o nome? ')
tamanho_nome = len(nome)

while indice < tamanho_nome:
    string_final += '*' + nome[indice]
    string_final_2 += f'-{nome[indice]}'

    indice += 1

string_final += '*'
string_final_2 += '-'

print(string_final)
print(string_final_2)


# ========================[EXECUÇÃO]=============================
if __name__ == '__main__':
    # Chamada da função principal ou lógica principal aqui
    pass
