---
title: Relatório de Experimento - Lei de Hooke e Oscilações
author: |-
  \begin{tabular}{cc}
    Álvaro Antônio de Lacerda Rosário & RA: 12511ETE011 \\
    Ana Clara Pereira da Silva & RA: 12521ETE001 \\
    Marya Eduarda Rodrigues da Costa & RA: 12511ETE006 \\
    Vinicius Xavier Faria & RA: 12411ETE005
  \end{tabular}
lang: pt-br
linestretch: 1.5
header-includes:
  - \usepackage{graphicx}
  - \usepackage{indentfirst}
  - \renewcommand{\contentsname}{Sumário}
  - \usepackage{titling}
  - \graphicspath{{figuras/}{../}}
  - \pretitle{\begin{center}\includegraphics[width=3cm]{logo-infis.png}\\[2cm]\LARGE\bfseries}
  - \posttitle{\end{center}}
  - \preauthor{\begin{center}\large}
  - \postauthor{\end{center}}
  - \predate{\begin{center}\large}
  - \postdate{\end{center}\vspace{2cm}\newpage}
subtitle: |-
  Laboratório de Ensino em Oscilações, Ondas e Termodinâmica \
  Instituto de Física (INFIS) \
  Universidade Federal de Uberlândia
geometry: left=3cm,right=2cm,top=3cm,bottom=2cm
fontsize: 12pt
keywords:
  - Lei de Hooke
  - Sistema massa-mola
  - Constante elástica
  - Movimento Harmônico Simples
toc-title: Sumário
---

# Resumo {.unnumbered}

> **[A FAZER: Redigir o Resumo definitivo]**
> *Orientações:* Escrever um parágrafo único de 150 a 250 palavras contendo:
> 1. Objetivo: validação da Lei de Hooke e determinação de $k$ da mola helicoidal.
> 2. Métodos utilizados: estático (deformação sob massas calibradas) e dinâmico (período de oscilação do MHS).
> 3. Principais resultados: $k_{\text{est}} = (15{,}64 \pm 0{,}33)\text{ N/m}$ e $k_{\text{din}} = (15{,}75 \pm 0{,}44)\text{ N/m}$, com discrepância de apenas $0{,}70\%$.
> 4. Conclusão: confirmação do regime elástico linear ($R^2 > 0{,}997$) e equivalência estatística entre os métodos.

\noindent **Palavras-chave:** Lei de Hooke. Sistema massa-mola. Constante elástica. Movimento Harmônico Simples.

\newpage

# Abstract {.unnumbered}

> **[A FAZER: Redigir a versão em inglês do Resumo]**
> *Guidelines:* Translate the Brazilian Portuguese abstract into technical English, keeping the same structure (Objectives, Methods, Results $k_{\text{est}}$ and $k_{\text{din}}$, Discrepancy, and Conclusions).

\noindent **Keywords:** Hooke's Law. Mass-spring system. Spring constant. Simple Harmonic Motion.

\newpage
\tableofcontents
\newpage

# Introdução

## Lei de Hooke

A Lei de Hooke descreve o comportamento elástico de corpos como molas, estabelecendo que a força restauradora é proporcional à deformação sofrida, desde que não se ultrapasse o limite de elasticidade do material. Matematicamente, expressa-se por:

\begin{equation}
F = -k x
\end{equation}

Onde $F$ é a força restauradora, $k$ é a constante elástica da mola (que indica sua rigidez) e $x$ é a deformação em relação à posição de equilíbrio. O sinal negativo mostra que a força atua sempre no sentido oposto ao deslocamento, buscando restabelecer a posição de equilíbrio. No equilíbrio estático, essa força equilibra o peso da massa suspensa, permitindo determinar experimentalmente o valor de $k$ a partir da relação entre massa e deformação.

## Lei de Hooke e Oscilações

\begin{figure}[htbp]
\centering
\includegraphics[width=0.6\textwidth]{r1_fig1.jpg}
\caption{Esquema da montagem experimental do sistema massa-mola. Fonte: Ribeiro (2005, p. 78).}
\label{fig:esquema_montagem}
\end{figure}

Ao acoplar uma massa de valor $m$, a mola sofre uma deformação, que chamaremos de $x_e$, tal que o módulo da força elástica fica igual ao peso e o sistema fica em equilíbrio. Assim,

\begin{equation}
mg = k x_e
\end{equation}

Linearizando essa equação, obtemos a constante $k$:

