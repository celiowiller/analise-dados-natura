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
print()
'''
total_vendas_por_rep: var que recebe como valor a totalização das vendas por representante 

 df.groupby('Rep'): este trecho esta "agrupando" elementos do df - com base nas colunas  'Rep' - representantes de venda  - e 'Quantity - quantidade de produtos; cada grupo, agora, contem todas as linhas de vendas feitas por um mesmo representante

 [['Quantity']]: aqui, estamos praticando a seleção apenas da coluna 'Quantity'; [[]] ao usar os caracteres colchetes duplos estamos retornando - a partir desta seleção - um "novo" Dataframe(em vez de um Series)

 .sum(): aplicando, ao fazer uso da função sum(), sobre a coluna 'Quantity' a soma para cada grupo(com cada representante), nos da o seguinte resultado: soma total dos produtos vendidos por cada um dos representantes.
'''

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 2A - TOTAL DE VENDAS REALIZADAS POR REPRESENTANTE *** este numero precisa fazer sentido, tambem, para nós')
# qtde_vendas_por_rep = df.groupby('Rep').count()
qtde_vendas_por_rep = df.groupby('Rep').size()
print()
print('Qtde vendas realizadas para cada representante')
print(qtde_vendas_por_rep )
print()


print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 2B - MÉDIA DE VENDAS POR REPRESENTANTE')
media_vendas_por_rep = df.groupby(['Rep'])[['Quantity']].mean()
print()
print('\nMédia de vendas de produto por representante\n')
print(media_vendas_por_rep)
print()

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 3 - USO DA FUNÇÃO DE AGREGAÇÃO')
agregando_operacoes = df.groupby('Rep')['Quantity'].agg(
    Qtde_T_Negociacoes = 'count',
    Qtde_T_Produtos_Vendidos = 'sum',
    Media_Produto_Rep = 'mean' 
)
print()
print('Resultado da função de agregação\n')
print(agregando_operacoes)

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 4A - MENOR PREÇO DE PRODUTO VENDIDO POR REP')
menor_preco_rep_prod = df.groupby(['Rep'])[['Price']].min()

print()
print('Menor preço de produto vendido por representante\n')
print(menor_preco_rep_prod)

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 4B - MAIOR PREÇO DE PRODUTO VENDIDO POR REP')
maior_preco_rep_prod = df.groupby(['Rep'])[['Price']].max()

print()
print('Maior preço de produto vendido por representante\n')
print(maior_preco_rep_prod)
'''
menor_preco_rep_prod: var que recebe como valor o menor valor da coluna Price

 df.groupby('Rep'): este trecho esta "agrupando" elementos do df - com base nas colunas  'Rep' - representantes de venda  - e 'Price - preço dos produtos; cada grupo, agora, contem todas as linhas de vendas feitas por um mesmo representante

 [['Price']]: aqui, estamos praticando a seleção apenas da coluna 'Price'; [[]] ao usar os caracteres colchetes duplos estamos retornando - a partir desta seleção - um "novo" Dataframe(em vez de um Series)

 .min(): aplicando, ao fazer uso da função min(), sobre a coluna 'Price' o valor minido de cada produto para cada grupo(com cada representante), nos da o seguinte resultado: o produto mais "barato" vendido por cada um dos representantes.
'''
print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 5 - MENOR PREÇO DE UM PRODUTO ')
menor_preco_prod = df.groupby(['Product'])[['Price']].min()
print()
print('Menor preço de um produto\n')
print(menor_preco_prod)
print()


print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 6 - MAIOR PREÇO DE UM PRODUTO ')
menor_preco_prod = df.groupby(['Product'])[['Price']].max()
print()
print('Maior preço de um produto\n')
print(menor_preco_prod)
print()


print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 7A - MENOR VALOR/PREÇO DE UM PRODUTO VENDIDO PELO REP ')
# AQUI, BUSCAMOS O PRODUTO "MAIS BARATO/COM O MENOR VALOR" QUE UM UNICO REP VENDEU
operacao_7 = df[df['Price'] == df['Price'].min()][['Product', 'Rep', 'Price']]

