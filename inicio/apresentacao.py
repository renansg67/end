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

col2.expander(":material/book: Sumário").markdown('''
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

    ##### Matriz de rigidez

    ##### Propagação de ondas acústicas

    ##### Atenuação de ondas acústicas


    ''')