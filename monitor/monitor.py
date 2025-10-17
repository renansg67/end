import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from database import (
    fetch_access_counts, 
    fetch_user_activity,
    get_user_email_safely,
    update_user_activity
)

# ====================================================================
# CONFIGURAÇÃO GERAL
# ====================================================================

# Define o tempo limite para um usuário ser considerado "Online" (em minutos)
INACTIVITY_THRESHOLD_MINUTES = 5

def format_status(row):
    """
    Calcula se o usuário está Online, Inativo ou Offline baseado no último acesso.
    Retorna o status formatado com emoji.
    """
    if pd.isna(row['ultimo_acesso_ativo']):
        return "⚪ Offline"
    
    last_access = row['ultimo_acesso_ativo'].to_pydatetime()
    time_difference = datetime.now() - last_access
    
    if time_difference < timedelta(minutes=INACTIVITY_THRESHOLD_MINUTES):
        # Online: Último acesso há menos de 5 minutos
        return f"🟢 Online (em {row['last_access_page']})"
    elif time_difference < timedelta(minutes=60):
        # Inativo: Último acesso entre 5 e 60 minutos
        return f"🟡 Inativo (há {int(time_difference.total_seconds() // 60)} min)"
    else:
        # Offline: Último acesso há mais de 60 minutos
        return f"🔴 Offline"

def format_timedelta(dt):
    """Formata a diferença de tempo para exibição amigável."""
    if pd.isna(dt):
        return "N/A"
        
    delta = datetime.now() - dt.to_pydatetime()
    seconds = delta.total_seconds()

    if seconds < 60:
        return f"{int(seconds)} segundos atrás"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{int(minutes)} min atrás"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{int(hours)} horas atrás"
    else:
        days = seconds // 86400
        return f"{int(days)} dias atrás"

def show_monitor_page():
    user_email = get_user_email_safely()
    user_role = st.session_state['user_role']

    update_user_activity(user_email, user_role, 'monitor')

    col1, col2, col3 = st.columns([1, 5, 1])
    col2.title("💻 Monitor de Atividade & Acessos")
    col2.markdown("---")

    # --- 1. MONITORAMENTO EM TEMPO REAL ---
    col2.header("Status em Tempo Real (Atualização a cada 10s)")
    
    # Criamos um placeholder para atualizar dinamicamente o status
    realtime_placeholder = st.empty()
    
    # Colocamos a lógica de atualização dentro do placeholder
    with realtime_placeholder.container():
        
        # O Streamlit connection usa um TTL=10s para cache, garantindo atualização.
        df_activity = fetch_user_activity()

        if df_activity.empty:
            col2.info("Nenhuma atividade registrada ainda.")
            
        else:
            # Calcula o Status
            df_activity['status'] = df_activity.apply(format_status, axis=1)
            
            # Formata a última atividade
            df_activity['Última Atividade'] = df_activity['ultimo_acesso_ativo'].apply(format_timedelta)
            
            # Renomeia e seleciona colunas para exibição
            df_display = df_activity[[
                'status', 
                'Última Atividade',
                'email', 
                'role', 
                'last_access_page'
            ]].rename(columns={
                'email': 'Usuário',
                'role': 'Função',
                'last_access_page': 'Página Atual'
            })
            
            # Oculta a coluna original para evitar confusão se o usuário expandir
            df_display['Página Atual'] = df_display['Página Atual'].str.title()
            
            # Exibe o Dataframe em tempo real
            col2.dataframe(
                df_display, 
                width="stretch",
                hide_index=True
            )
            
            # Métricas rápidas
            col1, col2, col3, col4, col5 = st.columns([1, 1.67, 1.67, 1.67, 1])
            col2.metric("Usuários Ativos", df_activity['status'].str.contains("🟢 Online").sum())
            col3.metric("Usuários Inativos", df_activity['status'].str.contains("🟡 Inativo").sum())
            col4.metric("Usuários Registrados", df_activity['email'].nunique())

    col1, col2, col3 = st.columns([1, 5, 1])
    col2.markdown("---")

    # --- 2. HISTÓRICO GERAL DE ACESSOS ---
    col2.header("Histórico de Acessos e Estatísticas")

    with st.spinner("Buscando estatísticas de acesso..."):
        df_counts = fetch_access_counts()
    
    if not df_counts.empty:
        # Formata a coluna 'ultimo_acesso' para exibição
        df_counts['ultimo_acesso'] = df_counts['ultimo_acesso'].dt.strftime('%d/%m/%Y %H:%M:%S')
        
        # Renomeia colunas para exibição
        df_counts.rename(columns={
            'email': 'Usuário',
            'role': 'Função',
            'total_acessos': 'Total de Logins',
            'ultimo_acesso': 'Último Login'
        }, inplace=True)

        col2.dataframe(
            df_counts,
            width="stretch",
            hide_index=True
        )
    else:
        col2.warning("Nenhum histórico de acesso encontrado na tabela 'acessos'.")
        

if __name__ == '__main__':
    # Esta parte só é executada se este arquivo for rodado como script principal, 
    # mas em uma aplicação multipáginas, ele é acessado via app.py
    show_monitor_page()
