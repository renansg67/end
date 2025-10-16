# database.py (Versão PostgreSQL usando st.connection)

import streamlit as st
import pandas as pd
from typing import Dict
from datetime import datetime
# Importações necessárias para o SQLAlchemy/Streamlit Connection
# Usamos 'text as sql' para facilitar a escrita de queries DDL/DML com session.execute
from sqlalchemy import text 

# ----------------------------------------------------
# CONFIGURAÇÃO DE CONEXÃO (st.connection)
# ----------------------------------------------------

# O nome "sql" deve corresponder ao que está em [connections.sql] no secrets.toml
@st.cache_resource
def get_connection():
    """Inicializa e cacheia a conexão SQL (PostgreSQL)."""
    # st.connection busca a URL automaticamente do secrets.toml
    return st.connection("supabase_postgres", type="sql")

conn = get_connection()

# ====================================================================
# CONFIGURAÇÃO GERAL DE TABELAS
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
        # Nomes de colunas do SQL que PRECISAM DE FORMATAÇÃO antes de INSERT/UPDATE (ex: lista para string)
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
        # Mapeamento para conversão SQL -> Frontend (pandas)
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
    
    # Lógica específica para o campo 'palavras_chave' (se for lista)
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
            
            # --- CORREÇÃO DE MIGRAÇÃO DE ESQUEMA ---
            # Para garantir que a coluna 'role' seja adicionada à tabela de monitoramento, 
            # forçamos a exclusão da tabela se ela já existir, e a recriamos em seguida.
            # DROP TABLE IF EXISTS apaga todos os dados anteriores desta tabela!
            # session.execute(text("DROP TABLE IF EXISTS usuarios_atividade;")) # Removido para não perder dados após a correção

            # 1. Tabela Livros
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS livros (
                    id TEXT PRIMARY KEY, 
                    titulo TEXT,
                    autor TEXT,
                    ano INTEGER,
                    categoria TEXT,
                    subcategoria TEXT,
                    idioma TEXT,
                    editora TEXT,
                    isbn TEXT,
                    palavras_chave TEXT,
                    tipo_de_material TEXT,
                    nivel TEXT,
                    localizacao_fisica TEXT,
                    disponibilidade TEXT,
                    resumo TEXT,
                    imagem_capa_url TEXT,
                    link_externo TEXT,
                    data_de_entrada TEXT
                );
            """))

            # 2. Tabela Equipamentos
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS equipamentos (
                    patrimonio_id TEXT PRIMARY KEY,
                    nome_equipamento TEXT,
                    fabricante TEXT,
                    modelo TEXT,
                    categoria TEXT,
                    principio_funcionamento TEXT,
                    numero_serie TEXT,
                    localizacao_laboratorio TEXT,
                    status_operacional TEXT,
                    data_aquisicao TEXT,
                    data_ultima_calibracao TEXT,
                    manual_url TEXT,
                    obs_gerais TEXT
                );
            """))
            
            # 3. Tabela Acessos (Logins)
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS acessos (
                    id SERIAL PRIMARY KEY,
                    email TEXT NOT NULL,
                    data_hora_acesso TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    role TEXT
                );
            """))

            # 4. Tabela de Atividade/Monitor 
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS usuarios_atividade (
                    email TEXT PRIMARY KEY,
                    ultimo_acesso_ativo TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    role TEXT,
                    last_access_page TEXT
                );
            """))
            
            session.commit()

    except Exception as e:
        # Aumentei a clareza da mensagem de erro aqui
        st.error(f"Erro ao criar tabelas no PostgreSQL. Verifique a sintaxe: {e}")
        print(f"Erro detalhado ao criar tabelas no DB: {e}")


# ====================================================================
# FUNÇÕES DE ACESSO E ATIVIDADE (DML)
# ====================================================================

def register_access(email: str, role: str):
    """
    Registra um novo evento de acesso (LOGIN) no PostgreSQL.
    """
    current_time = datetime.now()
    
    query = """
        INSERT INTO acessos (email, data_hora_acesso, role) 
        VALUES (:email, :data_hora_acesso, :role)
    """
    
    data = {
        'email': email,
        'data_hora_acesso': current_time,
        'role': role
    }

    try:
        with conn.session as session:
            session.execute(text(query), data)
            session.commit()
    except Exception as e:
        print(f"Alerta: Falha ao registrar acesso do usuário {email}. Erro: {e}")