\begin{equation}
y = m a + b
\end{equation}

\begin{equation}
y = m\left(\frac{g}{k}\right) + b
\end{equation}

\begin{equation}
a = \frac{g}{k} \quad \text{ou} \quad k = \frac{g}{a}
\end{equation}

Como o equilíbrio é estático, essa relação é usada no método estático para determinarmos a constante elástica $k$.

## Equações do Movimento Harmônico: determinando $x(t)$, $v(t)$ e $a(t)$

Dada a equação anterior e aplicando a segunda lei de Newton, obtemos:

\begin{equation}
m \frac{d^2x}{dt^2} = -kx
\end{equation}

O resultado dessa equação nos proporciona o movimento harmônico simples, cuja solução do deslocamento $x$ é dada por:

\begin{equation}
x(t) = A \cos(\omega t + \phi)
\end{equation}

Com isso, sabendo que $\frac{dx}{dt} = v$, onde $v$ é a velocidade, obtém-se a seguinte equação para a velocidade:

\begin{equation}
v(t) = -A \omega \operatorname{sen}(\omega t + \phi)
\end{equation}

Analogamente, considerando que $\frac{d^2x}{dt^2} = a$, obtemos a expressão para a aceleração:

\begin{equation}
a(t) = -A \omega^2 \cos(\omega t + \phi)
\end{equation}

onde:

- $A$ é a amplitude;
- $\omega$ é a frequência angular do sistema;
- $\phi$ é a fase inicial;

A relação da massa e constante elástica é:

\begin{equation}
\omega = \sqrt{\frac{k}{m}}
\end{equation}

## Período ($T$)

O período é definido como o tempo necessário para que o sistema massa-mola realize uma oscilação completa, retornando à posição e velocidade iniciais. Para o Movimento Harmônico Simples (MHS), seu valor é dado por:

\begin{equation}
T = 2\pi\sqrt{\frac{m}{k}}
\end{equation}

Em que $T$ é o período (em segundos), $m$ é a massa total oscilante e $k$ a constante elástica. Uma propriedade importante é que o período não depende da amplitude — fenômeno chamado isocronismo. Quanto maior a massa, mais lenta é a oscilação; quanto mais rígida a mola, mais rápida. Essa relação também permite calcular $k$ de forma independente, por meio do método dinâmico, linearizando a equação na forma:

\begin{equation}
T^2 = \left(\frac{4\pi^2}{k}\right) m
\end{equation}

## Energias no Oscilador Vertical

No oscilador massa-mola vertical sob ação da gravidade, a energia mecânica total $E_m$ envolve a energia cinética da massa, a energia potencial elástica da mola e a energia potencial gravitacional.

Seja $y$ o deslocamento vertical medido a partir da posição de relaxamento da mola (onde a mola não está esticada, $y = 0$). Na posição de equilíbrio estático, a mola deforma de $y_e = \frac{mg}{k}$. Ao deslocar o corpo de uma coordenada $x$ em relação ao ponto de equilíbrio estático, a deformação total é $y = y_e + x$. As energias associadas ao sistema são:

1. **Energia Cinética ($E_c$):** associada ao movimento da massa:
\begin{equation}
E_c = \frac{1}{2} m v^2 = \frac{1}{2} m \left(\frac{dx}{dt}\right)^2
\end{equation}

2. **Energia Potencial Elástica ($E_{\text{el}}$):** armazenada na mola deformada:
\begin{equation}
E_{\text{el}} = \frac{1}{2} k y^2 = \frac{1}{2} k (y_e + x)^2 = \frac{1}{2} k y_e^2 + k y_e x + \frac{1}{2} k x^2
\end{equation}

3. **Energia Potencial Gravitacional ($E_{\text{grav}}$):** adotando a posição $y = 0$ como referência:
\begin{equation}
E_{\text{grav}} = -m g y = -m g (y_e + x) = -m g y_e - m g x
\end{equation}

Somando as energias potenciais elástica e gravitacional e notando que no equilíbrio $k y_e = m g$:
\begin{equation}
E_{\text{pot, total}} = E_{\text{el}} + E_{\text{grav}} = \left(\frac{1}{2} k y_e^2 - m g y_e\right) + (k y_e - m g) x + \frac{1}{2} k x^2 = -\frac{1}{2}\frac{m^2 g^2}{k} + \frac{1}{2} k x^2
\end{equation}

