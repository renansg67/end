import streamlit as st

st.set_page_config(page_title="Materiais e Inspeções", layout="centered")

st.title("Ensaios não destrutivos para a caracterização de materiais de construção não metálicos")

st.header("Início", divider=True)

st.write("Quando se fala de materiais de construção não metálicos, pode-se fazer referência tanto às estruturas de concreto quanto às de madeira, que são amplamente utilizadas. O objetivo da utilização de ensaios não destrutivos para a caracterização desses materiais, como tem se apresentado nas últimas décadas com o avanço do conhecimento e das técnicas da área, é complementar e facilitar as análises, além de permitir maior escalabilidade quanto às condições de resistência e rigidez do material ensaiado. Além disso, esse método visa complementar a caracterização realizada por meio de ensaios destrutivos, podendo encurtar o caminho até a caracterização destrutiva, desde que as propriedades da peça ensaiada sejam conhecidas e existam estudos anteriores detalhados o suficiente para validar o ensaio não destrutivo aplicado com boa margem de confiança. Dependendo do tipo de estudo, é possível até dispensar métodos destrutivos, que exigem mais tempo para execução.")

st.write("O concreto, apesar de possuir em seu interior material metálico proveniente das armaduras utilizadas para resistir aos esforços de tração, é avaliado por meio de ensaios específicos voltados às características do próprio concreto, sem considerar o efeito dessas armaduras. Isso permite avaliar a influência dos diversos elementos de sua composição, como cimento, agregados miúdos e graúdos, e o aglomerante (normalmente o cimento), possibilitando sua caracterização a partir de ensaios semidestrutivos e não destrutivos, utilizados para validar os processos de fabricação. Na primeira categoria enquadra-se o ensaio de penetração de pinos, enquanto a segunda contempla métodos como a esclerometria e a propagação de ondas de tensão, incluindo os procedimentos vibracionais e ultrassônicos. Para todos esses ensaios aplicados ao concreto, é sempre importante avaliar os fatores que podem influenciá-los. O material, quando exposto a intempéries em condições inadequadas, pode passar por processos de degradação. Neste capítulo serão abordados os principais fenômenos que podem ocorrer, bem como a importância de uma avaliação prévia das condições de ensaio, de modo a obter dados coerentes quanto às propriedades de resistência à compressão e de rigidez do material. Com base nessas análises e nas devidas considerações, é possível aprimorar tanto os ensaios realizados em laboratório com corpos de prova quanto aqueles conduzidos em estruturas reais. As principais normas brasileiras utilizadas nesta parte são: ABNT NBR 7584:2012, que trata do ensaio de medição da dureza superficial para o concreto endurecido, e ABNT NBR 8802:2019, referente ao ensaio de ultrassom.")

st.write("Comparada ao concreto, diversos métodos de ensaio análogos são utilizados para a madeira, com as devidas adaptações. Por se tratar de um material ortotrópico, ou seja, com propriedades elásticas distintas em três planos ortogonais de isotropia, a maior dificuldade está relacionada à elevada heterogeneidade apresentada pela madeira, que, ao compor estruturas vivas como as árvores, possui diversas particularidades que exigem atenção em sua caracterização. A utilização de ensaios não destrutivos, como o de propagação de ondas de tensão, tem ganhado cada vez mais espaço devido à correlação existente com as propriedades de resistência e rigidez. Além desse método, o ensaio de flexão estática normatizado pela ABNT NBR 7190:2022 estabelece o procedimento adequado para caracterizar a propriedade de rigidez, fornecendo aos profissionais da área a possibilidade de incorporar métodos vibracionais baseados no cálculo do módulo de elasticidade a partir da frequência fundamental de ressonância obtida por meio da análise de Fourier. Nesta parte serão detalhados os métodos de vibração transversal, em que uma barra biapoiada é posta em oscilação após sofrer uma deflexão inicial, e o dos modos de vibração, que permitem calcular propriedades como os módulos de elasticidade longitudinal e transversal a partir dos modos flexionais e torsionais.")