def fetch_all_accesses() -> pd.DataFrame:
    """Busca o log de todos os acessos (QUERY DE LEITURA)."""
    try:
        # conn.query() para leitura simples (com cache)
        df = conn.query("SELECT email, data_hora_acesso, role FROM acessos ORDER BY data_hora_acesso DESC")
        return df
    except Exception:
        return pd.DataFrame()

def fetch_access_counts() -> pd.DataFrame:
    """
    Busca o total de acessos por usuário usando conn.query() para obter os dados 
    e Pandas para fazer o merge da 'role'.
    """
    
    # 1. Primeira Query: Contagem de Acessos e Último Acesso (Timestamp)
    count_query = """
        SELECT
            email,
            COUNT(id) AS total_acessos, 
            MAX(data_hora_acesso) AS ultimo_acesso
        FROM acessos
        GROUP BY email
        ORDER BY ultimo_acesso DESC;
    """
    
    # Executa a primeira query usando st.connection.query()
    # Adiciona um TTL (Time To Live) de cache, por exemplo, 1 minuto (60 segundos)
    try:
        df = conn.query(count_query, ttl=60)
    except Exception as e:
        st.error(f"Erro na primeira fase de contagem de acessos (PostgreSQL): {e}")
        return pd.DataFrame()
        
    # 2. Adiciona o Role mais recente (se a primeira query retornou dados)
    if not df.empty:
        
        # Query para buscar o role mais recente
        role_query = """
            SELECT email, role 
            FROM acessos 
            WHERE data_hora_acesso IN (SELECT MAX(data_hora_acesso) FROM acessos GROUP BY email)
        """
        
        try:
            # Executa a segunda query (Cache TTL = 0 para garantir que a role seja atualizada junto)
            df_roles = conn.query(role_query, ttl=0)
            
            # 3. Faz o Merge no Pandas
            df_roles.rename(columns={'role': 'role_recente'}, inplace=True)
            
            df = pd.merge(df, df_roles, on='email', how='left')
            
            # Renomeia a coluna final para 'role', substituindo o nome do log anterior
            df.rename(columns={'role_recente': 'role'}, inplace=True)
            
        except Exception as e:
            st.error(f"Erro na fase de busca de roles (PostgreSQL): {e}")
            # Retorna o DataFrame que já tem, sem o role.
            return df
            
    # 4. Reordena as colunas para melhor visualização (opcional)
    if not df.empty and 'role' in df.columns:
        cols = ['email', 'role', 'total_acessos', 'ultimo_acesso']
        df = df[cols]

    return df

def fetch_user_activity() -> pd.DataFrame:
    """Busca o status atual de atividade de todos os usuários."""
    query = """
        SELECT email, role, last_access_page, ultimo_acesso_ativo 
        FROM usuarios_atividade
        ORDER BY ultimo_acesso_ativo DESC;
    """
    try:
        # Usa conn.query() para leitura simples (cache TTL baixo para "tempo real")
        # 10 segundos de cache para o monitoramento
        df = conn.query(query, ttl=10) 
        return df
    except Exception as e:
        print(f"Alerta: Falha ao buscar atividade dos usuários. Erro: {e}")
        return pd.DataFrame()


def update_user_activity(email: str, role: str, last_access_page: str):
    """
    Atualiza o timestamp, role e última página acessada do usuário (UPSERT no PostgreSQL).
    Esta função suporta a tabela 'usuarios_atividade' para o Monitor de status.
    """
    current_time = datetime.now()
    
    # Usa ON CONFLICT (UPSERT) para atualizar os campos quando o email já existe
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
        'email': email,
        'ultimo_acesso_ativo': current_time,
        'role': role,
        'last_access_page': last_access_page
    }

    try:
        with conn.session as session:
            session.execute(text(query), data)
            session.commit()
    except Exception as e:
        print(f"Alerta: Falha ao registrar atividade do usuário {email}. Erro: {e}")


# ====================================================================
# FUNÇÕES CRUD GENERALIZADAS (DML)
# ====================================================================

