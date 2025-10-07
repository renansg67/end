import streamlit as st

st.set_page_config(page_title="Materiais e Inspeções", layout="wide")

col1, col2, col3 = st.columns([1, 3, 1])

col2.title("📘 Ensaios Não Destrutivos (FEAGRI/LME)")
col2.markdown("""
Bem-vindo ao repositório interativo de materiais didáticos e informações sobre
**ensaios não destrutivos, inspeção de árvores e normas técnicas**.

👉 Use o menu superior para navegar pelos conteúdos:

- **Materiais não metálicos**: concreto e madeira;  
- **Ensaios não destrutivos**: esclerometria, ultrassom, penetração de pinos, vibrações;  
- **Árvores urbanas**: inspeções com drone, espada de ar, tomografia, termografia etc.;  
- **Inspeção de nível 3**: modelos probabilísticos, ensaio de ancoragem e laudo técnico;  
- **Normas ABNT**: principais referências normativas aplicáveis.  
""")

col2.expander(":material/book: Sumário", expanded=True).markdown('''
    ##### Materiais de construção não metálicos
    - [Início](materiais_nao_metalicos#inicio)
    - [Concreto](materiais_nao_metalicos#concreto)
        - [Ensaio para medição da dureza superficial](materiais_nao_metalicos#ensaio-para-medicao-da-dureza-superficial)
        - [Ensaio de propagação de ondas de tensão](materiais_nao_metalicos#ensaio-de-propagacao-de-ondas-de-tensao)
            - [Método da frequência de ressonância](materiais_nao_metalicos#metodo-da-frequencia-de-ressonancia)
            - [Método da propagação de pulso ultrassônico](materiais_nao_metalicos#metodo-da-propagacao-de-pulso-ultrassonico)
        - [Ensaio de penetração de pinos](materiais_nao_metalicos#ensaio-de-penetracao-de-pinos)
    - [Madeira](materiais_nao_metalicos#madeira)
        - [Métodos utilizando a frequência de ressonância](materiais_nao_metalicos#metodos-utilizando-a-frequencia-de-ressonancia)
            - [Método de vibração transversal](materiais_nao_metalicos#metodo-de-vibracao-transversal)
            - [Método dos modos de vibração](materiais_nao_metalicos#metodo-dos-modos-de-vibracao)
        - [Ensaio de flexão estática](materiais_nao_metalicos#ensaio-de-flexao-estatica)
        - [Método da propagação de ondas de tensão](materiais_nao_metalicos#metodo-da-propagacao-de-ondas-de-tensao)
            - [Barra viscoelástica submetida a um impacto](materiais_nao_metalicos#barra-viscoelastica-submetida-a-um-impacto)
            - [Cronometragem do tempo de propagação da onda de tensão](materiais_nao_metalicos#cronometragem-do-tempo-de-propagacao-da-onda-de-tensao)
            - [Método do pulso-eco](materiais_nao_metalicos#metodo-do-pulso-eco)
            - [Pitch and catch](materiais_nao_metalicos#pitch-and-catch)
            - [Posicionamento dos acelerômetros](materiais_nao_metalicos#posicionamento-dos-acelerometros)

    ##### Classificação de madeira estrutural

    - [Ensaios não destrutivos normatizados para a classificação da madeira estrutural]()
        - [Início](classificacao_madeira_estrutural#inicio)
        - [Sobre os ensaios e a ABNT NBR 7190:2022](classificacao_madeira_estrutural#sobre-os-ensaios-e-a-abnt-nbr-7190-2022)
            - [Classificação visual](classificacao_madeira_estrutural#classificacao-visual)
            - [Classificação mecânica](classificacao_madeira_estrutural#classificacao-mecanica)
            - [Densidade aparente](classificacao_madeira_estrutural#densidade-aparente)

    ##### Inspeção de estruturas de madeira e concreto

    - [Ensaios não destrutivos para a inspeção de estruturas de madeira e concreto](inspecao_concreto#ensaios-nao-destrutivos-para-a-inspecao-de-estruturas-de-madeira-e-concreto)
        - [Início](inspecao_concreto#inicio)
        - [Madeira](inspecao_concreto#madeira)
            - [Cronometragem do tempo de viagem da onda de tensão](inspecao_concreto#cronometragem-do-tempo-de-viagem-da-onda-de-tensao)
            - [Penetrografia](inspecao_concreto#penetrografia)
            - [*Pilodyn*](inspecao_concreto#pilodyn)
            - [Tomografia acústica](inspecao_concreto#tomografia-acustica)
            - [Tomografia elétrica](inspecao_concreto#tomografia-eletrica)
            - [Termografia](inspecao_concreto#termografia)
            - [Radar de penetração de solo (GPR)](inspecao_concreto#radar-de-penetracao-de-solo-gpr)
    - [Concreto](inspecao_concreto#concreto)
        - [Método eletromagnético (Pacometria)](inspecao_concreto#metodo-eletromagnetico-pacometria)
            - [Pacometria no ensaio de esclerometria](inspecao_concreto#pacometria-no-ensaio-de-esclerometria)
            - [Pacometria no ensaio de ultrassonografia](inspecao_concreto#pacometria-no-ensaio-de-ultrassonografia)
            - [Pacometria no ensaio de potencial de corrosão](inspecao_concreto#pacometria-no-ensaio-de-potencial-de-corrosao)
            - [Pacometria no ensaio de resistividade elétrica](inspecao_concreto#pacometria-no-ensaio-de-resistividade-eletrica)
            - [Pacometria no ensaio de penetração de pinos](inspecao_concreto#pacometria-no-ensaio-de-penetracao-de-pinos)
        - [Ensaio de penetração de pinos](inspecao_concreto#ensaio-de-penetracao-de-pinos)
        - [Ensaio de raios X e $\\gamma$](inspecao_concreto#ensaio-de-raios-x-e-g-gammag)
        - [Ensaio de inspeção de imagens](inspecao_concreto#ensaio-de-inspecao-de-imagens)
        - [Ensaio de profundidade de carbonatação](inspecao_concreto#ensaio-de-profundidade-de-carbonatacao)
        - [Ensaio de resistividade elétrica](inspecao_concreto#ensaio-de-resistividade-eletrica)
        - [Ensaio de potencial de corrosão](inspecao_concreto#ensaio-de-potencial-de-corrosao)
        - [Radar de penetração de solo (GPR)](inspecao_concreto#radar-de-penetracao-de-solo-gpr)
        - [Termografia](inspecao_concreto#termografia)

    ##### Inspeção de árvores

    - [Ensaios não destrutivos para inspeção de árvores urbanas](inspecao_de_arvores#ensaios-nao-destrutivos-para-inspecao-de-arvores-urbanas)
        - [Inspeção técnica nível 3](inspecao_de_arvores#inspecao-tecnica-nivel-3)
            - [Drone](inspecao_de_arvores#drone)
            - [Trabalho em altura em árvores](inspecao_de_arvores#trabalho-em-altura-em-arvores)
            - [Espada de ar](inspecao_de_arvores#espada-de-ar)
            - [Tomografia](inspecao_de_arvores#tomografia)
            - [Sonda](inspecao_de_arvores#sonda)
            - [Modelos probabilísticos](inspecao_de_arvores#modelos-probabilisticos)
            - [Clinômetro](inspecao_de_arvores#clinometro)
            - [Hipsômetro](inspecao_de_arvores#hipsometro)
            - [Trado de incremento](inspecao_de_arvores#trado-de-incremento)
            - [Câmeras termográficas](inspecao_de_arvores#cameras-termograficas)
            - [Ensaio de ancoragem](inspecao_de_arvores#ensaio-de-ancoragem)
            - [Laudo de inspeção](inspecao_de_arvores#laudo-de-inspecao)

    ##### Matriz de rigidez

    - [Bases teóricas para obtenção da matriz de rigidez por método de propagação de ondas](matriz_de_rigidez#bases-teoricas-para-obtencao-da-matriz-de-rigidez-por-metodo-de-propagacao-de-ondas)
        - [Início](matriz_de_rigidez#inicio)
        - [Materiais isotrópicos](matriz_de_rigidez#materiais-isotropicos)
            - [Matriz de rigidez](matriz_de_rigidez#materiais-isotropicos)
            - [Matriz de flexibilidade](matriz_de_rigidez#materiais-isotropicos)
        - [Materiais isotrópicos transversais](matriz_de_rigidez#materiais-isotropicos-transversais)
            - [Plano 12 de isotropia](matriz_de_rigidez#plano-12-de-isotropia)
                - [Matriz de rigidez](matriz_de_rigidez#materiais-isotropicos-transversais)
                - [Matriz de flexibilidade](matriz_de_rigidez#materiais-isotropicos-transversais)
            - [Plano 13 de isotropia](matriz_de_rigidez#plano-13-de-isotropia)
                - [Matriz de rigidez](matriz_de_rigidez#plano-13-de-isotropia)
                - [Matriz de flexibilidade](matriz_de_rigidez#plano-13-de-isotropia)
            - [Plano 23 de isotropia](matriz_de_rigidez#plano-23-de-isotropia)
                - [Matriz de rigidez](matriz_de_rigidez#plano-23-de-isotropia)
                - [Matriz de flexibilidade](matriz_de_rigidez#plano-23-de-isotropia)
        - [Materiais ortotrópicos](matriz_de_rigidez#materiais-ortotropicos)
            - [Matriz de rigidez](matriz_de_rigidez#materiais-ortotropicos)
            - [Matriz de flexibilidade](matriz_de_rigidez#materiais-ortotropicos)
                - [Propagação nos planos](matriz_de_rigidez#propagacao-nos-planos)
                    - [Propagação de ondas no plano 12](matriz_de_rigidez#propagacao-de-ondas-no-plano-12)
                    - [Propagação de ondas no plano 13](matriz_de_rigidez#propagacao-de-ondas-no-plano-13)
                    - [Propagação de ondas no plano 23](matriz_de_rigidez#propagacao-de-ondas-no-plano-23)


    ##### Propagação de ondas acústicas

    - [Fatores que afetam a propagação de ondas acústicas em sólidos](propagacao_de_ondas_acusticas#fatores-que-afetam-a-propagacao-de-ondas-acusticas-em-solidos)
        - [Início](propagacao_de_ondas_acusticas#inicio)
        - [Fatores relacionados aos fenômenos ondulatórios](propagacao_de_ondas_acusticas#fatores-relacionados-aos-fenomenos-ondulatorios)
            - [Impedância acústica](propagacao_de_ondas_acusticas#impedancia-acustica)
            - [Coeficientes de reflexão e transmissão](propagacao_de_ondas_acusticas#coeficientes-de-reflexao-e-transmissao)
            - [Fenômeno da refração](propagacao_de_ondas_acusticas#fenomeno-da-refracao)
            - [Conceito de ângulo crítico](propagacao_de_ondas_acusticas#conceito-de-angulo-critico)
            - [Divergência do feixe acústico](propagacao_de_ondas_acusticas#divergencia-do-feixe-acustico)
            - [Ressonância](propagacao_de_ondas_acusticas#ressonancia)
            - [Zona de Fresnel (Campo próximo)](propagacao_de_ondas_acusticas#zona-de-fresnel-campo-proximo)
            - [Zona de Fraunhofer (Campo distante)](propagacao_de_ondas_acusticas#zona-de-fraunhofer-campo-distante)
            - [Anisotropia do material](propagacao_de_ondas_acusticas#anisotropia-do-material)
                - [Materiais isotrópicos](propagacao_de_ondas_acusticas#materiais-isotropicos)
                - [Materiais ortotrópicos](propagacao_de_ondas_acusticas#materiais-ortotropicos)
                - [Materiais compósitos e laminados](propagacao_de_ondas_acusticas#materiais-compositos-e-laminados)
            - [Temperatura e umidade](propagacao_de_ondas_acusticas#temperatura-e-umidade)
            - [Grãos e cristais](propagacao_de_ondas_acusticas#graos-e-cristais)
            - [Tamanho e forma](propagacao_de_ondas_acusticas#tamanho-e-forma)
            - [Frequência dos transdutores](propagacao_de_ondas_acusticas#frequencia-dos-transdutores)
            - [Amortecimento dos transdutores](propagacao_de_ondas_acusticas#amortecimento-dos-transdutores)


    ##### Atenuação de ondas acústicas

    - [Atenuação de ondas acústicas em sólidos](atenuacao_de_ondas_acusticas#atenuacao-de-ondas-acusticas-em-solidos)
        - [Início](atenuacao_de_ondas_acusticas#inicio)
        - [Principais fatores relacionados à atenuação](atenuacao_de_ondas_acusticas#fatores-principais-relacionados-a-atenuacao)
        - [Atenuação em materiais isotrópicos](atenuacao_de_ondas_acusticas#atenuacao-em-materiais-isotropicos)
        - [Materiais com fontes dispersoras](atenuacao_de_ondas_acusticas#materiais-com-fontes-dispersoras)
        - [Impacto das fontes dispersoras](atenuacao_de_ondas_acusticas#impacto-das-fontes-dispersoras)
        - [Atenuação em materiais com grãos colunares](atenuacao_de_ondas_acusticas#atenuacao-em-materiais-com-graos-colunares)
        - [Atenuação em materiais pouco rígidos](atenuacao_de_ondas_acusticas#atenuacao-em-materiais-pouco-rigidos)
        - [Atenuação na madeira](atenuacao_de_ondas_acusticas#atenuacao-na-madeira)

    ''')