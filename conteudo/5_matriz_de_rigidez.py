import streamlit as st

col1, col2, col3 = st.columns([1, 3, 1])

col2.title("Bases teóricas para obtenção da matriz de rigidez por método de propagação de ondas")

col2.header("Início")

col2.write("As bases teóricas envolvidas na obtenção da matriz de rigidez depende do tipo de material analisado, tendo em vista que ele pode apresentas comportamento elástico distinto em diferentes direções. O capítulo relacionado à atenuação de ondas acústicas em sólidos discute com maior ênfase os diferentes fatores que podem afetar a propagação de ondas acústicas e modificar a sua velocidade ao passar pelo material. Dessa forma, torna-se fundamental entender as características do tipo de material ensaiado visando adequar o tamanho, a forma e o tipo de transdutores utilizados. Diversos estudos foram realizados para avaliação do método de propagação de ondas na avaliação das propriedades de rigidez de um material. É sabido que existe uma correlação entre os coeficientes de rigidez em determinadas direções e as propriedades de resistência e rigidez dos materiais. Prova disso, são os ensaios realizados em amostras de madeira em forma de barra, onde são propagados pulsos ultrassônicos na direção longitudinal e, com o valor da densidade $\\rho$ calcula-se o coeficiente de rigidez definido por")

col2.latex(r"C_{LL}=\rho V_{LL}^{2}")

col2.write("Todavia esse método é restrito somente a algumas condições tendo em vista que o comportamento elástico altamente anisotrópico da madeira dificulta a relação do coeficiente de rigidez em outras direções.")

col2.write("Sabe-se que a rigidez é uma propriedade relacionada à dificuldade de um corpo deformar quando submetido a um carregamento, seja de compressão, tração, cisalhamento ou flexão. A lei de Hooke generalizada, define que um estado tridimensional de tensões em formato cúbico de material isotrópico, quando submetido a esforços de tensão normal e cisalhamento em todas as faces, tem as seguintes deformações específicas em diferentes direções e planos")

col2.latex(r'''
    \begin{array}{rcl}
        \epsilon_{x}&=&\dfrac{1}{E}[\sigma_{x}-\nu(\sigma_{y}+\sigma_{z})]\\
        \epsilon_{y}&=&\dfrac{1}{E}[\sigma_{y}-\nu(\sigma_{x}+\sigma_{z})]\\
        \epsilon_{z}&=&\dfrac{1}{E}[\sigma_{z}-\nu(\sigma_{x}+\sigma_{y})
    \end{array}
''')
col2.latex(r'''
    \begin{matrix}
        \gamma_{yz}=\dfrac{\tau_{yz}}{G} & \gamma_{zx}=\dfrac{\tau_{zx}}{G} & \gamma_{xy}=\dfrac{\tau_{xy}}{G}
    \end{matrix}
''')

col2.write("enquanto que para materiais ortotrópicos")

col2.latex(r"""
    \begin{array}{rcl}
        \epsilon_{x}&=&\dfrac{\sigma_{x}}{E_{x}}-\dfrac{\nu_{yx}\sigma_{y}}{E_{y}}-\dfrac{\nu_{zx}\sigma_{z}}{E_{z}}\\
        \epsilon_{y}&=&-\dfrac{\nu_{xy}\sigma_{x}}{E_{x}}+\dfrac{\sigma_{y}}{E_{y}}-\dfrac{\nu_{zy}\sigma_{z}}{E_{z}}\\
        \epsilon_{z}&=&-\dfrac{\nu_{xz}\sigma_{x}}{E_{x}}-\dfrac{\nu_{yz}\sigma_{y}}{E_{y}}+\dfrac{\sigma_{z}}{E_{z}}
    \end{array}
""")

col2.latex(r"""
    \begin{matrix}
        \gamma_{yz}=\dfrac{\tau_{yz}}{G_{yz}} & \gamma_{zx}=\dfrac{\tau_{zx}}{G_{yz}} & \gamma_{xy}=\dfrac{\tau_{xy}}{G_{yz}}
    \end{matrix}
""")

col2.write("Na forma matricial, podemos escrever o mesmo conjunto de equações como")