Como o primeiro termo é constante, pode-se escolher a energia potencial no ponto de equilíbrio ($x = 0$) como referência nula. Dessa forma, a **energia potencial efetiva** do sistema reduz-se à expressão harmônica clássica:
\begin{equation}
E_p(x) = \frac{1}{2} k x^2
\end{equation}

A energia mecânica total conservada ao longo de todo o movimento oscilatório (sem atrito) é dada por:
\begin{equation}
E_m = E_c + E_p = \frac{1}{2} m v^2 + \frac{1}{2} k x^2 = \frac{1}{2} k A^2 = \text{constante}
\end{equation}

Na presença de forças dissipativas (como a resistência do ar ou atrito interno nas espiras), parte dessa energia mecânica é gradualmente dissipada na forma de calor, gerando oscilações amortecidas.

## Objetivos

### Objetivo Geral

Comprovar a validade da Lei de Hooke e analisar o comportamento de um sistema massa-mola com base nos experimentos realizados em laboratório.

### Objetivos Específicos

1. **Determinação da Constante Elástica ($k$):** Determinar o valor da constante elástica de uma mola helicoidal a partir de dois métodos experimentais distintos: o método estático (baseado na deformação da mola sob ação de forças gravitacionais em equilíbrio, $mg = k\Delta x$) e o método dinâmico (baseado no período de oscilação do sistema, $T = 2\pi\sqrt{\frac{m}{k}}$).
2. **Verificação da Lei de Hooke:** Validar empiricamente a Lei de Hooke ($F = -k\Delta x$), analisando a proporcionalidade direta entre a força restauradora exercida pela mola e o seu deslocamento ($\Delta x$) em relação à posição de equilíbrio, dentro do limite elástico do material.
3. **Análise do Movimento Harmônico Simples (MHS):** Investigar o comportamento dinâmico do sistema massa-mola em oscilação, analisando a relação de dependência funcional entre o período de oscilação ($T$) e a massa acoplada ($m$).
4. **Tratamento de Dados e Linearização Gráfica:** Construir e interpretar gráficos com base nas medições obtidas em laboratório, aplicando o processo de linearização de equações (por exemplo, $T^2 = \frac{4\pi^2}{k} m$) para transformar relações não lineares em retas, permitindo extrair a constante elástica ($k$) por meio do ajuste linear (coeficiente angular).

# Procedimento Experimental

## Materiais Utilizados

- Mola helicoidal de aço;
- Suporte de massas com haste: $m_{\text{suporte}} = (10{,}00 \pm 0{,}25)\text{ g}$;
- Conjunto de massas calibradas: $m_{\text{peso}} = (50{,}00 \pm 0{,}75)\text{ g}$ cada;
- Régua milimetrada vertical: incerteza instrumental $\delta x = \pm 0{,}5\text{ mm}$;
- Cronômetro digital: incerteza instrumental $\delta t = \pm 0{,}005\text{ s}$;
- Suporte universal com garras de fixação.

## Metodologia

O experimento foi dividido em duas etapas:

1. **Método Estático:** Fixou-se a mola verticalmente na haste e registrou-se a posição inicial de referência com apenas o suporte de massas acoplado ($x_0 = 460{,}0\text{ mm}$). Em seguida, foram adicionados sucessivamente 5 discos de massa ($m_{\text{peso}}$), registrando-se a nova posição de equilíbrio $x$ a cada incremento. A deformação estática foi calculada por $\Delta x = x_0 - x$.
2. **Método Dinâmico:** Para cada configuração de massa acoplada (de 1 a 5 pesos adicionados ao suporte), o sistema foi deslocado levemente da posição de equilíbrio e liberado para oscilar. Cronometrou-se o intervalo de tempo correspondente a 20 oscilações completas ($t_{20}$). O procedimento foi repetido 10 vezes para cada quantidade de massa.

# Resultados e Discussão

## Método Estático

Os dados obtidos para a posição de equilíbrio e a respectiva deformação da mola em função da massa suspensa estão apresentados na Tabela 1.

