#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração do gráfico do Método Estático (Laboratório de Oscilações UFU)
"""

import os
import csv
import math
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DADOS_DIR = os.path.join(BASE_DIR, "dados")
FIGURAS_DIR = os.path.join(BASE_DIR, "figuras")

def calcular_incerteza_massa(n_pesos, sigma_suporte=0.25, delta_var=0.50, delta_inst=0.25):
    sigma_peso = math.sqrt(delta_var**2 + delta_inst**2)
    return math.sqrt(sigma_suporte**2 + n_pesos * (sigma_peso**2))

def gerar_grafico():
    caminho_csv = os.path.join(DADOS_DIR, "dados_estatico.csv")
    
    massas_g = []
    posicoes_mm = []
    sigma_x_mm = []
    n_pesos_lista = []
    
    with open(caminho_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            massas_g.append(float(row["massa_g"]))
            posicoes_mm.append(float(row["posicao_mm"]))
            sigma_x_mm.append(float(row["incerteza_x_mm"]))
            n_pesos_lista.append(i)
            
    m_array = np.array(massas_g)
    x_array = np.array(posicoes_mm)
    
    x0 = x_array[0]
    delta_x_mm = x_array - x0
    delta_x_cm = delta_x_mm / 10.0
    
    sigma_x0 = sigma_x_mm[0]
    sigma_deltax_cm = np.sqrt(np.array(sigma_x_mm)**2 + sigma_x0**2) / 10.0
    sigma_m_g = np.array([calcular_incerteza_massa(n) for n in n_pesos_lista])
    
    g = 9.784
    delta_x_m = delta_x_mm / 1000.0
    m_kg = m_array / 1000.0
    
    p, cov = np.polyfit(m_kg, delta_x_m, 1, cov=True)
    slope, intercept = p[0], p[1]
    slope_err = np.sqrt(cov[0, 0])
    
    k_est = g / slope
    sigma_k_est = (g / (slope**2)) * slope_err
    
    r_matrix = np.corrcoef(m_kg, delta_x_m)
    r2 = r_matrix[0, 1]**2
    
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 14,
        "mathtext.fontset": "cm"
    })
    
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    
    ax.errorbar(
        m_array, delta_x_cm,
        xerr=sigma_m_g, yerr=sigma_deltax_cm,
        fmt="o", color="#1f77b4", ecolor="#d62728", elinewidth=1.2,
        capsize=3, capthick=1.2, markersize=6, label="Dados Experimentais"
    )
    
    m_fit = np.linspace(min(m_array)-10, max(m_array)+10, 100)
    deltax_fit_cm = (slope * (m_fit / 1000.0) + intercept) * 100.0
    
    eq_text = (
        r"$\Delta x = (%.4f \cdot m + %.4f)$ m" "\n"
        r"$k_{\text{est}} = (%.2f \pm %.2f)\text{ N/m}$" "\n"
        r"$R^2 = %.4f$"
    ) % (slope, intercept, k_est, sigma_k_est, r2)
    
    ax.plot(m_fit, deltax_fit_cm, color="#2ca02c", linestyle="--", linewidth=1.8, label=f"Ajuste Linear:\n{eq_text}")
    
    ax.set_title("Método Estático: Elongação da Mola em Função da Massa", pad=12, fontweight="bold")
    ax.set_xlabel(r"Massa suspensa $m$ (g)")
    ax.set_ylabel(r"Elongação $\Delta x$ (cm)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper left", frameon=True, framealpha=0.95, edgecolor="gray")
    
    plt.tight_layout()
    out_path = os.path.join(FIGURAS_DIR, "grafico_metodo_estatico.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Gráfico estático salvo em: {out_path}")

if __name__ == "__main__":
    gerar_grafico()
