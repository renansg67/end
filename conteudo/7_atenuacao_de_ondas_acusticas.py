import streamlit as st

col1, col2, col3 = st.columns([1, 3, 1])

col2.title("Atenuação de ondas acústicas em sólidos")

col2.header("Início")

col2.write("São vários os mecanismos de atenuação de ondas acústicas em sólidos. Neste capítulo será visto inicialmente um abordagem mais generalizada para vários tipos de materiais e os mecanismos de atenuação envolvidos com base em suas características e particularidades. Serão tratados os principais fatores relacionados à atenuação de ondas acústicas em sólidos, em materiais isotrópicos, fontes dispersoras de ondas acústicas, do que o impacto delas depende e materiais com pouca rigidez. Em seguida, numa abordagem focada na madeira, serão apresentadas as bases teóricas para o cálculo do coeficiente de atenuação e, por fim, os fatores que afetam a medida da atenuação, tratando da geometria da amostra e das características do material.")

col2.header("Principais fatores relacionados à atenuação")

col2.write("As ondas sonoras diminuem de intensidade quanto maior a distância em relação à fonte. Deve-se atentar que apesar de nos ensaios envolvendo amostras de pequeno porte a reflexão do feixe ultrassônico aproximá-lo da fonte emissora, a atenuação ocorre da mesma forma, estando associada à distância percorrida. A perda de intensidade geralmente se dá devido ao espalhamento geométrico, dispersão e absorção.")

col2.header("Atenuação em materiais isotrópicos")

col2.write("Em materiais isotrópicos, a atenuação depende das características da fonte irradiante. Ou seja, dependendo do padrão de direcionalidade do feixe ultrassônico do transdutor isso pode alterar o grau de atenuação do feixe. Feixes menos divergentes viajam mais distante no material.")

col2.header("Materiais com fontes dispersoras")

col2.write("Em materiais com dispersores como: fronteiras de grãos, inclusões segregadas e poros de gás, a atenuação ocorre devido a: Reflexão do feixe ultrassônico ao encontrar descontinuidades; redirecionamento parcial do feixe de onda plana coerente ao passar pelo material e dispersão da energia em várias direções.")

col2.header("Impacto das fontes dispersoras")

col2.write("O impacto das fontes de dispersão depende de seu tamanho em relação ao comprimento de onda do feixe ultrassônico. Dispersores menores que o comprimento de onda colaboram menos com a atenuação do sinal. Em dispersores com dimensões próximas do comprimento de onda do feixe emitido pelo transdutor o espalhamento torna-se problemático, havendo maior atenuação do sinal. Para corrigir isso, recomenda-se utilizar fontes com maior comprimento de onda, porém, como consequência há perda de sensibilidade à descontinuidades e de resolução.")

col2.header("Atenuação em materiais com grãos colunares")

col2.write("Alguns materiais com grãos colunares como: compósitos laminados e aços inoxidáveis apresentam comportamento elástico altamente anisotrópico. Neles a atenuação se dá devido às distorções do feixe de onda incidente e mudança de trajetória do feixe decorrente dos caminhos preferenciais existentes, podendo afetar a análise de sinais.")

col2.header("Atenuação em materiais pouco rígidos")

col2.write("Materiais pouco rígidos como: chumbo, plástico e materiais de acoplamento contribuem para maior atenuação do sinal. Neste contexto, a atenuação ocorre devido à conversão de parte da energia mecânica (acústica) em térmica e, devido ao fato da energia na forma de calor ser irrecuperável. Em materiais com essas características, recomenda-se ensaiar amostras com pequena espessura visando minimizar a absorção, principal fenômeno envolvido nesses materiais.")

col2.header("Atenuação na madeira")

col2.write("Em materiais como a madeira, a base teórica da atenuação de ondas acústicas depende do tensor de Christoffel, a partir das equações abaixo")

col2.latex(r"""
\begin{equation}
    [\Gamma^{*}(\omega)-\Lambda^{*}\delta_{ij}]=0\\
\end{equation}
""")

col2.latex(r"""
\begin{equation}
    \begin{bmatrix}
        \Gamma_{11}^{*} - \Lambda^{*} &&\\
        & \Gamma_{22}^{*} - \Lambda^{*} &\\
        && \Gamma_{33}^{*} - \Lambda^{*}
    \end{bmatrix}=0
\end{equation}
""")

col2.markdown("onde o autovalor $\\Lambda^{*}$ é dado por")

col2.latex(r"""
\begin{equation}
    \Lambda^{*}=\dfrac{\rho\nu_{ij}^{2}}{(1-i\alpha_{ij}\nu_{ij}/\omega)^{2}}
\end{equation}
""")