st.header(":factory: Concreto")

st.write("Conforme o livro *Materiais de Construção Civil* de Falcão Bauer, temos os seguintes ensaios")

st.subheader("Ensaio para medição da dureza superficial")

st.write("Este ensaio visa aferir, a partir do impacto, a dureza superficial do concreto, avaliada nos primeiros 2 cm superficiais. Com base na reflexão do embulo um valor adimensional é lido pelo equipamento para cada impacto. Devido à alta repetibilidade de impactos que pode ocorrer neste ensaio, torna-se fundamental seguir a sequência de passos conforme a ABNT NBR 7584:2012 para a calibração adequada do esclerômetro. Para isso, deve ser feito uso de uma bigorna específica para a calibração. Conforme especifica a norma, no mínimo 10 impactos devem ser realizados na bigorna de modo que o índice esclerométrico obtido seja igual a 80. De posse dos índices obtidos, calcula-se o fator de correção do índice esclerométrico médio efetivo associado a uma área de ensaio por meio da equação")

st.latex(r'''
    k=\dfrac{n I_{E_{\text{nom}}}}{\displaystyle\sum_{i=1}^{n}I_{E_{i}}}
''')

st.write("O índice esclerométrico nominal depende do esclerômetro utilizado e deve ser fornecido pelo fabricante do equipamento. O próximo passo é definir a área de ensaio que pode variar de 9 cm² a 20 cm². Nela, pelo menos 16 impactos devem ser realizados, com pontos de impacto distintos e distando pelo menos 3 cm entre si. Com o conjunto de dados em mãos, deve-se calcular o valor do índice esclerométrico médio da área. Feito isso, deve-se descartar índices que destoem em mais de 10% da média calculada. Pelo menos 5 valores devem restar, caso contrário, a área de ensaio deve ser descartada. Com os índices esclerométricos restantes, uma nova média deve ser calculada e nenhum de seus valores deve destoar em mais de 10%. Este valor representa o índice esclerométrico médio, que precisa ser ajustado com base no coeficiente de correção do esclerômetro obtido para cálculo do índice esclerométrico médio efetivo citado anteriormente, pela equação")

st.latex(r'''
    I_{E\alpha}=k\cdot I_{E}
''')

st.write("É imprescindível que o profissional responsável pelo ensaio tenha em mente a importância de limpar a área de ensaio por meio de polimento utilizando disco ou prisma de carborundum se a limpeza for manual. Utilizar máquina politriz dotada de acessórios para desgaste e polimento da superfície de concreto pode agilizar o procedimento. Superfícies úmidas e carbonatadas devem ser evitadas, tendo em vista que a umidade pode subestimar o índice esclerométrico obtido, enquanto que a carbonatação pode superestimar o valor de índice em decorrência do aumento de dureza da superfície. Ao definir a área de ensaio recomenda-se que a superfície seja vertical e que o esclerômetro seja posicionado corretamente, ortogonal à superfície de impacto. Em áreas com elementos de dimensões menores que 100 mm na direção de impacto (menor espessura), visando evitar fenômenos de ressonância, vibração e dissipação de energia no resultado obtido, deve-se evitar o local. Caso não seja encontrada uma melhor alternativa, deve-se utilizar um apoio na face oposto visando aumentar a rigidez do elemento. Quanto maior a heterogeneidade maior deve ser a quantidade de áreas de ensaio. De cada área de ensaio obtém-se somente um índice esclerométrico médio efetivo.")

st.subheader("Ensaio de propagação de ondas de tensão")

st.write("Neste tipo de ensaio, a análise se inicia a partir da interpretação do sinal decorrente de ondas mecânicas (acústicas) produzidas no meio, que podem apresentar diferentes frequências de propagação, a depender da forma como o corpo de prova ou a estrutura são excitados. Ondas acústicas audíveis possuem menor frequência em relação às ondas ultrassônicas. As primeiras podem ser produzidas por um impacto na superfície do corpo de prova, enquanto as segundas, por meio do uso de transdutores operando em frequências acima de 20 kHz.")

