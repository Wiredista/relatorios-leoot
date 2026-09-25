#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração dos gráficos de simulação teórica do MHS
"""

import os
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
FIGURAS_DIR = os.path.join(BASE_DIR, "figuras")

def gerar_graficos_mhs():
    k = 15.70
    m = 0.160
    omega = np.sqrt(k / m)
    T = 2 * np.pi / omega
    A = 0.03
    phi = 0.0
    
    t = np.linspace(0, 2 * T, 1000)
    
    x = A * np.cos(omega * t + phi)
    v = -A * omega * np.sin(omega * t + phi)
    a = -A * (omega**2) * np.cos(omega * t + phi)
    
    Ec = 0.5 * m * (v**2)
    Ep = 0.5 * k * (x**2)
    Em = Ec + Ep
    
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 12,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "mathtext.fontset": "cm"
    })
    
    # 1. Grafico de Cinematica
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6.5), sharex=True, dpi=300)
    
    ax1.plot(t, x * 100, color="#1f77b4", linewidth=1.8, label=r"$x(t) = A\cos(\omega t)$")
    ax1.set_ylabel(r"Posição $x$ (cm)")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper right", framealpha=0.9)
    ax1.set_title("Cinemática do MHS Vertical ($m = 160\\text{ g}$, $k = 15{,}70\\text{ N/m}$)", fontweight="bold", pad=10)
    
    ax2.plot(t, v * 100, color="#2ca02c", linewidth=1.8, label=r"$v(t) = -A\omega\sin(\omega t)$")
    ax2.set_ylabel(r"Velocidade $v$ (cm/s)")
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper right", framealpha=0.9)
    
    ax3.plot(t, a, color="#d62728", linewidth=1.8, label=r"$a(t) = -\omega^2 x(t)$")
    ax3.set_ylabel(r"Aceleração $a$ ($\text{m/s}^2$)")
    ax3.set_xlabel("Tempo $t$ (s)")
    ax3.grid(True, linestyle=":", alpha=0.6)
    ax3.legend(loc="upper right", framealpha=0.9)
    
    plt.tight_layout()
    p1 = os.path.join(FIGURAS_DIR, "grafico_cinematica_mhs.png")
    plt.savefig(p1, dpi=300)
    plt.close()
    print(f"Gráfico de cinemática salvo em: {p1}")
    
    # 2. Grafico de Energias
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=300)
    
    ax.plot(t, Ec * 1000, color="#d62728", linewidth=2.0, label=r"Energia Cinética $E_c = \frac{1}{2}mv^2$")
    ax.plot(t, Ep * 1000, color="#1f77b4", linewidth=2.0, linestyle="--", label=r"Energia Potencial Efetiva $E_p = \frac{1}{2}kx^2$")
    ax.plot(t, Em * 1000, color="#000000", linewidth=1.5, linestyle=":", label=r"Energia Mecânica Total $E_m = E_c + E_p$")
    
    ax.set_title("Conservação da Energia Mecânica no MHS Vertical", fontweight="bold", pad=12)
    ax.set_xlabel("Tempo $t$ (s)")
    ax.set_ylabel("Energia (mJ)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper right", framealpha=0.95, edgecolor="gray")
    
    plt.tight_layout()
    p2 = os.path.join(FIGURAS_DIR, "grafico_energias_mhs.png")
    plt.savefig(p2, dpi=300)
    plt.close()
    print(f"Gráfico de energias salvo em: {p2}")

if __name__ == "__main__":
    gerar_graficos_mhs()
