# ===============================[Formatação]==============================

# Novos tipos de formatação

# ==================================[Variaveis]========================

a = 'A'
b = 'B'
c= 1.234
string = 'a={0} b={1} a={0} c={2:.2f}' # Puxa por indices não nomeados dentro do format
formato= string.format(a,b,c)

string2 = 'a={nome1} b={nome2} a={nome1} c={nome3:.2f}' # Puxa por indices nomeados dentro do format
formato2 = string2.format(
    nome1=a,
    nome2=b,
    nome3=c
    )

#===========================[functions]===================================

print(formato)
print(formato2)