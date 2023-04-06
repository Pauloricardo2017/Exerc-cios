# ==========================================
# UMC Mogi Das Cruzes
# Programador: Paulo Ricardo de sousa
# Data: 30/03/2023
# Programa: Estoque
# ===========================================

Total = int(input('Total Em Estoque ='))
Venda = int(input('Total Vendido ='))
Vendas_Porcen = Venda/Total*100
Simbolo = '%'
print('Total Em Estoque = %i' % (Total))
print('Total Vendido = %i' % (Venda))
print('Porcentagem De Vendas = %.2f ' % (Vendas_Porcen))