col2.latex(r"""
    \begin{bmatrix}
        \epsilon_{x}\\
        \epsilon_{y}\\
        \epsilon_{z}\\
        \gamma_{yz}\\
        \gamma_{zx}\\
        \gamma_{xy}
    \end{bmatrix}=
    \begin{bmatrix}
        E_{x}^{-1} & -\nu_{yx}/E_{y} & -\nu_{zx}/E_{z} &&&\\
        & E_{y}^{-1} & -\nu_{zy}/E_{z} &&&\\
        & & E_{z}^{-1}& &&\\
        &&& G_{yz}^{-1} &&\\
        &&&& G_{zx}^{-1} &\\
        &&&&& G_{xy}^{-1}
    \end{bmatrix}
    \begin{bmatrix}
        \sigma_{x}\\
        \sigma_{y}\\
        \sigma_{z}\\
        \tau_{yz}\\
        \tau_{zx}\\
        \tau_{xy}
    \end{bmatrix}
""")

col2.write("Note que, a partir do sistema matricial obtido, podemos simplificar sua escrita como")

col2.latex(r"\bm{\epsilon}=\bm{S}\bm{\sigma}")

col2.markdown("onde $\\bm{\\epsilon}$ é o vetor de deformações específicas, $\\bm{S}$ é a matriz *compliance* e $\\bm{\\sigma}$ é o vetor de tensões. Isolando o vetor de tensões, chega-se que")

col2.latex(r"\bm{\sigma}=\bm{C}\bm{\epsilon}")

col2.markdown("consequentemente conclui-se que $\\bm{S}=\\bm{C}^{-1}$, onde $\\bm{C}$ é a matriz de rigidez.")

col2.header("Materiais isotrópicos")

col2.subheader("Matriz de rigidez")

col2.markdown("Quando lidamos com a matriz de rigidez para materiais isotrópicos, temos que levar em conta as simetrias envolvidas no material e como suas propriedades variam em diferentes direções. A matriz de rigidez nesse caso é simplificada e depende de somente 3 coeficientes de rigidez do material ($C_{11}$, $C_{12}$ e $C_{44}$), como é mostrado a seguir")

col2.latex(r"""
    C=\begin{bmatrix}
        C_{11} & C_{12} & C_{12} & & &\\ & C_{11} & C_{12} & & &\\
        & & C_{11} & & &\\
        & & & C_{44} & & \\
        & & & & C_{44} & \\
        & & & & & C_{44}\\
    \end{bmatrix}
""")

col2.write("em termos das velocidade de propagação das ondas longitudinais e transversais")

col2.latex(r"""
C=\rho\begin{bmatrix}
    V_{11}^{2} & V_{12}^{2} & V_{12}^{2} & & &\\ 
    & V_{11}^{2} & V_{12}^{2} & & &\\
    & & V_{11}^{2} & & &\\
    & & & V_{44}^{2} & & \\
    & & & & V_{44}^{2} & \\
    & & & & & V_{44}^{2}\\
\end{bmatrix}
""")

col2.subheader("Matriz de flexibilidade")

col2.latex(r"""
S=\begin{bmatrix}
    S_{11} & S_{12} & S_{12} & & &\\ & S_{11} & S_{12} & & &\\
    & & S_{11} & & &\\
    & & & S_{44} & & \\
    & & & & S_{44} & \\
    & & & & & S_{44}\\
\end{bmatrix}
""")

col2.markdown("se expandirmos esses coeficientes, temos que tanto o módulo de elasticidade longitudinal quanto o transversal e o coeficiente de Poisson independem da direção assumida. Dessa forma, em termos das propriedades elásticas do material, ele só depende de $\\nu$, $E$ e $G$ na matriz *compliance* $\\bm{S}$")

col2.latex(r"""
S=\begin{bmatrix}
    \dfrac{1}{E} & -\dfrac{\nu}{E} & -\dfrac{\nu}{E} & & &\\ 
    & \dfrac{1}{E} & -\dfrac{\nu}{E} & & &\\
    & & \dfrac{1}{E} & & &\\
    & & & \dfrac{1}{G} & & \\
    & & & & \dfrac{1}{G} & \\
    & & & & & \dfrac{1}{G}\\
\end{bmatrix}
""")

col2.header("Materiais isotrópicos transversais")

col2.write("Quando lidamos com materiais isotrópicos transversais, é necessário levar em consideração para a construção da matriz de rigidez a orientação do plano de isotropia, ou seja, em qual plano as propriedades do material são constantes quando as analisamos num sistema de dois eixos pertencentes ao plano formando um ângulo reto entre si. Nesse caso, dependendo do plano de isotropia e do referencial adotado para a simetria, é possível chegar em três matrizes de rigidez conforme será mostrado.")

