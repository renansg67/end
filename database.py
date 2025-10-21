# database.py (Versão PostgreSQL adaptada para Render/Variáveis de Ambiente)

import streamlit as st
import pandas as pd
import numpy as np
import time
from typing import Dict
from datetime import datetime
from sqlalchemy import text 
import os                       # <-- MUDANÇA 1: Importado
from dotenv import load_dotenv  # <-- MUDANÇA 1: Importado

# --- CONFIGURAÇÃO ---
# Carrega as variáveis do arquivo .env (se ele existir)
# Esta linha lê o .env e torna as variáveis
# acessíveis para o os.getenv() e para o st.connection
load_dotenv()
# --------------------


# =========================================================================
# FUNÇÕES DE AUTH E ROLE (Autônomo para evitar Duplicação de Chave em app.py)
# =========================================================================

### MUDANÇA 2: Função get_user_role reescrita para ler do os.environ ###
def get_user_role(email):
    """Define a role do usuário baseado em Variáveis de Ambiente."""
    
    # Lê a string de emails do ambiente (ex: "email1,email2")
    admin_emails_str = os.environ.get("ADMIN_EMAILS", "")
    editor_emails_str = os.environ.get("EDITOR_EMAILS", "")
    
    # Transforma a string em uma lista limpa
    admin_emails = [e.strip() for e in admin_emails_str.split(',') if e.strip()]
    editor_emails = [e.strip() for e in editor_emails_str.split(',') if e.strip()]

    if email in admin_emails:
        return "admin"
    elif email in editor_emails:
        return "editor"
    else:
        return "viewer"
# -------------------------------------------------------------------

def get_user_email_safely():
    """Tenta obter o email do usuário logado através da API nativa (st.user)."""
    user = st.user
    if user and hasattr(user, 'email'):
        return user.email
    return None
    
# ----------------------------------------------------
# CONFIGURAÇÃO DE CONEXÃO (st.connection)
# ----------------------------------------------------

# O nome "supabase_postgres" deve corresponder ao que está em [connections.sql] no secrets.toml
# ### MUDANÇA 3: get_connection() lendo do os.environ e passando kwargs ###
@st.cache_resource
def get_connection():
    """
    Inicializa e cacheia a conexão SQL (PostgreSQL).
    Esta abordagem lê explicitamente as variáveis do ambiente
    e as passa como kwargs para o st.connection, evitando
    a 'mágica' do secrets.toml ou da URL única.
    """
    try:
        return st.connection(
            # O nome "supabase_postgres" ainda é útil como ID da conexão
            "supabase_postgres",
            type="sql",
            dialect="postgresql",  # Informa que é Postgres
            driver="psycopg2",     # Informa o driver
            # Puxa explicitamente do os.environ
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("POSTGRES_DB"),
            username=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            connect_args={"connect_timeout": 40}
        )
    except Exception as e:
        st.error(f"Erro ao inicializar st.connection. Verifique as variáveis de ambiente. Erro: {e}")
        return None

conn = get_connection()

# ====================================================================
# CONFIGURAÇÃO GERAL DE TABELAS
# (O resto do seu código permanece 100% igual)
# ====================================================================

# Dicionário principal para configurar cada tabela
TABLE_CONFIG = {
    "livros": {
        "pk_column": "id",
        "columns": [
            "id", "titulo", "autor", "ano", "categoria", "subcategoria", "idioma", 
            "editora", "isbn", "palavras_chave", "tipo_de_material", "nivel", 
            "localizacao_fisica", "disponibilidade", "resumo", "imagem_capa_url", 
            "link_externo", "data_de_entrada"
        ],
        "format_cols": ["palavras_chave"] 
    },
    "equipamentos": {
        "pk_column": "patrimonio_id",
        "columns": [
            "patrimonio_id", "nome_equipamento", "fabricante", "modelo", "categoria", 
            "principio_funcionamento", "numero_serie", "localizacao_laboratorio", 
            "status_operacional", "data_aquisicao", "data_ultima_calibracao", 
            "manual_url", "obs_gerais"
        ],
        "mapping": { 
            'patrimonio_id': 'id', 
            'nome_equipamento': 'nome', 
            'localizacao_laboratorio': 'localizacao', 
            'status_operacional': 'disponibilidade', 
            'manual_url': 'link_manual', 
            'obs_gerais': 'descricao' 
        },
        "format_cols": []
    }
}

