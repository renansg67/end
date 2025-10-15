# database.py

import sqlite3
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime

# Nome do arquivo do banco de dados SQLite
DB_NAME = "catalogo_laboratorio.db" 

# --- FUNÇÕES GLOBAIS DE CONEXÃO ---

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados. 
       Deve ser usada em um bloco 'with'."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

# ====================================================================
# CRIAÇÃO DAS TABELAS
# ====================================================================

def create_tables():
    """Cria as tabelas 'livros', 'equipamentos' e 'acessos' se elas não existirem."""
    with get_db_connection() as conn: 
        cursor = conn.cursor()

        # 1. Tabela Livros
        # Colunas tiradas do seu TABLE_CONFIG['livros']
        cursor.execute("""
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
        """)

        # 2. Tabela Equipamentos
        # Colunas tiradas do seu TABLE_CONFIG['equipamentos']
        cursor.execute("""
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
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS acessos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,         
                data_hora_acesso TEXT NOT NULL,
                role TEXT
            );
        """)
        
        conn.commit()

def register_access(email: str, role: str):
    """
    Registra um novo evento de acesso para fins de contagem.
    (Usa INSERT simples para que cada login crie uma nova linha).
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    query = """
        INSERT INTO acessos (email, data_hora_acesso, role) 
        VALUES (:email, :data_hora_acesso, :role)
    """
    
    data = {
        'email': email,
        'data_hora_acesso': current_time,
        'role': role
    }

    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, data)
            conn.commit()
        except Exception as e:
            # Recomenda-se apenas imprimir o erro e seguir, para não quebrar a aplicação
            print(f"Alerta: Falha ao registrar acesso do usuário {email}. Erro: {e}")

def fetch_all_accesses() -> pd.DataFrame:
    """Busca o log de último acesso de todos os usuários."""
    with get_db_connection() as conn:
        df = pd.read_sql_query("SELECT email, data_hora_acesso, role FROM acessos ORDER BY data_hora_acesso DESC", conn)
    return df

def fetch_access_counts() -> pd.DataFrame:
    """
    Busca o total de acessos por usuário. (Versão simplificada para teste)
    """
    query = """
        SELECT
            email,
            COUNT(id) AS total_acessos,         
            MAX(data_hora_acesso) AS ultimo_acesso
        FROM acessos
        GROUP BY email
        ORDER BY ultimo_acesso DESC;
    """
    with get_db_connection() as conn:
        df = pd.read_sql_query(query, conn)
        
    # **Adicione o role separadamente se necessário:**
    if not df.empty:
        # Pega a role mais recente de cada usuário (a que está no log mais recente)
        role_query = """
            SELECT email, role 
            FROM acessos 
            WHERE data_hora_acesso IN (SELECT MAX(data_hora_acesso) FROM acessos GROUP BY email)
        """
        df_roles = pd.read_sql_query(role_query, conn)
        df = pd.merge(df, df_roles, on='email', how='left')
        
    return df

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
        "format_cols": [] # Equipamentos não precisam de formatação especial aqui
    }
}

# --- FUNÇÃO AUXILIAR DE FORMATAÇÃO ---
def _format_data(data: Dict, table_name: str) -> Dict:
    """Aplica formatação específica (ex: lista para string) aos dados."""
    config = TABLE_CONFIG[table_name]
    
    # Faz uma cópia para não modificar o dicionário original
    formatted_data = data.copy()
    
    # Lógica específica para o campo 'palavras_chave' (se for lista)
    if table_name == "livros" and 'palavras_chave' in formatted_data and isinstance(formatted_data['palavras_chave'], list):
        formatted_data['palavras_chave'] = ', '.join(formatted_data['palavras_chave'])
        
    return formatted_data

# ====================================================================
# FUNÇÕES CRUD GENERALIZADAS
# ====================================================================

def fetch_all_items(table_name: str) -> pd.DataFrame:
    """Busca todos os itens de uma tabela e aplica o mapeamento (se houver)."""
    config = TABLE_CONFIG[table_name]
    
    with get_db_connection() as conn:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)
    
    # Aplica o mapeamento (SQL -> Frontend) se estiver definido
    if 'mapping' in config:
        reverse_mapping = {sql_col: app_col for sql_col, app_col in config['mapping'].items()}
        df.rename(columns=reverse_mapping, inplace=True)
    
    # Renomeia a coluna PK para o nome amigável 'id' no DataFrame, se necessário
    if config['pk_column'] != 'id':
         df.rename(columns={config['pk_column']: 'id'}, inplace=True)

    return df


def add_item(table_name: str, data: Dict):
    """Insere um novo registro em uma tabela."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]
    
    # 1. Formata os dados (listas para strings, etc.)
    data = _format_data(data, table_name)
    
    # 2. Mapeamento de Chaves do Frontend para SQL (se necessário)
    # A lógica aqui é mais complexa, pois precisamos dos nomes exatos da tabela SQL
    sql_data = {}
    for sql_col in config['columns']:
        # Tenta reverter o mapeamento: usa o nome do frontend, senão usa o próprio nome SQL
        app_key = config.get('mapping', {}).get(sql_col, sql_col)
        
        # O PK é tratado separadamente, pois o frontend pode chamá-lo de 'id'
        if sql_col == pk_column and app_key == pk_column:
             app_key = 'id' # Assume que o frontend passa a PK como 'id'

        sql_data[sql_col] = data.get(app_key)


    columns_list = ', '.join(config['columns'])
    placeholders = ', '.join([f":{col}" for col in config['columns']])
    
    query = f"INSERT INTO {table_name} ({columns_list}) VALUES ({placeholders})"
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, sql_data)
            conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError(f"O ID {data.get('id')} já existe na tabela '{table_name}'.")
        except Exception as e:
            raise e