col2.subheader("Plano 12 de isotropia")

col2.markdown("##### Matriz de rigidez")

col2.markdown("Neste plano, para entendimento da matriz de rigidez, é preciso definir com as deformações variam em diferentes direções, com base na matriz de rigidez $\\bm{S}$ e a partir dela, estender os índices obtidos em termos dos elementos da matriz $\\bm{C}$. Nesse caso, como a isotropia ocorre no plano 12, temos que o módulo de elasticidade longitudinal em ambas as direções é igual. Portanto $C_{11}=C_{22}$. Já na direção 33 o coeficiente de rigidez varia em relação aos anteriores, dessa forma escreve-se $C_{33}$ para destacar o valor distinto. Quando analisamos os temos $C_{44}$, $C_{55}$ e $C_{66}$, associados à propagação de ondas de cisalhamento em função da dependência das velocidades, ao ter em mente que o termo $C_{44}$ possui associação com o termo $S_{44}$ da matriz \textit{compliance} indiretamente, e que este por sua vez, tem relação com o módulo de elasticidade transversal $G_{23}$, se considerarmos que as propriedades do material são igual no plano 12 e considerando componentes de tensão de cisalhamento iguais, ou seja, $\\tau=\\tau_{31}=\\tau_{32}$, temos que")

col2.latex(r"G_{31}\gamma_{31}=G_{32}\gamma_{32}")

col2.markdown("Além disso, restam os termos em função dos coeficientes de Poisson relacionados à matriz $\\bm{S}$ que podem ser associados aos de $\\bm{C}$. Na matriz $\\bm{S}$, as linhas 1 e 2 da matriz estão associadas à parcelas de deformação em diferentes direções considerando um estado de tensão em 3 dimensões com tensões normais e de cisalhamento atuantes ao mesmo tempo. Dessa forma, se considerarmos que ao aplicar uma tensão normal na direção 3, devido à isotropia no plano 12, espera-se que o material apresente $\\nu=\\nu_{31}=\\nu_{32}$. Como $\\nu_{31}$ e $\\nu_{32}$ estão associados à $S_{13}$ e $S_{23}$, respectivamente, e a matriz $\\bm{S}$ é simétrica em relação a diagonal principal, podemos afirmar que $S_{13}=S_{23}=S_{31}=S_{32}$. Dessa forma, $C_{13}=C_{23}=C_{31}=C_{32}$. O termo faltante, $C_{12}$ está associado ao termo $S_{12}$, sendo distinto dos anteriores e simétrico em relação a $C_{21}$, devido a isso os termos abaixo da diagonal principal não foram reescritos, conforme mostra a matriz de rigidez abaixo")

col2.latex(r"""
C=\begin{bmatrix}
    C_{11} & C_{12} & C_{13} & & &\\
    & C_{11} & C_{13} & & &\\
    & & C_{33} & & &\\
    & & & C_{44} & & \\
    & & & & C_{44} & \\
    & & & & & (C_{11}-C_{12})/2\\
\end{bmatrix}
""")

col2.markdown("##### Matriz de flexibilidade")

col2.latex(r"""
S=\begin{bmatrix}
    S_{11} & S_{12} & S_{13} & & &\\
    & S_{11} & S_{13} & & &\\
    & & S_{33} & & &\\
    & & & S_{44} & & \\
    & & & & S_{44} & \\
    & & & & & 2(S_{11}-S_{12})\\
\end{bmatrix}
""")

col2.write("Nota-se que a matriz possui 5 coeficientes de rigidez independentes ($C_{11}$, $C_{33}$, $C_{44}$, $C_{12}$ e $C_{13}$).")

col2.subheader("Plano 13 de isotropia")

col2.markdown("##### Matriz de rigidez")

col2.latex(r"""
C=\begin{bmatrix}
    C_{11} & C_{12} & C_{13} & & &\\
    & C_{22} & C_{12} & & &\\
    & & C_{11} & & &\\
    & & & C_{44} & & \\
    & & & & (C_{11}-C_{13})/2 & \\
    & & & & & C_{44}\\
\end{bmatrix}
""")

col2.markdown("##### Matriz de flexibilidade")

