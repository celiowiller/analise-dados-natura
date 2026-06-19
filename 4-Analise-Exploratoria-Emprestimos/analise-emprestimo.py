# 0. importar os recursos necessarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. carregamento e preparação dos dados 
df = pd.read_csv('loan.csv')

# exibir o df
print(df)
print(df.describe())

# 2. criar uma seleção para obter a mediana dos dados 
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median()) # aqui, estamos substituindo valores AUSENTES - caso ocorram - pela mediana obtida a partir dos valores da propria coluna

# 3. agora, vamos criar uma nova seleção a partir do historico de credito dos solicitantes
df['Credit_History'] = df['Credit_History'].fillna(0.0) # aqui, temos o seguinte: se o solicitante não forneceu o historico de credito - preencheremos esta coluna com o valor 0.0 - partido, então da premissa que este solicitante não tem historico

# 4. vamos, nesta passo, fazer na função dropna(): é uma função que remove - do df - todas as linhas que possuem valores ausentes  - este procedimento é classificado como: LIMPEZA DE DADOS!
df.dropna(
    subset = ['Loan_Status', 'ApplicantIncome', 'Education'], inplace = True
) # inplace = True: esta instrução modifica o df original


# 5. acessar o df a partir da coluna 'Loan_Status' e vamos mapear os valores 0.0 e 1.0 para associar aos caracteres 'Y' e 'N' -> 'Y' = 1.0, 'N' = 0.0 
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1.0, 'N': 0.0})

print('Primeiras linhas do df')
print(df.head(5))
print('--------------------------------------------------------------')


print('Coluna Loan_Status')
print(df['Loan_Status'])
print('--------------------------------------------------------------')

print('Contagem dos valores da coluna Loan_Status')
print(df['Loan_Status'].value_counts())
print('--------------------------------------------------------------')

print('Contagem dos valores nulos/ausentes do df')
print(df.isnull().sum())
print('--------------------------------------------------------------')

print('Contagem da coluna Gender')
print(df['Gender'].value_counts())
print('--------------------------------------------------------------')

print('Contagem de classificação das areas de propriedades')
print(df['Property_Area'].value_counts())
print('--------------------------------------------------------------')

print('Contagem de valores da coluna Credit_History')
print(df['Credit_History'].value_counts())
print('--------------------------------------------------------------')

# 6. observar  coluna Loan_Status a partir de outra perspectiva
print()
print('Observação de Loan_Status - com pivot_table')
obs_1 = df.pivot_table(
    values = 'Loan_Status',
    index = ['Credit_History'],
    aggfunc = 'mean'
) * 100
print(obs_1.round(2).astype(str) + '%')
print('------------------------------------------------------------------')
'''
acima, o bloco de código consegue detectar a seguinte tendencia: os candidatos que possuem historico de credito tendem - com altas taxas de probabilidade de aprovação (media aproximada de 80%) - a conseguir o credito solicitado; já, para os candidatos que não possuem historico de credito, a taxa de aprovaçã é menor, gira em torno de 31%
'''