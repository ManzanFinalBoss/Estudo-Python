# =========================[CABEÇALHO]=========================

# PROJETO:        Aula
# AUTOR:          Felipe Manzan
# DATA:           30/05/2025
# DESCRIÇÃO:      Estudando While
# VERSÃO:         1.0
# PYTHON:         3.13

"""
Operadores de atribuição
=     Atribuição simples           → x = 5       (atribui 5 à variável x)
+=    Soma e atribuição            → x += 3      (equivale a x = x + 3)
-=    Subtração e atribuição       → x -= 2      (equivale a x = x - 2)
*=    Multiplicação e atribuição   → x *= 4      (equivale a x = x * 4)
/=    Divisão e atribuição         → x /= 2      (equivale a x = x / 2)
//=   Divisão inteira e atribuição → x //= 2     (equivale a x = x // 2)
**=   Exponenciação e atribuição   → x **= 3     (equivale a x = x ** 3)
%=    Módulo e atribuição          → x %= 2      (equivale a x = x % 2)

"""

# =====================[VARIÁVEIS GLOBAIS]=======================

condicao = True
num = 1
contagem = 0

# ====================[PROGRAMA PRINCIPAL]=======================

# While quebra com a condição sendo False, ou com break dentro do laço

while True:
    print('si')
    num = num + 1

    if num > 2:
        print('fim')
        break

while contagem < 200000:
    contagem += 1

    if contagem  > 7 and contagem < 19:
        continue

    print(contagem)


# ========================[EXECUÇÃO]=============================
if __name__ == '__main__':
    # Chamada da função principal ou lógica principal aqui
    pass
