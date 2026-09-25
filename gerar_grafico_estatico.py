#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração do gráfico do Método Estático (Laboratório de Oscilações UFU)
Gera o gráfico de Deformação vs Massa (e Força vs Deformação)
Exporta a figura r1_fig1.png com qualidade acadêmica (300 DPI)
"""

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

def calcular_incerteza_massa(n_pesos, sigma_suporte=0.25, delta_var=0.50, delta_inst=0.25):
    sigma_peso = math.sqrt(delta_var**2 + delta_inst**2)
    return math.sqrt(sigma_suporte**2 + n_pesos * (sigma_peso**2))

def gerar_grafico():
    caminho_csv = "UFU/dados_estatico.csv"
    
    massas_g = []
    posicoes_mm = []
    sigma_x_mm = []
    n_pesos_lista = []
    
    with open(caminho_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            massas_g.append(float(row["massa_g"]))
            posicoes_mm.append(float(row["posicao_mm"]))
            sigma_x_mm.append(float(row["posicao_incerteza_mm"]))
            n_pesos_lista.append(i) # 0 a 5
            
    x0_mm = posicoes_mm[0] # 460.0 mm
    
    deformacoes_m = []
    sigma_delta_x_m = []
    massas_kg = []
    sigma_massas_kg = []
    
    for i in range(len(massas_g)):
        delta_x_mm = x0_mm - posicoes_mm[i]
        deformacoes_m.append(delta_x_mm / 1000.0)
        
        # Incerteza propagada da deformacao: sqrt(sigma_x0^2 + sigma_x^2)
        sig_dx_mm = math.sqrt(sigma_x_mm[0]**2 + sigma_x_mm[i]**2) if i > 0 else sigma_x_mm[0]
        sigma_delta_x_m.append(sig_dx_mm / 1000.0)
        
        m_kg = massas_g[i] / 1000.0
        sig_m_g = calcular_incerteza_massa(n_pesos_lista[i])
        massas_kg.append(m_kg)
        sigma_massas_kg.append(sig_m_g / 1000.0)
        
    x = np.array(massas_kg)
    y = np.array(deformacoes_m)
    x_err = np.array(sigma_massas_kg)
    y_err = np.array(sigma_delta_x_m)
    
    g = 9.78 # Aceleração da gravidade local (m/s^2)
    
    # Ajuste linear: y = a * x + b (Delta x = a * m + b)
    p, cov = np.polyfit(x, y, 1, cov=True)
    a, b = p[0], p[1]
    erro_a = np.sqrt(cov[0, 0])
    erro_b = np.sqrt(cov[1, 1])
    
    # R^2
    y_pred = a * x + b
    residuos = y - y_pred
    r2 = 1 - (np.sum(residuos**2) / np.sum((y - np.mean(y))**2))
    
    # Constante elástica: a = g / k => k = g / a
    k_est = g / a
    sigma_k_est = (g / (a**2)) * erro_a
    
    print(f"Ajuste Linear Estático: Delta x = ({a:.4f} ± {erro_a:.4f}) * m + ({b:.4f} ± {erro_b:.4f})")
    print(f"R² = {r2:.5f}")
    print(f"k_estático = ({k_est:.2f} ± {sigma_k_est:.2f}) N/m (com g = {g} m/s²)")
    
    # Configurar estilo visual
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
    
    # Linha de ajuste
    x_lin = np.linspace(0.0, 0.28, 100)
    y_lin = a * x_lin + b
    ax.plot(x_lin * 1000.0, y_lin * 1000.0, color='#003366', linestyle='--', linewidth=1.8,
            label=f'Ajuste: $\\Delta x = ({a:.3f})m {b:+.3f}$\n$R^2 = {r2:.4f}$')
    
    # Pontos experimentais
    ax.errorbar(x * 1000.0, y * 1000.0, xerr=x_err * 1000.0, yerr=y_err * 1000.0,
                fmt='o', color='#0066cc', ecolor='#333333', elinewidth=1.2,
                capsize=3.5, capthick=1.2, markersize=6, label='Dados Experimentais')
    
    ax.set_xlabel(r'Massa Total $m$ (g)', fontweight='bold')
    ax.set_ylabel(r'Deformação $\Delta x$ (mm)', fontweight='bold')
    ax.set_title(r'Gráfico de Deformação Estática: $\Delta x \times m$ (Lei de Hooke)', pad=12, fontweight='bold')
    
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.set_xlim(0, 280)
    ax.set_ylim(-5, 175)
    
    texto_info = (
        f"$\\mathbf{{Resultados:}}$\n"
        f"Inclinação $a = ({a:.3f} \\pm {erro_a:.3f})\\;\\mathrm{{m/kg}}$\n"
        f"Intercepto $b = ({b*1000:.1f} \\pm {erro_b*1000:.1f})\\;\\mathrm{{mm}}$\n"
        f"$\\mathbf{{k_{{est}} = ({k_est:.2f} \\pm {sigma_k_est:.2f})\\;\\mathrm{{N/m}}}}$"
    )
    ax.text(15, 160, texto_info, transform=ax.transData, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#f4f4f4', edgecolor='#999999', alpha=0.9))
    
    ax.legend(loc='lower right', framealpha=0.95)
    plt.tight_layout()
    
    plt.savefig("UFU/grafico_metodo_estatico.png", dpi=300)
    plt.savefig("grafico_metodo_estatico.png", dpi=300)
    plt.close()
    print("Gráfico estático salvo com sucesso em 'UFU/grafico_metodo_estatico.png'!")

if __name__ == "__main__":
    gerar_grafico()
