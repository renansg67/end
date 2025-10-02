import streamlit as st

st.title("Fatores que afetam a propagação de ondas acústicas em sólidos")

st.header("Início")

st.write("Existem diferentes fatores que afetam a propagação de ondas acústicas em sólidos, tornando essa análise complexa, uma vez que estão envolvidos tanto as características do material no qual as ondas se propagam quanto aspectos relacionados ao seu tamanho e forma.")

st.write("O ambiente também exerce influência, considerando-se as condições de temperatura, umidade e pressão, que podem afetar a propagação em diferentes níveis. Além disso, deve-se levar em conta a influência dos transdutores utilizados nos ensaios de propagação, visto que propriedades associadas ao material que compõe os transdutores, ao cabeamento, ao material de apoio, ao elemento ativo e ao tipo de acoplamento empregado impactam diretamente nos resultados obtidos.")

st.write("Outro fator igualmente relevante está relacionado aos fenômenos próprios das ondas acústicas, que, por si só, afetam a propagação em resposta aos fatores anteriormente mencionados: material da amostra, dimensões e geometria, condições ambientais e características dos transdutores.")

st.header("Fatores relacionados aos fenômenos ondulatórios")

st.subheader("Impedância acústica")

st.write("A propagação de ondas acústicas, em termos dos fenômenos ondulatórios envolvidos, sem considerar outros fatores, está sujeita à influência dos fenômenos de reflexão e refração ao atravessar materiais sólidos. Estes, diferentemente do ar e da água, são capazes de suportar tanto ondas de cisalhamento quanto ondas longitudinais (ou de pressão).")

st.markdown("Em materiais sólidos, quando ondas incidem em ângulo normal à sua superfície, pode ocorrer tanto a reflexão de parte do feixe ultrassônico quanto a transmissão pela interface que separa dois meios. Estudos demonstraram que é possível relacionar as parcelas transmitida e refletida do feixe acústico por meio da grandeza denominada *impedância acústica*, representada pelo símbolo $Z$. Ela é definida como o produto entre a massa específica e a velocidade de propagação do som no meio:")

st.latex(r"""
    \begin{equation}
        Z=\rho V
    \end{equation}
""")

st.subheader("Coeficientes de reflexão e transmissão")

st.markdown("Supondo que um feixe acústico incida perpendicularmente à interface que separa dois meios, quanto maior a diferença de impedância acústica entre eles, maior será a parcela de energia refletida de volta ao meio de origem. Inversamente, quanto mais próximos forem os valores de impedância acústica, maior será a energia transmitida. Assim, a impedância acústica $Z$ pode ser interpretada como a dificuldade que uma onda ultrassônica encontra para atravessar determinado meio.")

st.markdown("Definindo-se os coeficientes de reflexão e transmissão do feixe acústico como $R$ e $T$, respectivamente, a soma de ambas as parcelas deve ser igual a 1, desconsiderando perdas por conversão em outros modos de energia:")

st.latex(r"""
    \begin{equation}
        R+T=1
    \end{equation}
""")

st.markdown("Considerando dois meios com impedâncias acústicas $Z_{1}$ e $Z_{2}$, o coeficiente de reflexão é dado por:")

st.latex(r"""
    \begin{equation}
        R=\left(\dfrac{Z_{2}-Z_{1}}{Z_{2}+Z_{1}}\right)^{\!\!2}
    \end{equation}
""")

st.subheader("Fenômeno da refração")

st.write("Além da reflexão e da transmissão, ocorre o fenômeno da refração, caracterizado pela mudança na direção de propagação do feixe quando a incidência não é normal à interface entre os dois meios. Dependendo da impedância acústica, o feixe pode aproximar-se ou afastar-se da reta normal à interface.")

st.write("Quando a velocidade aumenta, o feixe acústico afasta-se da normal; quando diminui, aproxima-se dela, obedecendo à lei de Snell, que relaciona ângulos de incidência e refração com as velocidades de propagação, comprimentos de onda e índices de refração:")

st.latex(r"""
    \begin{equation}
        \dfrac{\sin\alpha_{1}}{\sin\alpha_{2}}=\dfrac{V_{1}}{V_{2}}=\dfrac{\lambda_{1}}{\lambda_{2}}=\dfrac{n_{2}}{n_{1}}
    \end{equation}
""")

st.write("Nota-se uma relação inversamente proporcional entre a velocidade de propagação e o comprimento de onda em relação ao índice de refração. Essa equação permite calcular velocidades ou ângulos, desde que se disponha de informações suficientes.")

st.subheader("Conceito de ângulo crítico")

