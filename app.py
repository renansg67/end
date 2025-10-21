import streamlit as st
# ⚠️ ASSUMIMOS QUE database.py EXISTE E CONTÉM AS FUNÇÕES ABAIXO
from database import (
    create_tables, 
    register_access,
    get_user_role,
    get_user_email_safely
) 

st.set_page_config(layout="wide")

# Garante que o DB e as tabelas (incluindo 'acessos') existam
create_tables()

pages = {
    "Início": [
        st.Page("./inicio/apresentacao.py", title="Página Inicial", icon=":material/flight_land:")
    ],
    "Conteúdo": [
        st.Page("./conteudo/1_materiais_nao_metalicos.py", title="Materiais de Construção não Metálicos", icon=":material/polymer:"),
        st.Page("./conteudo/2_classificacao_madeira_estrutural.py", title="Classificação de Madeira Estrutural", icon=":material/carpenter:"),
        st.Page("./conteudo/3_inspecao_de_estruturas_de_concreto_e_madeira.py", title="Inspeção de Estruturas (Concreto e Madeira)", icon=":material/cabin:"),
        st.Page("./conteudo/4_inspecao_de_arvores.py", title="Inspeção de Árvores", icon=":material/forest:"),
        st.Page("./conteudo/5_matriz_de_rigidez.py", title="Matriz de Rigidez", icon=":material/background_grid_small:"),
        st.Page("./conteudo/6_propagacao_de_ondas_acusticas.py", title="Propagação de Ondas Acústicas", icon=":material/waves:"),
        st.Page("./conteudo/7_atenuacao_de_ondas_acusticas.py", title="Atenuação de Ondas Acústicas", icon=":material/cadence:")
    ],
    "Equipamentos": [
        st.Page("./equipamentos/equipamentos.py", title="Equipamentos", icon=":material/build:")
    ],
    "Biblioteca": [
        st.Page("./biblioteca/introducao.py", title="Introdução", icon=":material/waving_hand:"),
        st.Page("./biblioteca/biblioteca.py", title="Biblioteca", icon=":material/book_5:")
    ],
    "Empréstimos": [
        st.Page("./emprestimos/emprestimos.py", title="Formulário", icon=":material/assignment:")
    ],
    "Monitor": [
        st.Page("./monitor/monitor.py", title="Monitor", icon=":material/query_stats:")
    ]
}

# ----------------------------------------------------
# LÓGICA DE AUTENTICAÇÃO E ROTEAMENTO (FLUXO ESTÁVEL)
# ----------------------------------------------------

user_email = get_user_email_safely()
col1, col2, col3 = st.columns([.25, 3, 1.5])

if user_email:
    # --- PARTE LOGADA: CONFIGURAÇÃO PÓS-LOGIN ---

    # 1. CONTROLE DE INICIALIZAÇÃO DE ESTADO
    
    # Verifica se a sessão estável já foi alcançada ou se o usuário mudou
    if 'session_initialized' not in st.session_state or st.session_state.get('user_email') != user_email:
        
        user_role = get_user_role(user_email)
        
        # Ação de Inicialização: SÓ PODE ACONTECER UMA VEZ POR LOGIN
        st.session_state['user_role'] = user_role 
        st.session_state['user_email'] = user_email
        st.session_state['access_registered'] = False # Reseta o registro
        
        # Registro de Acesso
        try:
            register_access(user_email, user_role)
            st.session_state['access_registered'] = True
        except Exception as e:
            print(f"Alerta: Falha ao registrar acesso do usuário {user_email}. Erro: {e}")
            
        # Marca a sessão como inicializada
        st.session_state['session_initialized'] = True
        
        # 🛑 CHAVE FINAL DE CORREÇÃO: Forçar o RERUN e PARAR a execução
        st.rerun() 
        st.stop() # Garante que o pg.run() não seja chamado na primeira execução não estável.
        
    
    # === 2. EXECUÇÃO ESTÁVEL (Após o RERUN e com st.session_state carregado) ===
    
    # Puxa o role e o email do state
    user_role = st.session_state['user_role']
    
    col1, col2, col3 = st.columns([1, 3, 1])
    col1.header(f":rainbow[Olá, {st.user.given_name}]")
    col1.write(f"Logado com: {st.user.email}")

    url_imagem_drive = "https://images.seeklogo.com/logo-png/14/1/unicamp-logo-png_seeklogo-144966.png"

    with col2.container(width='stretch', horizontal_alignment='center'):
        st.image(url_imagem_drive, width=150)
    # Componentes de UI ÚNICOS: Logout
    if col3.container(horizontal_alignment='right').button("Logout :material/logout:", type="primary", key="main_logout_button"):
        st.session_state.clear() 
        st.logout() 
        st.rerun()

    st.markdown("---") 

    # Implementação da Navegação Condicional
    final_pages = {}
    
    for group_name, page_list in pages.items():
        if group_name != "Monitor": 
            final_pages[group_name] = page_list
            
    if user_role == "admin" and "Monitor" in pages:
        final_pages["Monitor"] = pages["Monitor"]
        
    # Roteamento: Chamar a navegação e a execução da página
    pg = st.navigation(final_pages, position="top") 
    pg.run()