\begin{table}[htbp]
\centering
\caption{Dados experimentais do método estático.}
\label{tab:estatico}
\begin{tabular}{cccc}
\hline
\textbf{Configuração} & \textbf{Massa $m$ (g)} & \textbf{Posição $x$ (mm)} & \textbf{Deformação $\Delta x$ (mm)} \\ \hline
$m_s + 0\,m_p$ & $10{,}0$ & $460{,}0 \pm 0{,}5$ & $0{,}0 \pm 0{,}7$ \\
$m_s + 1\,m_p$ & $60{,}0$ & $434{,}0 \pm 0{,}5$ & $26{,}0 \pm 0{,}7$ \\
$m_s + 2\,m_p$ & $110{,}0$ & $396{,}0 \pm 0{,}5$ & $64{,}0 \pm 0{,}7$ \\
$m_s + 3\,m_p$ & $160{,}0$ & $366{,}0 \pm 0{,}5$ & $94{,}0 \pm 0{,}7$ \\
$m_s + 4\,m_p$ & $210{,}0$ & $335{,}0 \pm 0{,}5$ & $125{,}0 \pm 0{,}7$ \\
$m_s + 5\,m_p$ & $260{,}0$ & $306{,}5 \pm 0{,}5$ & $153{,}5 \pm 0{,}7$ \\ \hline
\end{tabular}
\end{table}

A Figura 2 apresenta o gráfico da deformação estática da mola em função da massa total suspensa, acompanhado das barras de incerteza experimental e da reta de regressão linear ajustada.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{grafico_metodo_estatico.png}
\caption{Gráfico de deformação estática $\Delta x \times m$ e ajuste linear (Lei de Hooke).}
\label{fig:estatico}
\end{figure}

### Análise e Discussão do Método Estático (Roteiro Teórico e de Resultados)

> **[A FAZER: Redigir o texto corrido da Discussão do Método Estático]**
>
> *Roteiro para a redação da sua análise:*
>
> 1. **Validação da Lei de Hooke e Linearidade dos Dados:**
>    - **Fundamentação teórica:** Na condição de equilíbrio estático ($P = F_e$), a força peso equilibra a força elástica ($mg = k\Delta x$), resultando na relação linear $\Delta x = \left(\frac{g}{k}\right) m$.
>    - **Resultado obtido:** O ajuste por mínimos quadrados forneceu a equação $\Delta x = (0{,}6254 \pm 0{,}0133)\,m - (0{,}0073 \pm 0{,}0021)$ com coeficiente de determinação $R^2 = 0{,}9982$.
>    - **Interpretação:** O valor de $R^2$ muito próximo de 1 comprova empiricamente a proporcionalidade direta entre força e deformação, validando a Lei de Hooke para o intervalo de massas utilizado ($10\text{ g}$ a $260\text{ g}$).
>
> 2. **Cálculo da Constante Elástica Estática ($k_{\text{est}}$):**
>    - O coeficiente angular da reta é $a = \frac{g}{k_{\text{est}}}$. Utilizando a gravidade local $g = 9{,}78\text{ m/s}^2$:
>      $$k_{\text{est}} = \frac{g}{a} = \frac{9{,}78}{0{,}6254} = (15{,}64 \pm 0{,}33)\text{ N/m}$$
>    - A incerteza $\sigma_{k_{\text{est}}}$ foi calculada através da propagação $\sigma_k = \frac{g}{a^2}\sigma_a$.
>
> 3. **Interpretação do Coeficiente Linear ($b$):**
>    - O intercepto obtido foi $b = -7{,}3 \pm 2{,}1\text{ mm}$.
>    - Explique que esse pequeno deslocamento decorre do assentamento inicial da mola sob a carga do suporte de massas e de pequenas folgas mecânicas na fixação superior.
>
> 4. **Limite de Elasticidade:**
>    - Destaque que não houve deformação plástica residual: ao retirar as massas ao final do experimento, a mola retornou exatamente à sua posição inicial de repouso ($x_0 = 460{,}0\text{ mm}$).

## Método Dinâmico

Na etapa dinâmica, foram medidos os tempos de 20 oscilações completas ($t_{20}$) em 10 repetições para cada uma das 5 massas acopladas ao suporte ($m_s + 1\,m_p$ até $m_s + 5\,m_p$). As medições estão organizadas na Tabela 2.

