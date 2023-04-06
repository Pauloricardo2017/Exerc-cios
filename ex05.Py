#==============================================
# UMC Mogi Das Cruzes
# Programador: Paulo Ricardo de Sousa
# Data: 29/03/2023
# Programa: Quantidade de Azulejos quadrado para preencher uma parede quadrada
# ==============================================================================
 
Lp = float (input('Digite a largura da parede :'))
La = float (input('Digite a largura do azulejo :'))
Areap = Lp*Lp
Areaa = La*La
Qa = Areap/Areaa
print ('Quantidade de azulejo: %f'% Qa)

