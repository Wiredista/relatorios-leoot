---
title: Relatório de Experimento - Lei de Hooke e Oscilações
author: |-
  \begin{tabular}{cc}
    Álvaro Antônio de Lacerda Rosário & RA: 12521ETE001 \\
    Ana Clara Pereira da Silva & RA: 12511ETE011 \\
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
  - \pretitle{\begin{center}\includegraphics[width=10cm]{logo-infis.png}\\[2cm]\LARGE\bfseries}
  - \posttitle{\end{center}}
  - \preauthor{\begin{center}\large}
  - \postauthor{\end{center}}
  - \predate{\vfill\begin{center}\large Uberlândia -- MG\\[0.3cm]}
  - \postdate{\end{center}\newpage}
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
date: '`\today`{=latex}'
toc-title: Sumário
---

# Resumo {.unnumbered}

O presente relatório investiga o comportamento mecânico de uma mola helicoidal suspensa verticalmente acoplada a massas calibradas, visando validar experimentalmente a Lei de Hooke e o modelo teórico do Movimento Harmônico Simples (MHS), além de determinar a constante elástica $k$ do sistema. A metodologia experimental estruturou-se em duas abordagens complementares: o método estático, baseado na medição da deformação vertical sob diferentes cargas suspensas, e o método dinâmico, baseado na cronometragem dos períodos de oscilação do MHS para cinco configurações de massa. Os ajustes lineares por mínimos quadrados resultaram em $k_{\text{est}} = (15{,}64 \pm 0{,}33)\text{ N/m}$ ($R^2 = 0{,}9982$) e $k_{\text{din}} = (15{,}75 \pm 0{,}44)\text{ N/m}$ ($R^2 = 0{,}9976$), revelando uma discrepância relativa de apenas $0{,}70\%$. A análise do intercepto linear dinâmico permitiu ainda estimar a massa efetiva oscilante da mola em $m_{\text{ef}} \approx 5{,}9\text{ g}$. O balanço analítico de energias mecânicas confirmou a conservação da energia mecânica total ($E_m = 3{,}14\text{ mJ}$) e a alternância contínua entre energia cinética e potencial harmônica com o dobro da frequência fundamental. Os resultados obtidos comprovam com elevada precisão a linearidade elástica do oscilador e a plena equivalência física e estatística entre os métodos estático e dinâmico.

\noindent **Palavras-chave:** Lei de Hooke. Sistema massa-mola. Constante elástica. Movimento Harmônico Simples. Conservação de energia.

\newpage

# Abstract {.unnumbered}

This report investigates the mechanical behavior of a vertically suspended helical spring coupled to calibrated masses, aiming to experimentally validate Hooke's Law and the theoretical Simple Harmonic Motion (SHM) model, as well as to determine the spring constant $k$ of the system. The experimental procedure was structured into two complementary approaches: the static method, based on measuring vertical elongation under different loads, and the dynamic method, based on timing the oscillation periods of SHM for five mass configurations. Linear regression fits via least squares yielded $k_{\text{est}} = (15.64 \pm 0.33)\text{ N/m}$ ($R^2 = 0.9982$) and $k_{\text{din}} = (15.75 \pm 0.44)\text{ N/m}$ ($R^2 = 0.9976$), showing a relative discrepancy of only $0.70\%$. Furthermore, analyzing the dynamic linear intercept enabled estimating the effective oscillating mass of the spring as $m_{\text{ef}} \approx 5.9\text{ g}$. The analytical energy balance confirmed the conservation of total mechanical energy ($E_m = 3.14\text{ mJ}$) and the continuous exchange between kinetic and harmonic potential energy at twice the fundamental angular frequency. The results demonstrate with high accuracy the elastic linearity of the oscillator and the physical and statistical equivalence between the static and dynamic methods.

\noindent **Keywords:** Hooke's Law. Mass-spring system. Spring constant. Simple Harmonic Motion. Energy conservation.

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
\includegraphics[width=0.4\textwidth]{r1_fig1.jpg}
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

### Análise e Discussão do Método Estático

