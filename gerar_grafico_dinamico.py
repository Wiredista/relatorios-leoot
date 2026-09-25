#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração do gráfico T² x m (Método Dinâmico - Laboratório de Oscilações UFU)
Exporta a figura r1_fig2.png com qualidade acadêmica (300 DPI)
"""

import csv
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt

def calcular_incerteza_massa(n_pesos, sigma_suporte=0.25, delta_var=0.50, delta_inst=0.25):
    sigma_peso = math.sqrt(delta_var**2 + delta_inst**2)
    return math.sqrt(sigma_suporte**2 + n_pesos * (sigma_peso**2))

def gerar_grafico():
    # Carregar dados
    caminho_csv = "UFU/dados_dinamico.csv"
    dados = {
        "m_60g": [],
        "m_110g": [],
        "m_160g": [],
        "m_210g": [],
        "m_260g": []
    }
    with open(caminho_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for k in dados:
                dados[k].append(float(row[k]))
                
    configuracoes = [
        ("m_60g", 0.060, 1),
        ("m_110g", 0.110, 2),
        ("m_160g", 0.160, 3),
        ("m_210g", 0.210, 4),
        ("m_260g", 0.260, 5)
    ]
    
    sigma_t_inst = 0.005
    n_osc = 20
    
    massas_kg = []
    sigma_massas_kg = []
    T2_lista = []
    sigma_T2_lista = []
    
    for col, m_kg, n_p in configuracoes:
        tempos = dados[col]
        n = len(tempos)
        media_t20 = statistics.mean(tempos)
        s_t20 = statistics.stdev(tempos)
        
        sigma_media_t20 = s_t20 / math.sqrt(n)
        sigma_t20_comb = math.sqrt(sigma_media_t20**2 + sigma_t_inst**2)
        
        T = media_t20 / n_osc
        sigma_T = sigma_t20_comb / n_osc
        
        T2 = T**2
        sigma_T2 = 2 * T * sigma_T
        
        sigma_m_g = calcular_incerteza_massa(n_p)
        
        massas_kg.append(m_kg)
        sigma_massas_kg.append(sigma_m_g / 1000.0)
        T2_lista.append(T2)
        sigma_T2_lista.append(sigma_T2)
        
    x = np.array(massas_kg)
    y = np.array(T2_lista)
    y_err = np.array(sigma_T2_lista)
    x_err = np.array(sigma_massas_kg)
    
    # Ajuste linear por mínimos quadrados: y = a*x + b
    p, cov = np.polyfit(x, y, 1, cov=True)
    a, b = p[0], p[1]
    erro_a = np.sqrt(cov[0, 0])
    erro_b = np.sqrt(cov[1, 1])
    
    # Coeficiente de determinação R²
    y_pred = a * x + b
    residuos = y - y_pred
    ss_res = np.sum(residuos**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1 - (ss_res / ss_tot)
    
    # Cálculo de k dinâmico: a = 4*pi^2 / k => k = 4*pi^2 / a
    k_din = (4 * (np.pi**2)) / a
    sigma_k_din = (4 * (np.pi**2) / (a**2)) * erro_a
    
    print(f"Ajuste Linear: T² = ({a:.4f} ± {erro_a:.4f}) * m + ({b:.4f} ± {erro_b:.4f})")
    print(f"R² = {r2:.5f}")
    print(f"k_dinamico = ({k_din:.2f} ± {sigma_k_din:.2f}) N/m")
    
    # Configurar estilo do gráfico
    plt.rcParams.update({
        'font.size': 11,
        'font.family': 'serif',
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.titlesize': 14
    })
    
    fig, ax = plt.subplots(figsize=(7, 4.8), dpi=300)
    
    # Linha de ajuste contínua
    x_lin = np.linspace(0.04, 0.28, 100)
    y_lin = a * x_lin + b
    ax.plot(x_lin, y_lin, color='#003366', linestyle='--', linewidth=1.8,
            label=f'Ajuste Linear: $T^2 = ({a:.3f})m + ({b:.3f})$\n$R^2 = {r2:.4f}$')
    
    # Pontos experimentais com barras de erro
    ax.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', color='#cc0000',
                ecolor='#333333', elinewidth=1.2, capsize=3.5, capthick=1.2,
                markersize=6, label='Dados Experimentais')
    
    # Rótulos e Título
    ax.set_xlabel(r'Massa Total $m$ (kg)', fontweight='bold')
    ax.set_ylabel(r'Período ao Quadrado $T^2$ ($\mathrm{s}^2$)', fontweight='bold')
    ax.set_title('Gráfico de Linearização: $T^2 \\times m$ (Método Dinâmico)', pad=12, fontweight='bold')
    
    # Grade e limites
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.set_xlim(0.04, 0.28)
    ax.set_ylim(0.10, 0.75)
    
    # Caixa de texto com os parâmetros físicos obtidos
    texto_info = (
        f"$\\mathbf{{Resultados:}}$\n"
        f"Inclinação $a = ({a:.3f} \\pm {erro_a:.3f})\\;\\mathrm{{s^2/kg}}$\n"
        f"Intercepto $b = ({b:.3f} \\pm {erro_b:.3f})\\;\\mathrm{{s^2}}$\n"
        f"$\\mathbf{{k_{{din}} = ({k_din:.2f} \\pm {sigma_k_din:.2f})\\;\\mathrm{{N/m}}}}$"
    )
    ax.text(0.06, 0.65, texto_info, transform=ax.transData, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#f4f4f4', edgecolor='#999999', alpha=0.9))
    
    ax.legend(loc='lower right', framealpha=0.95)
    plt.tight_layout()
    
    # Salvar em UFU/grafico_metodo_dinamico.png
    plt.savefig("UFU/grafico_metodo_dinamico.png", dpi=300)
    plt.savefig("grafico_metodo_dinamico.png", dpi=300)
    plt.close()
    print("Gráficos salvos com sucesso em 'UFU/grafico_metodo_dinamico.png'!")

if __name__ == "__main__":
    gerar_grafico()
