# Relatórios de Laboratório — LEOOT (UFU)

Repositório acadêmico destinado ao desenvolvimento, análise estatística de dados experimentais e compilação automatizada dos relatórios da disciplina de **Laboratório de Ensino em Oscilações, Ondas e Termodinâmica / Óptica**, ministrada no **Instituto de Física (INFIS)** da **Universidade Federal de Uberlândia (UFU)**.

---

## 👥 Integrantes do Grupo

| Aluno(a) | Matrícula / RA | Curso |
| :--- | :---: | :---: |
| **Álvaro Antônio de Lacerda Rosário** | `12511ETE011` | Engenharia Eletrônica e de Telecomunicações |
| **Ana Clara Pereira da Silva** | `12521ETE001` | Engenharia Eletrônica e de Telecomunicações |
| **Marya Eduarda Rodrigues da Costa** | `12511ETE006` | Engenharia Eletrônica e de Telecomunicações |
| **Vinicius Xavier Faria** | `12411ETE005` | Engenharia Eletrônica e de Telecomunicações |

---

## 📑 Relatórios Disponíveis

### 📌 [Relatório 1: Sistema Massa-Mola Vertical e Lei de Hooke](Relatório%201.md)
* **Arquivo Fonte (Markdown):** [Relatório 1.md](Relatório%201.md) (também disponível em [UFU/Relatório 1.md](UFU/Relatório%201.md))
* **Versão Compilada (PDF):** [Relatório 1.pdf](Relatório%201.pdf)
* **Objetivo:** Validação experimental da Lei de Hooke, determinação da constante elástica $k$ por métodos estático e dinâmico, e estudo do Movimento Harmônico Simples (MHS) vertical com balanço de energias mecânicas.

---

## 📂 Estrutura de Arquivos

```
relatorios-leoot/
├── README.md                          # Documentação geral do repositório
├── md2pdf.sh                          # Script de compilação Pandoc -> PDF (LaTeX)
├── logo-ufu.png                       # Brasão institucional da UFU para o cabeçalho
│
├── Relatório 1.md                     # Código-fonte do Relatório 1
├── Relatório 1.pdf                    # PDF compilado nas normas ABNT
│
├── dados_estatico.csv                 # Dados brutos do experimento estático (massa vs posição)
├── dados_dinamico.csv                 # Dados brutos do experimento dinâmico (tempos de oscilação)
│
├── calcular_tabelas.py                # Script em Python puro para propagação de incertezas e tabelas
├── gerar_grafico_estatico.py          # Script de regressão linear para o método estático
├── gerar_grafico_dinamico.py          # Script de regressão linear para o método dinâmico
├── gerar_graficos_mhs_simulacao.py    # Simulação teórica de cinemática e energias do MHS
│
├── grafico_metodo_estatico.png        # Gráfico de ajuste Δx vs m (k_est = 15,64 N/m)
├── grafico_metodo_dinamico.png        # Gráfico de ajuste T² vs m (k_din = 15,75 N/m)
├── grafico_cinematica_mhs.png         # Curvas temporais de posição, velocidade e aceleração
├── grafico_energias_mhs.png           # Balanço de energias cinética, potencial e mecânica
└── r1_fig1.jpg                        # Esquema conceitual da montagem experimental
```

---

## 🛠️ Como Reproduzir as Análises e Compilar

### 1. Pré-requisitos
* **Python 3** (com `numpy` e `matplotlib` para os gráficos)
* **Pandoc** ($\ge 2.19$)
* **TeX Live** (com `pdflatex`, `graphicx`, `amsmath`, `fcolorbox`)

### 2. Executar Scripts de Análise
Para recalcular as médias, incertezas e tabelas:
```bash
python3 calcular_tabelas.py
```

Para regenerar os gráficos em alta resolução (300 DPI):
```bash
python3 gerar_grafico_estatico.py
python3 gerar_grafico_dinamico.py
python3 gerar_graficos_mhs_simulacao.py
```

### 3. Compilar o Relatório em PDF
Para gerar o arquivo PDF formatado com capa ABNT e numeração de seções:
```bash
./md2pdf.sh "Relatório 1.md"
```

---

## 📚 Referências Principais
- **Apostila de Laboratório: Oscilações, Ondas e Óptica**, Instituto de Física, Universidade Federal de Uberlândia (UFU), 2024.
- **Sears & Zemansky: Física II — Termodinâmica e Ondas** (YOUNG, H. D.; FREEDMAN, R. A., 14ª ed., Pearson, 2016).
