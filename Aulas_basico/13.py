# ==============================[Formatação de String]==========================

#Introdução a f-string

# =================================[Variáveis]=========================================

nome = 'Felipe Manzan'
peso = 95
altura = 1.9
# .xf acrescenta x casas decimais e , a cada 3 numeros coloca uma virgula, ex: 10,000
teste= f'{nome} Tem {altura:,.2f} de altura' 
teste_2 = f'Pesa {peso}Kg e seu IMC é de {peso / (altura ** 2):,.2f}Kg/m^2'

# ==========================[Function]=================================

print(teste)
print(teste_2)