# --- FUNÇÃO AUXILIAR DE FORMATAÇÃO ---
def _format_data(data: Dict, table_name: str) -> Dict:
    """Aplica formatação específica (ex: lista para string) aos dados."""
    
    formatted_data = data.copy()
    
    if table_name == "livros" and 'palavras_chave' in formatted_data and isinstance(formatted_data['palavras_chave'], list):
        formatted_data['palavras_chave'] = ', '.join(formatted_data['palavras_chave'])
        
    return formatted_data


# ====================================================================
# CRIAÇÃO DAS TABELAS (DDL)
# ====================================================================

def create_tables():
    """Cria as tabelas 'livros', 'equipamentos', 'acessos' e 'usuarios_atividade' no PostgreSQL."""
    try:
        with conn.session as session: 
            
            # 1. Tabela Livros
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS livros (
                    id TEXT PRIMARY KEY, 
                    titulo TEXT, autor TEXT, ano INTEGER, categoria TEXT,
                    subcategoria TEXT, idioma TEXT, editora TEXT, isbn TEXT,
                    palavras_chave TEXT, tipo_de_material TEXT, nivel TEXT,
                    localizacao_fisica TEXT, disponibilidade TEXT, resumo TEXT,
                    imagem_capa_url TEXT, link_externo TEXT, data_de_entrada TEXT
                );
            """))

            # 2. Tabela Equipamentos
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS equipamentos (
                    patrimonio_id TEXT PRIMARY KEY, nome_equipamento TEXT, fabricante TEXT,
                    modelo TEXT, categoria TEXT, principio_funcionamento TEXT,
                    numero_serie TEXT, localizacao_laboratorio TEXT, status_operacional TEXT,
                    data_aquisicao TEXT, data_ultima_calibracao TEXT, manual_url TEXT, obs_gerais TEXT
                );
            """))
            
            # 3. Tabela Acessos (Logins)
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS acessos (
                    id SERIAL PRIMARY KEY, email TEXT NOT NULL,
                    data_hora_acesso TIMESTAMP WITHOUT TIME ZONE NOT NULL, role TEXT
                );
            """))

            # 4. Tabela de Atividade/Monitor 
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS usuarios_atividade (
                    email TEXT PRIMARY KEY,
                    ultimo_acesso_ativo TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    role TEXT, last_access_page TEXT
                );
            """))
            
            session.commit()

    except Exception as e:
        st.error(f"Erro ao criar tabelas no PostgreSQL. Verifique a sintaxe: {e}")
        print(f"Erro detalhado ao criar tabelas no DB: {e}")


# ====================================================================
# FUNÇÕES DE ACESSO E ATIVIDADE (DML)
# ====================================================================

def register_access(email: str, role: str):
    """Registra um novo evento de acesso (LOGIN) no PostgreSQL."""
    current_time = datetime.now()
    query = """
        INSERT INTO acessos (email, data_hora_acesso, role) 
        VALUES (:email, :data_hora_acesso, :role)
    """
    data = {'email': email, 'data_hora_acesso': current_time, 'role': role}

    try:
        with conn.session as session:
            session.execute(text(query), data)
            session.commit()
    except Exception as e:
        print(f"Alerta: Falha ao registrar acesso do usuário {email}. Erro: {e}")

def fetch_all_accesses() -> pd.DataFrame:
    """Busca o log de todos os acessos (QUERY DE LEITURA)."""
    try:
        df = conn.query("SELECT email, data_hora_acesso, role FROM acessos ORDER BY data_hora_acesso DESC")
        return df
    except Exception:
        return pd.DataFrame()

def fetch_access_counts() -> pd.DataFrame:
    """Busca o total de acessos por usuário usando conn.query() e Pandas."""
    
    count_query = """
        SELECT email, COUNT(id) AS total_acessos, MAX(data_hora_acesso) AS ultimo_acesso
        FROM acessos GROUP BY email ORDER BY ultimo_acesso DESC;
    """
    try:
        df = conn.query(count_query, ttl=60)
    except Exception as e:
        st.error(f"Erro na primeira fase de contagem de acessos (PostgreSQL): {e}")
        return pd.DataFrame()
        
    if not df.empty:
        role_query = """
            SELECT email, role 
            FROM acessos 
            WHERE data_hora_acesso IN (SELECT MAX(data_hora_acesso) FROM acessos GROUP BY email)
        """
        try:
            df_roles = conn.query(role_query, ttl=0)
            df_roles.rename(columns={'role': 'role_recente'}, inplace=True)
            df = pd.merge(df, df_roles, on='email', how='left')
            df.rename(columns={'role_recente': 'role'}, inplace=True)
        except Exception as e:
            st.error(f"Erro na fase de busca de roles (PostgreSQL): {e}")
            return df
            
    if not df.empty and 'role' in df.columns:
        cols = ['email', 'role', 'total_acessos', 'ultimo_acesso']
        df = df[cols]

    return df

