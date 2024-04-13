######################################################################################
# Análise de similaridade de curvas utilizando Dynamic Time Warping (DTW)
# By José Rubens Macedo Junior
# Date: 12/04/2024
######################################################################################

import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from dtw import dtw

# Caminho para o arquivo CSV
caminho_pasta = r"C:\pythonjr\analisador"
nome_arquivo = "curvas3.csv"
caminho_arquivo_csv = os.path.join(caminho_pasta, nome_arquivo)

def ler_arquivo_csv(caminho_arquivo):
    tempos = []
    corrente1 = []
    corrente2 = []

    with open(caminho_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')  # Definindo o delimitador como ponto e vírgula
        # Ignora o cabeçalho se houver
        next(leitor_csv, None)
        for linha in leitor_csv:
            # Supondo que as colunas estejam na ordem correta: tempo, corrente1, corrente2
            tempo = float(linha[0].replace(',', '.'))  # Substitui vírgula por ponto
            ponto_corrente1 = float(linha[1].replace(',', '.'))  # Substitui vírgula por ponto
            ponto_corrente2 = float(linha[2].replace(',', '.'))  # Substitui vírgula por ponto

            tempos.append(tempo)
            corrente1.append(ponto_corrente1)
            corrente2.append(ponto_corrente2)

    return tempos, corrente1, corrente2

# Chama a função para ler o arquivo CSV
tempos, corrente1, corrente2 = ler_arquivo_csv(caminho_arquivo_csv)

# Função para calcular a distância DTW entre duas séries temporais
def calcular_dtw(s1, s2):
    # Calcula a distância DTW entre as duas séries
    dist, _, _, _ = dtw(s1, s2, dist=lambda x, y: np.linalg.norm(x - y))
    return dist

# Calcula a distância DTW entre as duas correntes
dist_dtw = calcular_dtw(corrente1, corrente2)

# Plotagem das correntes
plt.plot(tempos, corrente1, label='Corrente de referência')
plt.plot(tempos, corrente2, label='Corrente medida')
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (A)')
plt.legend()
plt.grid(True, linestyle='--')

# Inclui o valor da distância DTW no título do gráfico
titulo = f'Índice de Similaridade (DTW) = {dist_dtw:.2f}'
plt.title(titulo)

plt.tight_layout()
plt.show()

