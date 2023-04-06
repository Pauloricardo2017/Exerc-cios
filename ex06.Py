# ======================================================
# UMC Mogi Das Cruzes
# Programador: Paulo Ricardo de Sousa
# Data: 29/03/2023
# Programa: Quantidade de Azulejo retangular para preencher uma parede retangular...
# ===================================================================================

Lar = float(input('Digite a Largura da parede:'))
Alt = float(input('Digite a altura da parede:'))
Lar1 = float(input('Digite a largura do azulejo:'))
Alt1 = float(input('Digite a altura do azulejo:'))
Area1 = Lar*Alt
Area2 = Alt1*Lar1
Qa = Area1/Area2
print('Quantidade de azulejo: %f' % Qa)