def fetch_user_activity() -> pd.DataFrame:
    """Busca o status atual de atividade de todos os usuários."""
    query = """
        SELECT email, role, last_access_page, ultimo_acesso_ativo 
        FROM usuarios_atividade ORDER BY ultimo_acesso_ativo DESC;
    """
    try:
        df = conn.query(query, ttl=10) 
        return df
    except Exception as e:
        print(f"Alerta: Falha ao buscar atividade dos usuários. Erro: {e}")
        return pd.DataFrame()


def update_user_activity(email: str, role: str, last_access_page: str):
    """Atualiza o timestamp, role e última página acessada do usuário (UPSERT no PostgreSQL)."""
    current_time = datetime.now()
    
    query = """
        INSERT INTO usuarios_atividade (email, ultimo_acesso_ativo, role, last_access_page) 
        VALUES (:email, :ultimo_acesso_ativo, :role, :last_access_page)
        ON CONFLICT (email) 
        DO UPDATE SET 
            ultimo_acesso_ativo = EXCLUDED.ultimo_acesso_ativo,
            role = EXCLUDED.role,
            last_access_page = EXCLUDED.last_access_page;
    """
    data = {
        'email': email, 'ultimo_acesso_ativo': current_time,
        'role': role, 'last_access_page': last_access_page
    }

    try:
        with conn.session as session:
            session.execute(text(query), data)
            session.commit()
    except Exception as e:
        print(f"Alerta: Falha ao registrar atividade do usuário {email}. Erro: {e}")


# ====================================================================
# FUNÇÕES CRUD GENERALIZADAS (DML)
# (O resto do seu código não precisa de nenhuma alteração)
# ====================================================================

def fetch_all_items(table_name: str) -> pd.DataFrame:
    """Busca todos os itens de uma tabela e aplica o mapeamento (se houver)."""
    config = TABLE_CONFIG[table_name]
    query = f"SELECT * FROM {table_name}"
    df = conn.query(query, ttl="5m") 
    
    if 'mapping' in config:
        reverse_mapping = {sql_col: app_col for sql_col, app_col in config['mapping'].items()}
        df.rename(columns=reverse_mapping, inplace=True)
    
    if config['pk_column'] != 'id':
        df.rename(columns={config['pk_column']: 'id'}, inplace=True)

    return df


def add_item(table_name: str, data: Dict):
    """Insere um novo registro em uma tabela."""
    config = TABLE_CONFIG[table_name]
    
    data = _format_data(data, table_name)
    sql_data = {}
    for sql_col in config['columns']:
        app_key = config.get('mapping', {}).get(sql_col, sql_col)
        
        if sql_col == config["pk_column"] and app_key == config["pk_column"]:
            app_key = 'id' 
            
        sql_data[sql_col] = data.get(app_key)

    columns_list = ', '.join(config['columns'])
    placeholders = ', '.join([f":{col}" for col in config['columns']])
    query = f"INSERT INTO {table_name} ({columns_list}) VALUES ({placeholders})"
    
    try:
        with conn.session as session:
            session.execute(text(query), sql_data)
            session.commit()
    except Exception as e:
        if 'duplicate key value violates unique constraint' in str(e):
            raise Exception(f"O ID já existe na tabela '{table_name}'.")
        raise e


def update_item(table_name: str, item_id: str, data: Dict):
    """Atualiza um registro em uma tabela pelo ID."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]

    data = _format_data(data, table_name)
    update_data_sql = {}
    
    for app_key, app_value in data.items():
        if app_key == 'id': continue

        sql_col = next((k for k, v in config.get('mapping', {}).items() if v == app_key), app_key)
        
        if sql_col == pk_column: continue
            
        update_data_sql[sql_col] = app_value

    if not update_data_sql:
        return 

    set_clauses = ', '.join([f"{sql_col} = :{sql_col}" for sql_col in update_data_sql.keys()])
    query = f"UPDATE {table_name} SET {set_clauses} WHERE {pk_column} = :pk_value"
    update_data_sql['pk_value'] = item_id
    
    try:
        with conn.session as session:
            session.execute(text(query), update_data_sql)
            session.commit()
    except Exception as e:
        raise e


def delete_item(table_name: str, item_id: str):
    """Exclui um registro de uma tabela pelo ID."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]
    
    query = f"DELETE FROM {table_name} WHERE {pk_column} = :item_id"
    
    try:
        with conn.session as session:
            session.execute(text(query), {'item_id': item_id})
            session.commit()
    except Exception as e:
        raise e