def update_user_activity(email: str):
    """
    Atualiza o timestamp da última atividade do usuário.
    Usa INSERT OR REPLACE INTO para garantir que só haja um registro por email.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    query = """
        INSERT OR REPLACE INTO usuarios_atividade (email, ultimo_acesso_ativo) 
        VALUES (:email, :ultimo_acesso_ativo)
    """
    
    data = {
        'email': email,
        'ultimo_acesso_ativo': current_time
    }

    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, data)
            conn.commit()
        except Exception as e:
            # Falha silenciosa
            print(f"Alerta: Falha ao registrar atividade do usuário {email}. Erro: {e}")

def update_item(table_name: str, item_id: str, data: Dict):
    """Atualiza um registro em uma tabela pelo ID."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]

    # 1. Formata os dados
    data = _format_data(data, table_name)

    # 2. Constrói o dicionário de atualização SQL e as cláusulas SET
    update_data_sql = {}
    
    # Mapeia as chaves do frontend para as colunas SQL e ignora a PK
    for app_key, app_value in data.items():
        if app_key == 'id':
            continue

        # Tenta reverter o mapeamento: pega o nome SQL. Se não, usa a chave do frontend
        sql_col = next((k for k, v in config.get('mapping', {}).items() if v == app_key), app_key)
        
        # Garante que a coluna não seja a PK
        if sql_col == pk_column:
            continue
            
        update_data_sql[sql_col] = app_value

    if not update_data_sql:
        return # Nada para atualizar

    set_clauses = ', '.join([f"{sql_col} = :{sql_col}" for sql_col in update_data_sql.keys()])
    
    # Usa um placeholder nomeado para o WHERE
    query = f"UPDATE {table_name} SET {set_clauses} WHERE {pk_column} = :pk_value"
    
    # Adiciona o valor da PK ao dicionário de execução
    update_data_sql['pk_value'] = item_id
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, update_data_sql)
            conn.commit()
        except Exception as e:
            raise e


def delete_item(table_name: str, item_id: str):
    """Exclui um registro de uma tabela pelo ID."""
    config = TABLE_CONFIG[table_name]
    pk_column = config["pk_column"]
    
    query = f"DELETE FROM {table_name} WHERE {pk_column} = ?"
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, (item_id,))
            conn.commit()
        except Exception as e:
            raise e