def fetch_all_items(table_name: str) -> pd.DataFrame:
    """Busca todos os itens de uma tabela e aplica o mapeamento (se houver)."""
    config = TABLE_CONFIG[table_name]
    
    # READ: Usa conn.query()
    query = f"SELECT * FROM {table_name}"
    # Busca os dados e usa cache para otimizar
    df = conn.query(query, ttl="5m") 
    
    # Aplica o mapeamento (SQL -> Frontend) se estiver definido
    if 'mapping' in config:
        # Inverte o mapeamento para renomear colunas do DB para o nome amigável do app
        reverse_mapping = {sql_col: app_col for sql_col, app_col in config['mapping'].items()}
        df.rename(columns=reverse_mapping, inplace=True)
    
    # Renomeia a coluna PK para o nome amigável 'id' no DataFrame, se necessário
    if config['pk_column'] != 'id':
        df.rename(columns={config['pk_column']: 'id'}, inplace=True)

    return df


def add_item(table_name: str, data: Dict):
    """Insere um novo registro em uma tabela."""
    config = TABLE_CONFIG[table_name]
    
    # 1. Formata e Mapeia os dados do Frontend para o nome da Coluna SQL
    data = _format_data(data, table_name)
    sql_data = {}
    for sql_col in config['columns']:
        # Determina a chave usada pelo frontend (ex: 'id' ou 'nome')
        app_key = config.get('mapping', {}).get(sql_col, sql_col)
        
        # Trata o caso em que a PK é 'patrimonio_id' no SQL, mas 'id' no Frontend
        if sql_col == config["pk_column"] and app_key == config["pk_column"]:
            app_key = 'id' 
            
        sql_data[sql_col] = data.get(app_key)


    columns_list = ', '.join(config['columns'])
    placeholders = ', '.join([f":{col}" for col in config['columns']])
    
    query = f"INSERT INTO {table_name} ({columns_list}) VALUES ({placeholders})"
    
    try:
        with conn.session as session:
            # EXECUTE: Usa text() para string SQL + placeholders nomeados
            session.execute(text(query), sql_data)
            session.commit()
    except Exception as e:
        # Exceção específica para conflito de chave primária no PostgreSQL
        if 'duplicate key value violates unique constraint' in str(e):
             raise Exception(f"O ID já existe na tabela '{table_name}'.")
        raise e


def update_item(table_name: str, item_id: str, data: Dict):
    """Atualiza um registro em uma tabela pelo ID."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]

    # 1. Formata os dados
    data = _format_data(data, table_name)

    # 2. Constrói o dicionário de atualização SQL e as cláusulas SET
    update_data_sql = {}
    
    for app_key, app_value in data.items():
        if app_key == 'id':
            continue

        # Mapeia a chave do frontend (app_key) de volta para o nome da coluna SQL (sql_col)
        sql_col = next((k for k, v in config.get('mapping', {}).items() if v == app_key), app_key)
        
        if sql_col == pk_column:
            continue
            
        update_data_sql[sql_col] = app_value

    if not update_data_sql:
        return 

    # Constrói as cláusulas SET: "coluna1 = :coluna1, coluna2 = :coluna2..."
    set_clauses = ', '.join([f"{sql_col} = :{sql_col}" for sql_col in update_data_sql.keys()])
    
    # Usa o placeholder nomeado :pk_value para o item_id
    query = f"UPDATE {table_name} SET {set_clauses} WHERE {pk_column} = :pk_value"
    
    update_data_sql['pk_value'] = item_id # Adiciona o valor da PK ao dicionário de execução
    
    try:
        with conn.session as session:
            # EXECUTE: Usa text() para string SQL + placeholders nomeados
            session.execute(text(query), update_data_sql)
            session.commit()
    except Exception as e:
        raise e


def delete_item(table_name: str, item_id: str):
    """Exclui um registro de uma tabela pelo ID."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]
    
    # Usa placeholder nomeado (:item_id)
    query = f"DELETE FROM {table_name} WHERE {pk_column} = :item_id"
    
    try:
        with conn.session as session:
            # EXECUTE: Usa text() para string SQL + placeholders nomeados
            session.execute(text(query), {'item_id': item_id})
            session.commit()
    except Exception as e:
        raise e
