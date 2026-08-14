'''
import numpy as np: Importa a biblioteca NumPy para operações numéricas, manipulação de vetores e geração de números aleatórios.

import pandas as pd: Importa o Pandas para criação e manipulação de tabelas (DataFrames) e séries temporais.

import matplotlib.pyplot as plt: Importa o módulo de plotagem do Matplotlib para construção de gráficos (embora não utilizado na etapa de exportação, fica disponível para visualização).
'''
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# Fixar a semente aleatória para garantir reprodutibilidade exata
np.random.seed(42)
'''
Define a semente do gerador de números pseudoaleatórios do NumPy para o valor 42.

Por que usar: Garante que todas as chamadas aleatórias subsequentes (np.random.normal, np.random.choice, np.random.lognormal) gerem exatamente os mesmos valores em qualquer máquina que rodar o código.
'''
# 1. Vetor de datas diárias para o ano de 2025
datas = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
n = len(datas) # 365 dias

'''
pd.date_range(...): Gera uma sequência contínua de datas diárias (freq='D') cobrindo o ano de 2025.

n = len(datas): Armazena o total de registros no ano (365 dias) na variável n.
'''

# 2. Construção do sinal de temperatura
t = np.linspace(0, 4 * np.pi, n)
sinal_base = 20 + 5 * np.sin(t) + 0.01 * np.arange(n) # Senoide + tendência linear
ruido = np.random.normal(loc=0, scale=1.2, size=n)      # Ruído branco gaussiano
temperatura = sinal_base + ruido

'''
np.linspace(0, 4 * np.pi, n): Cria um vetor de 365 pontos igualmente espaçados no intervalo de 0 a 4pi (dois ciclos senoidais completos).

sinal_base: Monta a tendência física do sinal misturando uma temperatura média de 20 graus Celsius, uma variação sazonal senoidal com amplitude de 5 graus Celsius e uma tendência de aquecimento linear (0.01 * np.arange(n)).

ruido: Gera um ruído branco gaussiano com média 0 e desvio padrão 1.2 graus Celsius para simular a variação diária natural.temperatura = sinal_base + ruido: Soma o sinal base com o ruído gaussiano.

temperatura = sinal_base + ruido: Soma o sinal base com o ruído gaussiano.
'''

# 3. Turbidez com distribuição log-normal (comum em dados ambientais)
turbidez = np.random.lognormal(mean=1.5, sigma=0.5, size=n)

'''
O que faz: Gera 365 valores de turbidez seguindo uma distribuição Log-Normal (com parâmetros u = 1.5 e sigma = 0.5).Aplicação: A distribuição log-normal é comumente usada para variáveis ambientais assimétricas que possuem piso zero e cauda longa para a direita.
'''

# 4. Inserção controlada de NaNs e Outliers
mask_nan_temp = np.random.choice([True, False], size=n, p=[0.05, 0.95])
temperatura[mask_nan_temp] = np.nan

outlier_indices = np.random.choice(n, size=6, replace=False)
temperatura[outlier_indices[0:3]] += 25.0  # Picos irreais de temperatura
turbidez[outlier_indices[3:6]] *= 8.0      # Picos irreais de turbidez

'''
mask_nan_temp: Cria uma máscara booleana onde cada dia tem 5% de probabilidade (p=[0.05, 0.95]) de ser True.

temperatura[mask_nan_temp] = np.nan: Substitui por NaN (valor ausente) as posições onde a máscara é True (simulando falha de sensor).

outlier_indices = np.random.choice(...): Sorteia 6 posições distintas de 0 a 364 sem reposição.

temperatura[outlier_indices[0:3]] += 25.0: Adiciona 25 graus Celsius em 3 dias aleatórios (picos irreais por erro elétrico/leitura).

turbidez[outlier_indices[3:6]] *= 8.0: Multiplica por 8 a turbidez em outros 3 dias aleatórios (picos irreais por erro de calibração).
'''

# DataFrame inicial
df_raw = pd.DataFrame({
    'data': datas,
    'temp_celsius': temperatura,
    'turbidez_ntu': turbidez
})
'''
Estrutura os três vetores unidimensionais (datas, temperatura, turbidez) em uma tabela bidimensional (DataFrame do Pandas) chamada df_raw.
'''

