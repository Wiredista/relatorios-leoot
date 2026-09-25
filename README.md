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

## 🛠️ Como Reproduzir as Análises e Compilar

### 1. Pré-requisitos
* **Python 3** (com `numpy` e `matplotlib` para gerar os gráficos)
* **Pandoc** ($\ge 2.19$)
* **TeX Live / PDFLaTeX** (com pacotes `graphicx`, `amsmath`, `fcolorbox`, `titling`, `indentfirst`)

### 2. Executar Scripts de Análise
Cada relatório possui sua própria subpasta `scripts/` contendo os códigos em Python para tratamento dos dados e geração dos gráficos. Para executá-los:

1. Navegue até a pasta de scripts do relatório desejado:
   ```bash
   cd relatorio-XX/scripts
   ```
2. Execute o script desejado (por exemplo, cálculo de tabelas ou geração de gráficos):
   ```bash
   python3 nome_do_script.py
   ```
Os scripts leem os arquivos da pasta `../dados/` e salvam os gráficos gerados diretamente em `../figuras/`.

### 3. Compilar Relatórios em PDF
A partir da raiz do repositório, execute o utilitário `md2pdf.sh` passando o caminho relativo do arquivo Markdown correspondente:
```bash
./md2pdf.sh "relatorio-XX/Relatório X.md"
```
O arquivo `.pdf` compilado será salvo automaticamente na mesma pasta do relatório.

---

## 📚 Referências Principais
- **Apostila de Laboratório: Oscilações, Ondas e Óptica**, Instituto de Física, Universidade Federal de Uberlândia (UFU), 2024.