col2.markdown("o mesmo depende do coeficiente de atenuação $\\alpha_{ij}$ característico do material. A técnica de medição da atenuação consiste em calcular o mesmo a partir da equação")

col2.latex(r"""
\begin{equation}
    \alpha_{ij}=-\dfrac{1}{d}\ln\left(\dfrac{A}{A_{0}}\right)
\end{equation}  
""")

col2.write("porém, deve-se levar em consideração os fatores que afetam a medida da atenuação, que são 3 os principais: Natureza da fonte irradiante, absorção e dispersão. O primeiro, como dito anteriormente, depende do transdutor utilizado que, dependendo da divergência do feixe, pode aumentar a atenuação do sinal a partir de fenômenos como a reflexão e refração. Estes dependem das características das fronteiras macroscópicas do meio, enquanto que a dispersão e a absorção dependem das características do material. Dessa forma expandimos nosso análise a esses dois fatores: Geometria da amostra e características do material.")

col2.markdown("A geometria da amostra diz respeito ao seu tamanho e forma. Esses dois elementos influenciam a atenuação das ondas acústicas. Amostras com maior comprimento ($L>50\\,\\text{mm}$) geram maior atenuação do sinal quando comparadas a amostras com comprimento abaixo deste. Quando se analisa o gráfico de amplitude do sinal ultrassônico em função da frequência dos transdutores, nota-se que em amostras de maior comprimento os transdutores apresentam menor frequência central, além de apresentarem decaimento da intensidade do sinal não linear no intervalo entre 0.1 MHz a 0.2 MHz. Para amostras mais curtas, diferente do que foi observado anteriormente, houve aumento na frequência central dos transdutores e decaimento linear na intensidade do sinal no mesmo intervalo de frequências.")

col2.write("Quando se trata do efeito decorrente das características do material nota-se que o tipo de onda propagada e a direção de propagação, dependendo da anisotropia do material, podem atenuar o sinal de diferentes formas. Nota-se que, na madeira, a direção longitudinal é a que apresenta menor coeficiente de atenuação quando se propaga ondas longitudinais. Todavia, quando se propaga o mesmo modo de onda no mesmo intervalo de frequências, a direção com maior atenuação é a tangencial. Outro aspecto relevante é que quando se propaga ondas transversais ou de cisalhamento, não há correlação entre o coeficiente de atenuação obtido e a direção de ensaio. Além disso, tanto para ondas longitudinais como transversais há aumento da atenuação quando aumenta-se a frequência do feixe ultrassônico.")

col2.write("É importante notar que os diferentes coeficientes de atenuação observados para cada direção das amostras em madeira dependem diretamente das características macroscópicas do meio como a disposição das fibras e partes que compõem a madeira. Na direção longitudinal nota-se a maior quantidade de elementos paralelos entre si, apresentando organização adequada à propagação de ondas longitudinais, como as fibras, parênquimas axiais e vasos condutores (plano RT). Quando mudamos para o plano de observação LT nota-se um comportamento parcialmente similar. Alguns elementos possuem paralelismos entre si, porém em menor quantidade em relação ao que é visto no plano RT. Neste novo plano é possível ver a seção transversal dos parênquimas radiais e as fibras. Ambos estão dispostos ortogonalmente entre si. Nesse caso, pode-se dizer que os parênquimas radiais estão a favor da propagação de ondas longitudinais por concordarem com a direção de propagação. O mesmo não pode ser dito das fibras neste caso, já que as mesmas estão dispostas ortogonalmente à direção de propagação. O último plano que pode ser analisado, o LR, é o que apresenta menos elementos que favorecem a propagação de ondas acústicas longitudinais. Nele, os parênquimas radiais são vistos lateralmente enquanto as fibras são mostradas ortogonais aos últimos. Porém, nessa disposição, tanto os parênquimas radiais quanto aos fibras são ortogonais à direção de propagação no plano LR, concordando com os maiores coeficientes de atenuação obtidos.")

col2.write("Outros fatores, também relacionados à atenuação que foram mencionados na seção anterior, dizem respeito à temperatura e à umidade da amostra. Nota-se que a rigidez do material e inversamente proporcional a ambas as grandezas, dessa forma, nota-se redução na velocidade de propagação do pulso ultrassônico ao aumentá-las.")

col2.write("Outra análise relevante foi feita, associada à propagação de ondas acústicas de cisalhamento em amostras com diferentes larguras dos anéis de crescimento. Nota-se que na direção radial, quando se aumenta largura dos anéis, há baixa correlação entre esse aumento e a alteração da velocidade de propagação, com ela tendendo a permanecer constante. Entretanto, na direção tangencial, ao aumentar a largura dos anéis, as ondas de cisalhamento apresentaram aumento de velocidade de propagação.")

