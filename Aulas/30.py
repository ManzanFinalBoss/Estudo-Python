# =========================[CABEÇALHO]=========================

# PROJETO:        Aula
# AUTOR:          Felipe Manzan
# DATA:           02/06/2025
# DESCRIÇÃO:      Estudando While
# VERSÃO:         1.0
# PYTHON:         3.13

# While dentro de While

# =====================[VARIÁVEIS GLOBAIS]=======================

qtd_linhas = 10
qtd_colunas = 20
linha = 1

# ====================[PROGRAMA PRINCIPAL]=======================

while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna +=1

    linha += 1

print('fim')

# ========================[EXECUÇÃO]=============================
if __name__ == '__main__':
    # Chamada da função principal ou lógica principal aqui
    pass