else: 
    # --- PARTE DESLOGADA: TELA DE LOGIN ---
    
    # Limpa todo o estado para garantir um novo início no próximo login
    if 'session_initialized' in st.session_state:
        st.session_state.clear()
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    col1.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Woody_Dicot_Stem_Cross_Section_Quercus_Wood_40x_%2834991087693%29.jpg")
    col2.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Gymnosperm_Stem_Soft_Wood_in_Pinus_%2836087417260%29.jpg")
    col3.image("https://upload.wikimedia.org/wikipedia/commons/a/aa/Gymnosperm_Stem_Circular_Bordered_Pits_in_Pinus_Wood_%2836484401545%29.jpg")
    col4.image("https://upload.wikimedia.org/wikipedia/commons/a/ac/Gymnosperm_Stem_Soft_Wood_in_Pinus_%2836087426450%29.jpg")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    # Botão de Login
    if col3.container(horizontal_alignment='right').button("Login :material/login:", type="primary", key="main_login_button"):
        st.login()
    
    col3.info(":material/warning: Por favor, clique no botão **'Login :material/login:'** no canto superior direito para autenticar com sua conta Google e entrar.")
    col3.warning(":material/lock: Este login é gerenciado com segurança via sua conta Google (OAuth).")
    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/UT_flaw_detection_-_crack.png/960px-UT_flaw_detection_-_crack.png")

    col2.markdown("""
    Seja bem-vindo(a) ao portal oficial do **LabEND (Laboratório de Ensaios Não Destrutivos)**, um núcleo de pesquisa e aplicação de técnicas avançadas no Laboratório de Materiais (LME).

    Nossa missão é ser a ponte entre o conhecimento científico e a comunidade, oferecendo recursos digitais para profissionais, pesquisadores e estudantes interessados na integridade estrutural e na avaliação de materiais sem causar danos.

    ### 🎯 Finalidade da Aplicação: Três Pilares Essenciais

    Esta aplicação foi desenvolvida com o objetivo de desmistificar e aproximar as técnicas de Ensaios Não Destrutivos (END) em três áreas principais:

    #### 1. Divulgação Científica e Conteúdo Técnico

    Explore a seção **Conteúdo** para mergulhar nos fundamentos dos END. Abordamos desde as propriedades de **Materiais Não Metálicos** até a **Inspeção de Estruturas de Concreto e Madeira** e a crucial **Inspeção de Árvores**. Compreenda a física por trás dessas técnicas com tópicos dedicados à **Propagação de Ondas Acústicas** e à **Matriz de Rigidez**.

    #### 2. Acervo de Equipamentos e Infraestrutura

    Acreditamos que a prática começa pelo conhecimento das ferramentas. Na seção **Equipamentos**, você encontrará o catálogo completo dos instrumentos de ponta disponíveis em nosso laboratório (LME), com especificações técnicas e suas aplicações diretas nos ensaios.

    #### 3. Biblioteca e Gestão de Recursos (Login Requerido)

    Para aqueles que buscam aprofundamento, o portal oferece um **Acervo Digital** especializado. 

    * A seção **Biblioteca** dá acesso ao nosso catálogo completo de livros e documentos técnicos (após o login seguro).
    * A seção **Empréstimos** permite que usuários autorizados solicitem o empréstimo de itens do acervo.

    ---

    ### 🚀 Comece Sua Jornada

    Para acessar o catálogo da biblioteca e utilizar as funcionalidades exclusivas de empréstimo e monitoria, por favor, utilize o sistema de login no menu lateral. Caso contrário, explore o **Conteúdo** e a lista de **Equipamentos** livremente.
    """)
    col1, col2, col3 = st.columns([.25, 3, 1.5])
    if col2.button("Começar", width="stretch", type="primary"):
        st.login()
    
    #col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Picea_abies_wood_texture.jpg/960px-Picea_abies_wood_texture.jpg")
    #col2.image("https://upload.wikimedia.org/wikipedia/commons/8/8d/CVN-69-SPIE-training.jpg", caption="")
    #col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Modeconversion.svg/889px-Modeconversion.svg.png")
    #col3.image("https://upload.wikimedia.org/wikipedia/commons/a/ad/Type_S.jpg")
    #col3.image("https://upload.wikimedia.org/wikipedia/commons/4/4b/16_wood_samples.jpg")
    