st.write("Os métodos tratados a seguir envolvem a propagação de ondas de tensão para obtenção da frequência de ressonância ou a propagação de ondas ultrassônicas visando à determinação da velocidade e, consequentemente, do módulo de elasticidade na direção de ensaio. É válido ressaltar que ambos os métodos são dinâmicos, ou seja, o material é submetido à propagação de ondas de tensão que podem ser de curta ou longa duração. No método da frequência de ressonância, o ensaio pode ser realizado em regime transiente, quando há mudança abrupta em seu estado, ou em regime estacionário, quando o material recebe estímulos vibracionais de maior duração. Já no segundo método (propagação de ondas ultrassônicas), por meio de diferentes arranjos de transdutores, determina-se o intervalo entre a emissão e a recepção do sinal acústico e calcula-se a velocidade.")

st.write("Diferentes tipos de ondas podem ser utilizados na propagação do feixe acústico no material estudado. As principais empregadas no ensaio são as ondas longitudinais, também chamadas de ondas de pressão ou de compressão, e as ondas transversais, também conhecidas como ondas de cisalhamento. Dependendo do tipo de transdutor utilizado, o tipo de onda transmitida pode variar. Ao utilizar transdutores de ondas longitudinais, a velocidade de propagação obtida pode ser relacionada com a equação")

st.latex(r'''
    V_{L}=\sqrt{\dfrac{2\mu+\lambda}{\rho}}
''')

st.write("em que μ e λ são conhecidos como parâmetros de Lamé, que relacionam as propriedades elásticas de um material e permitem simplificar a equação, podendo ainda ser expressos em função de propriedades como o módulo de elasticidade longitudinal, o módulo de elasticidade transversal e o coeficiente de Poisson, conforme mostrado a seguir:")

st.latex(r'''
    \begin{matrix}
        \mu=G=\dfrac{E}{2(1 + \nu)} & \lambda=\dfrac{E\nu}{(1+\nu)(1-2\nu)}
    \end{matrix}
''')

st.write("Para ondas transversais, a equação é simplificada, não dependendo de λ")

st.latex(r'''
    V_{T}=\sqrt{\dfrac{\mu}{\rho}}
''')

st.write("Além dessas relações, outra fundamental diz respeito ao módulo volumétrico κ, obtido quando o elemento de tensão cúbico é submetido a uma pressão em todas as suas faces simultaneamente:")

st.latex(r'''
    \kappa=\dfrac{E}{3(1-2\nu)}
''')

st.write("O módulo de elasticidade também pode ser reescrito em função de μ e λ, conforme a equação:")

st.latex(r'''
    E=\dfrac{\mu(2\mu+3\lambda)}{\mu+\lambda}
''')

st.write("enquanto o coeficiente de Poisson pode ser expresso por:")

st.latex(r'''
    \nu=\dfrac{\lambda}{2(\mu+\lambda)}
''')

st.write("Ao derivar a lei de Hooke em função dos parâmetros de Lamé:")

st.latex(r'''
    \begin{array}{rcl}   
        \sigma_{xx}&=&(2\mu+\lambda)u_{xx}+\lambda(u_{yy}+u_{zz})\\
        \sigma_{yy}&=&(2\mu+\lambda)u_{yy}+\lambda(u_{xx}+u_{zz})\\
        \sigma_{zz}&=&(2\mu+\lambda)u_{zz}+\lambda(u_{xx}+u_{yy})
    \end{array}
''')

st.write("considerando as seguintes condições:")