A partir dos dados experimentais dispostos na Tabela 1 e do comportamento gráfico ilustrado na Figura 2, analisa-se a condição de equilíbrio estático entre a força peso e a força elástica restauradora exercida pela mola ($P = F_e \implies mg = k\Delta x$). Isolando a elongação em função da massa total suspensa, obtém-se a relação teórica linear:

\begin{equation}
\Delta x = \left(\frac{g}{k}\right) m
\end{equation}

A aplicação do método dos mínimos quadrados sobre os pontos experimentais forneceu a seguinte equação ajustada:
\begin{equation}
\Delta x = (0{,}6254 \pm 0{,}0133)\,m - (0{,}0073 \pm 0{,}0021)
\end{equation}
com coeficiente de determinação $R^2 = 0{,}9982$. O elevado valor de $R^2$ (superior a $0{,}998$) atesta empiricamente a estrita proporcionalidade direta entre a força aplicada e a deformação da mola, validando a Lei de Hooke para todo o domínio de massas testado ($10\text{ g}$ a $260\text{ g}$).

Identificando o coeficiente angular da reta ajustada como $a = \frac{g}{k_{\text{est}}}$ e considerando a aceleração da gravidade local de Uberlândia ($g = 9{,}784\text{ m/s}^2$), determina-se a constante elástica estática:
\begin{equation}
k_{\text{est}} = \frac{g}{a} = \frac{9{,}784}{0{,}6254} = (15{,}64 \pm 0{,}33)\text{ N/m}
\end{equation}
onde a incerteza associada foi propagada através da relação $\sigma_{k_{\text{est}}} = \left(\frac{g}{a^2}\right)\sigma_a$.

O coeficiente linear obtido ($b = -7{,}3 \pm 2{,}1\text{ mm}$) apresenta um pequeno desvio em relação à origem teórica ($b = 0$), atribuído ao assentamento inicial das espiras da mola sob o peso do suporte de massas e a folgas mecânicas no ponto de fixação da haste. Adicionalmente, verificou-se a preservação da integridade estrutural do sistema: após a remoção completa de todas as massas ao final do experimento, a mola retornou exatamente à sua posição inicial de repouso ($x_0 = 460{,}0\text{ mm}$), comprovando que as deformações ocorreram estritamente dentro do limite elástico do material, sem qualquer deformação plástica residual.

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

### Análise e Discussão do Método Dinâmico

A análise dos tempos experimentais coletados (Tabela 2) e dos períodos processados (Tabela 3) evidencia a consistência do comportamento dinâmico do sistema. A dispersão observada entre as repetições reflete principalmente o tempo de reação humano no disparo e travamento do cronômetro manual, além de pequenas oscilações laterais residuais, sendo adequadamente tratada pela propagação combinada do desvio-padrão da média com a incerteza instrumental ($\sigma_{\text{inst}} = 0{,}01\text{ s}$).

A modelagem teórica do Movimento Harmônico Simples estabelece que o período de oscilação para uma mola ideal é dado por $T = 2\pi\sqrt{\frac{m}{k}}$. Elevando ambos os membros ao quadrado, obtém-se a relação de linearização:

\begin{equation}
T^2 = \left(\frac{4\pi^2}{k}\right) m
\end{equation}

A regressão linear por mínimos quadrados aplicada aos pares $(m, T^2)$ da Tabela 3 produziu a reta de ajuste apresentada na Figura 3:
\begin{equation}
T^2 = (2{,}5060 \pm 0{,}0706)\,m + (0{,}0148 \pm 0{,}0123)
\end{equation}
com coeficiente de determinação $R^2 = 0{,}9976$. A forte correlação linear obtida comprova empiricamente a propriedade do **isocronismo** das pequenas oscilações harmônicas, demonstrando que o período depende unicamente da inércia do sistema e da rigidez da mola, permanecendo independente da amplitude de oscilação.

