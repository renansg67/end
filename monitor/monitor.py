# pages/monitoramento_acessos.py

import streamlit as st
import pandas as pd
# Removido 'datetime' e 'fetch_all_accesses' se não for mais usada
from database import fetch_access_counts 

# A página Streamlit é o código direto. Não precisamos do wrapper show_access_monitor_page()
# Vamos definir as colunas de layout
col1, col2, col3 = st.columns([1, 5, 1])

# 1. Obter a role do usuário logado 
user_role = st.session_state.get('user_role')

col2.title("👁️ Monitoramento de Acessos")
st.markdown("---")

# 2. Verificação de Permissão
if user_role != "admin":
    col2.error("🔒 Acesso Negado. Apenas usuários com a função **ADMIN** podem visualizar o log de acessos.")
else:
    # --- RENDERIZAÇÃO APENAS PARA ADMIN ---
    col2.header("Log de Acessos Agregados por Usuário")

    try:
        # ATENÇÃO: CHAMADA CORRETA PARA A FUNÇÃO DE CONTAGEM
        df_acessos = fetch_access_counts() 
        
        # --- DEBUG: Verifique se há dados (apenas para Admin) ---
        # Remova esta linha após confirmar que funciona
        # col2.write("DEBUG: Dados retornados pela função fetch_access_counts:")
        # col2.write(df_acessos) 
        # --------------------------------------------------------
        
        if df_acessos.empty:
            col2.info("Nenhum acesso registrado ainda. Faça um login para iniciar o log.")
        else:
            col2.dataframe(
                df_acessos, 
                width="stretch",
                hide_index=True,
                column_config={
                    "email": "E-mail do Usuário",
                    "role": st.column_config.TextColumn("Função", help="Função mais recente do usuário."),
                    # MAPEAMENTO DAS NOVAS COLUNAS
                    "total_acessos": st.column_config.NumberColumn(
                        "Total de Acessos",
                        help="Número total de logins deste usuário.",
                        format="%d"
                    ),
                    "ultimo_acesso": st.column_config.DatetimeColumn(
                        "Último Acesso",
                        help="Data e hora do login mais recente.",
                        format="DD/MM/YYYY HH:mm:ss"
                    )
                }
            )
    except Exception as e:
        col2.error(f"Erro ao carregar o log de acessos: {e}")
        col2.exception(e)