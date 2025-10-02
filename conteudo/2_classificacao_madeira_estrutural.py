import streamlit as st
import graphviz

st.title("Ensaios não destrutivos normatizados para a classificação da madeira estrutural")

st.header("Início")

st.write("Neste capítulo, conheceremos os principais ensaios não destrutivos normatizados para a classificação da madeira estrutural. Neste contexto, será considerado o que a ABNT NBR 7190 traz como fundamentos para a classificação. Esta norma passou recentemente por mudanças visando melhorias relacionadas a diversos contextos da utilização da madeira. Desde 1997 não eram trazidas mudanças ou atualizações da mesma, porém, após um período de mais de 20 anos, em 2022 a norma recebeu uma série de atualizações, sendo separada em 7 partes distintas:")

st.markdown("""
    - ABNT NBR 7190-2, Estruturas de madeira -- Parte 2: Métodos de ensaio para classificação visual e mecânica de peças estruturais de madeira
    - ABNT NBR 7190-3, Estruturas de madeira -- Parte 3: Métodos de ensaio para corpos de prova isentos de defeitos para madeiras de florestas nativas
    - ABNT NBR 7190-4, Estruturas de madeira -- Parte 4: Métodos de ensaio para caracterização de peças estruturais
    - ABNT NBR 7190-5, Estruturas de madeira -- Parte 5: Métodos de ensaio para determinação da resistência e da rigidez de ligações com conectores mecânicos
    - ABNT NBR 7190-6, Estruturas de madeira -- Parte 6: Métodos de ensaio para caracterização de madeira lamelada colada estrutural
    - ABNT NBR 7190-7, Estruturas de madeira -- Parte 6: Métodos de ensaio para caracterização de madeira lamelada colada cruzada estrutural
""")

st.graphviz_chart('''
    digraph {
        "Lote de Madeira" -> "Tipo de Floresta"
        "Tipo de Floresta" -> "Plantada"
        "Tipo de Floresta" -> "Nativa"
        "Plantada" -> "Homogêneo"
        "Plantada" -> "Não homogêneo"
        "Nativa" -> "ABNT NBR 7190-3"
        "Homogêneo" -> "ABNT NBR 7190-4"
        "Não homogêneo" -> "ABNT NBR 7190-2"
    }
''')

st.header("Sobre os ensaios e a ABNT NBR 7190:2022")

st.write("Estes ensaios estão em concordância com parte dos ensaios de caracterização aplicados à madeira na seção anterior. A ABNT NBR 7190-2:2022 estabelece que lotes de madeira provenientes de florestas plantadas não homogêneos podem ser classificados com base em parâmetros visuais e mecânicos. Ou seja, a classe de resistência das peças estruturais deve ser determinada utilizando-se os dois parâmetros, sendo a classe estabelecida com base no pior entre ambos.")

st.subheader("Classificação visual")

st.write("Os parâmetros visuais¹ levam em conta a presença de defeitos. Neste caso, dependendo do tamanho dos defeitos diferentes classes podem ser atribuídas à peça, devendo ser descartada para uso estrutural, caso ultrapasse os limites estabelecidos em norma.")

st.info("¹Fissuras passantes ou não passantes; Inclinação excessiva das fibras; Dano mecânico; Presença de nós; Ataque biológico; Presença de medula; Bolsas de resina; Distorções dimensionais como: Arqueamento, torcimento, esmoado, encanoamento e encurvamento.")

st.subheader("Classificação mecânica")

st.markdown("No que diz respeito à classificação mecânica, ela consiste na determinação da densidade aparente e do módulo de elasticidade na flexão estática. O ensaio de flexão estática é realizado conforme detalhado anteriormente. Vale ressaltar que o ensaio deve seguir alguns critérios dimensionais da peça e do carregamento utilizado, de modo a evitar o rompimento da peça. Os parâmetros dimensionais tanto da peça quanto do aparato de ensaio consideram que, a peça deve ser ensaiada na posição deitada, ou seja, com a maior dimensão da seção transversal ($h$) na horizontal. Além disso, o vão livre deve ser de 18 vezes a largura ($b$) da peça ensaiada e, o comprimento apoiado deve ser igual à largura $b$ da peça. Quanto ao carregamento, a carga aplicada deve ser de $10\\%$ a $40\\%$ da força máxima de ruptura da peça. Como alternativa aos métodos destrutivos amplamente empregados para a caracterização até então, o módulo de elasticidade pode ser obtido por métodos vibracionais, também detalhados anteriormente, apresentando boa correlação com o ensaio de flexão.")

st.subheader("Densidade aparente")

st.markdown("A densidade aparente é determinada na condição-padrão estipulada pela norma, à $12\\%$ de umidade. Para peças com umidade distinta da estabelecida, no intervalo de $10\\%$ a $25\\%$, deve ser feita a correção da densidade atual para a aparente através da relação")

st.latex(r"""
    \begin{equation}
        \rho_{12}=\rho_{\text{test}}(1-0.5(U-0.12))
    \end{equation}
""")

st.write("O mesmo vale para o módulo de elasticidade obtido no ensaio de flexão estática que, a depender da umidade da peça, precisa ser corrigido conforme a relação mostrada anteriormente.")