col2.latex(r"""
S=\begin{bmatrix}
    S_{11} & S_{12} & S_{13} & & &\\
    & S_{22} & S_{12} & & &\\
    & & S_{11} & & &\\
    & & & S_{44} & & \\
    & & & & 2(S_{11}-S_{13}) & \\
    & & & & & S_{44}\\
\end{bmatrix}
""")

col2.subheader("Plano 23 de isotropia")

col2.markdown("##### Matriz de rigidez")

col2.latex(r"""
C=\begin{bmatrix}
    C_{11} & C_{12} & C_{12} & & &\\
    & C_{22} & C_{13} & & &\\
    & & C_{22} & & &\\
    & & & (C_{22}-C_{23})/2 & & \\
    & & & & C_{55} & \\
    & & & & & C_{55}\\
\end{bmatrix}
""")

col2.markdown("##### Matriz de flexibilidade")

col2.latex(r"""
S=\begin{bmatrix}
    S_{11} & S_{12} & S_{12} & & &\\
    & S_{22} & S_{13} & & &\\
    & & S_{22} & & &\\
    & & & 2(S_{22}-S_{23}) & & \\
    & & & & S_{55} & \\
    & &' & & & S_{55}\\
\end{bmatrix}
""")

col2.header("Materiais ortotrópicos")

col2.subheader("Matriz de rigidez")

col2.write("Para materiais ortotrópicos, observa-se maior complexidade em sua estrutura em relação aos dois tipos de materiais anteriores. Neste caso, há dependência de 9 coeficientes de rigidez.")

col2.latex(r"""
C=\begin{bmatrix}
    C_{11} & C_{12} & C_{13} & & &\\
    & C_{22} & C_{23} & & &\\
    & & C_{33} & & &\\
    & & & C_{44} & & \\
    & & & & C_{55} & \\
    & & & & & C_{66}\\
\end{bmatrix}
""")

col2.write("em termos das velocidades de propagação das ondas longitudinais, transversais, quase longitudinais e quase transversais, temos")

col2.latex(r"""
C=\rho\begin{bmatrix}
    V_{11}^{2} & V_{12}^{2} & V_{13}^{2} &&&\\
    & V_{22}^{2} & V_{23}^{2} &&&\\
    && V_{33}^{2} &&&\\
    &&& V_{44}^{2} &&\\
    &&&& V_{55}^{2} &\\
    &&&&& V_{66}^{2} \\
\end{bmatrix}
""")

col2.subheader("Matriz de flexibilidade")

col2.latex(r"""
S=\begin{bmatrix}
    S_{11} & S_{12} & S_{13} & & &\\
    & S_{22} & S_{23} & & &\\
    & & S_{33} & & &\\
    & & & S_{44} & & \\
    & & & & S_{55} & \\
    & & & & & S_{66}\\
\end{bmatrix}
""")

col2.markdown("Na madeira, material também ortotrópico, em termos das propriedades elásticas dos materiais na matriz *compliance*, temos: 6 coeficientes de Poisson ($\\nu_{21}$, $\\nu_{12}$, $\\nu_{31}$, $\\nu_{13}$, $\\nu_{32}$, $\\nu_{23}$), 3 módulos de elasticidade longitudinais ($E_{1}$, $E_{2}$, $E_{3}$) e 3 módulos de elasticidade transversais ($G_{23}$, $G_{31}$, $G_{12}$), ou seja, 12 propriedades elásticas, conforme apresenta a matriz $\\bm{S}$ abaixo")

col2.latex(r"""
S=\begin{bmatrix}
    \dfrac{1}{E_{1}} & -\dfrac{\nu_{21}}{E_{2}} & -\dfrac{\nu_{31}}{E_{3}} & & &\\
    -\dfrac{\nu_{12}}{E_{1}} & \dfrac{1}{E_{2}} & -\dfrac{\nu_{32}}{E_{3}} & & &\\
    -\dfrac{\nu_{13}}{E_{1}} & -\dfrac{\nu_{23}}{E_{2}} & \dfrac{1}{E_{3}} & & &\\
    &&& \dfrac{1}{G_{23}}&&\\
    &&&& \dfrac{1}{G_{31}}&\\
    &&&&& \dfrac{1}{G_{12}}\\
\end{bmatrix}
""")

col2.write("É importante notar que apesar da matriz *compliance* para materiais ortotrópicos ser simétrica teoricamente, na prática observam-se diferenças entre os 3 coeficientes calculados acima e abaixo da diagonal principal. Isso ocorre devido à grande heterogeneidade do material, além das incertezas associadas às medições em direções distintas.")

