import streamlit as st
from database import (
    get_user_email_safely,
    update_user_activity
)

def inspecao_de_arvores():
    user_email = get_user_email_safely()
    user_role = st.session_state['user_role']

    update_user_activity(user_email, user_role, 'inspeção de árvores')

    col1, col2, col3 = st.columns([1, 3, 1])

    col2.title("Ensaios não destrutivos para inspeção de árvores urbanas")

    col2.expander(":material/book: Sumário", expanded=False).markdown('''
        - [Ensaios não destrutivos para inspeção de árvores urbanas](#ensaios-nao-destrutivos-para-inspecao-de-arvores-urbanas)
            - [Inspeção técnica nível 3](#inspecao-tecnica-nivel-3)
                - [Drone](#drone)
                - [Trabalho em altura em árvores](#trabalho-em-altura-em-arvores)
                - [Espada de ar](#espada-de-ar)
                - [Tomografia](#tomografia)
                - [Sonda](#sonda)
                - [Modelos probabilísticos](#modelos-probabilisticos)
                - [Clinômetro](#clinometro)
                - [Hipsômetro](#hipsometro)
                - [Trado de incremento](#trado-de-incremento)
                - [Câmeras termográficas](#cameras-termograficas)
                - [Ensaio de ancoragem](#ensaio-de-ancoragem)
                - [Laudo de inspeção](#laudo-de-inspecao)
    ''')                                                             

    col3.warning("""
    🌴 **I Congresso de Manejo e Conservação de Árvores Urbanas – Painel 3 (24/03)**  
    **Tema:** Manutenção de Árvores Urbanas e Avaliação do Risco  
    **Mediador:** Rogério Bobrowski (UNICENTRO)  

    📌 **Palestras:**
    - *Fisiologia das árvores em ambiente urbano* – Daniela Biondi (UFPR)  
    - *Tecnologias aplicadas à manutenção de árvores* – Gustavo Garcia (Unicamp)  
    - *Tecnologia empregada para análise de risco em árvores valiosas* – Tania Cristina Castroviejo (Pd Instrumentos)  
    - *Desafios para a padronização dos procedimentos técnicos de análise de risco* – Sérgio Brazolin (IPT – SP)  

    ▶️ [Assistir no YouTube](https://www.youtube.com/watch?v=fozt9dPI17o)
    """)

    
    col2.write("Os principais ensaios não destrutivos para inspeção  de árvores urbanas estão em conformidade com a ABNT NBR 16246-3:2019. Ela trata da avaliação de risco das árvores urbanas trazendo especificando as práticas e equipamentos que devem ser utilizados em cada nível de inspeção.")
    col2.write("A inspeção técnica de nível 3 é a mais avançada entre todas as técnicas. Cabe aos técnicos e profissionais que a executam realizar a inspeção com técnicas de nível 2 visando ter uma panorama geral da árvore inspecionada. A de nível 2 consiste em etapas como: Inspeção em 360° ao redor da árvore visando identificar locais com fragilidades como ocos, fissuras, crescimento desordenado de fungos, perda de vitalidade, ataque de insetos xilófagos e galhos secos. Para isso, o profissional pode lançar mão de binóculos, trena florestal, clinômetro¹, hipsômetro² e trado de incremento³.")

    col1.info("¹Dispositivo utilizado para a medição de ângulo, facilitando cálculos dendrométricos")

    col1.info("²Dispositivo utilizado para calcular a altura das árvores de forma direta. O princípio de funcionamento é análogo ao do clinômetro, porém no hipsômetro os cálculos são realizados e mostrados em seu visor agilizando as etapas de cálculo manual.")

    col1.info("³Dispositivo manual normalmente utilizado para extrair amostras à altura do peito do operador, tendo em vista a necessidade de um posicionamento adequado para vencer a resistência do tronco durante o processo de extração das amostras cilíndricas} para extração de amostras do tronco. A utilização de martelo emborrachado para o ensaio de percussão pode ser feita objetivando encontrar locais com som cavo que possam indicar locais de fragilidade estrutural, seja por biodeterioração ou cavidades.")

    col2.header("Inspeção técnica nível 3")

    col2.write("Feito isso, a técnica de nível 3 caracteriza-se pelo uso de tecnologias mais avançadas para inspeção podendo utilizar práticas e equipamentos como:")

    col2.subheader("Drone")

    col2.write("O uso de aeronaves remotamente pilotadas (RPA), popularmente conhecidas como drones¹, tem se tornado cada vez mais frequente em inspeções arbóreas de nível 3. Esse recurso permite a obtenção de imagens e vídeos em alta resolução da copa, do tronco e de regiões de difícil acesso, reduzindo a necessidade de trabalhos em altura e aumentando a segurança da equipe responsável pela inspeção.")

    col3.info("¹Pode ser utilizado em locais de difícil acesso, quando as condições de escalada não forem adequadas para coletar dados em forma de imagens.")

    col2.write("A principal vantagem do drone está na possibilidade de realizar diagnósticos preliminares de forma rápida e não invasiva, abrangendo grandes áreas com menor custo e tempo de execução em comparação com métodos tradicionais. Por meio de sensores ópticos, câmeras de alta definição e, em alguns casos, câmeras multiespectrais ou termográficas, é possível identificar:")

    col2.markdown("""
    - sinais de estresse fisiológico, como desfolha, clorose ou necrose foliar;
    - falhas estruturais, como rachaduras e cavidades no tronco ou nas ramificações;
    - padrões de crescimento anômalos ou assimetrias na copa;
    - presença de pragas, fungos ou outros agentes bióticos;
    - interferências com edificações, redes elétricas ou mobiliário urbano.
    """)

    col2.write("Apesar de suas vantagens, o uso de drones em inspeções arbóreas apresenta limitações, como a dificuldade de visualização de defeitos internos (ocultos no tronco ou nas raízes) e a dependência de condições climáticas favoráveis, especialmente em relação à velocidade do vento e à luminosidade. Além disso, sua utilização deve estar de acordo com as normas vigentes da Agência Nacional de Aviação Civil (ANAC), que regulamenta o voo de aeronaves remotamente pilotadas em áreas urbanas, exigindo treinamento específico e, em alguns casos, cadastro da aeronave.")

    col2.write("Portanto, o drone deve ser entendido como uma ferramenta complementar às demais técnicas de inspeção arbórea. Quando associado a métodos de contato direto, como tomografia, penetrografia e análise com espada de ar, pode fornecer um diagnóstico mais completo da condição estrutural e fitossanitária das árvores urbanas.")

    col2.subheader("Trabalho em altura em árvores")

    col1, col2, col3 = st.columns([1, 3, 1])

    col2.write("O trabalho em altura¹ aplicado à inspeção de árvores consiste no acesso direto à copa ou a pontos específicos do tronco e das ramificações, por meio de técnicas de escalada, plataformas elevatórias ou andaimes. Esse método possibilita a realização de ensaios não destrutivos e observações visuais em regiões que não podem ser alcançadas a partir do solo, garantindo maior abrangência na avaliação fitossanitária e estrutural da árvore.")

    col3.info("¹Qualquer trabalho realizado acima de 2 m de altura exige os requisitos de segurança previstos na NR35.")

    col1, col2, col3, col4 = st.columns([1, 1, 2, 1])

    col2.write("As técnicas de escalada arbórea seguem princípios semelhantes aos utilizados em trabalhos verticais em edificações, sendo indispensável o uso de equipamentos de proteção individual (EPI) e de sistemas de ancoragem que garantam redundância e segurança. Os principais equipamentos incluem: capacete com jugular, cinturão tipo paraquedista, cordas dinâmicas ou semiestáticas, mosquetões com trava, talabartes e freios de descida. Para maior segurança, recomenda-se a utilização de dois pontos independentes de ancoragem durante a execução do procedimento.")

    col3.video("https://www.youtube.com/watch?v=CH2RBFUR5aA")

    col1, col2, col3 = st.columns([1, 3, 1])

    col2.write("A legislação brasileira sobre segurança do trabalho em altura é regida pela NR-35, que estabelece requisitos mínimos e medidas de proteção. Embora voltada ao ambiente industrial e de construção civil, essa norma serve como referência também para trabalhos de inspeção em arborização urbana, devendo ser adaptada às especificidades do meio natural.")

    col2.write("As principais vantagens do trabalho em altura em árvores incluem a inspeção detalhada de cavidades, fendas, rachaduras, apodrecimentos e outros defeitos que não são visíveis a partir do solo, além da possibilidade de aplicação localizada de ensaios, como penetrografia, tomografia e coleta de amostras com trado de incremento. Entretanto, os riscos associados ao acesso elevado, à movimentação sobre galhos e à eventual fragilidade estrutural da árvore demandam planejamento prévio, escolha adequada de técnicas e equipamentos, bem como treinamento especializado da equipe envolvida.")

    col2.write("Portanto, o trabalho em altura em árvores deve ser entendido como uma técnica complementar de inspeção, de aplicação restrita a situações em que os métodos realizados a partir do solo não sejam suficientes para uma avaliação confiável da segurança e estabilidade da árvore.")

    col2.subheader("Espada de ar")

    col2.write("A espada de ar é um equipamento amplamente utilizado em inspeções de árvores urbanas, sobretudo para a avaliação do sistema radicular. O método consiste na injeção de ar comprimido em alta pressão direcionada ao solo, promovendo a desagregação mecânica das partículas sem causar cortes ou danos significativos às raízes. Dessa forma, torna-se possível expor parte do sistema radicular para análise visual, coleta de dados e identificação de eventuais patologias.")

    col2.write("O uso da espada de ar apresenta diversas vantagens em relação a métodos tradicionais de escavação, como o uso de ferramentas manuais ou mecanizadas. Enquanto estas podem provocar lesões graves às raízes ou até mesmo comprometer a estabilidade da árvore, a técnica com ar comprimido preserva a integridade fisiológica do sistema radicular, permitindo que a planta mantenha suas funções vitais. Além disso, o procedimento é menos invasivo e possibilita a recuperação mais rápida do solo após a inspeção.")

    col2.write("A inspeção com espada de ar é recomendada em situações que envolvem:")

    col2.markdown("""
        - avaliação de ancoragem e distribuição das raízes principais;
        - investigação de danos mecânicos, apodrecimento ou processos de deterioração no sistema radicular;
        - análise das condições do solo, como compactação e presença de barreiras físicas que limitem o desenvolvimento radicular;
        - planejamento de intervenções urbanísticas em áreas próximas às árvores, minimizando riscos à sua estabilidade.
    """)

    col2.write("Apesar de suas vantagens, o método requer cuidados específicos, como o controle da pressão do ar para evitar danos a raízes finas, a delimitação criteriosa das áreas a serem escavadas e a utilização de equipamentos de proteção individual devido ao elevado ruído e à projeção de partículas. O uso deve ser conduzido por equipe treinada, capaz de interpretar corretamente os resultados obtidos.")

    col2.write("Assim, a espada de ar se consolidou como uma ferramenta eficaz e de alta aplicabilidade em inspeções arbóreas, proporcionando informações detalhadas sobre a saúde e a estabilidade das árvores com mínima interferência em sua estrutura e fisiologia.")

    col2.subheader("Tomografia")

    col1, col2, col3 = st.columns([1, 3, 1])

    col1.image(
        "https://upload.wikimedia.org/wikipedia/commons/b/bc/Badanie_drzewa_tomografem_akustycznym.jpg",
        caption=(
            "Tomografia acústica em árvore — imagem de Tomasz Majchrzak, "
            "disponível na Wikimedia Commons (CC BY-SA 4.0)."
        )
    )


    col2.write("Tanto o alburno como o cerne fazem parte do xilema secundário. O caule aumenta muito mais de diâmetro na periferia. O raio parenquimático tende a sofrer dilatação na região do floema, devido ao maior crescimento da periferia. Ele está presente tanto no xilema quanto no floema. O floema secundário é formado por células condutoras como os elementos de tubo crivado e suas células companheiras, raio parenquimático e tecidos de sustentação, podendo ser fibras ou esclereides. Da mesma forma do que no floema, no câmbio temos as iniciais fusiformes e as radiais. As radiais produzem raio parenquimático para dentro e para fora em relação ao câmbio. Já as fusiformes produzem os elementos de tubo crivado e suas células companheiras e os elementos axiais como fibras e esclereides. Em coníferas o xilema normalmente é composto somente por traqueides e células de raio, raramente parênquima axial. No floema, há presença de células crivadas em sucessão. Devido ao rompimento que ocorre nas camadas de maior diâmetro na epiderme, o felogênio é responsável por produzir súber para fora e feloderme para dentro.")

    data = [
        {"Atributo": "Folhas", "Gimnospermas": "Aciculifoliadas", "Angiospermas": "Latifoliadas"},
        {"Atributo": "Elementos de vaso", "Gimnospermas": "Não", "Angiospermas": "Sim"},
        {"Atributo": "Fruto", "Gimnospermas": "Não", "Angiospermas": "Sim"},
        {"Atributo": "Exemplos", "Gimnospermas": "Araucária, pinus", "Angiospermas": "Quase todas as nativas"},
        {"Atributo": "Flores", "Gimnospermas": "Não", "Angiospermas": "Sim"},
        {"Atributo": "Casca ao redor das sementes", "Gimnospermas": "Não", "Angiospermas": "Sim"},
        {"Atributo": "Sementes ao redor de um eixo", "Gimnospermas": "Sim", "Angiospermas": "Não"},
    ]

    col2.table(data)

    col2.write("As angiospermas englobam as monocotiledôneas (coco, milho, arroz e trigo) e as dicotiledôneas (soja, trigo, amendoim e café).")

    col2.subheader("Sonda")

    col2.write("Engloba diferentes métodos que podem ser utilizados para a sondagem da madeira como: espaçamento das fendas, profundidade de fissuras, retirada de amostras e verificação da dureza a partir de impactos na superfície.")

    col2.subheader("Modelos probabilísticos")

    col2.write("No contexto da inspeção de nível 3, os modelos probabilísticos e estatísticos desempenham papel essencial, pois permitem transformar os dados obtidos nos ensaios em estimativas quantitativas de risco. Diferentemente das inspeções de nível 1 e 2, que são majoritariamente visuais e qualitativas, aqui as medições alimentam modelos matemáticos que quantificam a probabilidade de falha da árvore em diferentes cenários.")

    col2.write("O princípio fundamental é que a árvore, por ser um organismo vivo e heterogêneo, apresenta incertezas que inviabilizam diagnósticos determinísticos. Dessa forma, recorre-se a distribuições de probabilidade que representam a variabilidade das propriedades da madeira, da integridade radicular e do comportamento estrutural frente a esforços externos, como vento e saturação do solo.")

    col2.write("Entre os modelos aplicados destacam-se:")

    col2.markdown("""
        - Modelos de confiabilidade estrutural, que utilizam parâmetros obtidos em ensaios (módulo de elasticidade, resistência residual, rigidez radicular) para estimar a probabilidade de ruptura;
        - Modelos bayesianos, que permitem atualizar o risco à medida que novas inspeções e dados são incorporados, reduzindo a incerteza ao longo do tempo;
        - Distribuições estatísticas de resistência, como normal, lognormal ou Weibull, que descrevem a variabilidade da resistência da madeira em função da espécie e do estado fitossanitário;
        - Simulações de Monte Carlo, que possibilitam avaliar cenários complexos, variando condições ambientais como intensidade do vento, umidade do solo e presença de defeitos internos.
    """)

    col2.write("Com isso, a inspeção de nível 3 não se limita a identificar defeitos, mas busca quantificar o risco associado, oferecendo subsídios técnicos robustos para a decisão sobre manejo, monitoramento ou remoção. A utilização de modelos probabilísticos garante maior objetividade e transparência ao processo, reduzindo a subjetividade inerente às inspeções puramente visuais.")

    col2.subheader("Clinômetro")

    col2.write("O clinômetro é um equipamento amplamente utilizado em inspeções arbóreas para a medição de ângulos e inclinações. Sua aplicação mais comum em arborização urbana consiste na estimativa da altura de árvores por meio da medição do ângulo de inclinação em relação à horizontal, associada à distância entre o observador e a base do tronco. A partir desses dados, aplica-se a relação trigonométrica básica que permite calcular a altura total ou parcial da árvore.")

    col2.write("O procedimento padrão envolve posicionar o operador a uma distância conhecida da base da árvore, alinhando a linha de visada do clinômetro com o topo da copa e, em seguida, com a base. Com esses dois ângulos, é possível determinar a altura relativa utilizando funções trigonométricas, como a tangente. Esse método é simples, rápido e não invasivo, sendo especialmente útil em áreas urbanas onde não é viável o uso de equipamentos mais complexos.")

    col2.write("Além da estimativa de altura, o clinômetro também pode ser utilizado para:")

    col2.markdown("""
        - verificar a inclinação do tronco em relação à vertical, fornecendo indícios sobre a estabilidade da árvore;
        - auxiliar em estudos de crescimento e desenvolvimento arbóreo;
        - apoiar análises de risco em árvores próximas a edificações, redes elétricas e áreas de circulação de pessoas.
    """)

    col2.write("Embora o clinômetro seja um equipamento de fácil manuseio, sua precisão depende diretamente de fatores como a calibração adequada, a visibilidade do topo da árvore e a medição correta da distância entre o observador e a base do tronco. O uso em conjunto com instrumentos complementares, como o hipsômetro ou tecnologias de varredura a laser, pode aumentar a confiabilidade dos resultados.")

    col2.write("Assim, o clinômetro permanece como uma ferramenta fundamental nas inspeções técnicas de árvores urbanas, oferecendo uma solução prática e de baixo custo para a avaliação preliminar da altura e da inclinação das árvores em meio urbano.")

    col2.subheader("Hipsômetro")

    col1, col2, col3, col4 = st.columns([1, 2, 1, 1])

    col2.write("O hipsômetro é um equipamento destinado à estimativa da altura de árvores, funcionando como uma evolução do clinômetro ao incorporar escalas ou sistemas digitais que facilitam os cálculos. O princípio de funcionamento baseia-se na medição de ângulos de visada entre a horizontal e pontos específicos da árvore, como a base e o topo, associados à distância entre o observador e o tronco. A partir desses dados, aplica-se a relação trigonométrica da tangente, permitindo determinar a altura total ou parcial da árvore.")

    col2.write("Os hipsômetros podem ser analógicos, com escalas graduadas que permitem leitura direta da altura, ou digitais, que utilizam sensores ópticos e a inserção prévia da distância horizontal para fornecer o resultado automaticamente. Em modelos mais avançados, o próprio equipamento pode medir a distância até a árvore por meio de telemetria a laser, aumentando a precisão das estimativas.")


    col2.write("Entre as principais aplicações do hipsômetro em inspeções arbóreas destacam-se:")

    col2.markdown("""
        - determinação da altura total da árvore;
        - medição de alturas parciais, como a de fustes ou ramificações específicas;
        - apoio em análises de risco relacionadas à proximidade da copa com edificações e redes elétricas;
        - acompanhamento do crescimento de árvores em estudos de monitoramento florestal ou urbano.
    """)

    col1, col2, col3 = st.columns([1, 3, 1])

    col2.write("Apesar de suas vantagens, a utilização do hipsômetro requer atenção a alguns fatores que podem comprometer a precisão da medição, como a visibilidade do topo da árvore, a presença de copas densas que dificultem a definição do ponto de referência e a correta calibração do equipamento. Assim como no clinômetro, recomenda-se realizar as medições a partir de diferentes pontos de observação para reduzir incertezas.")

    col2.write("Dessa forma, o hipsômetro constitui uma ferramenta prática e de boa relação custo-benefício, sendo muito utilizada em conjunto com o clinômetro e outros instrumentos de medição, como o trado de incremento ou o radar de penetração, no contexto de inspeções técnicas de árvores urbanas.")

    col2.latex(r"H=L(\tan\alpha\pm\tan\beta)")

    col2.subheader("Trado de incremento")

    col1, col2, col3, col4 = st.columns([1, 1.5, 1.5, 1])

    col2.write("O trado de incremento é um equipamento amplamente utilizado em inspeções arbóreas para a coleta de amostras cilíndricas do lenho, permitindo a análise direta das características anatômicas e mecânicas da madeira. O instrumento consiste em uma broca oca de pequeno diâmetro, acoplada a uma manivela, que é introduzida no tronco em profundidade suficiente para retirar um cilindro da madeira interna, denominado testemunho.")

    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Biologist_taking_wood_core_IMG_20201127_121400.jpg/960px-Biologist_taking_wood_core_IMG_20201127_121400.jpg")

    col3.markdown(
        'Biologist taking wood core, por Serdar Vardar, disponível em [Wikimedia Commons](https://commons.wikimedia.org/wiki/File%3ABiologist_taking_wood_core_IMG_20201127_121400.jpg), licenciada sob **CC BY-SA 4.0**.',
        unsafe_allow_html=True
    )

    col2.write("O principal objetivo do uso do trado de incremento é fornecer informações sobre:")

    col2.markdown("""
    - a idade da árvore, por meio da contagem dos anéis de crescimento;
    - a taxa de crescimento e histórico de desenvolvimento do lenho;
    - a presença de deteriorações internas, como apodrecimento, cavidades ou ataque de organismos xilófagos;
    - a densidade e a qualidade estrutural da madeira, que podem ser correlacionadas a propriedades mecânicas de resistência e rigidez.
    """)

    col1, col2, col3 = st.columns([1, 3, 1])

    col2.write("Apesar de ser considerado um método minimamente invasivo, o uso do trado de incremento gera perfurações que podem se tornar pontos de entrada para fungos e pragas. Por esse motivo, deve-se limitar o número de coletas em uma mesma árvore, evitando repetições desnecessárias, além de aplicar práticas de assepsia no equipamento e nas áreas de perfuração. Em alguns casos, recomenda-se o uso de selantes ou pastas cicatrizantes para reduzir os riscos de infecção.")

    col2.write("O procedimento exige que a broca seja posicionada em ângulo ortogonal à superfície do tronco e introduzida até atingir o centro geométrico ou até a profundidade necessária para a coleta representativa. Após a retirada do testemunho, este deve ser devidamente acondicionado e identificado para análise laboratorial.")

    col2.write("Assim, o trado de incremento constitui uma ferramenta valiosa para a caracterização do estado interno do tronco e para a obtenção de dados históricos de crescimento, sendo amplamente empregado em inspeções técnicas de árvores urbanas e em estudos de dendrocronologia.")

    col2.subheader("Ensaio de ancoragem ou estabilidade (*Tree pulling test*)")

    col2.subheader("Detecção de raiz")

    col2.subheader("Câmeras termográficas")

    col1, col2, col3 = st.columns([1, 3, 1])

    col2.write("O uso de câmeras termográficas em inspeções arbóreas representa um avanço significativo na detecção de anomalias internas e na avaliação do estado fitossanitário das árvores. Essas câmeras captam a radiação infravermelha emitida pela superfície, transformando-a em imagens que revelam variações de temperatura invisíveis a olho nu. Pequenas diferenças térmicas podem indicar a presença de cavidades, zonas de apodrecimento, infiltração de umidade ou até ataques de fungos e insetos que alteram o equilíbrio térmico do tronco.")

    col1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Infrared_thermal_imaging_during_a_yacht_survey.jpg/500px-Infrared_thermal_imaging_during_a_yacht_survey.jpg", caption="FLIR E50 - Câmera Termográfica (CC BY-SA 4.0)")

    col1.markdown(
        "Imagem: [FLIR E50 - Câmera Termográfica](https://commons.wikimedia.org/wiki/File:Infrared_thermal_imaging_during_a_yacht_survey.jpg) por Suenosazules, disponível em Wikimedia Commons, licenciada sob [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).",
        unsafe_allow_html=True
    )

    col2.write("Uma das principais vantagens da termografia é o caráter totalmente não invasivo: não há necessidade de perfurações ou cortes para acessar informações do interior da madeira. Além disso, o método possibilita a inspeção em tempo real, permitindo ao técnico observar, durante o próprio levantamento de campo, regiões suspeitas que merecem avaliação complementar. Por essa razão, a termografia tem sido utilizada não apenas em árvores isoladas, mas também em inventários arbóreos urbanos de grande escala, onde a agilidade na coleta de dados é fundamental.")

    col2.write("Apesar disso, a interpretação dos resultados requer cautela. A incidência solar, a temperatura ambiente, a umidade relativa do ar e até mesmo o vento podem influenciar o padrão térmico observado, gerando variações que não estão necessariamente associadas a defeitos internos. Assim, a experiência do avaliador e, em alguns casos, a associação com outros métodos — como a tomografia acústica ou o uso da espada de ar — tornam-se fundamentais para validar as informações obtidas.")

    col2.write("Portanto, as câmeras termográficas devem ser vistas como uma ferramenta de triagem poderosa e precisa, que, quando utilizada em conjunto com outros ensaios não destrutivos, amplia significativamente a confiabilidade do diagnóstico sobre a saúde e a estabilidade das árvores urbanas.")

    col2.subheader("Laudo de inspeção")

    col2.write("Após a realização da inspeção, o operador deve preencher um laudo visando documentar os procedimentos realizados em campo conforme as informações requeridas pela normal. Com isso, facilita-se a padronização das informações e procedimentos utilizados para a análise independente do operador que estiver realizando a inspeção. Além disso, é válido ressaltar que as técnicas citadas anteriormente podem ou não ser utilizadas em conjunto, cabendo ao profissional envolvido na inspeção decidir entre quais técnicas e métodos utilizar visando obter os dados necessários para a avaliação de risco, desde que todos os passos e procedimentos sejam documentados.")

if __name__ == "__main__":
    inspecao_de_arvores()