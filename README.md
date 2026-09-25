# Relatórios de Laboratório — LEOOT (UFU)

Repositório acadêmico destinado ao versionamento, análise estatística de dados experimentais e compilação automatizada dos relatórios da disciplina de **Laboratório de Ensino em Oscilações, Ondas e Termodinâmica / Óptica**, ministrada no **Instituto de Física (INFIS)** da **Universidade Federal de Uberlândia (UFU)**.

---

## 👥 Integrantes do Grupo

| Aluno(a) | Matrícula / RA | Curso |
| :--- | :---: | :---: |
| **Álvaro Antônio de Lacerda Rosário** | `12511ETE011` | Engenharia Eletrônica e de Telecomunicações |
| **Ana Clara Pereira da Silva** | `12521ETE001` | Engenharia Eletrônica e de Telecomunicações |
| **Marya Eduarda Rodrigues da Costa** | `12511ETE006` | Engenharia Eletrônica e de Telecomunicações |
| **Vinicius Xavier Faria** | `12411ETE005` | Engenharia Eletrônica e de Telecomunicações |

---

## 📑 Relatórios do Semestre

### 📌 [Relatório 1: Sistema Massa-Mola Vertical e Lei de Hooke](relatorio-01/Relatório%201.md)
* **Diretório do Experimento:** [`relatorio-01/`](relatorio-01/)
* **Arquivo Fonte (Markdown):** [relatorio-01/Relatório 1.md](relatorio-01/Relatório%201.md)
* **Documento Compilado (PDF):** [relatorio-01/Relatório 1.pdf](relatorio-01/Relatório%201.pdf)
* **Objetivo:** Validação experimental da Lei de Hooke, determinação da constante elástica $k$ por métodos estático e dinâmico, e estudo do Movimento Harmônico Simples (MHS) vertical com balanço de energias mecânicas.

---

## 📂 Arquitetura do Repositório

O repositório é organizado de forma modular, mantendo na raiz apenas arquivos globais e cada relatório isolado em sua respectiva pasta com seus próprios dados, scripts e figuras:

```
relatorios-leoot/
├── README.md                          # Documentação geral do repositório
├── md2pdf.sh                          # Script global de compilação Markdown -> PDF (Pandoc/LaTeX)
├── logo-ufu.png                       # Brasão institucional da UFU (usado no cabeçalho dos relatórios)
│
└── relatorio-01/                      # 🔬 Relatório 1: Sistema Massa-Mola Vertical
    ├── Relatório 1.md                 # Código-fonte formatado nas normas ABNT
    ├── Relatório 1.pdf                # PDF compilado pronto para entrega
    │
    ├── dados/                         # Planilhas com dados experimentais brutos
    │   ├── dados_estatico.csv         # Medições estáticas (massa vs posição)
    │   └── dados_dinamico.csv         # Medições dinâmicas (tempos de 10 oscilações)
    │
    ├── scripts/                       # Scripts em Python para tratamento e plotagem
    │   ├── calcular_tabelas.py        # Processamento estatístico e propagação de incertezas
    │   ├── gerar_grafico_estatico.py  # Regressão linear Δx vs m (Método Estático)
    │   ├── gerar_grafico_dinamico.py  # Regressão linear T² vs m (Método Dinâmico)
    │   └── gerar_graficos_mhs_simulacao.py # Simulação teórica de cinemática e energias do MHS
    │
    └── figuras/                       # Figuras e gráficos gerados em alta resolução (300 DPI)
        ├── grafico_metodo_estatico.png
        ├── grafico_metodo_dinamico.png
        ├── grafico_cinematica_mhs.png
        ├── grafico_energias_mhs.png
        └── r1_fig1.jpg                # Esquema conceitual da montagem experimental
```

---

## 🛠️ Como Reproduzir as Análises e Compilar

### 1. Pré-requisitos
* **Python 3** (com `numpy` e `matplotlib` para gerar os gráficos)
* **Pandoc** ($\ge 2.19$)
* **TeX Live / PDFLaTeX** (com pacotes `graphicx`, `amsmath`, `fcolorbox`, `titling`, `indentfirst`)

### 2. Executar Scripts de Análise do Relatório 1
Navegue até a pasta de scripts do relatório:
```bash
cd relatorio-01/scripts

# Processar as tabelas com incertezas propagadas:
python3 calcular_tabelas.py

# Gerar todos os gráficos:
python3 gerar_grafico_estatico.py
python3 gerar_grafico_dinamico.py
python3 gerar_graficos_mhs_simulacao.py
```

### 3. Compilar o Relatório em PDF
A partir da raiz do repositório, execute o utilitário `md2pdf.sh` passando o caminho do Markdown:
```bash
./md2pdf.sh "relatorio-01/Relatório 1.md"
```
O PDF atualizado será salvo automaticamente na pasta correspondente (`relatorio-01/Relatório 1.pdf`).

---

## 📚 Referências Principais
- **Apostila de Laboratório: Oscilações, Ondas e Óptica**, Instituto de Física, Universidade Federal de Uberlândia (UFU), 2024.
- **Sears & Zemansky: Física II — Termodinâmica e Ondas** (YOUNG, H. D.; FREEDMAN, R. A., 14ª ed., Pearson, 2016).