col2.subheader("Propagação nos planos")

col2.markdown("##### Propagação de ondas no plano 12")

col2.latex(r"""
\begin{equation}
    \begin{bmatrix}
        \Gamma_{11}-\rho V^{2} & \Gamma_{12} & \Gamma_{13}\\
        \Gamma_{12} & \Gamma_{22}-\rho V^{2} & \Gamma_{23}\\
        \Gamma_{13} & \Gamma_{23} & \Gamma_{33}-\rho V^{2}
    \end{bmatrix}
    \begin{bmatrix}
        p_{1}\\
        p_{2}\\
        p_{3}
    \end{bmatrix}=0
\end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \Gamma_{12}^{2}=(\Gamma_{11}-\rho V^{2})(\Gamma_{22}-\rho V^{2})
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        [(C_{12}+C_{66})n_{1}n_{2}]^{2}=(C_{11}n_{1}^{2}+C_{66}n_{2}^{2}-\rho V^{2})(C_{66}n_{1}^{2}+C_{22}n_{2}^{2}-\rho V^{2})
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        C_{12}=\dfrac{\sqrt{(C_{11}n_{1}^{2}+C_{66}n_{2}^{2}-\rho V^{2})(C_{66}n_{1}^{2}+C_{22}n_{2}^{2}-\rho V^{2})}-C_{66}n_{1}n_{2}}{n_{1}n_{2}}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \begin{bmatrix}
            \Gamma_{11}-\rho V^{2} & \Gamma_{12}&\\
            \Gamma_{12} & \Gamma_{22}-\rho V^{2}&\\
            && \Gamma_{33}-\rho V^{2}
        \end{bmatrix}
        \begin{bmatrix}
            p_{1}\\
            p_{2}\\
            0
        \end{bmatrix}=0
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \dfrac{p_{1}}{p_{2}}=\dfrac{\Gamma_{12}}{\rho V^{2}-\Gamma_{11}}=\dfrac{\rho V^{2}-\Gamma_{22}}{\Gamma_{12}}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        2V_{Q_{L},Q_{T}}^{2}\rho=(\Gamma_{11}+\Gamma_{22})\pm[(\Gamma_{11}-\Gamma_{22})^{2}+4\Gamma_{12}^{2}]^{1/2}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        2V_{T}^{2}\rho=\Gamma_{33}
    \end{equation}
""")

col2.markdown("##### Propagação de ondas no plano 13")

col2.latex(r"""
    \begin{equation}
        \begin{bmatrix}
            \Gamma_{11}-\rho V^{2} & 0 & \Gamma_{13}\\
            0 & \Gamma_{22}-\rho V^{2} & 0\\
            \Gamma_{13} & 0 & \Gamma_{33}-\rho V^{2}
        \end{bmatrix}=0
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \Gamma_{13}^{2}=(\Gamma_{11}-\rho V^{2})(\Gamma_{33}-\rho V^{2})
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        [(C_{13}+C_{55})n_{1}n_{3}]^{2}=(C_{11}n_{1}^{2}+C_{55}n_{3}^{2}-\rho V^{2})(C_{55}n_{1}^{2}+C_{33}n_{3}^{2}-\rho V^{2})
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        C_{13}=\dfrac{\sqrt{(C_{11}n_{1}^{2}+C_{55}n_{3}^{2}-\rho V^{2})(C_{55}n_{1}^{2}+C_{33}n_{3}^{2}-\rho V^{2})}-C_{55}n_{1}n_{3}}{n_{1}n_{3}}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \begin{bmatrix}
            \Gamma_{11}-\rho V^{2} & & \Gamma_{13}\\
            & \Gamma_{22}-\rho V^{2}&\\
            \Gamma_{13} && \Gamma_{33}-\rho V^{2}
            \end{bmatrix}
            \begin{bmatrix}
            p_{1}\\
            0\\
            p_{3}
        \end{bmatrix}=0
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \dfrac{p_{1}}{p_{3}}=\dfrac{\Gamma_{13}}{\rho V^{2}-\Gamma_{11}}=\dfrac{\rho V^{2}-\Gamma_{33}}{\Gamma_{13}}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        2V_{Q_{L},Q_{T}}^{2}\rho=(\Gamma_{11}+\Gamma_{33})\pm[(\Gamma_{11}-\Gamma_{33})^{2}+4\Gamma_{13}^{2}]^{1/2}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        2V_{T}^{2}\rho=\Gamma_{22}
    \end{equation}
""")

