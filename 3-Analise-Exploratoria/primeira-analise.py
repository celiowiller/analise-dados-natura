# ANALISE PIPELINE (FLUXO) DE VENDAS
# importar as bibliotecas necessarias
import pandas as pd
import numpy as np

# BLOCO I - 
'''
1. carregar os dados
2. ler as primeiras do df
3. fazer um resumo estatistico
'''
df = pd.read_excel('vendas.xlsx')
print('Primeiras 5 linhas do df')
print()
print(df.head(5))

print()

print('RESUMO ESTATISTICO')
print(df.describe())
print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 1 - TOTALIZAÇÃO DE VENDAS POR REPRESENTANTE')

# definir uma var para receber como valor  a totalização das vendas ppor representante
total_vendas_por_rep = df.groupby('Rep')[['Quantity']].sum()
print()
print('Total de vendas de produtos por representante: \n')
print(total_vendas_por_rep)

'''
total_vendas_por_rep: var que recebe como valor a totalização das vendas por representante 

 df.groupby('Rep'): este trecho esta "agrupando" elementos do df - com base nas colunas  'Rep' - representantes de venda  - e 'Quantity - quantidade de produtos; cada grupo, agora, contem todas as linhas de vendas feitas por um mesmo representante

 [['Quantity']]: aqui, estamos praticando a seleção apenas da coluna 'Quantity'; [[]] ao usar os caracteres colchetes duplos estamos retornando - a partir desta seleção - um "novo" Dataframe(em vez de um Series)

 .sum(): aplicando, ao fazer uso da função sum(), sobre a coluna 'Quantity' a soma para cada grupo(com cada representante), nos da o seguinte resultado: soma total dos produtos vendidos por cada um dos representantes.
'''