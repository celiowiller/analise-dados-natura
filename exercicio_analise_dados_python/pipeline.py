'''
import numpy as np: Carrega o NumPy para operações vetoriais de alto desempenho e filtros numéricos via convolução.

import pandas as pd: Utilizado para estruturas tabulares (DataFrames), indexação temporal e agregações em séries temporais.

import matplotlib.pyplot as plt: المódulo do Matplotlib para renderização do dashboard técnico com subplots.

df = pd.read_csv(...): Carrega o arquivo em formato CSV salvo anteriormente no disco rígido para a memória RAM como um DataFrame.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cópia explícita para evitar o aviso 'SettingWithCopyWarning' do Pandas
#df = df_raw.copy()

df = pd.read_csv('dados_ambientais_processados.csv')

# ==============================================================================
# ETAPA 1: SANITIZAÇÃO (LIMPEZA) E IMPUTAÇÃO DE DADOS
# ==============================================================================

# --- 1.1 Identificação de Lacunas ---
# .isna() retorna um DataFrame booleano (True para NaN)
# .sum() soma os True (1s), resultando no total de falhas por coluna
nans_temp = df['temp_celsius'].isna().sum()
perc_temp = (nans_temp / len(df)) * 100

print(f"Diagnóstico de NaNs em 'temp_celsius': {nans_temp} registros ({perc_temp:.2f}%)")

'''
df['temp_celsius'].isna(): Retorna uma Series de valores booleanos (True onde o dado é NaN e False onde o dado é válido).

.sum(): Soma os valores booleanos (True equivale a 1), contabilizando o total de falhas na leitura do sensor.

(nans_temp / len(df)) * 100: Calcula a porcentagem de falhas em relação ao total de 365 amostras diárias.
'''

# --- 1.2 Imputação via Interpolação Linear ---
# Lógica Matemática: Conecta os pontos conhecidos adjacentes (y0, x0) e (y1, x1) por uma
# reta. Para um ponto x ausente, y é calculado por: y = y0 + (x - x0) * ((y1 - y0) / (x1 - x0))
# É a escolha ideal para séries temporais contínuas onde a variação física é suave.
df['temp_celsius'] = df['temp_celsius'].interpolate(method='linear')

'''
Conceito Matemático: Estima o valor ausente em um ponto x através da equação da reta que conecta os dois pontos válidos vizinhos
Aplicação Prática: Preserva a continuidade física de variáveis ambientais (como temperatura da água) sem introduzir ruídos bruscos ou saltos artificiais.
'''

# --- 1.3 Tratamento Estatístico de Outliers via Regra do IQR ---
# Lógica Matemática:
# Q1 (Percentil 25) e Q3 (Percentil 75) delimitam os 50% centrais dos dados.
# O Intervalo Interquartil (IQR = Q3 - Q1) mede a dispersão robusta.
# A regra de Tukey define como outlier qualquer ponto fora de [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
Q1 = df['turbidez_ntu'].quantile(0.25)
Q3 = df['turbidez_ntu'].quantile(0.75)
IQR = Q3 - Q1

limite_superior = Q3 + 1.5 * IQR
mediana_turb = df['turbidez_ntu'].median()



# Lógica Computacional com np.where(condição, valor_se_verdadeiro, valor_se_falso):
# Vetoriza a substituição sem a necessidade de loops lentos em Python puro.
df['turbidez_ntu'] = np.where(
    df['turbidez_ntu'] > limite_superior, 
    mediana_turb, 
    df['turbidez_ntu']
)

print(f"Limiar de Outlier para Turbidez: {limite_superior:.2f} NTU")
print(f"Outliers substituídos pela mediana ({mediana_turb:.2f} NTU).")

'''
Conceito Estatístico (Regra de Tukey):Q1 (1º Quartil / Percentil 25) e Q3 (3º Quartil / Percentil 75) delimitam 50% da distribuição central.

IQR = Q3 - Q1: Amplitude interquartil que mede a dispersão robusta.

{Limite Superior} = Q3 + 1.5 x IQR: Qualquer valor acima deste limiar é considerado um outlier (erro de escala/calibração).

