import streamlit as st
from database import (
    get_user_email_safely,
    update_user_activity
)

def inspecao_concreto():
    user_email = get_user_email_safely()
    user_role = st.session_state['user_role']

    update_user_activity(user_email, user_role, 'inspeção de estrututuras de concreto e madeira')

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.title("Ensaios não destrutivos para a inspeção de estruturas de madeira e concreto")

    col2.expander(":material/book: Sumário", expanded=True).markdown('''
        - [Ensaios não destrutivos para a inspeção de estruturas de madeira e concreto](#ensaios-nao-destrutivos-para-a-inspecao-de-estruturas-de-madeira-e-concreto)
            - [Início](#inicio)
            - [Madeira](#madeira)
                - [Cronometragem do tempo de viagem da onda de tensão](#cronometragem-do-tempo-de-viagem-da-onda-de-tensao)
                - [Penetrografia](#penetrografia)
                - [*Pilodyn*](#pilodyn)
                - [Tomografia acústica](#tomografia-acustica)
                - [Tomografia elétrica](#tomografia-eletrica)
                - [Termografia](#termografia)
                - [Radar de penetração de solo (GPR)](#radar-de-penetracao-de-solo-gpr)
        - [Concreto](#concreto)
            - [Método eletromagnético (Pacometria)](#metodo-eletromagnetico-pacometria)
                - [Pacometria no ensaio de esclerometria](#pacometria-no-ensaio-de-esclerometria)
                - [Pacometria no ensaio de ultrassonografia](#pacometria-no-ensaio-de-ultrassonografia)
                - [Pacometria no ensaio de potencial de corrosão](#pacometria-no-ensaio-de-potencial-de-corrosao)
                - [Pacometria no ensaio de resistividade elétrica](#pacometria-no-ensaio-de-resistividade-eletrica)
                - [Pacometria no ensaio de penetração de pinos](#pacometria-no-ensaio-de-penetracao-de-pinos)
            - [Ensaio de penetração de pinos](#ensaio-de-penetracao-de-pinos)
            - [Ensaio de raios X e $\\gamma$](#ensaio-de-raios-x-e-g-gammag)
            - [Ensaio de inspeção de imagens](#ensaio-de-inspecao-de-imagens)
            - [Ensaio de profundidade de carbonatação](#ensaio-de-profundidade-de-carbonatacao)
            - [Ensaio de resistividade elétrica](#ensaio-de-resistividade-eletrica)
            - [Ensaio de potencial de corrosão](#ensaio-de-potencial-de-corrosao)
            - [Radar de penetração de solo (GPR)](#radar-de-penetracao-de-solo-gpr)
            - [Termografia](#termografia)
    ''')

    col2.header("Início")

    col2.write("Quando se trata da inspeção de estruturas os ensaios não destrutivos têm se mostrado boas alternativas para os ensaios destrutivos até então utilizados isoladamente. Entretanto, com o avanço dos vários métodos de inspeção e da tecnologia empregada tornou-se mais ágil e confiável o diagnóstico das estruturas. Estas estão sempre presentes em nosso cotidiano variando entre diferentes tipos de materiais. A madeira por exemplo, ainda pouco empregada na construção de casas no Brasil, possui uso mais corriqueiro em países como os Estados Unidos. O concreto, por sua vez, é amplamente utilizado em todo o país compondo uma variedade de construções civis, sendo mais predominando que a madeira no setor. Todavia, apesar de ambos os materiais serem adequados para diversos tipos de construções e locais para a habitação e lazer humano, elas estão sujeitos ao desgaste e perde de resistência seja devido à fatores naturais decorrentes do tempo atmosférico ou devido a patologias decorrentes de falhas de processo. Sendo assim, inspecionar estruturas que possuem um papel ativo na sociedade sem ocasionar danos ou comprometimento às mesmas requer a utilização de métodos não destrutivos. Nesta seção serão discutidos os principais métodos utilizados tanto em estruturas de madeira quanto em concreto. Vale ressaltar que no caso da madeira, por ela ser proveniente do material biológico estruturas das árvores, diversos métodos que são utilizadas na madeira viva são estendidos para a madeira pós-abatimento, seja nas toras ou em peças estruturais, cabendo ao operador aplicá-las em diferentes contextos conforme a validação científica dos mesmos. Quanto ao concreto, sua inspeção requer levar em conta a presença da armadura em seu interior. Apesar do nome do ensaio ter como palavra chave o concreto, entender o efeito da armadura é fundamental para a tomada de decisão quanto a real qualidade do concreto inspecionado. A análise se iniciará pela madeira, mostrando ensaios como: o de cronometragem do tempo de viagem da onda de tensão, amplamente utilizado no setor florestal para avaliar a qualidade da madeira em árvores; o ensaio de penetrografia, que pode ser utilizado tanto em estruturas quanto em árvores para avaliar a qualidade da madeira do fuste por meio da análise das amplitudes de resistência à penetração e resistência à rotação; O ensaio de Pilodyn, parecido com o anterior no princípio por envolver a inserção de um metal de pequena espessura para aferir a densidade nas camadas mais superficiais; a tomografia acústica, que pode também ser vista como uma generalização do primeiro ensaio (cronometragem), onde vários sensores são distribuídos ao redor do tronco; o de tomografia elétrica, análogo ao anterior, porém ao invés de propagar ondas acústicas propaga-se corrente elétrica; o de termografia, baseado na detecção de falhas por meio das diferenças de temperatura na superfície do material analisado, fornecendo maior direcionamento à inspeção; o teste de tração, onde é realizada uma tração no tronco para simular a ação do vento e são medidas as cargas aplicadas e a deflexão do tronco para determinação da estabilidade e o GPR, utilizado para mapear o posicionamento das raízes das árvores no solo.")

    col2.header("Madeira")

    col2.subheader("Cronometragem do tempo de viagem da onda de tensão")

    col2.write("Este ensaio baseia-se em estimar o tempo de viagem de ondas de tensão através da seção transversal da madeira visando avaliar a sua qualidade em diferentes direções. O ensaio faz uso de dois acelerômetros que são posicionados diametralmente opostos no tronco da árvore e, com base num impacto induzido nos no tronco, um sistema de medição associado a ambos os acelerômetros capta os sinais transmitido e recebido e obtém o tempo de propagação. Conhecendo-se a distância entre os acelerômetros calcula-se a velocidade de propagação ao longo do tronco. Estudos já foram realizados para algumas espécies visando obter as velocidades típicas para cada uma, visando facilitar o processo de análise da qualidade interior do tronco quanto a presença de decaimento. A partir dos parâmetros de velocidade estabelecidos, dependendo do valor medido é possível aferir com boa assertividade, árvores com deterioração interna. Todavia, é importante ressaltar que a solução pode não ser definitiva em vários casos devido à vasta gama de espécies e características intrínsecas de cada indivíduo e condições ambientais. Desta maneira, a utilização de métodos complementares diretos pode aumentar a confiabilidade da avaliação e evitar que os abatimentos sejam feitos de forma desnecessária para condições de deterioração em que falsos positivos foram detectados. Tais métodos diretos podem envolver o uso de penetrógrafos e Pilodyn nas direções em que as medidas de velocidades gerarem maior dúvida quanto aos estado real do fuste. Também é importante frisar que outros métodos podem ser utilizados visando aumentar a confiabilidade da inspeção, porém, deve-se considerar a viabilidade dos métodos empregados com relação aos custos envolvidos e quanto ao tempo de execução do ensaio por árvore. Estima-se que, em média, o tempo gasto para realizar o ensaio de cronometragem do tempo de viagem da onda de tensão é de cerca de 2 minutos, enquanto um ensaio baseado no mesmo princípio como o de tomografia acústica leva cerca de 30 minutos. Ou seja, em ambos os casos existem incertezas envolvidas que requerem outros ensaios não destrutivos ou semi destrutivos para a validação, porém, resumir lançar mão de ensaios mais longos de serem realizados requer parcimônia e a avaliação de métodos que garantam tanto a confiabilidade e assertividade nos laudos realizados quanto escalabilidade, tendo em vista a atual situação de várias prefeituras do país que não dispõem de recursos mínimos para sequer adquirir equipamentos mais tecnológicos, limitando-se à inspeção visual. É importante ressaltar que cabe aos profissionais envolvidos na inspeção conhecerem cada espécie e o perfil de tomografia ultrassônica e de velocidades ao redor do tronco. Em algumas espécies, ocos no interior do tronco não necessariamente indicam uma condição de alto risco que exija o abatimento da árvore. Todavia, os estudos precisam avançar visando aprimorar os métodos para avaliação de risco nas árvores, tendo em vista que por ser um método indireto que utiliza ondas de tensão que possuem vários fatores que podem influenciar nas medidas, deve-se atentar quanto aos resultados obtidos visando minimizar decisões equivocadas quanto a condição do fuste.")

    col2.write("Retornando ao contexto do ensaio especificado nesta seção, além da avaliação da condição do fuste, é possível utilizar a cronometragem do tempo de viagem na direção longitudinal do tronco visando determinar a orientação das fibras, ou seja, o ângulo que elas forma em relação à vertical. O conceito por trás deste método consiste em posicionar os acelerômetros de modo que uma reta imaginária que os conecta possua diferentes angulações em relação à vertical, podendo começar em zero e aumentar gradualmente abrangendo ângulos pequenos. A rota com menor tempo de propagação é a que apresenta a direção paralela às fibras devido ao caminho preferencial tomado pelo feixe ultrassônico ao atravessar o material. Tal método tem se mostrado útil para a avaliação e apresenta boa correção com o ângulo medido após o abatimento das toras da árvore para confirmação dos resultados.")

    col2.subheader("Penetrografia")

    col2.write("Este ensaio caracteriza-se pela utilização de brocas de pequeno diâmetro -- micro brocas -- que são direcionadas para o interior da madeira e visa oferecer parâmetros associados à resistência à penetração e ao giro da broca durante a perfuração. Ele é considerado invasivo já que ocasiona na abertura de um orifício no material analisado, porém não gera danos à madeira de árvores vivas quando realizado de forma adequada, de modo que as próprias árvores são capazes de cicatrizar e preencher o local com madeira evitando o ataque de insetos ou fungos.")

    col2.write("Dessa forma, o ensaio de penetrografia baseia-se em duas premissas fundamentais: a demanda de potência à penetração e demanda de potência devido à rotação. Na primeira o atrito é desconsiderado e leva-se em conta somente a dificuldade da broca penetrar concentrando-se a análise em sua ponto. Em contrapartida, na demanda de potência devido à rotação, o atrito é uma grandeza de interesse e pode ser utilizado para avaliar a presença de material na porção lateral da broca com base na resistência apresentada.")

    col2.write("Com base nessas duas medidas é possível avaliar a condição do fuste já que a resistência à penetração pode fornecer dados relacionado à densidade do material, enquanto que a resistência à rotação fornece dados associados à presença de material na lateral da broca. O operador, após realizar o ensaio obtém as duas curvas associadas a cada parâmetro medido, também conhecidas como curvas de amplitude. Com base nisso é possível tomar decisões quanto ao estado do tronco após detectar regiões onda há rachaduras internas, regiões de deterioração, cavidades ou galerias e regiões de madeira sã.")

    col2.subheader("*Pilodyn*")

    col2.write("Equipamento manual de pequeno porte constituído de uma agulha na ponta. Possui a finalidade de determinar a qualidade da madeira na região mais próxima à casca avaliando se o material apresenta resistência à penetração adequada. Quanto maior a penetração da agulha, menor a densidade da madeira e vice-versa. Representa um método de medida direta da qualidade da madeira, podendo ser utilizado com outras técnicas para melhora da inspeção.")

    col2.subheader("Tomografia acústica")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("Este método é caracterizado pelo uso de um equipamento multi sensor com acelerômetros. Os acelerômetros são distribuídos ao redor do tronco, equidistantes e numa mesma altura ao longo da face lateral do tronco¹. O objetivo do ensaio é avaliar a qualidade da madeira no interior do fuste diferenciando entre regiões de madeira sã, com biodeterioração ou cavidades. Para isso, o ensaio baseia-se na propagação de ondas ultrassônicas no interior do tronco. Os múltiplos sensores distribuídos captam o sinal ultrassônico emitido por um acelerômetro impactado pelo martelo sônico e, com base no arranjo e na distribuição dos mesmos ao longo do tronco, determina-se a velocidade de propagação nas diferentes rotas que conectam o acelerômetro emissor aos receptores. Neste ensaio, é necessário que todos os acelerômetros sejam impactados para que a malha de difração tenha a maior quantidade de dados possível. A quantidade de acelerômetros utilizada varia de acordo com o diâmetro do tronco, mas na maior parte dos casos, 8 sensores oferecem análises representativas do estado do fuste.")

    col2.write("Outro aspecto relevante deste ensaio tem relação com os modelos interpoladores utilizados na diferenciação das velocidades. Os modelos entregam gráficos bidimensionais mostrando a seção do tronco analisada variando entre diferentes categorias ou faixas de velocidade. Velocidade mais lentas podem indicar cavidades ou deterioração da madeira no interior, enquanto que velocidade mais altas representam uma condição de madeira sã, com rigidez e resistência adequados.")

    col3.info("¹As alturas normalmente utilizadas são: Diâmetro à altura do peito (DAP) e diâmetro à altura do solo (DAS). Os mesmos são obtidos a partir da medida da circunferência do tronco. Ao assumir que o tronco é circular, a aproximação das medidas de diâmetro é feita pela equação $D=C/\\pi$ ou $r=C/(2\\pi)$")

    col2.subheader("Tomografia elétrica")

    col2.write("A tomografia elétrica é baseada em múltiplos sensores, de maneira semelhante ao ensaio de tomografia acústica. Porém, ao invés do ensaio ser baseado na propagação de ondas ultrassônicas no interior do tronco, é corrente elétrica. A partir da corrente propagada entre os sensores, mede-se a resistividade elétrica entre os diferentes pontos a partir da malha de difração estabelecida entre eles. Valores de resistividade mais baixos podem indicar locais com presença de deterioração e cavidades no interior do tronco, enquanto que altos valores de resistividade são bons indicativos de madeira sã com rigidez e resistência adequadas. É importante lembrar que esta técnica depende em grande parte da umidade no interior do tronco. Regiões mais úmidas tendem a apresentar menor resistividade, enquanto secas uma maior resistividade. Dessa forma, mesmo que haja cavidades no interior do fuste, ele pode não ser detectado dependendo de sua condição de umidade. A interpretação também requer cuidados, já que altos valores de resistividade no caso de cavidades secas não indicam rigidez e resistência estrutural da árvore. A análise deve ser feita de maneira atenta visando diferenciar regiões secas devido à cavidades ou madeira sã.")

    col2.subheader("Termografia")

    col2.write("A termografia é uma técnica que tem ganhado cada vez mais espaço no país, podendo ser utilizada para encontrar regiões com fissuras ou danos que podem ser visíveis dependendo dos procedimentos utilizados para a análise. Um fator limitante deste ensaio diz respeito aos horários em que a inspeção é realizada, já que o material requer uma janela de aquecimento ou resfriamento que permita ao equipamento registrar as diferenças de cor tendo em vista as mudanças que ocorrem nas propriedades de condutividade térmica do material podendo indicar locais com material degradado ou com cavidades mais internas que impactam na radiação captada nas camadas mais superficiais do mesmo.")

    col2.subheader("Radar de penetração de solo (GPR)")

    col2.write("O radar de penetração de solo, conhecido pela sigle em inglês, GPR, é utilizado para mapear o posicionamento das raízes no solo. Baseado na emissão e recepção de ondas eletromagnéticas em frequências típicas de ondas de rádio por meio de antenas, o sinal captado pela antena receptora é interpretado e, a partir do processamento do mesmo, é possível estimar o posicionamento das raízes de forma indireta com base na diferença de umidade e outros aspectos das raízes em relação ao solo. Estudos já foram realizados visando avaliar a viabilidade de utilizar o GPR na região do tronco da árvore de modo a identificar cavidades e deterioração no fuste. Todavia, ainda não é o método mais indicado em relação a outros mais consolidados como ensaios ultrassônicos e de penetrografia.")

    col2.header("Concreto")

    col2.subheader("Método eletromagnético (Pacometria)")

    col2.write("O método de pacometria utiliza o princípio eletromagnético para detecção de armaduras no concreto. Por meio da detecção, ele é capaz de obter a espessura do cobrimento, ou seja, a distância da superfície do concreto até à da armadura e estimar o diâmetro das armaduras sem necessidade de abertura de janelas de inspeção. Todavia, deve-se levar em conta os erros envolvidos na aferição de acordo com a profundidade das armaduras e seu arranjo no interior do concreto. Para isso, o máximo de informações relacionadas ao projeto da estrutura deve ser coletado visando melhor direcionamento dos profissionais responsáveis pela inspeção. Este ensaio possui a característica de fornecer apoio a diversos outros ensaios, já que em vários destes é necessário realizar mapeamento das armaduras na estrutura. Alguns dos exemplos serão discutidos a seguir para explanar os principais usos da pacometria em conjunto a outros ensaios.")

    col2.markdown("##### Pacometria no ensaio de esclerometria")

    col2.write("No ensaio de esclerometria, a pacometria deve ser realizada previamente visando mapear as armaduras na área de ensaio definida. Tal procedimento deve ser feito tendo em vista a influência que regiões com armadura exercem no índice esclerométrico obtido do impacto do esclerômetro, podendo superestimar o valor real do concreto. Por avaliar a dureza superficial do concreto nos primeiros $20\\,\\text{mm}$ de profundidade, cobrimentos com espessuras menores podem ocasionar imprecisões no ensaio de esclerometria, portanto, torna-se fundamental a detecção magnética de armaduras para a correta aferição do índice esclerométrico efetivo e, consequentemente, sua resistência à compressão.")

    col2.markdown("##### Pacometria no ensaio de ultrassonografia")

    col2.write("No ensaio de ultrassonografia, é imprescindível conhecer o correto posicionamento das armaduras no interior do concreto. Tendo em vista as diferentes velocidades de propagação do pulso acústico no concreto e no aço, sendo maior no aço, visando obter as propriedades de rigidez do concreto, deve-se considerar a influência que a armadura exerce nas velocidades medidas, de modo a adaptar o ensaio considerando sua influência ou visando distanciar-se da regiões onde a armadura está presente para minimizar seus efeitos na velocidade de propagação acústica. Neste ensaio, regiões com alta concentração de aço podem superestimar os valores de velocidade de propagação no concreto e, consequentemente, na sua resistência à compressão.")

    col2.markdown("##### Pacometria no ensaio de potencial de corrosão")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("Neste ensaio a pacometria é fundamental por permitir aos operadores localizar áreas para a abertura de janelas de inspeção para fixar o eletrodo de trabalho.²")

    col3.info("Polo positivo, vermelho.")

    col2.write("O ensaio de potencial de corrosão caracteriza-se por ser semi-destrutivo já que requer uma pequena quebra da estrutura para acesso às armaduras. Com a pacometria, a definição da janela torna-se um procedimento ágil de ser utilizado para que o ensaio seja o mínimo invasivo.")

    col2.markdown("##### Pacometria no ensaio de resistividade elétrica")

    col2.write("No ensaio de resistividade elétrica a pacometria é fundamental. Conforme é descrito no capítulo onde são detalhados os ensaios para inspeção de estruturas de concreto, vê-se que o ensaio de resistividade elétrica pode aferir tanto a predisposição das armaduras à corrosão, quanto a taxa de corrosão caso o fenômeno já tenha se iniciado. Nas duas situações saber a localização das armaduras é fundamental. No primeiro caso, as regiões de armadura tendem a ser evitadas, enquanto no segundo caso, são buscadas regiões com presença de armadura no local de medição da resistividade $\rho$. Portanto, é imprescindível que o ensaio de pacometria seja feito em conjunto com o de resistividade visando melhorar a qualidade dos dados obtidos.")

    col2.markdown("##### Pacometria no ensaio de penetração de pinos")

    col2.write("Neste ensaio, devido ao disparo de pinos em direção ao concreto realizado por um equipamento específico, torna-se imprescindível conhecer o posicionamento das armaduras já que o ensaio visa aferir a resistência à compressão com base na profundidade alcançada pelo pino até que toda a energia cinética e térmica ao longo do percurso fossem dissipadas. Devido à maior rigidez do aço em relação ao concreto, isso pode ocasionar em redução da profundidade de penetração do pino se disparado num região que contenha armaduras, podendo superestimar os valores de resistência já que uma menor profundidade está associada a uma maior resistência.")

    col2.subheader("Ensaio de penetração de pinos")

    col2.write("Neste ensaio, resgatando tópicos relacionados aos ensaios de caracterização do concreto, devido ao fato da profundidade de penetração dos pinos estar associada às propriedades de resistência e rigidez do concreto, ele pode ser enquadrado com um ensaio de inspeção. A inspeção nesse contexto visa, a partir dos dados de resistência e rigidez obtidos do ensaio verificar se o concreto atende ou não os parâmetros requeridos.")

    col2.subheader("Ensaio de raios X e $\\gamma$")

    col2.write("Ensaios deste tipo envolvem a utilização de radiação ionizante que atravessa os corpos de prova ou amostras estudadas e sensibilizam um filme radiográfico. Regiões mais escuras no filme são características de uma maior incidência de radiação, enquanto regiões mais claras evidenciam que a maior parte da radiação foi absorvida pelo material da amostra. Eles são úteis para avaliações qualitativas de estruturas, mas requerem atenção ao manipular os equipamentos devido aos riscos envolvidos à saúde humana, podendo gerar mutações nas células e câncer.")

    col2.write("Apesar de ambos lidarem com radiação ionizante, os dois ensaios se diferenciam em vários aspectos. Os que serão tratados aqui dizem respeito à: Fonte de radiação, energia de radiação, complexidade dos equipamentos, necessidade de energia elétrica, radiação pós-ensaio e espessura das amostras ensaiadas.")

    col2.markdown("O primeiro deles, a fonte de radiação, se difere em ambos. Quando se utiliza raios X, a radiação é proveniente de um tubo de raios catódicos, enquanto que no de raios $\\gamma$ uma pastilha radioativa é responsável pelas emissões. A energia de radiação também se difere. No raio X a energia depende da corrente elétrica $i$ e na tensão $U$ aplicadas e dependem do material a ser ensaiado. Já com raios $\\gamma$, o principal fator associado à energia tem relação com a composição ou elemento constituinte da pastilha radioativa. Alguns elementos geram radiação de maior intensidade, com maior capacidade de penetrar materiais. A complexidade dos equipamentos depende do tipo de material ensaiado. No ensaio de raios X, quanto maior a espessura da amostra, mais robusta é a instalação e equipamentos envolvidos no ensaio.")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("Quando se utiliza raios $\\gamma$, o aparato¹ não se altera da mesma forma, já que depende do elemento constituindo da pastilha radioativa para fornecer maior capacidade de penetração. O ensaio de raios X requer o uso de energia elétrica, enquanto o de raios $\\gamma$ não requer. Vale ressaltar que no primeiro, ao cessar o fornecimento de energia elétrica a radiação para de ser emitida. Já no ensaio por raios $\\gamma$, a radiação permanece sendo constantemente emitida, por conta disso, requer isolamento adequado dentro da fonte de radiação, por meio de metais pesados como o chumbo. No que diz respeito à espessura das amostras ensaiadas, o ensaio por raios $\\gamma$ é mais adequado por não exigir mudanças consideráveis no aparato quando comparado ao de raios X.")

    col3.info("¹O aparato do ensaio de raios $\\gamma$ normalmente consiste num equipamento que permite aos operadores, direcionarem, à distância, a pastilha radioativa até a extremidade de um tubo-guia com colimador para direcionar os raios para a amostra minimizando a exposição dos operadores. Este equipamento apresenta os seguintes elementos: Cabo de controle, podendo ser operado elétrica ou mecanicamente; fonte de radiação, responsável por comportar a pastilha radioativa, por isso requer bom isolamento; tubo-guia, para direcionar a pastilha e colimador. Além disso, o filme radiográfico contendo normalmente sais de prata em sua composição precisa ser disposto na extremidade oposta, ortogonal ao colimador, de modo que a amostra esteja entre ambos.")

    col2.markdown("Portanto, tendo em vista as características de cada ensaio, o uso deve ser adequado de acordo com a situação de cada inspeção. Em locais mais isolados, onde não é possível ter acesso à energia elétrica, recomenda-se o ensaio de raios $\\gamma$. Porém, em ambos os casos deve-se atentar quanto as condições de execução do ensaio, cercando-se a área com espaçamento adequado visando minimizar os riscos tanto para operadores quanto pessoas não envolvidas na inspeção.")

    col2.subheader("Ensaio de inspeção de imagens")

    col2.write("O ensaio de inspeção de imagens representa uma maneira de, por meio de fotografias tiradas de diferentes locais das estruturas, avaliar possíveis defeitos no material. As imagens capturadas podem fornecer um panorama mais superficial do que ocorre no concreto, porém, devido à facilidade de execução normalmente é o primeiro método não destrutivo empregado para avaliações. Todavia, cabe à operação o entendimento de que nem todas as patologias do concreto são detectadas a olho nu, devendo ser utilizadas outras técnicas complementares para que se tenha melhor detalhamento do real estado da estrutura. Casos como presença de carbonatação por exemplo requerem a realização de ensaios específicos, já que o fenômeno não altera as características visuais do concreto, podendo passar despercebido nas inspeções. Além disso, descontinuidades subsuperficiais e internas são inviáveis de serem avaliadas por imagens da área externa ou superficial do concreto. Dessa forma, é importante lembrar que apesar do método de inspeção de imagens poder ser utilizado para inspeção do concreto, o diagnóstico relacionado ao estado da estrutura não pode ser resumido a este ensaio, sendo imprescindível a utilização de métodos mais tecnológicos além da percepção humana.")

    col2.subheader("Ensaio de profundidade de carbonatação")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("O ensaio de profundidade de carbonatação é imprescindível de ser realizado em estruturas de concreto. Baseado no indicador de fenolftaleína, ele permite diferenciar partes da estrutura que estão com $\\text{pH}>9$ por meio da coloração rosada presente no local. Entretanto, no caso da carbonatação, devido a tendência de redução no valor do pH, regiões carbonatadas tendem a ficar incolores pelo indicador. O fenômeno químico tratado, se não acompanhado e corrigido de forma correta, pode ocasionar sérios riscos à integridade do concreto e das armaduras em seu interior. Ele é caracterizado por não ser visível a olho nu, necessitando do teste indicado anteriormente por meio do indicador de fenolftaleína. No concreto, a presença de carbonatação tende a aumentar a dureza do concreto devido à característica rochosa do material, de modo que sua resistência à compressão tende a aumentar. Todavia, no que diz respeito ao aço das armaduras, ele apresenta um risco à integridade já que colabora para a despassivação das armaduras, aumentando a susceptibilidade do material à corrosão.")

    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Reinforcement_corrosion.JPG/960px-Reinforcement_corrosion.JPG", caption="Corrosion of reinforcement in concrete, dgania b, israel")

    col2.write("O processo de despassivação ocorre normalmente quando a frente de carbonatação está muito avançada, a ponto de ultrapassar a profundidade das armaduras. Para que a carbonatação ocorra, diferentes elos da cadeia de riscos à estrutura precisam ser ligados. A conexão dos elos depende desde as condições de dimensionamento quanto a utilização de materiais no projeto. Também é cabível citar as condições de confecção da estrutura e suas partes, tendo em vista a execução inadequada desses processos pode aumentar a quantidade de fragilidades na estrutura. A fragilidade é uma função que também depende do ambiente, ou seja, alguns ambientes podem ser mais agressivos ao concreto e degradá-lo com maior velocidade.")

    col2.markdown("Para que a carbonatação ocorra, é necessário que o concreto apresente fissuras que viabilizem a entrada de água e gás carbônico em seu interior. O gás carbônico ($\\text{CO}_{2}$) do ar é capaz de reagir com a água no interior das fissuras e produzir o ácido carbônico ($\\text{H}_{2}\\text{CO}_{3}$), conforme a equação abaixo")

    col2.latex(
        r"\text{H}_{2}\text{O} + \text{CO}_{2} \rightarrow \underset{\text{(Ácido carbônico)}}{\text{H}_{2}\text{CO}_{3}}"
    )

    col2.markdown("Em seguida, o ácido carbônico presente no interior da fissura, reage com o hidróxido de cálcio ($\\text{Ca(OH)}_{2}$ do concreto endurecido, formando o carbonato de cálcio ($\\text{CaCO}_{3}$), conforme a equação abaixo")

    col2.latex(r"\text{H}_2\text{CO}_3 + \text{Ca(OH)}_2 \rightarrow \text{CaCO}_3 + \text{H}_2\text{O}")

    col2.write("Dessa forma, conforme observado nas duas etapas é possível afirmar que além da produção de carbonato de cálcio ocorre uma tendência de diminuição do pH do concreto. O concreto normalmente apresenta pH alcalino, em torno de 13. Entretanto, a produção de carbonato de cálcio tende a modificar o pH de alcalino para neutro na região.")

    col2.write("Com o avanço deste processo, a redução de pH na parte em concreto ocasiona numa maior susceptibilidade das armaduras à despassivação e, posteriormente, à corrosão.")

    col2.markdown("O princípio de corrosão considerando um caso em que a frente de carbonatação apresenta avanço acentuado, causando despassivação, depende do ferro presente no aço das armaduras. O ferro em sua forma neutra, ao doar 2 elétrons, é capaz de produzir o íon ferro ($\\text{Fe}^{2+}$), sua forma carregada")

    col2.latex(r"\text{Fe} \rightarrow \text{Fe}^{2+} + 2\,\text{e}^{-}")

    col2.write("No caso em que as armaduras entram em contato com o oxigênio do ar atmosférico e da água seja pela elevada umidade local ou devido às precipitações, na presença dos elétrons livres presentes na armadura, o íon hidroxila é produzido conforme a equação abaixo")

    col2.latex(r"\frac{1}{2}\text{O}_2 + \text{H}_2\text{O} + 2\,\text{e}^{-} \rightarrow 2\,\text{OH}^{-}")

    col2.write("Na presença de água, a hidroxila produzida apresenta maior mobilidade. Na presença do íon ferro produzido na penúltima equação, forma-se o hidróxido de ferro, caracterizado pela camada de ferrugem observada no aço")

    col2.latex(r"\text{Fe}^{2+} + 2\,\text{OH}^{-} \rightarrow \underset{\text{Ferrugem}}{\text{Fe(OH)}_2}")

    col2.markdown("A corrosão também pode ocorrer por ação do íon cloreto ($\\text{Cl}^{-}$). Ao atuar no concreto, pode produzir, na presença de água, ácido clorídrico, reduzindo o pH do material, conforme a equação abaixo")

    col2.latex(r"\text{H}_2\text{O} + \text{Cl}^{-} \rightarrow \text{HCl} + \text{O}_2")

    col2.write("Em contrapartida, no aço presente na armadura as etapas de corrosão consistem na produção de cloreto férrico ($\\text{FeCl}_{2}$) a partir da reação entre o íon cloreto e o íon ferro conforme mostrado abaixo")

    col2.latex(r"\text{Fe}^{2+} + 2\,\text{Cl}^{-} \rightarrow \text{FeCl}_2")

    col2.write("e, na presença do íon hidroxila, ocorre a seguinte reação")

    col2.latex(r"\text{FeCl}_2 + \text{OH}^{-} \rightarrow \text{Fe(OH)}_2 + 2\,\text{Cl}^{-}")

    col2.subheader("Ensaio de resistividade elétrica")

    col2.markdown("Este ensaio visa avaliar a predisposição que as armaduras possuem à corrosão com base em medidas de resistividade feitas na superfície do concreto. A resistividade $\\rho$, é uma grandeza física que quantifica a dificuldade que um determinado material apresenta em conduzir corrente elétrica e pode ser expressa conforme a equação")

    col2.latex(r"\rho=\dfrac{RA}{L}")

    col2.markdown("onde $R$ é a resistência elétrica, medida em $\\Omega$, $A$ é a área da seção transversal do material condutor, e $L$ o comprimento do condutor. Para aferições realizadas no concreto, as medidas são normalmente expressas em $\\text{k}\\Omega\\,\\text{cm}$. Valores mais baixos de resistividade representam um risco à qualidade da estrutura, podendo ocasionar numa menor longevidade e durabilidade do material.")

    col2.write("Deve-se atentar ao realizar o ensaio de resistividade elétrica quanto a idade da estrutura ensaiada. Estruturas recém construídas tendem a apresentar valores mais baixos de resistividade, tendo em vista o maior teor de água em seu interior. Nesse caso, adaptações devem ser realizadas de modo a considerar a idade do concreto. Em estruturas mais antigas, as medidas realizadas tendem a ser mais confiáveis e refletem com maior fidelidade o estado do concreto. Nesse contexto, valores mais altos de resistividade são preferíveis aos mais baixos.")

    col2.write("Outro aspecto importante deste ensaio relaciona-se com o preparo da área de ensaio. Os profissionais que o realizam devem se certificar da: correta limpeza e escarificação da superfície do concreto; evitar áreas com presença de armadura, tendo em vista a influência do aço que reduz a resistividade; áreas com carbonatação, já que esta eleva os valores de resistividade e leva os operadores a interpretações incorretas em relação a durabilidade das armaduras; locais com excesso de umidade e superfícies irregulares, com presença de emboço; entre outros fatores. Dessa forma, ensaios de profundidade de carbonatação e de detecção magnética das armaduras são fundamentais como requisitos pré-ensaio de resistividade.")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("Tendo em vista a importância da correta interpretação dos dados de ensaio, pesquisadores elaboraram esta tabela mostrando como a avaliação da predisposição das armaduras à corrosão pode ser interpretada com base nos valores obtidos em diferentes condições: Estimativa da probabilidade de corrosão¹ e indicação da taxa de corrosão.²")

    col3.info("¹A aferição deve ser feita na superfície do concreto evitando áreas com presença de armadura.")

    col3.info("²A aferição deve ser feita na superfície do concreto em áreas com presença de armadura, análogo ao método de potencial de corrosão.")

    data = [
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$\\rho\\geq 100$",      "Risco de corrosão": "🟢 Insignificante"},
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$50 < \\rho < 100$", "Risco de corrosão": "🟡 Baixo"},
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$10 < \\rho < 50$",  "Risco de corrosão": "🟠 Moderado"},
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$\\rho\\leq 10$",       "Risco de corrosão": "🔴 Elevado"},
    ]

    col2.table(data)

    col2.caption("Estimativa de probabilidade de corrosão.")

    data = [
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$\\rho > 100$",      "Taxa de corrosão": "🟡 Baixa"},
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$10 < \\rho < 20$",  "Taxa de corrosão": "🟠 Baixa a moderada"},
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$5 < \\rho < 10$",   "Taxa de corrosão": "🔴 Alta"},
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$\\rho < 5$",        "Taxa de corrosão": "🟣 Muito alta"},
    ]

    col2.table(data)

    col2.caption("Indicação da taxa de corrosão.")

    col2.subheader("Ensaio de potencial de corrosão")

    col2.write("O ensaio de potencial de corrosão tem o objetivo de estimar a probabilidade de corrosão nas armaduras com base na diferença de potencial medida entre os polos dos eletrodos de trabalho e de referência. A tabela abaixo mostra as probabilidades de corrosão com base na tensão medida conforme a ASTM 876-C:2022")

    data = [
        {"U (mV)": "$U > -200$",        "Probabilidade (%)": "🟢 5"},
        {"U (mV)": "$-350 < U < -200$", "Probabilidade (%)": "🟠 Duvidosa"},
        {"U (mV)": "$U < -350$",        "Probabilidade (%)": "🔴 95"},
    ]

    col2.table(data)

    col2.write("Para realizar o ensaio, o operador precisa inicialmente definir o lote ou área de inspeção. Em seguida, com um martelo específico, realizar o ensaio de percussão visando encontrar regiões com som cavo. Após isso, o ensaio de pacometria é fundamental para detecção das armaduras conforme é descrito numa seção deste documento. A partir do momento em que a área de ensaio é definida, deve ser realizada a escarificação do local garantindo uniformidade e limpeza do concreto para que os valores de tensão sejam menos influenciados. Em seguida, o operador deve abrir uma janela de inspeção visando acessar parte das armaduras. Nesta etapa, é interessante a realização do ensaio de carbonatação ao longo da janela aberta, já que o ensaio é capaz de, com base na profundidade de carbonatação aferida pelo indicador de fenolftaleína, mostrar se a armadura já passou por processo de despassivação. Após esta etapa, deve aplicar uma solução de tensoativo (detergente) e fixar o eletrodo de trabalho (Vermelho, +) na armadura exposta na janela de inspeção. Com o outro polo -- eletrodo de referência (Porta COM, preto, -) -- realizar as medidas em vários pontos da área de inspeção.")

    col2.markdown("O eletrodo de referência, normalmente composto por $\\text{Cu}/\\text{CuSO}_{4}$, pode ser confeccionado com os seguintes itens: Tubo roscado nas extremidades; tampa traseira contendo encaixe para o *plug* da porta COM, o-ring e haste de cobre; tampa dianteira contendo o-ring, disco de madeira e esponja; a solução no interior é uma combinação de água e sulfato de cobre até que haja formação de precipitado na solução (ponto de supersaturação).")

    col2.write("O tratamento de dados deste ensaio recomendado pela ASTM requer a construção de curvas equipotenciais visando detectar as áreas com maior incidência de corrosão nas armaduras. As medidas para corrigir o processo de corrosão envolvem a utilização de inibidores seguida de inspeções periódicas pós-aplicação para acompanhamento do local.")

    col2.subheader("Radar de penetração de solo (GPR)")

    col2.write("No contexto de ensaios envolvendo estruturas de concreto, o GPR se mostra útil para mapeamento das armaduras da estrutura, podendo fornecer modelos 3D de área mapeadas com precisão e permitindo aos profissionais envolvidos ficarem mais a par das condições internas da estrutura, seja em casos em que as informações relacionadas à estrutura são escassas ou para auxiliar em outros tipos de ensaios onde é de interesse da operação saber o posicionamento exato das armaduras no interior do concreto.")

    col2.subheader("Termografia")

    col2.write("No concreto, o ensaio de termografia pode ser utilizado para detectar falhas superficiais ou subsuperficiais cujos defeitos reflitam na radiação captada na superfície do concreto. É comum sua utilização para detectar regiões com desplacamento do concreto, fissuras e regiões com umidade. Em casos específicos é possível detectar a presença das armaduras. Análogo ao que ocorre em estruturas de madeira, no concreto, falhas que promovam a existência de vazios ou umidade na estrutura modificam as propriedades térmicas de condução do material e, consequentemente, regiões sãs e com defeitos aquecem e esfriam em tempos distintos, apresentando gradientes de temperatura que permitem detectar as falhas com melhor direcionamento. Todavia, é um método que requer o uso de outros métodos não destrutivos permitindo que a inspeção seja detalhada o suficiente para estimar os danos, principalmente em regiões profundas e mais internas da estrutura de concreto.")

if __name__ == "__main__":
    inspecao_concreto()