Identificando o coeficiente angular da reta ajustada como $a = \frac{4\pi^2}{k_{\text{din}}}$, calcula-se a constante elástica dinâmica:
\begin{equation}
k_{\text{din}} = \frac{4\pi^2}{a} = \frac{4\pi^2}{2{,}5060} = (15{,}75 \pm 0{,}44)\text{ N/m}
\end{equation}
sendo a incerteza calculada por $\sigma_{k_{\text{din}}} = \left(\frac{4\pi^2}{a^2}\right)\sigma_a$.

Ademais, a análise do coeficiente linear ($b = 0{,}0148 \pm 0{,}0123\text{ s}^2$) revela um aspecto físico fundamental. Em um modelo puramente ideal (mola de massa nula), a reta deveria cruzar a origem ($b = 0$). No entanto, como a mola real possui massa finita $m_{\text{mola}}$, suas espiras também participam do movimento oscilatório com velocidades que variam linearmente do suporte fixo até a extremidade livre. A mecânica clássica demonstra que a inércia efetiva adicional introduzida pela mola equivale a $m_{\text{ef}} \approx \frac{1}{3} m_{\text{mola}}$, de modo que a equação do período assume a forma $T^2 = \frac{4\pi^2}{k}(m + m_{\text{ef}}) = a\cdot m + b$. A partir dessa relação, determina-se a massa efetiva da mola:
\begin{equation}
m_{\text{ef}} = \frac{b}{a} = \frac{0{,}0148}{2{,}5060} \approx 0{,}0059\text{ kg} = (5{,}9 \pm 4{,}9)\text{ g}
\end{equation}
O valor positivo do intercepto reflete com clareza a contribuição inercial da massa própria da mola no período de oscilação.

### Comparação entre os Métodos Estático e Dinâmico

Confrontando os valores obtidos para a constante elástica da mesma mola helicoidal:
- **Método Estático:** $k_{\text{est}} = (15{,}64 \pm 0{,}33)\text{ N/m}$
- **Método Dinâmico:** $k_{\text{din}} = (15{,}75 \pm 0{,}44)\text{ N/m}$

Calcula-se a discrepância percentual relativa entre as duas determinações:
\begin{equation}
\text{Discrepância} = \frac{|k_{\text{est}} - k_{\text{din}}|}{k_{\text{est}}} \times 100\% = \frac{|15{,}64 - 15{,}75|}{15{,}64} \times 100\% = 0{,}70\%
\end{equation}

A discrepância de apenas $0{,}70\%$ — amplamente inferior a $1\%$ — aliada à sobreposição integral dos intervalos de incerteza experimental ($[15{,}31\,;\,15{,}97]\text{ N/m}$ e $[15{,}31\,;\,16{,}19]\text{ N/m}$), comprova com rigor a concordância física, a acurácia das medições e a perfeita equivalência entre a resposta estática (Lei de Hooke) e a resposta dinâmica (MHS) do oscilador.

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

Observando as curvas da Figura 4, nota-se que todas as grandezas cinemáticas são descritas por funções harmônicas trigonométricas interligadas por defasagens de fase bem definidas. Para facilitar a interpretação física, traçaram-se linhas verticais tracejadas nos instantes notáveis correspondentes aos múltiplos de um quarto de período ($t = k\frac{T}{4}$, com $k \in \mathbb{N}$), nos quais a massa atinge os extremos de oscilação ($x = \pm A$) ou cruza a posição de equilíbrio ($x = 0$):

1. **Instantes nos extremos de deslocamento ($x = \pm A$, em $t = 0, \frac{T}{2}, T, \dots$):**
   - A velocidade do corpo anula-se instantaneamente ($v = 0$) para possibilitar a inversão no sentido do movimento, exatamente como observado a olho nu durante a prática de laboratório.
   - Concomitantemente, a aceleração atinge seu valor máximo em módulo ($|a_{\text{máx}}| = \omega^2 A \approx 1{,}96\text{ m/s}^2$).