col2.markdown("##### Propagação de ondas no plano 23")

col2.latex(r"""
    \begin{equation}
        \begin{bmatrix}
        \Gamma_{11}-\rho V^{2} & 0 & 0\\
        0 & \Gamma_{22}-\rho V^{2} & \Gamma_{23}\\
        0 & \Gamma_{23} & \Gamma_{33}-\rho V^{2}
        \end{bmatrix}=0
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \Gamma_{23}^{2}=(\Gamma_{22}-\rho V^{2})(\Gamma_{33}-\rho V^{2})
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        [(C_{23}+C_{44})n_{2}n_{2}]^{2}=(C_{22}n_{2}^{2}+C_{44}n_{3}^{2}-\rho V^{2})(C_{44}n_{2}^{2}+C_{33}n_{3}^{2}-\rho V^{2})
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        C_{23}=\dfrac{\sqrt{(C_{22}n_{2}^{2}+C_{44}n_{3}^{2}-\rho V^{2})(C_{44}n_{2}^{2}+C_{33}n_{3}^{2}-\rho V^{2})}-C_{44}n_{2}n_{3}}{n_{2}n_{3}}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \begin{bmatrix}
            \Gamma_{11}-\rho V^{2} & &\\
            & \Gamma_{22}-\rho V^{2}& \Gamma_{23}\\
            & \Gamma_{23} & \Gamma_{33}-\rho V^{2}
        \end{bmatrix}
        \begin{bmatrix}
            0\\
            p_{2}\\
            p_{3}
        \end{bmatrix}=0
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        \dfrac{p_{2}}{p_{3}}=\dfrac{\Gamma_{23}}{\rho V^{2}-\Gamma_{22}}=\dfrac{\rho V^{2}-\Gamma_{33}}{\Gamma_{23}}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        2V_{Q_{L},Q_{T}}^{2}\rho=(\Gamma_{22}+\Gamma_{33})\pm[(\Gamma_{22}-\Gamma_{33})^{2}+4\Gamma_{23}^{2}]^{1/2}
    \end{equation}
""")

col2.latex(r"""
    \begin{equation}
        2V_{T}^{2}\rho=\Gamma_{11}
    \end{equation}
""")

import streamlit as st

data = [
    {"Coeficiente de rigidez": "$C_{11}$", "Expressão": "$\\rho V_{11}^{2}$", "Tipo de onda": "L"},
    {"Coeficiente de rigidez": "$C_{22}$", "Expressão": "$\\rho V_{22}^{2}$", "Tipo de onda": "L"},
    {"Coeficiente de rigidez": "$C_{33}$", "Expressão": "$\\rho V_{33}^{2}$", "Tipo de onda": "L"},
    {"Coeficiente de rigidez": "$C_{44}$", "Expressão": "$\\rho V_{44}^{2}$", "Tipo de onda": "T"},
    {"Coeficiente de rigidez": "$C_{55}$", "Expressão": "$\\rho V_{55}^{2}$", "Tipo de onda": "T"},
    {"Coeficiente de rigidez": "$C_{66}$", "Expressão": "$\\rho V_{66}^{2}$", "Tipo de onda": "T"},
    {"Coeficiente de rigidez": "$C_{12}$", "Expressão": "$\\Gamma$", "Tipo de onda": "$Q_{L}, Q_{T}$"},
    {"Coeficiente de rigidez": "$C_{13}$", "Expressão": "$\\Gamma$", "Tipo de onda": "$Q_{L}, Q_{T}$"},
    {"Coeficiente de rigidez": "$C_{23}$", "Expressão": "$\\Gamma$", "Tipo de onda": "$Q_{L}, Q_{T}$"},
]

col2.table(data)

