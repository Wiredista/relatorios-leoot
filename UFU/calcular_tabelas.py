#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para processamento e tratamento estatístico dos dados experimentais
(Laboratório de Oscilações - UFU)
Sem dependências externas (utiliza apenas a biblioteca padrão do Python).
"""

import csv
import math
import statistics

def calcular_incerteza_massa(n_pesos, sigma_suporte=0.25, delta_var=0.50, delta_inst=0.25):
    """
    Calcula a incerteza combinada da massa total m = m_suporte + n * m_peso.
    Incerteza de cada peso: combinacao em quadratura da variacao entre pesos e erro instrumental:
    sigma_p = sqrt(delta_var^2 + delta_inst^2)
    Incerteza total: sigma_m = sqrt(sigma_suporte^2 + n * sigma_p^2)
    """
    sigma_peso = math.sqrt(delta_var**2 + delta_inst**2)
    sigma_total = math.sqrt(sigma_suporte**2 + n_pesos * (sigma_peso**2))
    return sigma_total

def ler_csv_dinamico(caminho_csv="UFU/dados_dinamico.csv"):
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
    
    configuracoes = [
        ("m_60g", 60.0, 1),
        ("m_110g", 110.0, 2),
        ("m_160g", 160.0, 3),
        ("m_210g", 210.0, 4),
        ("m_260g", 260.0, 5)
    ]
    
    sigma_t_inst = 0.005  # incerteza instrumental do cronometro (s)
    n_oscilacoes = 20
    
    print("=" * 80)
    print("INCERTEZAS CALCULADAS PARA AS MASSAS (TABELA 2)")
    print("=" * 80)
    for col, m_nom, n_p in configuracoes:
        err_m = calcular_incerteza_massa(n_p)
        print(f"Configuração {n_p} peso(s): ({m_nom:.1f} ± {err_m:.2f}) g  -->  ({m_nom:.1f} ± {err_m:.1f}) g")
    
    print("\n" + "=" * 80)
    print("TABELA 3: TRATAMENTO ESTATÍSTICO DOS DADOS DINÂMICOS")
    print("=" * 80)
    print(f"{'Massa (g)':<18} | {'Tempo Médio t20 (s)':<22} | {'Período T (s)':<14} | {'sigma_T (s)':<12} | {'T^2 (s^2)':<10}")
    print("-" * 80)
    
    linhas_resumo = []
    
    for col, m_nom, n_p in configuracoes:
        tempos = dados[col]
        n = len(tempos)
        
        media_t20 = statistics.mean(tempos)
        s_t20 = statistics.stdev(tempos)
        
        # Erro padrao da media combinado com o instrumental
        sigma_media_t20 = s_t20 / math.sqrt(n)
        sigma_t20_comb = math.sqrt(sigma_media_t20**2 + sigma_t_inst**2)
        
        # Periodo unitario e incerteza
        T = media_t20 / n_oscilacoes
        sigma_T = sigma_t20_comb / n_oscilacoes
        
        # T^2
        T2 = T**2
        sigma_T2 = 2 * T * sigma_T
        
        sigma_m = calcular_incerteza_massa(n_p)
        
        print(f"{m_nom:.1f} ± {sigma_m:.1f} g{'':<6} | {media_t20:.2f} ± {sigma_media_t20:.2f} s{'':<7} | {T:.3f} s{'':<7} | {sigma_T:.3f} s{'':<5} | {T2:.3f} s^2")
        
        linhas_resumo.append({
            "m_nom": m_nom,
            "sigma_m": sigma_m,
            "media_t20": media_t20,
            "sigma_media_t20": sigma_media_t20,
            "T": T,
            "sigma_T": sigma_T,
            "T2": T2,
            "sigma_T2": sigma_T2
        })
        
    print("\n" + "=" * 80)
    print("CÓDIGO LATEX GERADO PARA A TABELA 3:")
    print("=" * 80)
    print(r"\begin{table}[htbp]")
    print(r"\centering")
    print(r"\caption{Tratamento estatístico dos dados dinâmicos (período $T$ e $T^2$).}")
    print(r"\label{tab:dinamico_resumo}")
    print(r"\begin{tabular}{ccccc}")
    print(r"\hline")
    print(r"\textbf{Massa $m$ (g)} & \textbf{Tempo médio $\bar{t}_{20}$ (s)} & \textbf{Período $T$ (s)} & \textbf{Incerteza $\sigma_T$ (s)} & \textbf{$T^2$ ($\text{s}^2$)} \\ \hline")
    for r in linhas_resumo:
        m_str = f"${r['m_nom']:.1f} \\pm {r['sigma_m']:.1f}$".replace('.', ',')
        t_str = f"${r['media_t20']:.2f} \\pm {r['sigma_media_t20']:.2f}$".replace('.', ',')
        T_str = f"${r['T']:.3f}$".replace('.', ',')
        sig_str = f"${r['sigma_T']:.3f}$".replace('.', ',')
        T2_str = f"${r['T2']:.3f}$".replace('.', ',')
        print(f"{m_str} & {t_str} & {T_str} & {sig_str} & {T2_str} \\\\")
    print(r"\hline")
    print(r"\end{tabular}")
    print(r"\end{table}")

if __name__ == "__main__":
    processar_dados()