np.where(condição, valor_se_verdadeiro, valor_se_falso): Função vetorial que avalia cada elemento do vetor. Se for superior ao limite, substitui pela mediana ({x}), que é insensível a valores extremos.
'''


# ==============================================================================
# ETAPA 2: INDEXAÇÃO TEMPORAL E RESUMO ESTATÍSTICO
# ==============================================================================

# --- 2.1 Conversão para Datetime e Indexação ---
# Garante que o índice seja um DatetimeIndex válido para o resample
df['data'] = pd.to_datetime(df['data'])
df.set_index('data', inplace=True)

'''
pd.to_datetime(...): Converte strings de texto (ex: '2025-01-01') no tipo de dado especializado datetime64[ns].

.set_index('data'): Transforma a coluna de datas no índice oficial da tabela, habilitando métodos de amostragem temporal (resample).
'''

# --- 2.2 Engenharia de Atributos ---
condicoes = [
    (df['temp_celsius'] < 18.0),
    (df['temp_celsius'] >= 18.0) & (df['temp_celsius'] <= 24.0),
    (df['temp_celsius'] > 24.0)
]
rotulos = ['Baixa', 'Ideal', 'Elevada']

df['temp_status'] = np.select(condicoes, rotulos, default='Desconhecido')

'''
np.select: Mapeia uma estrutura de decisão condicional ordenada sem a necessidade de construir laços for em Python. Se uma condição for atendida, atribui o rótulo da mesma posição na lista rotulos.
'''

# --- 2.3 Agregação Mensal via Resample ---
resumo_mensal = df.resample('ME').agg({
    'temp_celsius': ['mean', 'std'],
    'turbidez_ntu': ['mean', 'max']
})

# Renomeando colunas para visualização limpa
resumo_mensal.columns = [
    'temp_media', 'temp_desvio_padrao', 
    'turbidez_media', 'turbidez_maxima'
]

print("\n--- Resumo Mensal ---")
print(resumo_mensal.head())

'''
.resample('ME'): Agrupa os dados pela frequência de fechamento mensal (Month End).

.agg(...): Aplica estatísticas distintas a colunas específicas:
    Média (u) e desvio padrão (sigma) para a temperatura
    Média (u) e valor máximo para a turbidez.

resumo_mensal.columns = [...]: Achata a estrutura do MultiIndex de colunas gerada pela agregação, facilitando a navegação na tabela resumo.
'''

# ==============================================================================
# ETAPA 3: SINAL E MÉDIA MÓVEL COM NUMPY PURO (CONVOLUÇÃO)
# ==============================================================================

# Lógica Matemática da Convolução Discreta:
# A média móvel de janela W=7 é dada por: Y[t] = (1/W) * sum_{j=0}^{W-1} X[t - j]
# Isso equivale a convolucionar o sinal X com um filtro/kernel K de tamanho W,
# onde cada elemento de K possui valor 1/W = 1/7 (~0.1428).

# 1. Conversão da série do Pandas em array unidimensional do NumPy
temp_vec = df['temp_celsius'].to_numpy()

# 2. Criação do kernel de média móvel normalizado
janela = 7
kernel = np.ones(janela) / janela

# 3. Operação de Convolução
# mode='same' garante que o vetor resultante tenha exatamente o mesmo tamanho (N=365)
# do vetor original, tratando as bordas.
temp_mm7 = np.convolve(temp_vec, kernel, mode='same')

# 4. Reincorporação ao DataFrame Pandas para alinhamento com o índice temporal
df['temp_mm7'] = temp_mm7

'''
Em termos simples:
A Janela (7 dias): Em vez de olhar para um único dia, você pega a temperatura do dia atual mais a dos 6 dias anteriores.

O Pesinho (1/7): Cada um desses 7 dias tem o mesmo peso. Você soma as 7 temperaturas e divide por 7 (que é o mesmo que multiplicar cada uma por 1/7).

O Efeito "Deslizante": O cálculo vai deslizando dia a dia ao longo do ano todo.

mode='same' no NumPy: Garante que o resultado final continue tendo 365 dias, exatamente no mesmo tamanho da sua tabela original.