data = [
    {"Direção de Propagação": "$X_1$", "Componente Normal": "$n_1=1$", "Direção da polarização": "$X_1$", "Tipo": "$L$", "Velocidade": "$C_{11}=\\rho V_{11}^{2}$"},
    {"Direção de Propagação": "", "Componente Normal": "$n_2=0$", "Direção da polarização": "$X_2$", "Tipo": "$T$", "Velocidade": "$C_{66}=\\rho V_{66}^{2}$"},
    {"Direção de Propagação": "", "Componente Normal": "$n_3=0$", "Direção da polarização": "$X_3$", "Tipo": "$T$", "Velocidade": "$C_{55}=\\rho V_{55}^{2}$"},

    {"Direção de Propagação": "$X_2$", "Componente Normal": "$n_1=0$", "Direção da polarização": "$X_1$", "Tipo": "$T$", "Velocidade": "$C_{66}=\\rho V_{66}^{2}$"},
    {"Direção de Propagação": "", "Componente Normal": "$n_2=1$", "Direção da polarização": "$X_2$", "Tipo": "$L$", "Velocidade": "$C_{22}=\\rho V_{22}^{2}$"},
    {"Direção de Propagação": "", "Componente Normal": "$n_3=0$", "Direção da polarização": "$X_3$", "Tipo": "$T$", "Velocidade": "$C_{44}=\\rho V_{44}^{2}$"},

    {"Direção de Propagação": "$X_3$", "Componente Normal": "$n_1=0$", "Direção da polarização": "$X_1$", "Tipo": "$T$", "Velocidade": "$C_{55}=\\rho V_{55}^{2}$"},
    {"Direção de Propagação": "", "Componente Normal": "$n_2=0$", "Direção da polarização": "$X_2$", "Tipo": "$T$", "Velocidade": "$C_{44}=\\rho V_{44}^{2}$"},
    {"Direção de Propagação": "", "Componente Normal": "$n_3=1$", "Direção da polarização": "$X_3$", "Tipo": "$L$", "Velocidade": "$C_{33}=\\rho V_{33}^{2}$"},

    {"Direção de Propagação": "$X_1,X_2$", "Componente Normal": "$n_1,n_2$", 
     "Direção da polarização": "$\\dfrac{p_1}{p_2}=\\dfrac{\\Gamma_{12}}{\\rho V^2-\\Gamma_{11}}=\\dfrac{\\rho V^2-\\Gamma_{22}}{\\Gamma_{12}}$", 
     "Tipo": "$Q_L,Q_T$", 
     "Velocidade": "$2V_{Q_L,Q_T}^{2}\\rho=(\\Gamma_{11}+\\Gamma_{22})\\pm[(\\Gamma_{11}-\\Gamma_{22})^2+4\\Gamma_{12}^{2}]$"},
    {"Direção de Propagação": "$X_3$", "Componente Normal": "$n_3=0$", "Direção da polarização": "$X_3$", "Tipo": "$T$", "Velocidade": "$2V_T^2\\rho=\\Gamma_{33}$"},

    {"Direção de Propagação": "$X_1,X_3$", "Componente Normal": "$n_1,n_3$", 
     "Direção da polarização": "$\\dfrac{p_1}{p_3}=\\dfrac{\\Gamma_{13}}{\\rho V^2-\\Gamma_{11}}=\\dfrac{\\rho V^2-\\Gamma_{33}}{\\Gamma_{13}}$", 
     "Tipo": "$Q_L,Q_T$", 
     "Velocidade": "$2V_{Q_L,Q_T}^{2}\\rho=(\\Gamma_{11}+\\Gamma_{33})\\pm[(\\Gamma_{11}-\\Gamma_{33})^2+4\\Gamma_{13}^{2}]$"},
    {"Direção de Propagação": "$X_2$", "Componente Normal": "$n_2=0$", "Direção da polarização": "$X_2$", "Tipo": "$T$", "Velocidade": "$2V_T^2\\rho=\\Gamma_{22}$"},

    {"Direção de Propagação": "$X_2,X_3$", "Componente Normal": "$n_2,n_3$", 
     "Direção da polarização": "$\\dfrac{p_2}{p_3}=\\dfrac{\\Gamma_{23}}{\\rho V^2-\\Gamma_{22}}=\\dfrac{\\rho V^2-\\Gamma_{33}}{\\Gamma_{23}}$", 
     "Tipo": "$Q_L,Q_T$", 
     "Velocidade": "$2V_{Q_L,Q_T}^{2}\\rho=(\\Gamma_{22}+\\Gamma_{33})\\pm[(\\Gamma_{22}-\\Gamma_{33})^2+4\\Gamma_{23}^{2}]$"},
    {"Direção de Propagação": "$X_1$", "Componente Normal": "$n_1=0$", "Direção da polarização": "$X_1$", "Tipo": "$T$", "Velocidade": "$2V_T^2\\rho=\\Gamma_{11}$"},
]

st.table(data)