2. **Instantes na posição de equilíbrio ($x = 0$, em $t = \frac{T}{4}, \frac{3T}{4}, \dots$):**
   - A velocidade atinge sua magnitude máxima ($|v_{\text{máx}}| = \omega A \approx 19{,}8\text{ cm/s}$), enquanto a aceleração torna-se rigorosamente nula ($a = 0$).
   - Este resultado frequentemente causa estranheza à intuição inicial, pela dificuldade comum em separar visualmente velocidade de aceleração. No entanto, a explicação torna-se evidente ao analisar a dinâmica newtoniana: como $a = \frac{F_{\text{res}}}{m}$ e a força restauradora líquida obedece à Lei de Hooke ($F_{\text{res}}(x) = -kx$), na posição de equilíbrio a força resultante é nula ($F_{\text{res}}(0) = 0$), implicando obrigatoriamente que a aceleração deve ser nula ($a = 0$), mesmo que o corpo esteja se movendo em velocidade máxima.

\noindent A consistência matemática dessas relações decorre da própria estrutura do cálculo diferencial. Partindo da função posição $x(t) = A\cos(\omega t + \phi_0)$ e derivando-a sucessivamente em relação ao tempo, obtêm-se:
\begin{align}
v(t) &= \frac{dx}{dt} = -A\omega\operatorname{sen}(\omega t + \phi_0) = A\omega\cos\left(\omega t + \phi_0 + \frac{\pi}{2}\right) \\
a(t) &= \frac{dv}{dt} = \frac{d^2x}{dt^2} = -A\omega^2\cos(\omega t + \phi_0) = -\omega^2 x(t) = A\omega^2\cos(\omega t + \phi_0 + \pi)
\end{align}

\noindent Revela-se aqui uma admirável harmonia entre a física e a matemática: enquanto a velocidade sofre um adiantamento de fase de $90^\circ$ ($\frac{\pi}{2}\text{ rad}$), a aceleração sofre uma rotação de fase de $180^\circ$ ($\pi\text{ rad}$), tornando-se a própria função posição refletida e reescalada por $-\omega^2$. A matemática do cálculo diferencial não apenas prevê que a aceleração é máxima quando a posição é máxima, mas também impõe, com o sinal negativo, a exigência mecânica fundamental de que a aceleração deve sempre apontar no sentido oposto ao deslocamento — confirmando, com elegância teórica, a natureza puramente restauradora da mola.

### Balanço e Conservação das Energias ao Longo de um Período

A Figura 5 apresenta a evolução temporal das energias cinética ($E_c$), potencial harmônica efetiva ($E_p$) e mecânica total ($E_m$) ao longo de um ciclo completo de oscilação ($t \in [0, T]$).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{grafico_energias_mhs.png}
\caption{Distribuição e conservação de energia do oscilador ao longo de um período ($T = 0{,}634\text{ s}$).}
\label{fig:energias}
\end{figure}

Analisando o comportamento energético do sistema, observa-se a conservação da energia mecânica total ($E_m$). Utilizando o valor médio da constante elástica ($k \approx 15{,}70\text{ N/m}$) e a amplitude de oscilação $A = 0{,}020\text{ m}$, a energia mecânica total do sistema é dada por:

\begin{equation}
E_m = \frac{1}{2} k A^2 = \frac{1}{2} (15{,}70)(0{,}020)^2 = 3{,}14\text{ mJ}
\end{equation}

Este valor permanece rigorosamente constante ao longo do tempo, caracterizando um sistema conservativo ideal.

Ao longo do ciclo de oscilação, ocorre uma conversão contínua entre a energia potencial elástica harmônica ($E_p$) e a energia cinética ($E_c$):
- **Nos extremos do movimento ($x = \pm A$):** O corpo para instantaneamente para inverter o sentido do movimento ($v = 0$), zerando a energia cinética ($E_c = 0$). Consequentemente, toda a energia do sistema se encontra armazenada sob a forma de energia potencial elástica, de modo que $E_p = E_m = 3{,}14\text{ mJ}$.
- **Na posição de equilíbrio ($x = 0$):** A deformação em relação ao ponto de equilíbrio é nula ($E_p = 0$) e o corpo atinge sua velocidade máxima ($v_{\text{máx}}$). Nesse ponto, atinge-se a totalidade da energia sob a forma de energia cinética ($E_c = 3{,}14\text{ mJ}$).

