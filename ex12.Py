# =======================================
# UMC Mogi Das Cruzes
# Programador: Paulo Ricardo de Sousa
# Data: 30/03/2023
# Programa: Resto da divisão
# ========================================

Num1 = float(input('Digite o primeiro número = '))
Num2 = float(input('Digite o Segundo Número ='))
Inteira = Num1//Num2
Resto1 = Num1 % Num2
Resto2 = divmod(Num1, Num2)
print('Resto da Divisão = %f' % (Resto1))
print('Parte inteira e o Resto Usando Função Divmod', Resto2)