st.write("Um caso particular ocorre quando o feixe refratado forma um ângulo de 90° com a normal à interface. Nessa condição definem-se dois ângulos críticos, dependendo do tipo de onda propagada:")

st.markdown("""
    - o primeiro está associado à onda longitudinal que incide e se refrata em 90°;  
    - o segundo, ao ângulo crítico necessário para que uma onda transversal se refrate na mesma direção da interface.
""")

st.write("A partir da lei de Snell, considerando $\\alpha_{2}=90^{\\circ}$ e $\\sin 90^{\\circ}=1$, a equação do ângulo crítico $\\alpha_{\\text{cr}}$ torna-se:")

st.latex(r"""
    \begin{equation}
        \alpha_{\text{cr}}=\arcsin\left(\dfrac{V_{1}}{V_{2}}\right)
    \end{equation}
""")

st.write("Em termos das ondas longitudinais e transversais:")

st.latex(r"""
    \begin{equation}
        \begin{matrix}
            (\alpha_{\text{cr}})_{1}=\arcsin\dfrac{(V_{L})_{1}}{(V_{L})_{2}} &
            (\alpha_{\text{cr}})_{2}=\arcsin\dfrac{(V_{T})_{1}}{(V_{T})_{2}}
        \end{matrix}
    \end{equation}
""")

st.subheader("Divergência do feixe acústico")

st.markdown("Outro aspecto relevante diz respeito às características dos transdutores, em especial ao padrão de direcionalidade do feixe. Ele depende tanto do comprimento de onda $\\lambda$ da onda emitida quanto do diâmetro $D$ do transdutor. Feixes menos divergentes apresentam maior capacidade de penetração no material.")

st.write("O ângulo de divergência do feixe é dado por:")

st.latex(r"""
    \begin{equation}
        \phi=\arcsin\left(1.2\dfrac{\lambda}{D}\right)
    \end{equation}
""")

st.subheader("Ressonância")

st.write("A frequência de ressonância de um corpo de prova é obtida pela relação:")

st.write(r"""
    \begin{equation}
        f=n\dfrac{V}{2L}
    \end{equation}
""")

st.write("em que $n$ corresponde à ordem do harmônico. Para $n=1$, tem-se a frequência de ressonância fundamental.")

st.subheader("Zona de Fresnel (Campo próximo)")

st.write("Nos ensaios, deve-se considerar a região próxima ao transdutor, denominada *zona de Fresnel*, caracterizada por um padrão de interferências complexas, no qual o feixe ainda não está estabilizado. O comprimento dessa região é dado por:")

st.latex(r"""
    \begin{equation}
        N=\dfrac{D^{2}}{4\lambda}
    \end{equation}
""")

st.write("O conhecimento da zona de Fresnel é fundamental para a correta análise dos sinais obtidos durante o ensaio.")

st.subheader("Zona de Fraunhofer (Campo distante)")

st.write("A zona de Fraunhofer, ou campo distante, corresponde à região em que o feixe ultrassônico já se apresenta estabilizado e divergente de forma previsível. Nessa área, as medições são mais consistentes e confiáveis, tornando possível a detecção de falhas e a caracterização interna de materiais como metais, madeira e concreto. A previsibilidade na propagação das ondas nessa região garante maior confiabilidade na avaliação da integridade estrutural.")

st.subheader("Anisotropia do material")

st.write("A anisotropia de um material está relacionada à variação de suas propriedades elásticas em diferentes direções de propagação da onda ultrassônica. Esse efeito tem impacto direto nas velocidades medidas, uma vez que estas estão associadas aos coeficientes de rigidez do meio. Assim, compreender a anisotropia é fundamental para a correta interpretação dos resultados em ensaios não destrutivos.")

st.markdown("**Materiais isotrópicos**")

st.write("Nos materiais isotrópicos, as propriedades elásticas são equivalentes em todas as direções. Como consequência, a velocidade de propagação das ondas ultrassônicas não depende da orientação do feixe. O concreto, apesar de apresentar heterogeneidades internas devido à presença de agregados, vazios e microfissuras, pode ser considerado aproximadamente isotrópico em escala macroscópica. Dessa forma, suas variações de velocidade tendem a ser pouco significativas quando comparadas a materiais mais anisotrópicos.")

st.markdown("**Materiais ortotrópicos**")

st.write("Nos materiais ortotrópicos, há três direções principais de simetria elástica, nas quais as propriedades diferem consideravelmente. Um exemplo clássico é a madeira, cuja estrutura fibrosa confere direções preferenciais de propagação. Assim, a velocidade das ondas varia de forma expressiva a depender da orientação do ensaio em relação às fibras: longitudinalmente (ao longo das fibras), radialmente (perpendicular às fibras) ou tangencialmente (em direção paralela aos anéis de crescimento). Esse comportamento deve ser considerado na calibração e interpretação dos resultados para evitar leituras equivocadas sobre sua resistência e integridade.")