\begin{table}[htbp]
\centering
\caption{Tempos de 20 oscilações ($t_{20}$) em 10 repetições para cada massa (em segundos).}
\label{tab:dinamico_bruto}
\begin{tabular}{cccccc}
\hline
\textbf{Medição} & \textbf{60 g} & \textbf{110 g} & \textbf{160 g} & \textbf{210 g} & \textbf{260 g} \\ \hline
1 & $11{,}52$ & $10{,}66$ & $13{,}20$ & $15{,}64$ & $16{,}34$ \\
2 & $7{,}01$ & $10{,}48$ & $13{,}31$ & $16{,}40$ & $16{,}20$ \\
3 & $8{,}39$ & $10{,}60$ & $12{,}28$ & $13{,}60$ & $16{,}10$ \\
4 & $8{,}20$ & $11{,}47$ & $12{,}86$ & $14{,}05$ & $16{,}35$ \\
5 & $8{,}04$ & $10{,}33$ & $13{,}31$ & $13{,}76$ & $16{,}61$ \\
6 & $8{,}07$ & $10{,}06$ & $13{,}11$ & $14{,}43$ & $15{,}99$ \\
7 & $7{,}91$ & $10{,}74$ & $13{,}18$ & $14{,}71$ & $17{,}10$ \\
8 & $8{,}64$ & $10{,}53$ & $12{,}09$ & $15{,}03$ & $16{,}36$ \\
9 & $8{,}36$ & $10{,}92$ & $11{,}50$ & $15{,}41$ & $15{,}94$ \\
10 & $7{,}31$ & $11{,}08$ & $11{,}88$ & $15{,}11$ & $16{,}60$ \\ \hline
\end{tabular}
\end{table}

A partir das repetições, calculou-se o tempo médio $\bar{t}_{20}$, o desvio padrão da média $\sigma_{\bar{t}}$, o período individual de uma oscilação $T = \frac{\bar{t}_{20}}{20}$ e o quadrado do período $T^2$, compilados na Tabela 3.

\begin{table}[htbp]
\centering
\caption{Tratamento estatístico dos dados dinâmicos (período $T$ e $T^2$).}
\label{tab:dinamico_resumo}
\begin{tabular}{ccccc}
\hline
\textbf{Massa $m$ (g)} & \textbf{Tempo médio $\bar{t}_{20}$ (s)} & \textbf{Período $T$ (s)} & \textbf{Incerteza $\sigma_T$ (s)} & \textbf{$T^2$ ($\text{s}^2$)} \\ \hline
$60{,}0 \pm 0{,}6$ & $8{,}35 \pm 0{,}39$ & $0{,}417$ & $0{,}019$ & $0{,}174$ \\
$110{,}0 \pm 0{,}8$ & $10{,}69 \pm 0{,}13$ & $0{,}534$ & $0{,}006$ & $0{,}286$ \\
$160{,}0 \pm 1{,}0$ & $12{,}67 \pm 0{,}21$ & $0{,}634$ & $0{,}011$ & $0{,}401$ \\
$210{,}0 \pm 1{,}1$ & $14{,}81 \pm 0{,}28$ & $0{,}741$ & $0{,}014$ & $0{,}549$ \\
$260{,}0 \pm 1{,}3$ & $16{,}36 \pm 0{,}11$ & $0{,}818$ & $0{,}005$ & $0{,}669$ \\ \hline
\end{tabular}
\end{table}

A Figura 3 apresenta o gráfico de dispersão de $T^2 \times m$ com as respectivas barras de erro e a reta ajustada por regressão linear.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{grafico_metodo_dinamico.png}
\caption{Gráfico de linearização $T^2 \times m$ e reta de ajuste linear pelo método dinâmico.}
\label{fig:dinamico}
\end{figure}

### Análise e Discussão do Método Dinâmico (Roteiro Teórico e de Resultados)