# agora, vamos agrupar e aplicar a função adequada ao agrupamento
df.groupby(['Rep'])[['Quantity']].sum()
print()
print('Produto com o menor valor/preço vendido(se houver mais de um:)')
print(operacao_7)
print()
# -------------------------------------------------------------------
print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 7B - MENOR VALOR/PREÇO DE UM PRODUTO VENDIDO PELO REP ')
# AQUI, BUSCAMOS O PRODUTO "MAIS BARATO/COM O MENOR VALOR" QUE UM UNICO REP VENDEU
# esta é a abordagem adequada para não " deixar passar" nenhum valor relevante para a analise
operacao_7B = df.groupby('Rep')['Price'].idxmin()
resultado = df.loc[operacao_7B]
print()
print('Produto com o menor valor/preço vendido por representante')
print(resultado[['Rep', 'Product', 'Price']])

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 7C - MAIOR VALOR/PREÇO DE UM PRODUTO VENDIDO PELO REP ')
# AQUI, BUSCAMOS O PRODUTO "MAIS BARATO/COM O MENOR VALOR" QUE UM UNICO REP VENDEU
# esta é a abordagem adequada para não " deixar passar" nenhum valor relevante para a analise
operacao_7C = df.groupby('Rep')['Price'].idxmax()
resultado = df.loc[operacao_7C]
print()
print('Produto com o maior valor/preço vendido por representante')
print(resultado[['Rep', 'Product', 'Price']])

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 8 - TOTALIZAÇÃO DE MAIS DE UMA COLUNA ')
# totalizar as colunas 'Quantity' e 'Price' fazendo uso do groupby()
operacao_8 = df.groupby(['Rep']).agg({
    'Quantity': 'sum', 'Price': 'sum'
})
print()
print('Total de vendas por representante / total de preços tambem:\n')
print(operacao_8)
print()

print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 9 - FAZER USO DO PIVOT TABLE')

def func_intervalo(x):
    # definir a expressão de retorno da função
    return x.max() - x.min() # dessa forma, estamos retornando um intervalo de valores
# acima, a função executa a seguinte operação: obtem o valor maximo de preço de produto
# vendido, por cada um dos reps e subtrai pelo menor preço de produto vendido por cada rep
# gerando um valor de intervalo
# fazer uso da função pivot_table()
operacao_9 = pd.pivot_table(
    df, 
    index = ['Manager', 'Rep'],
    values = ['Price'], 
    aggfunc = func_intervalo
) # aggfunc = func_intervalo: nada mais é do que uma expressão de função -> pois tem atribuido, à ela, como valor a chamada da função func_intervalo

print('Pivot table com faixa de valores obtidos da coluna Price:\n')
print(operacao_9)
print()


print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 10 - ANALISE MULTIVARIADA COM PIVOT TABLE')
operacao_10 = pd.pivot_table(
    df,
    index = ['Manager', 'Rep'],
    columns = 'Product',
    values = ['Price', 'Quantity'],
    aggfunc = {
        'Price':[np.sum, np.mean],
        'Quantity': [np.sum]
        },
        fill_value = 0             
)

print()
print('Analise multivariada com Pivot Table\n')
print(operacao_10)


print('-----------------------------------------------------------------')
print()
print('OPERAÇÃO 11 - ANALISE DA CORRELAÇÃO ENTRE VARIAVEIS/CLASSE/COLUNA')
# vamos, abaixo, criar uma coluna nova, no df, observar o resultado 
df['Total_Sales'] = df['Quantity'] * df['Price']
print('Dataframe com a nova coluna de Total_Sales adicionada\n')
print(df[['Rep', 'Product', 'Quantity', 'Price', 'Total_Sales']].head())

# a correlação entre as colunas
correlacao = df[['Price', 'Quantity', 'Total_Sales']].corr()
print()
print('Correlação entre Preço, Quantidade e Vendas Totais\n')
print(correlacao)
print()