st.latex(r'''
    \begin{array}{rcl}
        P&=&(2\mu+\lambda)\left(\dfrac{P}{E}\right)+\lambda\left(-\dfrac{2\nu P}{E}\right)\\ 
        0&=&(2\mu+\lambda)\left(-\dfrac{\nu P}{E}\right)+\lambda\left(\dfrac{P}{E}-\dfrac{\nu P}{E}\right)
    \end{array}
''')

st.write("chega-se às equações que relacionam λ = f(E, ν),  ν = f(μ, λ) e E = f(μ, λ)")

st.markdown("**Método da frequência de ressonância**")

st.write("No concreto, este ensaio, como mencionado anteriormente, visa obter as propriedades de rigidez do material. Por meio dele, o corpo de prova é colocado sobre um sistema vibratório que pode estar apoiado em diferentes pontos do próprio corpo de prova. A partir disso, o objeto recebe um impacto externo e o sistema de medição do equipamento, conectado a um computador, realiza a análise de sinais com base no intervalo de frequências abrangido pela propagação e retorna o módulo de elasticidade dinâmico do corpo de prova.")

st.write("Com esse valor, utiliza-se a ABNT NBR 8522-2:2021, que fornece as diretrizes necessárias para o cálculo do módulo de elasticidade estático $E_{\text{est}}$. Outros métodos, menos automatizados, para a obtenção do módulo de elasticidade estático, baseiam-se em relações empíricas estabelecidas por estudos da área. Nesses métodos, os parâmetros considerados levam em conta características como: massa do corpo de prova; o formato, normalmente confeccionado seguindo o padrão prismático, com seção circular ou retangular; e a própria frequência de ressonância.")

st.write("Uma equação que relaciona todos esses elementos é mostrada a seguir:")

st.latex(r'''
    E_{\text{din}}=CMn^{2}
''')

st.write("em que *C* é o fator de forma, associado ao tipo de prisma conforme detalhado anteriormente, *M* é a massa do corpo de prova e *n* é a frequência de ressonância fundamental.")

st.write("Um corpo de prova possui várias frequências de vibração, ou seja, frequências que produzem vibrações de maior amplitude. A fundamental é caracterizada por ser a primeira frequência que gera uma amplitude de vibração destoante das anteriores, também chamada de frequência de ressonância do primeiro harmônico.Um corpo de prova possui várias frequências de vibração, ou seja, frequências que produzem vibrações de maior amplitude. A fundamental é caracterizada por ser a primeira frequência que gera uma amplitude de vibração destoante das anteriores, também chamada de frequência de ressonância do primeiro harmônico.")

st.markdown("**Método da propagação de pulso ultrassônico**")

st.latex(r'''
    \begin{array}{rcl}
        E_{\text{din}}&=&f(\rho,\nu,V)\\
        V&=&\sqrt{\dfrac{E_{\text{din}}(1-\nu)}{\rho(1+\nu)(1-2\nu)}}
    \end{array}
''')

st.write("Módulo de elasticidade estático¹")

st.latex(r'''
    E=f(V)
''')

st.write("Resistência à compressão")

st.latex(r'''
    f_{C}=f(V)
''')

st.write("Fatores que afetam a velocidade de propagação do pulso ultrassônico no concreto²")

st.info("¹Tanto o módulo de elasticidade estático quanto a resistência à compressão podem ser obtidos de maneira experimental por meio do ensaio de propagação de ondas desde que o concreto ensaiado possua similaridade aqueles em que já foram obtidas as funções dependentes da velocidade do pulso ultrassônico")

st.info("²Idade do concreto; massa específica do concreto; massa específica, tipo e características dos agregados; temperatura e umidade; efeito da armadura (teórico); efeito da armadura em estruturas reais; tipo de cimento; tipo de cura; tipo de adensamento; direção de ensaio}")

st.markdown("**Ensaio de penetração de pinos**")

st.write("Ensaio caracterizado por ser semidestrutivo, no qual se realiza o disparo de um pino com auxílio de um dispositivo carregado com pólvora. O disparo direciona o pino para dentro do corpo de prova ou da estrutura estudada e, com base na profundidade de penetração, estima-se a resistência do concreto à compressão.")

