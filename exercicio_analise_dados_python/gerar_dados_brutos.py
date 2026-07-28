import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fixar a semente aleatória para garantir reprodutibilidade exata
np.random.seed(42)

# 1. Vetor de datas diárias para o ano de 2025
datas = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
n = len(datas) # 365 dias

# 2. Construção do sinal de temperatura
t = np.linspace(0, 4 * np.pi, n)
sinal_base = 20 + 5 * np.sin(t) + 0.01 * np.arange(n) # Senoide + tendência linear
ruido = np.random.normal(loc=0, scale=1.2, size=n)      # Ruído branco gaussiano
temperatura = sinal_base + ruido

# 3. Turbidez com distribuição log-normal (comum em dados ambientais)
turbidez = np.random.lognormal(mean=1.5, sigma=0.5, size=n)

# 4. Inserção controlada de NaNs e Outliers
mask_nan_temp = np.random.choice([True, False], size=n, p=[0.05, 0.95])
temperatura[mask_nan_temp] = np.nan

outlier_indices = np.random.choice(n, size=6, replace=False)
temperatura[outlier_indices[0:3]] += 25.0  # Picos irreais de temperatura
turbidez[outlier_indices[3:6]] *= 8.0      # Picos irreais de turbidez

# DataFrame inicial
df_raw = pd.DataFrame({
    'data': datas,
    'temp_celsius': temperatura,
    'turbidez_ntu': turbidez
})