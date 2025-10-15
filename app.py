# app.py

import streamlit as st
from database import create_tables, register_access # Incluído register_access
from datetime import datetime
import sqlite3
import pandas as pd
# Importe a classe ou função show_access_monitor_page se não estiver em monitor/monitor.py
# from monitor.monitor import show_access_monitor_page # Exemplo se você estivesse usando funções

st.set_page_config(layout="wide")

# Garante que o DB e as tabelas (incluindo 'acessos') existam
create_tables()

def get_user_role(email):
    """Define a role do usuário baseado no e-mail e secrets.toml."""
    # Sua lógica de roles aqui:
    if email in st.secrets.get("roles", {}).get("admins", []):
        return "admin"
    elif email in st.secrets.get("roles", {}).get("editors", []):
        return "editor"
    else:
        return "viewer"

def get_user_email_safely():
    """Tenta obter o email do usuário logado através da API nativa (st.user)."""
    # Usamos o st.user que é a API moderna e suporta o fluxo OAuth
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
# LÓGICA DE AUTENTICAÇÃO E ROTEAMENTO
# ----------------------------------------------------

user_email = get_user_email_safely()
col1, col2, col3 = st.columns([1, 3, 1])

if user_email:
    # --- PARTE LOGADA: CONFIGURAÇÃO PÓS-LOGIN ---

    user_role = get_user_role(user_email)
    
    # 1. Armazenamento da Role na Session State (ESSENCIAL para as páginas)
    st.session_state['user_role'] = user_role 
    st.session_state['user_email'] = user_email
    
    # 2. Registrar o Acesso no DB
    try:
        register_access(user_email, user_role)
    except Exception as e:
        print(f"Alerta: Falha ao registrar acesso do usuário {user_email}. Erro: {e}")

    # 3. Componentes de UI ÚNICOS: Logout
    if col3.button("Logout :material/logout:", type="secondary"):
        # Usa a função nativa confirmada
        st.logout() 
        st.rerun()

    st.markdown("---") 

    # 4. Implementação da Navegação Condicional
    final_pages = {}
    
    # Adicionar páginas visíveis para TODOS (Grupos)
    for group_name, page_list in pages.items():
        if group_name == "Monitor":
            # Exclui o grupo Monitor por padrão
            continue
            
        # Exemplo: Ocultar Empréstimos para Viewers (se necessário)
        # if group_name == "Empréstimos" and user_role == "viewer":
        #     continue
            
        final_pages[group_name] = page_list
            
    # Adicionar páginas RESTRICTED para ADMIN
    if user_role == "admin":
        if "Monitor" in pages:
            final_pages["Monitor"] = pages["Monitor"] # Adiciona o grupo restrito
        
    # 5. Roteamento: Chamar a navegação e a execução da página
    pg = st.navigation(final_pages, position="top") 
    pg.run()


else: 
    # --- PARTE DESLOGADA: TELA DE LOGIN ---
    
    # 1. Botão de Login
    if col3.button("Login :material/login:", type="secondary"):
        # Usa a função nativa confirmada
        st.login() 
    
    # 2. Conteúdo da Landing Page
    col2.title(":wave: Bem-vindo(a)!")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    col1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Picea_abies_wood_texture.jpg/960px-Picea_abies_wood_texture.jpg", caption="Norway spruce (Picea abies) freshly cut wood texture. Growth rings.")
    col3.info(":material/warning: Por favor, clique no botão **'Login :material/login:'** no canto superior direito para autenticar com sua conta Google e entrar.")
    col3.warning(":material/lock: Este login é gerenciado com segurança via sua conta Google (OAuth).")
    col2.image("https://upload.wikimedia.org/wikipedia/commons/8/8d/CVN-69-SPIE-training.jpg")
