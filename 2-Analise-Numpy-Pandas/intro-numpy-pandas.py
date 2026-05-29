# agora, vamos começar a lidar  com elementos de maior complexidade
# portanto, vamos iniciar os codigos importando os recursos de módulo para que tudo funcione adequadamente
import numpy as np # aqui, a lib numpy recebe um "apelido", portanto, quando precisarmso referenciar a lib numpy basta escrever np

# criar duas matrizes - ambas receberão valores distintos
matriz1 = np.array([ [2, 4], [5, -6]  ]) # esta é a função array, com origem no numpy, especificamente usada para criar arrays

matriz2 = np.array([ [9, -4], [3, 5] ])


# definir a operação de soma das matrizes
matrizResultante = matriz1 + matriz2 

# exibir o resultado da soma das matrizes
print('O resultado da operação é: ', matrizResultante) 

#=======================================================================
# AULA DE 29/05/2026

print()
print('===================== OPERAÇÕES/ANALISES COM NUMPY/PANDAS ====================')
# agora, vamos importat o pandas
import pandas as pd

# definir uma Series  -uma Series nada mais é do que: uma matriz unidimensional, ou seja, de uma  unica linha
umaSerie = pd.Series([1, 2, 3, np.nan, 6, 8, 'Ola'])

# acima, temos um valor chamado 'np.nan' -> este é o um recurso, com origem no np, que nos oferece a possibilidade de trabalhar com um elemento 'não-numérico'(not-a-number); basicamente, temos uma lista de valores que são atribuidos à uma variavel - a partir do recurso Serries com origem no pandas para formar a matriz unidimensional

print(umaSerie) 

# ---------------------------------------------------------------------------------------

print()
print('=================  criar alguns Dataframes ====================')
print()
print('=================  criar Dataframe 1 ====================')

# neste passo, será definida uma nova variavel para receber um conjunto d evalroes 
algumasDatas = pd.date_range('20260506', periods = 6)
print(algumasDatas)

'''
para criar o conjunto de dados DateTimeIndex precisamos usar pouco recursos - são estes:

pd -> lib pandas

date_range() -> esta é ua função para criar o intervalo/conjunto de valores baseados em datas

parametros: '20260506' -> parametro string que referencia o ponto inicial de data para a construção do intervalo de valores 

parametros: periods = 6 -> esta é a quantidade de valores - periodos - que queremos definir para o intervalo.

por padrão, o pandas estabeleceu para o intervalo  de datas gerado, uma 'freq' (frequency) diária -> freq= 'D'

então o resultado é este: DateTimeeIndex(
['2026-05-06', '2026-05-07', '2026-05-08', '2026-05-09',
               '2026-05-10', '2026-05-11'], dtype='datetime64[ns]', freq='D')

'''

# agora, vamos definir o DataFrame
df1 = pd.DataFrame(np.random.randn(6, 4), index = algumasDatas, columns = list('ABCD'))

'''
DataFrame: classe, do pandas, para criar os "quadros de dados" - baseados em linha e coluna

o 1º argumento significa np.random.randn(6, 4): uso do numpy para a geração de numeros randomicos para "popular" o df1; o valores de parametro da função randn(6, 4) significam: este df1 será preenchido por valores randomicos para a seguinte estrutura: 6 linhas e 4 colunas

o 2º argumento index = algumasDatas significa: define qual será o recurso de indice principal do df1; o indice principal de qualquer DF é o indice de LINHAS - AXIS = 0

o 2º argumento columns = list('ABCD') significa: define os labels/nomes das colunas do df1
'''
print()
print('Este é o nosso 1º dataframe')
print(df1)
print()
# -------------------------------------------------------------------

print('=================  criar Dataframe 2 ====================')

# gerar um novo dataframe; será gerado a partir de um dicionario]

# quando usamos dicionarios - baseados em pares key/value - o elemento key se tornará a coluna do df2 e quaisquer valores associados ao keys se tornarão o valores que popularão o df2

df2 = pd.DataFrame({
    'A': 1., # valor constante repetido para todas as linhas do df2

    'B': pd.Timestamp('20260605'),

    'C': pd.Series(1, index = list(range(4)), dtype = 'float64'), # Series com 4 elementos do tipo float que resulta no numero 1.0 - > indicado no argumento 1 

    'D': np.array([3.0] * 4, dtype = 'int32'), # array com 4 valores  - indicados na equacão - [3.0] * 4 - mas devemos lembra que o array foi definido com o dtype = inte32

    'E': pd.Categorical(['teste', 568, 'novo teste', 42]), # categorico com valores variados
    
    'F': 'esta é uma string' # mesma string vai "popular" todas as linhas da coluna F 
})

print()
print('Este é o df2 ')
print(df2)

print()
print('=================  observando - analise primaria  - os contexto dos DFs ====================')
print()

# uso do comando/palavra reservada dtypes(data types) demonstrar os tipos de dados do df
print('composição dos data types do df1')
print(df1.dtypes) 
print('composição dos data types do df2')
print(df2.dtypes) 
print()

# neste passo, vamos fazer uma "leitura" resumida dos DFs; para este proposito será utilizada a função head() -> por padrão, a função head() Lê as primeiras 5 linhas do df
print('primeiras do df1')
print(df1.head(2))
print('primeiras do df2')
print(df2.head(2))
print()
# neste passo, vamos fazer uma "leitura" resumida dos DFs; para este proposito será utilizada a função tail() -> por padrão, a função head() Lê as ultimas 3 linhas do df
print('ultimas linhas do df1')
print(df1.tail(2))
print('ultimas linhas do df2')
print(df2.tail(2))
print()

# neste passo, vamos fazer uma "leitura" indice dos DFs; para este proposito será utilizado o comando index
print('indices do df1')
print(df1.index)
print('indices do df2')
print(df2.index)
# neste passo, vamos fazer uma "leitura" colunas dos DFs; para este proposito será utilizado o comando columns
print('colunas do df1')
print(df1.columns)
print('colunas do df2')
print(df2.columns)
print()

# neste passo, vamos fazer uma "leitura" de resumo/resumir, estatisticamente, DFs; para este proposito será utilizado a função describe()

print('resumo estatistico do df1')
print(df1.describe())
print('--------------------------')
print('resumo estatistico do df2')
print(df2.describe())

'''
count: contagem da qtde de valores NÃO NULOS do df (df1 = 6, df2 = 4)

mean: média, simples, aritmética dos valores que compõem o df

min: é o menor valor - valor minimo - dentro de cada coluna do df

std: desvio padrão -> mede o quanto os dados variam entre si!

25%: 1º QUARTIL -> significa que 25% dos valores contidos em cada coluna do df são iguais ou estão abaixo deste indice

50%: 2º QUARTIL -> significa que 50% dos valores contidos em cada coluna do df são considerados a MEDIANA 

75%: 3º QUARTIL ->  significa que 75% dos valores contidos em cada coluna do df são iguais ou estão abaixo deste indice

max: é o maior valor - valor maximo - dentro de cada coluna do df
'''