st.write("As correlações extraídas nesse ensaio associam a profundidade de penetração à resistência à compressão. Devido a isso, torna-se fundamental conhecer previamente as propriedades do concreto ensaiado em laboratório, a fim de estabelecer correlações de resistência em estruturas reais.")

st.write("Devem-se também considerar as condições do ensaio e realizar um estudo preliminar para evitar áreas com alta concentração de armaduras, regiões com concreto carbonatado, presença de umidade no material e outros fatores que possam influenciar os resultados.")

st.write("Além disso, o ensaio deve contemplar concretos endurecidos de maior resistência, de modo que o pino não ultrapasse o limite de penetração estabelecido em norma.")

st.header(":deciduous_tree: Madeira")

st.write("A caracterização de peças em madeira segue o que está estabelecido na ABNT NBR 7190:2022. A norma estabelece que a caracterização das propriedades de resistência e rigidez da madeira devem ser obtidas na condição-padrão, quando a umidade das peças encontra-se em 12%. A umidade em base seca é dada por")

st.latex(r'''
    U_{\text{BS}}=\dfrac{m_{\text{inicial}}-m_{\text{seca}}}{m_{\text{seca}}}=\dfrac{m_{\text{água}}}{m_{\text{seca}}}
''')

st.markdown(
    "Além da umidade, deve-se levar em conta os diferentes tipos de densidade que podem ser medidos com amostras de madeira: "
    "Densidade básica ($\\rho_{\\text{b\\'{a}sica}}$) e densidade aparente ($\\rho_{\\text{aparente}}$). "
    "Essas grandezas são dadas por:"
)

st.latex(r'''
    \begin{matrix}
        \rho_{\text{básica}}=\dfrac{m_{\text{seca}}}{v_{\text{saturado}}} & \rho_{\text{aparente}}=\dfrac{m_{\text{aparente}}}{v_{\text{aparente}}}
    \end{matrix}
''')

st.write("As propriedades de resistência e rigidez podem ser corrigidas conforme as equações abaixo")

st.latex(r'''
    \begin{array}{rcl}
        f_{12}&=f_{U}\big(1+0.03(U-12)\big)\\
        E_{12}&=E_{U}\big(1+0.02(U-12)\big)
    \end{array}
''')

st.write("Com isso em mente, a caracterização das propriedades de resistência e rigidez pode ser feita utilizando-se diferentes métodos, como: vibração transversal, modos de vibração, flexão estática e de propagação de ondas de tensão.")

st.subheader("**Métodos utilizando a frequência de ressonância**")

st.markdown("**Método de vibração transversal**")

st.write("O método de vibração transversal consiste em submeter uma barra de madeira biapoiada nas extremidades a uma deflexão inicial e, em seguida, liberá-la para oscilar verticalmente. A partir dos sistema de medição utilizado, determina-se a frequência de ressonância fundamental e calcula-se o módulo de elasticidade (MOE) por meio da equação")

st.latex(r'''
    \text{MOE}=\dfrac{f^{2}WS^{3}}{2.46Ig}
''')

st.write("a partir do aparato experimental abaixo")

st.markdown("**Método dos modos de vibração**")

st.write("O método relacionado aos modos de vibração consiste na análise de Fourier do gráfico de amplitude do sinal num intervalo de frequências. Existem três modos de vibração que normalmente são utilizados e dividem-se em: longitudinal, flexural e torsional. O ensaio envolvendo este método consiste em impactar uma barra de madeira em um das extremidades e, a partir de microfones condensadores localizados na extremidade oposto e com um circuito medidor adequado, obtêm-se o gráfico de ação combinada de deslocamentos flexurais e torsionais. Após a decomposição dos gráficos para cada modo específico de vibração, determinam-se as frequências de ressonância da amostra ensaiada. Com esta grandeza em mãos, torna-se possível calcular o módulo de elasticidade e de cisalhamento, ou módulo de elasticidade transversal, conforme as equações abaixo por meio do modo de vibração longitudinal")

