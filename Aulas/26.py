# ==============================[Constantes no python]=========================================

# Usando constanates e simplificações no python
# N existe constante de verdade, más letras maiúsculas simbolizam uma constante

# ======================================[Exemplificações]=================================

# ======================================[Constantes]=================================

RADAR_1 = 60 # Velocidade máxima do radar
LOCAL_1 = 100 # Posição do radar 1
RADAR_RANGE = 1 # Alcance do radar

# ======================================[Variáveis]=================================

velocidade = 61 # Velocidade do carro
local_carro = 102 # posição do carro

# ======================================[Simplificações]=================================

velocidade_carro_passou_radar_1 = velocidade > RADAR_1 # verifica se o carro está acima da velocidade máxima do radar
posicao_carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and\
    local_carro <= (LOCAL_1 + RADAR_RANGE) # verifica se o carro está dentro do alcance do radar
carro_multado_radar_1 = posicao_carro_passou_radar_1 and velocidade_carro_passou_radar_1 # verifica se o carro foi multado

# =========================================[função do code]==============================

if velocidade_carro_passou_radar_1:
    print('A velocidade do carro está acima do limite')

if posicao_carro_passou_radar_1:
    print('O carro está no alcance do radar')    

if carro_multado_radar_1:
    print('O carro foi multado')    



