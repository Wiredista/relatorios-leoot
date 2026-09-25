#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração do gráfico do Método Dinâmico (T² vs m)
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
FIGURAS_DIR = os.path.join(BASE_DIR, "figuras")

sys.path.insert(0, SCRIPT_DIR)
import calcular_tabelas

def gerar_grafico():
    resultados = calcular_tabelas.processar_dados()
    
    massas_g = np.array([r["massa_g"] for r in resultados])
    sigma_m_g = np.array([r["sigma_m_g"] for r in resultados])
    
    m_kg = np.array([r["massa_kg"] for r in resultados])
    sigma_m_kg = np.array([r["sigma_m_kg"] for r in resultados])
    
    T2 = np.array([r["T2"] for r in resultados])
    sigma_T2 = np.array([r["sigma_T2"] for r in resultados])
    
    p, cov = np.polyfit(m_kg, T2, 1, cov=True)
    slope, intercept = p[0], p[1]
    slope_err = np.sqrt(cov[0, 0])
    intercept_err = np.sqrt(cov[1, 1])
    
    k_din = (4 * np.pi**2) / slope
    sigma_k_din = (4 * np.pi**2 / (slope**2)) * slope_err
    
    m_ef = intercept / slope
    sigma_m_ef = m_ef * np.sqrt((intercept_err/intercept)**2 + (slope_err/slope)**2)
    
    r_matrix = np.corrcoef(m_kg, T2)
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
        massas_g, T2,
        xerr=sigma_m_g, yerr=sigma_T2,
        fmt="s", color="#1f77b4", ecolor="#d62728", elinewidth=1.2,
        capsize=3, capthick=1.2, markersize=6, label="Dados Experimentais"
    )
    
    m_fit_g = np.linspace(min(massas_g)-10, max(massas_g)+10, 100)
    T2_fit = slope * (m_fit_g / 1000.0) + intercept
    
    eq_text = (
        r"$T^2 = (%.3f \cdot m + %.4f)\text{ s}^2$" "\n"
        r"$k_{\text{din}} = (%.2f \pm %.2f)\text{ N/m}$" "\n"
        r"$m_{\text{ef}} = (%.1f \pm %.1f)\text{ g}$" "\n"
        r"$R^2 = %.4f$"
    ) % (slope, intercept, k_din, sigma_k_din, m_ef*1000, sigma_m_ef*1000, r2)
    
    ax.plot(m_fit_g, T2_fit, color="#d62728", linestyle="--", linewidth=1.8, label=f"Ajuste Linear:\n{eq_text}")
    
    ax.set_title("Método Dinâmico: Quadrado do Período em Função da Massa Suspensa", pad=12, fontweight="bold")
    ax.set_xlabel(r"Massa suspensa $m$ (g)")
    ax.set_ylabel(r"Quadrado do Período $T^2$ ($\text{s}^2$)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper left", frameon=True, framealpha=0.95, edgecolor="gray")
    
    plt.tight_layout()
    out_path = os.path.join(FIGURAS_DIR, "grafico_metodo_dinamico.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Gráfico dinâmico salvo em: {out_path}")

if __name__ == "__main__":
    gerar_grafico()