st.latex(r'''
    E=4\rho L^{2}\left(\!\dfrac{f_{L,n}}{n}\!\right)^{2}
''')

st.write("modo flexional")

st.latex(r'''
    E=\dfrac{4\pi^{2}L^{4}\rho f_{F,n}^{2}A}{Ik_{i}^{4}}
''')

st.write("ou modo torsional")

st.latex(r'''
    G=4\rho l^{2}\left(\dfrac{f_{n}^{T}}{n}\right)^{2}
''')

st.markdown("**Ensaio de flexão estática**")

st.write("Quando falamos do método de flexão estática, podemos usar tanto o ensaio de 3 pontos quanto o de 4 pontos para a determinação do módulo de elasticidade, porém, com a reformulação da ABNT NBR 7190, para lotes de florestas plantadas não homogêneos, é possível utilizar a parte quatro da norma para determinação do módulo de elasticidade na flexão estática a partir da equação")

st.latex(r'''
    E_{0}=\dfrac{1}{4}\left(\dfrac{L}{b}\right)^{\!\!3}\dfrac{\Delta F}{\Delta e}\dfrac{1}{h}
''')

st.write("obtida por meio da combinação das equações de deflexão no meio do vão livre a partir da equação de Euler e do momento de inércia da seção retangular em torno do eixo de menor inércia da barra")

st.latex(r'''
    \begin{matrix}
       \Delta e=\dfrac{\Delta FL^{3}}{48E_{0}I} & I = \dfrac{b^{3}h}{12}
    \end{matrix}
''')

st.write("seguindo o aparato experimental mostrado abaixo")

st.markdown("A premissa do ensaio é ser não destrutivo, por conta disso, a carga $\\Delta F$ aplicada é de $10\\%$ a $40\\%$ da máxima para ruptura da peça, e precisa ser estimada antes da realização do ensaio de flexão estática. Com a deflexão máxima $\\Delta e$ obtida por sensores de deslocamento, calcula-se o módulo de elasticidade $E_{0}$.")

st.markdown("**Método da propagação de ondas de tensão**")

st.markdown("Por fim, o método de propagação de ondas de tensão, envolve a propagação de ondas ultrassônicas por meio do impacto -- regime transiente -- ou por meio de transdutores que emitem feixes ultrassônicos com frequências acima da audível por humanos,  caracterizando o regime estacionário. Ambos os métodos podem ser utilizados em diferentes contextos de ensaios, como: Cronometragem do tempo de viagem do pulso acústico, pulso-eco e pitch and catch.")

st.markdown("**Barra viscoelástica submetida a um impacto**")

st.write("Para introduzir esses métodos, considere uma barra viscoelástica submetida a um impacto em uma das extremidades. Análogo ao que foi feito anteriormente para obtenção dos diferentes modos de vibração, a amostra é excitada repentinamente, num impacto de curta duração, produzindo, na extremidade impactada, uma onda de compressão/pressão que atravessa o material longitudinalmente até atingir a face da extremidade oposta, marcando o limite da interface madeira-ar. Devido à grande diferença de impedância acústica entre os dois meios, e considerando que o feixe acústico incide ortogonal à interface, a quase totalidade do feixe é refletida. Porém, a onda de compressão torna-se uma onda de tração, com a direção de vibração horizontal das partículas permanecendo inalterada, tendo em mente que a onda é longitudinal.")

st.write("A intensidade do sinal ultrassônico decai quanto maior a distância percorrida pelo feixe ultrassônico dentro do material. Utilizando-se um osciloscópio, com o sinal recebido, determina-se a curva de atenuação do sinal descrita pela equação")

st.latex(r'''
    I(x)=I_{0}e^{-\alpha x}
''')