Resumo: É uma forma ultra-rápida de calcular a média semanal para cada dia do ano e suavizar o gráfico.
'''

# ==============================================================================
# ETAPA 4: VISUALIZAÇÃO TÉCNICA E CIENTÍFICA (MATPLOTLIB)
# ==============================================================================

# Criar a figura e os eixos (2 linhas, 1 coluna) com eixos X vinculados
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 8), sharex=True)

'''
plt.subplots(2, 1, ...): Cria uma figura contendo dois painéis ortogonais empilhados verticalmente (ax1 superior, ax2 inferior).

sharex=True: Vincula o eixo do tempo (X) entre os dois subplots. Dar zoom ou rotacionar o tempo no painel inferior atualiza o painel superior sincronizadamente.
'''

# ------------------------------------------------------------------------------
# Painel Superior: Temperatura
# ------------------------------------------------------------------------------
# Dados Diários (linha cinza mais fina e transparente para servir de fundo)
ax1.plot(
    df.index, df['temp_celsius'], 
    color='#7f7f7f', alpha=0.4, linewidth=1.0, 
    label='Temperatura Diária (Imputada)'
)

# Média Móvel de 7 dias (linha azul sólida e espessa destacando a tendência)
ax1.plot(
    df.index, df['temp_mm7'], 
    color='#1f77b4', linewidth=2.0, 
    label='Média Móvel (7 dias - Convolução)'
)

# Linha Limiar Crítico de Alerta (25°C)
ax1.axhline(
    y=25.0, color='#d62728', linestyle='--', linewidth=1.5, 
    label='Limite Crítico Operacional (25.0 °C)'
)

# Formatação do Painel 1
ax1.set_ylabel('Temperatura (°C)', fontsize=11, fontweight='bold')
ax1.set_title('Série Temporal de Monitoramento Ambiental - Estação 01 (2025)', fontsize=13, fontweight='bold', pad=12)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9)

'''
Painel Superior (ax1 - Temperatura)
ax1.plot(..., color='#7f7f7f', alpha=0.4, linewidth=1.0): Plota a série diária em tom cinza translúcido (alpha=0.4) para atuar como ruído de fundo.

ax1.plot(..., color='#1f77b4', linewidth=2.0): Plota a média móvel de 7 dias obtida via convolução em azul destacado.

ax1.axhline(y=25.0, color='#d62728', linestyle='--'): Desenha uma linha de referência fixa indicando o patamar de atenção/alerta operacional.
'''

# ------------------------------------------------------------------------------
# Painel Inferior: Turbidez
# ------------------------------------------------------------------------------
# Curva de Turbidez Tratada
ax2.plot(
    df.index, df['turbidez_ntu'], 
    color='#2ca02c', linewidth=1.2, 
    label='Turbidez Tratada (NTU)'
)

# Preenchimento sob a curva para destacar volume/intensidade
ax2.fill_between(
    df.index, df['turbidez_ntu'], 
    color='#2ca02c', alpha=0.2
)

'''
Painel Inferior (ax2 - Turbidez)
ax2.plot(..., color='#2ca02c'): Plota a curva tratada de turbidez em verde.

ax2.fill_between(df.index, df['turbidez_ntu'], alpha=0.2): Preenche a área sombreada entre o valor zero e a curva de turbidez, ajudando a identificar visualmente os volumes de pico acumulados.
'''

# Formatação do Painel 2
ax2.set_ylabel('Turbidez (NTU)', fontsize=11, fontweight='bold')
ax2.set_xlabel('Data de Amostragem', fontsize=11, fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9)

'''
Estilização Técnica Finalax.grid(True, linestyle=':', alpha=0.6): Adiciona uma grade tracejada de baixa opacidade para facilitar a leitura visual dos eixos sem poluir a imagem.plt.tight_layout(): Ajusta as margens da figura para evitar que os rótulos do eixo $Y$ fiquem sobrepostos com os títulos das imagens.
'''

# Ajuste fino de layout para evitar sobreposição de rótulos
plt.tight_layout()

# Exibição do gráfico
plt.show()