A energia potencial depende de $\cos^2(\omega t + \phi_0)$ e a energia cinética de $\operatorname{sen}^2(\omega t + \phi_0)$. Por dependerem do quadrado das funções trigonométricas, essas energias variam com o dobro da frequência angular fundamental ($2\omega$). Isso implica que o sistema completa dois ciclos completos de conversão energética a cada período mecânico $T$ da oscilação do corpo.

# Conclusão

A análise experimental apresentada permitiu a validação da Lei de Hooke e do Movimento Harmônico Simples através dos coeficientes de determinação $R^2 > 0{,}997$ obtidos pelos ajustes lineares.

Os valores da constante elástica obtidos pelo Método Estático, $(15{,}64 \pm 0{,}33)\text{ N/m}$, e pelo Método Dinâmico, $(15{,}75 \pm 0{,}44)\text{ N/m}$, apresentaram excelente concordância experimental com apenas $0{,}70\%$ de discrepância percentual, confirmando a compatibilidade entre as duas metodologias.

Também foi realizada a análise do intercepto linear no método dinâmico, resultando na estimativa da massa efetiva oscilante da mola no valor de $m_{\text{ef}} \approx 5{,}9\text{ g}$. Este resultado evidencia a importância da contribuição da inércia própria da mola no comportamento do sistema.

Por fim, os principais fatores associados às incertezas e erros experimentais foram o tempo de reação no acionamento do cronômetro manual, o erro de paralaxe nas leituras da régua milimetrada e o efeito de amortecimento residual devido à resistência do ar sobre o corpo em oscilação. Apesar dessas fontes de erro, a precisão alcançada comprova de forma consistente os conceitos abordados na teoria.

# Referências {.unnumbered}

\noindent BOSELLI, M. A.; ALMEIDA, G. F. B. (org.). **Apostila de Laboratório: Oscilações, Ondas e Óptica**. Versão 0.1. Uberlândia: Instituto de Física, Universidade Federal de Uberlândia, 2024. Disponível em: \url{https://moodle.ufu.br/pluginfile.php/1875362/mod_resource/content/1/apostila_OOO_23.pdf}. Acesso em: 25 set. 2026.

\vspace{0.4cm}

\noindent HALLIDAY, D.; RESNICK, R.; WALKER, J. **Fundamentos de Física: Gravitação, Ondas e Termodinâmica**. 10. ed. Rio de Janeiro: LTC, 2016. v. 2.

# Declaração de Uso de Inteligência Artificial {.unnumbered}

Em conformidade com o documento institucional *Recomendações para o Uso e Desenvolvimento Ético e Responsável de Inteligência Artificial na Universidade Federal de Uberlândia* (Item 4.1.3), declara-se que a ferramenta de IA **Antigravity (Google DeepMind / Gemini)** foi utilizada exclusivamente como suporte computacional para:

1. **Tratamento Estatístico e Automação Numérica:** Desenvolvimento de scripts em Python para cálculo de médias, propagação de incertezas instrumentais e estatísticas, e regressões lineares pelos métodos estático e dinâmico.
2. **Visualização de Dados:** Geração dos gráficos experimentais ($\Delta x \times m$ e $T^2 \times m$) e das curvas de simulação temporal teórica do MHS ($x, v, a$ e balanço de energias).
3. **Tipografia e Sintaxe:** Formatação estrutural do modelo em Markdown/LaTeX nas normas ABNT, ajuste dimensional de tabelas e automação de compilação via Pandoc/PDFLaTeX.

\noindent Ressalta-se que **a redação do relatório, formulação de hipóteses, interpretação física dos resultados, discussões e conclusões foram desenvolvidas exclusivamente pelos alunos do grupo**, limitando-se a intervenção textual da IA a revisões gramaticais, pontuação e sintaxe de equações em LaTeX. Todos os cálculos e gráficos gerados foram validados pelo grupo.