st.markdown("**Materiais compósitos e laminados**")

st.write("Nos materiais compósitos e laminados, a anisotropia é ainda mais pronunciada e complexa. Cada camada ou fase do material contribui de maneira distinta para a resposta global, influenciando a velocidade e a atenuação das ondas ultrassônicas. A presença de interfaces entre as camadas pode gerar fenômenos adicionais, como reflexões múltiplas e dispersões. Nesse contexto, a modelagem matemática e a caracterização experimental tornam-se indispensáveis para a adequada avaliação do desempenho mecânico e da integridade estrutural desses materiais.")

st.subheader("Temperatura e umidade")

st.write("Outro fator que afeta a velocidade de propagação diz respeito às condições de temperatura e umidade do material ensaiado. Sabe-se que, para a madeira, sua rigidez transversal tende a diminuir com o aumento dessas duas grandezas. Dependendo do material, alguns estudos precisam ser realizados visando a um maior aprofundamento, tendo em vista as variações e os comportamentos apresentados por cada tipo de material.")

st.subheader("Grãos e cristais")

st.write("Além disso, a presença de grãos e cristais também pode afetar a propagação, tendo em vista a maior tendência de desvios na trajetória do feixe ultrassônico inicial devido aos caminhos preferenciais existentes no material, ocasionando maior tempo de viagem entre dois pontos.")

st.markdown("Outro fator que pode afetar a propagação são as propriedades físicas do material, como o módulo de elasticidade e a densidade. Ambos influenciam a velocidade de propagação de ondas ultrassônicas. A equação que relaciona essas grandezas assemelha-se ao comportamento presente em uma corda tensionada quando se deseja medir o tempo de propagação de um pulso após esta ser excitada, em que as grandezas envolvidas são: a tensão na corda $\\tau$, a densidade linear da corda $\\mu$, dada em kg/m no SI, e a velocidade de propagação do pulso:")

st.latex(r"""
    \begin{equation}
        V=\sqrt{\dfrac{\tau}{\mu}}
    \end{equation}
""")

st.markdown("Quando se adapta a mesma equação para um corpo sólido, a tensão na corda torna-se o módulo de elasticidade, ou módulo de Young ($Y$); a densidade linear torna-se a massa específica por unidade de volume $\\rho$; e a velocidade de propagação da onda transversal gerada na corda torna-se a velocidade de propagação do pulso acústico, que pode variar entre frequências audíveis e inaudíveis (ultrassônicas), como é visto na equação abaixo:")

st.latex(r"""
    \begin{equation}
        Y=\rho V^{2}
    \end{equation}
""")

st.markdown("As relações observadas entre as mudanças no módulo de elasticidade e na massa específica volumétrica mostram que, quanto maior a rigidez do material, maior a velocidade de propagação do feixe acústico ao longo dele. Em contrapartida, o aumento da densidade leva à redução da velocidade de propagação. Apesar de a análise, nesse contexto, ser simples quando se varia apenas uma grandeza por vez, na realidade a velocidade pode ser mais complexa de analisar, tendo em vista que tanto $Y$ quanto $\\rho$ podem variar em conjunto.")

st.markdown("Por exemplo, quando se analisa a qualidade da madeira presente em árvores por meio de sua inspeção, estabelecem-se três categorias de qualidade: madeira sã, deteriorada e com cavidades. Ao refazer a análise anterior em termos das propriedades do material, observa-se que a madeira sã deve apresentar tanto rigidez quanto densidade maiores que as outras duas categorias, de modo a promover maior velocidade de propagação do pulso acústico em seu interior. Já na madeira deteriorada, conclui-se que sua rigidez é menor em comparação à madeira sã, uma vez que o material deteriorado, na maioria dos casos, apresenta maior maciez e facilidade de deformação em decorrência de carregamentos. No entanto, sua densidade pode não ser tão simples de analisar em relação à madeira sã, pois, mesmo deteriorada, a presença de água e o nível de deterioração podem não modificar a densidade de forma acentuada. E, mesmo que ocorresse deterioração intensa, um caso em que tanto $Y$ quanto $\\rho$ caíssem na mesma proporção levaria a uma velocidade de propagação acústica equivalente à da madeira sã. Todavia, na prática, observa-se que a velocidade de propagação tende a reduzir na madeira deteriorada. Nesse caso, tanto a rigidez quanto a densidade são reduzidas, mas há maior perda de densidade em relação à rigidez em números absolutos, de modo que")

