# formatar data para: dd/MM/AAAA
from datetime import datetime

data_atual = datetime.now()
print('Esta é a data no formato padrão: ', data_atual)

# formatando a data 
data_formatada = data_atual.strftime('%d/%m/%Y')
print()
print('Data no formato PT-BR: ', data_formatada)