> **Roteiro para a redação da sua análise:**
>
> 1. **Análise dos Tempos Medidos e Tratamento de Outliers:**
>    - Discuta a variabilidade das medições. Note que na 1ª tomada com $60\text{ g}$, o valor medido foi $11{,}52\text{ s}$, discrepante da média ($\approx 8{,}0\text{ s}$).
>    - Atribua esse desvio a fatores operacionais (tempo de reação do operador ao disparar/parar o cronômetro ou contagem de ciclos adicionais de oscilação).
>
> 2. **Linearização Teórica e Ajuste Gráfico ($T^2 \times m$):**
>    - **Fundamentação teórica:** A equação teórica do período do MHS é $T = 2\pi\sqrt{\frac{m}{k}}$. Ao elevar ao quadrado, obtém-se $T^2 = \left(\frac{4\pi^2}{k}\right) m$.
>    - **Resultado obtido:** O ajuste linear forneceu a reta $T^2 = (2{,}5060 \pm 0{,}0706)\,m + (0{,}0148 \pm 0{,}0123)$ com $R^2 = 0{,}9976$.
>    - A forte linearidade confirma que o período independe da amplitude para pequenas oscilações (propriedade do **isocronismo**).
>
> 3. **Cálculo da Constante Elástica Dinâmica ($k_{\text{din}}$):**
>    - A partir do coeficiente angular $a = 2{,}5060\text{ s}^2/\text{kg}$:
>      $$k_{\text{din}} = \frac{4\pi^2}{a} = \frac{4\pi^2}{2{,}5060} = (15{,}75 \pm 0{,}44)\text{ N/m}$$
>    - A incerteza foi calculada por $\sigma_k = \frac{4\pi^2}{a^2}\sigma_a$.
>
> 4. **Massa Efetiva da Mola (Significado Físico do Intercepto $b$):**
>    - Na modelagem ideal (mola de massa desprezível), a reta cruzaria a origem ($b = 0$).
>    - Na realidade, a mola possui massa finita $m_{\text{mola}}$ e suas espiras também oscilam. A teoria da mecânica clássica estabelece que a massa efetiva oscilante é $m_{\text{ef}} \approx \frac{1}{3} m_{\text{mola}}$.
>    - Relacionando com a equação $T^2 = \frac{4\pi^2}{k}(m + m_{\text{ef}}) = a\cdot m + b$, obtém-se:
>      $$m_{\text{ef}} = \frac{b}{a} = \frac{0{,}0148}{2{,}5060} \approx 0{,}0059\text{ kg} = 5{,}9\text{ g}$$
>    - Explique que o valor positivo do intercepto $b = 0{,}0148\text{ s}^2$ reflete fisicamente essa contribuição da massa própria da mola!
>
> 5. **Comparação e Concordância entre os Métodos:**
>    - Compare os dois valores obtidos:
>      - **Método Estático:** $k_{\text{est}} = (15{,}64 \pm 0{,}33)\text{ N/m}$
>      - **Método Dinâmico:** $k_{\text{din}} = (15{,}75 \pm 0{,}44)\text{ N/m}$
>    - Calcule o erro relativo percentual (discrepância):
>      $$\text{Erro Relativo} = \frac{|15{,}64 - 15{,}75|}{15{,}64} \times 100\% = 0{,}70\%$$
>    - Conclua que a discrepância é inferior a $1\%$ e que os intervalos de incerteza se sobrepõem perfeitamente ($[15{,}31\,;\,15{,}97]\text{ N/m}$ e $[15{,}31\,;\,16{,}19]\text{ N/m}$), comprovando a concordância e a acurácia de ambos os métodos experimentais.

## Simulação Cinemática e Energética do Oscilador

Para aprofundar a análise física do oscilador harmônico (conforme solicitado no item **d** do roteiro da apostila), selecionou-se a massa intermediária $m = 160\text{ g} = 0{,}160\text{ kg}$ acoplada à mola de constante $k = 15{,}70\text{ N/m}$, operando com amplitude típica de oscilação $A = 2{,}0\text{ cm} = 0{,}020\text{ m}$. Os parâmetros dinâmicos calculados para esta configuração foram:
- Frequência angular: $\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{15{,}70}{0{,}160}} \approx 9{,}906\text{ rad/s}$;
- Período de oscilação: $T = \frac{2\pi}{\omega} \approx 0{,}634\text{ s}$.

### Funções Cinemáticas: Deslocamento, Velocidade e Aceleração

A Figura 4 ilustra o comportamento temporal simultâneo do deslocamento $x(t)$, da velocidade $v(t)$ e da aceleração $a(t)$ ao longo de dois períodos completos de oscilação ($2T \approx 1{,}268\text{ s}$).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{grafico_cinematica_mhs.png}
\caption{Curvas cinemáticas $x(t)$, $v(t)$ e $a(t)$ para $m = 160\text{ g}$, $k = 15{,}70\text{ N/m}$ e $A = 2{,}0\text{ cm}$.}
\label{fig:cinematica}
\end{figure}