st.latex(r"""
    \begin{equation}
        \sqrt{\dfrac{Y_{\text{sã}}}{\rho_{\text{sã}}}}>\sqrt{\dfrac{Y_{\text{deteriorada}}}{\rho_{\text{deteriorada}}}}
    \end{equation}
""")

st.markdown("Retomando a análise para a madeira com cavidades, nesse caso, devido aos vazios existentes em seu interior, a densidade tende a diminuir consideravelmente, ficando em torno de $1\\,\\text{kg}/\\text{m}^{3}$. Todavia, a rigidez oferecida pelos poros de ar é nula, de modo que a relação estabelecida anteriormente torna-se")

st.latex(r"""
    \begin{equation}
        \sqrt{\dfrac{Y_{\text{sã}}}{\rho_{\text{sã}}}}>\sqrt{\dfrac{Y_{\text{deteriorada}}}{\rho_{\text{deteriorada}}}}>\sqrt{\dfrac{Y_{\text{cavidade}}}{\rho_{\text{cavidade}}}}
    \end{equation}
""")

st.write("Em termos das velocidades:")

st.latex(r"""
    \begin{equation}
        V_{\text{sã}}>V_{\text{deteriorada}}>V_{\text{cavidade}}
    \end{equation}
""")

st.markdown("A partir da relação estabelecida, conclui-se que, quanto maior o valor proveniente da razão $Y/\\rho$, maior a velocidade de propagação das ondas acústicas.")

st.subheader("Tamanho e forma")

st.markdown("Após a análise anterior, envolvendo as propriedades dos materiais, outros fatores não menos importantes dizem respeito ao tamanho e à forma do sólido. Na propagação de ondas acústicas, seu comportamento pode ser influenciado em função desses fatores. No ensaio ultrassônico, por exemplo, sólidos prismáticos com maior comprimento ($L>50\\,\\text{mm}$) tendem a gerar maior atenuação do sinal.")

st.write("Conforme discutido anteriormente na parte referente aos ensaios com ultrassom, observa-se que a intensidade do sinal diminui quanto maior a distância percorrida pelo feixe acústico através do material, evidenciando a correlação com a maior atenuação observada em sólidos de maior comprimento. A velocidade de propagação, por depender das características do material, não sofre alteração, independentemente do comprimento do sólido, desde que suas propriedades permaneçam constantes ao longo da direção de propagação, em comparação ao mesmo sólido encurtado.")

st.subheader("Frequência dos transdutores")

st.write("Outro aspecto está relacionado à frequência dos transdutores. É válido ressaltar que, entre os diversos tipos existentes, cada um possui uma frequência de operação ideal, denominada frequência central. Ao seu redor, existe um intervalo de frequências no qual o transdutor pode operar, fornecendo a qualidade adequada do sinal.")

st.write("Entretanto, deve-se considerar, ao realizar os ensaios, que quanto maior a frequência do feixe acústico emitido, maior será a atenuação do sinal, independentemente do material. Portanto, é necessário adequar o tipo de transdutor ao material, com base no estudo prévio de sua anisotropia.")

st.write("Normalmente, materiais isotrópicos, sem a presença de fronteiras de grãos em seu interior, podem ser ensaiados em frequências mais elevadas quando comparados a materiais ortotrópicos, como a madeira, que requerem frequências mais baixas, muitas vezes se iniciando em 20 kHz. Contudo, já foram realizados estudos nesse tipo de material utilizando transdutores de 1 MHz = 1000 kHz, valor muito acima das menores frequências ultrassônicas.")

st.subheader("Amortecimento dos transdutores")

st.write("Este termo, apesar de estar associado aos transdutores, depende das características de um componente importante dos mesmos. Esse componente é denominado material de apoio (*backing material*) e é responsável por absorver ou refletir as ondas acústicas no elemento ativo do transdutor.")

st.write("O amortecimento está relacionado à capacidade que o material de apoio possui de absorver ou refletir o feixe acústico incidente no elemento ativo. Um material de apoio com alto amortecimento apresenta maior capacidade de absorver a energia mecânica incidente. Como consequência, ele possui uma maior largura de banda de frequências e, além disso, maior resolução. Em contrapartida, há maior perda de sensibilidade a descontinuidades, já que boa parte do sinal é absorvida, podendo passar despercebida na análise.")

st.write("A alta resolução axial é garantida pela maior largura de banda, caracterizada pela emissão de pulsos de menor duração — pulsos curtos — que conferem essa capacidade ao transdutor.")