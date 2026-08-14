Exercício Prático: Análise, Sanitização e Visualização de Séries Temporais Ambientais

Objetivo Geral

Desenvolver uma rotina completa de análise de dados operacionais/ambientais em Python, aplicando técnicas de imputação de dados faltantes, detecção e remoção de outliers, engenharia de atributos temporais, cálculo de médias móveis via convolução e construção de gráficos técnicos para relatórios.
Ferramentas Permitidas
	NumPy (Vetores, operações matriciais e convolução)
	Pandas (DataFrames, séries temporais e agregações)
	Matplotlib (Subplots e estilização de dados)

Nota: Não é permitido o uso de frameworks de banco de dados (como SQL) nem bibliotecas de alto nível para gráficos (como Seaborn) nesta etapa. *** caso desejem definir matrizes de correlação, o uso do seaborn esta totalmente permitido

Parte 0: Carga/Geração dos Dados Brutos

Utilize o bloco Python fornecido pelo instrutor para gerar o arquivo/DataFrame sintético df_raw, contendo 365 leituras diárias de dois sensores de monitoramento de água:
	temp_celsius: Temperatura da água (°C), contendo falhas operacionais (NaN) e ruído gaussiano.
	turbidez_ntu: Turbidez da água (NTU), seguindo distribuição log-normal e apresentando picos de erro de calibração (outliers).

Tarefas a Realizar

Etapa 1: Sanitização e Imputação de Dados (Pandas & NumPy)
	Identificação de lacunas: Diagnostique a quantidade e o percentual de dados faltantes (NaN) em cada coluna.
	Imputação de Séries Temporais: Aplique interpolação linear contínua na coluna temp_celsius para preencher as lacunas mantendo a fluidez da série temporal.
	Tratamento Estatístico de Outliers:
	Calcule o Intervalo Interquartil (IQR=Q3-Q1) para a variável turbidez_ntu.
	Estabeleça o limite superior crítico (Q3+1.5×IQR). **** 
	Identifique as medições discrepantes acima do limite superior e substitua-as pela mediana da série.

Etapa 2: Indexação Temporal e Resumo Estatístico
	Defina a coluna data como o índice temporal do DataFrame (DatetimeIndex).
	Engenharia de Atributos: Crie uma coluna categórica temp_status classificando os registros diários em:
	'Baixa' (temperatura < 18.0 °C)
	'Ideal' (temperatura entre 18.0 °C e 24.0 °C)
	'Elevada' (temperatura > 24.0 °C)
	Agregação Mensal: Gere uma tabela resumo agregando os dados por mês (resample), exibindo a média e o desvio padrão da temperatura, além da média e do valor máximo da turbidez.

Etapa 3: Sinal e Média Móvel com NumPy Puro
	Extraia o vetor limpo de temp_celsius como um array 1D do NumPy.
	Sem utilizar funções de alto nível do Pandas (como .rolling()), implemente uma média móvel de 7 dias utilizando a operação de convolução de vetores (np.convolve) com um kernel unitário normalizado.
	Incorpore a nova série da média móvel de volta ao DataFrame para alinhamento temporal.

Etapa 4: Visualização Técnica e Científica (Matplotlib)


Gere uma figura com 2 painéis alinhados verticalmente (2x1) compartilhando o eixo horizontal do tempo (sharex=True), seguindo o padrão de publicação técnica:
	Painel Superior (Temperatura):
	Curva dos dados diários brutos/imputados em tom cinza suave (linhas finas).
	Curva da Média Móvel de 7 dias destacada em azul (linha mais espessa).
	Linha de referência horizontal tracejada na cor vermelha para o limite crítico de 〖25.0〗^∘ "C" .
	Painel Inferior (Turbidez):
	Curva de turbidez tratada com preenchimento da área sob a linha (fill_between).
	Acabamento:
	Legendas em ambos os painéis.
	Títulos apropriados nos eixos Y com unidades de medida e título principal da figura.
	Grade discreta (grid) para leitura rápida de valores.