st.markdown("nela, um dos parâmetros de maior interesse é o coeficiente de atenuação $\\alpha$, que descreve o quanto o sinal decai com base na distância percorrida, dado em dB/m")

st.write("Tal sequência de eventos é fundamental para o entendimento dos 3 ensaios citados anteriormente.")

st.markdown("**Cronometragem do tempo de propagação da onda de tensão**")

st.write("No ensaio de cronometragem do tempo de viagem do pulso acústico, a extremidade impactada pode possuir tanto acelerômetros quanto transdutores dependendo do circuito utilizado para a medição. Fundamentalmente, esse tipo de ensaio requer que os sensores sejam posicionados nas extremidades da barra nas faces laterais, já que o impacto ocorre na seção transversal. Associados a um cronômetro, um acelerômetro é responsável por captar o sinal da onda de compressão e iniciar a contagem do cronômetro. O pulso, ao alcançar a extremidade oposta é detectado por outro acelerômetro que envia o sinal para o cronômetro pausar a contagem. A partir do tempo obtido e utilizando conceitos de cinemática do movimento retilíneo e uniforme, determina-se a velocidade de propagação conhecendo-se o comprimento da barra ensaiada")

st.latex(r'''
    V=\dfrac{L}{\Delta t}
''')

st.markdown("**Método do pulso-eco**")

st.write("Quando se trata do método de pulso-eco, o aparato experimental consiste em utilizar um sensor, normalmente um transdutor, fixado na extremidade à que será impactada da barra. A onda de tensão de baixa frequência enviada através da barra alcança o sensor e a amplitude do sinal é medida em função do tempo. A distância entre dois pulsos mostrados na tela do osciloscópio estão relacionados ao tempo que o pulso demorou para viajar duas vezes o comprimento da barra, portanto, a relação da cinemática torna-se")

st.latex(r'''
    V=\dfrac{2L}{\Delta t}
''')

st.write("Neste método é interessante ressaltar que ao analisar a velocidade e aceleração das partículas em função do tempo, nota-se que a velocidade decai exponencialmente, enquanto que a aceleração permanece constante até que a propagação seja totalmente atenuada. Além disso o comportamento das curvas do sinal é distinto em cada caso. As partículas por estarem sujeita à vibração longitudinal causada pela onda de compressão, oscilam em torno de um ponto de equilíbrio. Se traçássemos um segmento vertical contendo este ponto, notaríamos que em metade do tempo a onda se move concordando com o sentido de propagação e, na outra metade, realiza um movimento que discorda do sentido positivo da propagação. Já com relação à aceleração das partículas, os pulsos ocupam somente o primeiro quadrante do gráfico, mostrando que a aceleração pode ser maior ou igual a zero, porém, sempre concorda com o sentido da onda de compressão.")

st.markdown("***Pitch and catch***")

st.write("No método *pitch and catch* o aparato consiste na associação de transdutores, um de emissão e outro de recepção do sinal acústico, a um osciloscópio. Diferente dos métodos que envolvem impactar o espécime de forma abrupta, neste a emissão origina-se do sinal elétrico enviado pelo osciloscópio através dos cabos a ele conectados, transmissão para o transdutor emissor e conversão do sinal elétrico pelo transdutor em ondas mecânicas que atravessam o material. Os transdutores, dispostos nas faces laterais nos extremos da amostra longilínea, são responsáveis pela emissão e recepção do sinal. Neste ensaio, o transdutor receptor, capta o sinal e o osciloscópio mostra a amplitude da tensão em volts como função do tempo. Esse método também pode ser utilizado na obtenção das grandezas mostradas anteriormente.")

st.markdown("**Posicionamento dos acelerômetros**")

st.write("Durante os ensaios em barras de madeira, deve-se atentar quanto ao posicionamento dos acelerômetros na peça, tendo em vista que a intensidade do sinal depende diretamente do local em que eles se encontram ou quais faces eles são apoiados em relação à fonte de impacto.")