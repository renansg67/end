import streamlit as st
# ⚠️ ASSUMIMOS QUE database.py EXISTE E CONTÉM AS FUNÇÕES ABAIXO
from database import create_tables, register_access 
from datetime import datetime
import pandas as pd
import sqlite3 # Importação necessária se o database.py usa sqlite3

st.set_page_config(layout="wide")

# Garante que o DB e as tabelas (incluindo 'acessos') existam
create_tables()

def get_user_role(email):
    """Define a role do usuário baseado no e-mail e st.secrets.toml."""
    # Lógica de roles - Adapte conforme seu st.secrets
    admin_emails = st.secrets.get("roles", {}).get("admins", [])
    editor_emails = st.secrets.get("roles", {}).get("editors", [])
    
    if email in admin_emails:
        return "admin"
    elif email in editor_emails:
        return "editor"
    else:
        return "viewer"

def get_user_email_safely():
    """Tenta obter o email do usuário logado através da API nativa (st.user)."""
    user = st.user
    if user and hasattr(user, 'email'):
        return user.email
    return None

pages = {
    "Início": [
        st.Page("./inicio/apresentacao.py", title="Página Inicial", icon="✈️")
    ],
    "Conteúdo": [
        st.Page("./conteudo/1_materiais_nao_metalicos.py", title="Materiais de Construção não Metálicos", icon="🧱"),
        st.Page("./conteudo/2_classificacao_madeira_estrutural.py", title="Classificação de Madeira Estrutural", icon="🪵"),
        st.Page("./conteudo/3_inspecao_concreto.py", title="Inspeção de Concreto", icon="🪨"),
        st.Page("./conteudo/4_inspecao_de_arvores.py", title="Inspeção de Árvores", icon="🌳"),
        st.Page("./conteudo/5_matriz_de_rigidez.py", title="Matriz de Rigidez", icon="📚"),
        st.Page("./conteudo/6_propagacao_de_ondas_acusticas.py", title="Propagação de Ondas Acústicas", icon=":material/waves:"),
        st.Page("./conteudo/7_atenuacao_de_ondas_acusticas.py", title="Atenuação de Ondas Acústicas", icon="🔊")
    ],
    "Equipamentos": [
        st.Page("./equipamentos/equipamentos.py", title="Equipamentos", icon="🛠")
    ],
    "Biblioteca": [
        st.Page("./biblioteca/biblioteca.py", title="Biblioteca", icon="📚")
    ],
    "Empréstimos": [
        st.Page("./emprestimos/emprestimos.py", title="Formulário", icon="ℹ️")
    ],
    "Monitor": [
        st.Page("./monitor/monitor.py", title="Monitor", icon=":material/thumb_up:")
    ]
}

# ----------------------------------------------------
# LÓGICA DE AUTENTICAÇÃO E ROTEAMENTO (FLUXO ESTÁVEL)
# ----------------------------------------------------

user_email = get_user_email_safely()
col1, col2, col3 = st.columns([1, 3, 1])

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
    
    # Componentes de UI ÚNICOS: Logout
    if col3.button("Logout :material/logout:", type="secondary", key="main_logout_button"):
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
        
    # Botão de Login
    if col3.button("Login :material/login:", type="secondary", key="main_login_button"):
        st.login()
        
    # Conteúdo da Landing Page
    col2.title("👋 Bem-vindo(a) à Plataforma!")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    col1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Picea_abies_wood_texture.jpg/960px-Picea_abies_wood_texture.jpg", caption="[Image of Wood Texture]")
    col3.info(":material/warning: Por favor, clique no botão **'Login :material/login:'** no canto superior direito para autenticar com sua conta Google e entrar.")
    col3.warning(":material/lock: Este login é gerenciado com segurança via sua conta Google (OAuth).")
    col2.image("https://upload.wikimedia.org/wikipedia/commons/8/8d/CVN-69-SPIE-training.jpg", caption="")