> **[A FAZER: Redigir a Discussão da Cinemática do MHS]**
>
> *Pontos a abordar na redação:*
> 1. **Defasagens de Fase:**
>    - A velocidade $v(t)$ está adiantada de $\frac{\pi}{2}\text{ rad}$ ($90^\circ$) em relação ao deslocamento $x(t)$. Quando a massa atinge os extremos ($x = \pm A$), a velocidade é nula ($v = 0$). Quando passa pelo equilíbrio ($x = 0$), a velocidade atinge seu valor máximo em módulo ($v_{\text{máx}} = \omega A \approx 19{,}8\text{ cm/s}$).
>    - A aceleração $a(t)$ está em oposição de fase ($\pi\text{ rad}$ ou $180^\circ$) com a posição ($a(t) = -\omega^2 x(t)$). É máxima nos pontos de inversão de movimento ($a_{\text{máx}} = \omega^2 A \approx 1{,}96\text{ m/s}^2$) e nula na posição de equilíbrio.
> 2. **Confronto com as Observações Experimentais:**
>    - Relatar como esse comportamento foi visualmente observado em laboratório (o corpo "para" instantaneamente no topo e na base antes de inverter o sentido do movimento e atinge a velocidade perceptivelmente mais rápida ao cruzar a marca de equilíbrio).

### Balanço e Conservação das Energias ao Longo de um Período

A Figura 5 apresenta a evolução temporal das energias cinética ($E_c$), potencial harmônica efetiva ($E_p$) e mecânica total ($E_m$) ao longo de um ciclo completo de oscilação ($t \in [0, T]$).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{grafico_energias_mhs.png}
\caption{Distribuição e conservação de energia do oscilador ao longo de um período ($T = 0{,}634\text{ s}$).}
\label{fig:energias}
\end{figure}

> **[A FAZER: Redigir a Discussão de Energias do MHS]**
>
> *Pontos a abordar na redação:*
> 1. **Conservação da Energia Mecânica Total:**
>    - A energia mecânica total $E_m = \frac{1}{2}kA^2 = \frac{1}{2}(15{,}70)(0{,}020)^2 = 3{,}14\text{ mJ}$ permanece rigorosamente constante ao longo de todo o tempo.
> 2. **Transformação e Frequência das Energias:**
>    - A energia potencial é máxima nos extremos ($x = \pm A$), onde $E_p = E_m = 3{,}14\text{ mJ}$ e $E_c = 0$.
>    - Na posição de equilíbrio ($x = 0$), toda a energia se converte em cinética ($E_c = 3{,}14\text{ mJ}$ e $E_p = 0$).
>    - Como as funções de energia dependem do quadrado das funções trigonométricas ($\cos^2$ e $\operatorname{sen}^2$), as oscilações de energia ocorrem com o **dobro da frequência angular fundamental** ($2\omega$), completando dois ciclos energéticos a cada período mecânico $T$.

# Conclusão

> **[A FAZER: Redigir a Conclusão final do relatório]**
>
> *Estrutura recomendada para a conclusão:*
> 1. **Validação das Leis Físicas:** Concluir que a Lei de Hooke e o modelo do Movimento Harmônico Simples foram empiricamente validados com coeficientes de correlação linear $R^2 > 0{,}997$.
> 2. **Síntese dos Valores da Constante Elástica:**
>    - Método Estático: $k_{\text{est}} = (15{,}64 \pm 0{,}33)\text{ N/m}$
>    - Método Dinâmico: $k_{\text{din}} = (15{,}75 \pm 0{,}44)\text{ N/m}$
>    - Discrepância percentual: $0{,}70\%$, comprovando excelente concordância experimental.
> 3. **Massa Efetiva da Mola:** Destacar que o intercepto linear do método dinâmico permitiu estimar a massa efetiva oscilante da mola em $m_{\text{ef}} \approx 5{,}9\text{ g}$.
> 4. **Análise de Incertezas e Fontes de Erro:** Citar os principais fatores de dispersão (tempo de reação no cronômetro, erro de paralaxe na leitura da régua milimetrada e amortecimento residual do ar).

# Referências {.unnumbered}

\noindent BOSELLI, M. A.; ALMEIDA, G. F. B. (org.). **Apostila de Laboratório: Oscilações, Ondas e Óptica**. Versão 0.1. Uberlândia: Instituto de Física, Universidade Federal de Uberlândia, 2024. Disponível em: \url{https://moodle.ufu.br/pluginfile.php/1875362/mod_resource/content/1/apostila_OOO_23.pdf}. Acesso em: 25 set. 2026.

\vspace{0.4cm}

\noindent HALLIDAY, D.; RESNICK, R.; WALKER, J. **Fundamentos de Física: Gravitação, Ondas e Termodinâmica**. 10. ed. Rio de Janeiro: LTC, 2016. v. 2.
