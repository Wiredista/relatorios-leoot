#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para processamento e tratamento estatístico dos dados experimentais
(Laboratório de Oscilações - UFU)
Sem dependências externas (utiliza apenas a biblioteca padrão do Python).
"""

import os
import csv
import math
import statistics

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DADOS_DIR = os.path.join(BASE_DIR, "dados")

def calcular_incerteza_massa(n_pesos, sigma_suporte=0.25, delta_var=0.50, delta_inst=0.25):
    sigma_peso = math.sqrt(delta_var**2 + delta_inst**2)
    sigma_total = math.sqrt(sigma_suporte**2 + n_pesos * (sigma_peso**2))
    return sigma_total

def ler_csv_dinamico(caminho_csv=None):
    if caminho_csv is None:
        caminho_csv = os.path.join(DADOS_DIR, "dados_dinamico.csv")
    colunas = {
        "m_60g": [],
        "m_110g": [],
        "m_160g": [],
        "m_210g": [],
        "m_260g": []
    }
    with open(caminho_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for k in colunas:
                colunas[k].append(float(row[k]))
    return colunas

def processar_dados():
    dados = ler_csv_dinamico()
    
    massas_info = [
        {"nome": "m_60g", "m_total_g": 60.0, "n_pesos": 1},
        {"nome": "m_110g", "m_total_g": 110.0, "n_pesos": 2},
        {"nome": "m_160g", "m_total_g": 160.0, "n_pesos": 3},
        {"nome": "m_210g", "m_total_g": 210.0, "n_pesos": 4},
        {"nome": "m_260g", "m_total_g": 260.0, "n_pesos": 5},
    ]
    
    sigma_relogio = 0.01  # erro instrumental do cronometro (s)
    N_oscilacoes = 10
    
    resultados = []
    
    for info in massas_info:
        chave = info["nome"]
        tempos_10t = dados[chave]
        n_medidas = len(tempos_10t)
        
        massa_g = info["m_total_g"]
        sigma_m = calcular_incerteza_massa(info["n_pesos"])
        
        t_medio_10 = statistics.mean(tempos_10t)
        sigma_amostral_10 = statistics.stdev(tempos_10t)
        sigma_media_10 = sigma_amostral_10 / math.sqrt(n_medidas)
        sigma_total_10 = math.sqrt(sigma_media_10**2 + sigma_relogio**2)
        
        T_medio = t_medio_10 / N_oscilacoes
        sigma_T = sigma_total_10 / N_oscilacoes
        
        T2 = T_medio**2
        sigma_T2 = 2 * T_medio * sigma_T
        
        resultados.append({
            "massa_g": massa_g,
            "sigma_m_g": sigma_m,
            "massa_kg": massa_g / 1000.0,
            "sigma_m_kg": sigma_m / 1000.0,
            "t_medio_10": t_medio_10,
            "sigma_total_10": sigma_total_10,
            "T_medio": T_medio,
            "sigma_T": sigma_T,
            "T2": T2,
            "sigma_T2": sigma_T2
        })
        
    return resultados

def imprimir_tabela_3(resultados):
    print("\n" + "="*85)
    print("TABELA 3: Médias dos Tempos, Período Experimental e Grandezas Derivadas")
    print("="*85)
    header_m = "Massa (g)"
    header_t = "t_médio (10 osc) [s]"
    header_T = "Período T [s]"
    header_T2 = "T² [s²]"
    print(f"{header_m:<15} | {header_t:<22} | {header_T:<18} | {header_T2:<18}")
    print("-" * 85)
    for r in resultados:
        m_str = f"{r['massa_g']:.0f} ± {r['sigma_m_g']:.2f}"
        t_str = f"{r['t_medio_10']:.3f} ± {r['sigma_total_10']:.3f}"
        T_str = f"{r['T_medio']:.4f} ± {r['sigma_T']:.4f}"
        T2_str = f"{r['T2']:.4f} ± {r['sigma_T2']:.4f}"
        print(f"{m_str:<15} | {t_str:<22} | {T_str:<18} | {T2_str:<18}")
    print("="*85)

if __name__ == "__main__":
    res = processar_dados()
    imprimir_tabela_3(res)