# ==============================================================================
# CONTINUAÇÃO DO PROCESSAMENTO E EXPORTAÇÃO PARA CSV
# ==============================================================================

# 5. Exportação para CSV (formatado com 2 casas decimais)
caminho_arquivo = 'dados_ambientais_processados.csv'

'''
O que faz: Cria a variável caminho_arquivo guardando o texto (string) do nome ou caminho do arquivo onde os dados serão salvos.

Por que usar: Armazenar o caminho em uma variável evita que você precise digitar a string em vários lugares. Se mudar o nome do arquivo depois, altera apenas nesta linha.
'''

try:
    # Tenta exportar o DataFrame formatado com 2 casas decimais
    df_raw.round(2).to_csv(caminho_arquivo, encoding='utf-8')
    print(f" Processamento finalizado com sucesso!")
    print(f" Arquivo exportado para: '{caminho_arquivo}'")

except PermissionError:
    print(f" Erro de Permissão: Não foi possível salvar '{caminho_arquivo}'.")
    print(" Verifique se o arquivo está aberto no Excel ou em outro programa e feche-o antes de rodar novamente.")

except FileNotFoundError:
    print(f" Erro de Caminho: O diretório especificado para '{caminho_arquivo}' não foi encontrado.")

except Exception as e:
    print(f" Ocorreu um erro inesperado ao salvar o arquivo CSV: {e}")

'''
O que faz: Inicia um bloco de código vigiado pelo Python.

Por que usar: Tudo o que está dentro do try será executado normalmente. Caso ocorra qualquer erro (como falha de permissão de gravação), o Python interrompe a execução do bloco e pula imediatamente para o tratamento (except), impedindo que o programa quebre/crash.

df_raw.round(2): Pega todas as colunas numéricas de ponto flutuante do DataFrame df_raw e arredonda seus valores para 2 casas decimais.

.to_csv(...): Transforma a tabela do Pandas em um arquivo de texto no formato CSV (valores separados por vírgula) e grava no disco rígido.

caminho_arquivo: Passa o nome do arquivo definido na primeira linha.

encoding='utf-8': Define o padrão universal de codificação de texto (UTF-8). Isso garante que acentos (ã, ç, é) e símbolos como o grau Celsius (°C) não fiquem corrompidos no arquivo.

print(f" Processamento finalizado com sucesso!")
    print(f" Arquivo exportado para: '{caminho_arquivo}'")
O que faz: Exibe no terminal as mensagens indicando que a exportação ocorreu sem falhas.

Detalhe técnico: O prefixo f antes das aspas indica uma f-string, permitindo colocar {caminho_arquivo} para imprimir dinamicamente o nome do arquivo salvo.

except PermissionError:
O que faz: Captura especificamente a exceção PermissionError.

Quando acontece: Quando o sistema operacional impede a gravação do arquivo. O motivo mais comum é o arquivo .csv já estar aberto no Microsoft Excel, Power BI ou outro programa que bloqueia o arquivo para escrita, ou por falta de permissão de administrador na pasta.

print(f" Erro de Permissão: Não foi possível salvar '{caminho_arquivo}'.")
    print(
        " Verifique se o arquivo está aberto no Excel ou em outro programa e"
        " feche-o antes de rodar novamente."
    )
O que faz: Exibe uma instrução clara no terminal informando a causa provável e orientando você a fechar o software que está bloqueando o arquivo.

except FileNotFoundError:
O que faz: Captura a exceção FileNotFoundError.

Quando acontece: Quando você tenta salvar o arquivo dentro de uma pasta/diretório que não existe no seu computador (por exemplo, se o caminho fosse 'relatorios/2026/dados.csv' e a pasta relatorios não tivesse sido criada).

print(
        " Erro de Caminho: O diretório especificado para"
        f" '{caminho_arquivo}' não foi encontrado."
    )
O que faz: Avisa no terminal que o caminho especificado não existe na estrutura de pastas.

except Exception as e:
O que faz: Captura qualquer outro tipo de erro inesperado que não seja nem de permissão nem de caminho.

Detalhe técnico: A cláusula as e armazena a mensagem de erro original do Python na variável e.

print(f" Ocorreu um erro inesperado ao salvar o arquivo CSV: {e}")
O que faz: Imprime o texto descritivo do erro contido na variável e, permitindo identificar a falha sem interromper a execução do script.
'''