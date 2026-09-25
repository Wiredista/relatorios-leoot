#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração dos gráficos de Simulação do MHS (Itens d.i e d.ii da Apostila UFU)
1. Funções cinemáticas x(t), v(t), a(t)
2. Evolução temporal das Energias (Cinética, Elástica, Gravitacional e Mecânica Total)
Exporta:
- UFU/grafico_cinematica_mhs.png
- UFU/grafico_energias_mhs.png
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def gerar_graficos():
    # Parâmetros físicos baseados no experimento
    m = 0.160       # Massa escolhida: 160 g = 0.160 kg (m_s + 3 m_p)
    k = 15.70       # Constante elástica média (N/m)
    g = 9.78        # Gravidade local (m/s^2)
    A = 0.020       # Amplitude de oscilação: 2.0 cm = 0.020 m
    
    omega = math.sqrt(k / m)      # Frequência angular (rad/s)
    T = 2 * math.pi / omega       # Período (s) ~ 0.634 s
    y_e = (m * g) / k             # Deformação estática de equilíbrio (m) ~ 0.0998 m (9.98 cm)
    
    print(f"Parâmetros: m = {m*1000:.1f} g, k = {k:.2f} N/m, omega = {omega:.3f} rad/s, T = {T:.3f} s, y_e = {y_e*100:.2f} cm")
    
    # -------------------------------------------------------------
    # 1. GRÁFICO DAS FUNÇÕES CINEMÁTICAS: x(t), v(t), a(t)
    # -------------------------------------------------------------
    t_cin = np.linspace(0, 2 * T, 500)
    x_t = A * np.cos(omega * t_cin)                  # Deslocamento em m
    v_t = -A * omega * np.sin(omega * t_cin)         # Velocidade em m/s
    a_t = -A * (omega**2) * np.cos(omega * t_cin)    # Aceleração em m/s^2
    
    plt.rcParams.update({
        'font.size': 10,
        'font.family': 'serif',
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9
    })
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7.5, 6.5), sharex=True, dpi=300)
    
    # Deslocamento
    ax1.plot(t_cin, x_t * 100.0, color='#004488', linewidth=1.8, label=r'$x(t) = A\cos(\omega t)$')
    ax1.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax1.set_ylabel(r'$x(t)$ (cm)', fontweight='bold')
    ax1.set_title(r'Cinemática do Oscilador Harmônico ($m = 160\text{ g}$, $k = 15{,}70\text{ N/m}$, $A = 2{,}0\text{ cm}$)', fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper right')
    
    # Velocidade
    ax2.plot(t_cin, v_t * 100.0, color='#008844', linewidth=1.8, label=r'$v(t) = -A\omega\operatorname{sen}(\omega t)$')
    ax2.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax2.set_ylabel(r'$v(t)$ (cm/s)', fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper right')
    
    # Aceleração
    ax3.plot(t_cin, a_t, color='#cc0000', linewidth=1.8, label=r'$a(t) = -A\omega^2\cos(\omega t)$')
    ax3.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax3.set_xlabel('Tempo $t$ (s)', fontweight='bold')
    ax3.set_ylabel(r'$a(t)$ ($\mathrm{m/s^2}$)', fontweight='bold')
    ax3.grid(True, linestyle=':', alpha=0.6)
    ax3.legend(loc='upper right')
    
    # Marcar os períodos T e 2T
    for ax in (ax1, ax2, ax3):
        ax.axvline(T, color='#888888', linestyle=':', linewidth=1.2)
        ax.axvline(2*T, color='#888888', linestyle=':', linewidth=1.2)
        
    ax1.text(T, ax1.get_ylim()[1]*0.8, ' $t = T$', color='#555555', fontsize=9)
    ax1.text(2*T, ax1.get_ylim()[1]*0.8, ' $t = 2T$', color='#555555', fontsize=9)
    
    plt.tight_layout()
    plt.savefig("UFU/grafico_cinematica_mhs.png", dpi=300)
    plt.savefig("grafico_cinematica_mhs.png", dpi=300)
    plt.close()
    print("Gráfico de cinemática salvo em 'UFU/grafico_cinematica_mhs.png'!")
    
    # -------------------------------------------------------------
    # 2. GRÁFICO DAS ENERGIAS AO LONGO DE 1 PERÍODO (t in [0, T])
    # -------------------------------------------------------------
    t_en = np.linspace(0, T, 500)
    x_en = A * np.cos(omega * t_en)                  # Posição relativa ao equilíbrio (m)
    v_en = -A * omega * np.sin(omega * t_en)         # Velocidade (m/s)
    y_total = y_e + x_en                            # Deformação total absoluta da mola a partir do relaxamento (m)
    
    # Energias (em mJ para melhor legibilidade na escala)
    E_cin = 0.5 * m * (v_en**2) * 1000.0                       # mJ
    E_pot_ef = 0.5 * k * (x_en**2) * 1000.0                   # mJ (potencial harmônica efetiva)
    E_mec_total = E_cin + E_pot_ef                            # mJ (total conservada)
    
    # Energias absolutas (elástica e gravitacional em relação a y=0)
    E_el_abs = 0.5 * k * (y_total**2) * 1000.0                # mJ
    E_grav_abs = - m * g * y_total * 1000.0                   # mJ
    E_soma_abs = E_cin + E_el_abs + E_grav_abs                # mJ (também constante!)
    
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    
    ax.plot(t_en, E_cin, color='#008844', linewidth=2.0, linestyle='-', label=r'Energia Cinética $E_c = \frac{1}{2}mv^2$')
    ax.plot(t_en, E_pot_ef, color='#cc0000', linewidth=2.0, linestyle='--', label=r'Energia Potencial Efetiva $E_{p} = \frac{1}{2}kx^2$')
    ax.plot(t_en, E_mec_total, color='#003366', linewidth=2.2, linestyle='-', label=r'Energia Mecânica Total $E_m = E_c + E_p = \frac{1}{2}kA^2$')
    
    ax.set_xlabel('Tempo $t$ (s)', fontweight='bold')
    ax.set_ylabel('Energia (mJ)', fontweight='bold')
    ax.set_title(r'Distribuição e Conservação de Energia ao Longo de 1 Período ($T = 0{,}634\text{ s}$)', pad=12, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlim(0, T)
    ax.set_ylim(0, max(E_mec_total) * 1.35)
    
    # Informações no gráfico
    E_total_val = 0.5 * k * (A**2) * 1000.0
    info_box = (
        f"$\\mathbf{{Par\\hat{{a}}metros:}}$\n"
        f"Massa $m = {m*1000:.0f}\\;\\mathrm{{g}}$\n"
        f"Amplitude $A = {A*100:.1f}\\;\\mathrm{{cm}}$\n"
        f"$\\mathbf{{E_{{total}} = {E_total_val:.2f}\\;\\mathrm{{mJ}}}}$ (Constante)"
    )
    ax.text(0.02, 0.95, info_box, transform=ax.transAxes, verticalalignment='top',
            fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f4f4f4', edgecolor='#999999', alpha=0.9))
    
    ax.legend(loc='lower right', framealpha=0.95)
    plt.tight_layout()
    plt.savefig("UFU/grafico_energias_mhs.png", dpi=300)
    plt.savefig("grafico_energias_mhs.png", dpi=300)
    plt.close()
    print("Gráfico de energias salvo em 'UFU/grafico_energias_mhs.png'!")

if __name__ == "__main__":
    gerar_graficos()
