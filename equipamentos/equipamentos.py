# equipamentos/equipamentos.py

import streamlit as st
import pandas as pd
from datetime import datetime

# Importa AUTH do app.py e CRUD de Equipamentos do database.py
from app import get_user_email_safely, get_user_role 
from database import (
    fetch_all_items, 
    add_item, 
    update_item, 
    delete_item
)

def fetch_all_equipamentos():
    return fetch_all_items("equipamentos")

def add_equipamento(data):
    # O frontend envia a PK como 'id'
    return add_item("equipamentos", data)

def update_equipamento(equip_id, data):
    return update_item("equipamentos", equip_id, data)

def delete_equipamento(equip_id):
    return delete_item("equipamentos", equip_id)

# =========================================================================
# FUNÇÃO DE ADMIN/CRUD PARA EQUIPAMENTOS
# =========================================================================

def show_admin_interface_equipamentos(df_equipamentos, user_role):
    """Renderiza os formulários de CRUD para equipamentos, visível apenas para Admin/Editor."""
    
    col1, col2, col3 = st.columns([1, 5, 1])
    col2.header("🛠️ Administração de Equipamentos (CRUD)")
    col2.markdown("---") 
    
    tab_create, tab_update, tab_delete = col2.tabs(["➕ Criar Equipamento", "✏️ Editar Equipamento", "🗑️ Deletar Equipamento"])

    # --- TAB CRIAR ---
    with tab_create:
        st.subheader("Cadastrar Novo Equipamento")
        
        with st.form("form_create_equipamento", clear_on_submit=True):
            
            # CHAVES ÚNICAS: create_new_...
            col1, col2 = st.columns(2)
            new_id = col1.text_input("1. ID Único/Tag de Patrimônio", key="create_new_equip_id_key")
            new_nome = col2.text_input("2. Nome do Equipamento", key="create_new_equip_nome_key")
            
            col3, col4 = st.columns(2)
            new_fabricante = col3.text_input("3. Fabricante", key="create_new_equip_fabricante_key")
            new_modelo = col4.text_input("4. Modelo", key="create_new_equip_modelo_key")
            
            col5, col6 = st.columns(2)
            opcoes_local = ["Sala de Ensaios", "Sala de Preparação", "Campo", "Depósito"]
            new_localizacao = col5.selectbox("5. Localização Atual", options=opcoes_local, key="create_new_equip_localizacao_key")
            
            opcoes_disp = ["Disponível", "Em Uso", "Em Manutenção", "Em Calibração"]
            new_disponibilidade = col6.selectbox("6. Disponibilidade", options=opcoes_disp, key="create_new_equip_disponibilidade_key")
            
            new_descricao = st.text_area("7. Descrição/Especificações", key="create_new_equip_descricao_key")
            
            col7, col8 = st.columns(2)
            new_data_aquisicao = col7.date_input("8. Data de Aquisição", value=datetime.now().date(), key="create_new_equip_data_aquisicao_key")
            new_link_manual = col8.text_input("9. Link do Manual (URL)", key="create_new_equip_link_manual_key")

            # 10. Data de Entrada (Campo interno)
            new_data_de_entrada_sistema = str(datetime.now().date())
            st.markdown(f"**10. Data de Entrada no Sistema:** _{new_data_de_entrada_sistema}_")
            
            submitted = st.form_submit_button("Cadastrar Equipamento", type="primary")
            
            if submitted:
                new_data = {
                    'id': new_id, 
                    'nome': new_nome, 
                    'fabricante': new_fabricante, 
                    'modelo': new_modelo,
                    'localizacao': new_localizacao,
                    'disponibilidade': new_disponibilidade,
                    'descricao': new_descricao,
                    'data_aquisicao': str(new_data_aquisicao), # Converter para string
                    'link_manual': new_link_manual,
                    'data_de_entrada_sistema': new_data_de_entrada_sistema
                }

                try:
                    add_equipamento(new_data)
                    st.success(f"Equipamento '{new_nome}' cadastrado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao cadastrar: {e}")

    # --- TAB EDITAR (COM CHAVES DINÂMICAS) ---
    with tab_update:
        st.subheader("Editar Equipamento Existente")

        # Inicializa o estado de sessão para o equipamento selecionado
        if 'selected_equip_id' not in st.session_state:
            st.session_state['selected_equip_id'] = None
        
        if df_equipamentos.empty:
            st.info("Nenhum equipamento para editar.")
            return 
            
        # 1. Seleção do Equipamento
        equip_names = df_equipamentos['nome'].tolist()
        name_to_id = {row['nome']: row['id'] for index, row in df_equipamentos.iterrows()}
        
        # Lógica de persistência da seleção
        initial_name = None
        if st.session_state['selected_equip_id'] is not None:
            id_to_name = {v: k for k, v in name_to_id.items()}
            initial_name = id_to_name.get(st.session_state['selected_equip_id'])

        if initial_name is None and equip_names:
             initial_name = equip_names[0]
        
        initial_index = equip_names.index(initial_name) if initial_name in equip_names else 0


        selected_name = st.selectbox(
            "Selecione o Equipamento para Edição:", 
            equip_names, 
            index=initial_index,
            key="update_select_equip_name_key" 
        )
        
        # 2. Atualizar o estado de sessão e obter o ID
        if selected_name:
            equip_id = name_to_id.get(selected_name)
            st.session_state['selected_equip_id'] = equip_id
        else:
            equip_id = None


        # 3. Renderização do Formulário de Edição
        if equip_id:
            current_equip = df_equipamentos[df_equipamentos['id'] == equip_id].iloc[0].to_dict()

            st.info(f"Editando equipamento com ID (não editável): **{equip_id}**")
            
            with st.form("form_update_equipamento"):
                
                # CHAVES DINÂMICAS: f"update_up_nome_{equip_id}"
                col1, col2 = st.columns(2)
                up_nome = col1.text_input("2. Nome do Equipamento", value=current_equip.get('nome', ''), key=f"update_up_equip_nome_{equip_id}")
                up_fabricante = col2.text_input("3. Fabricante", value=current_equip.get('fabricante', ''), key=f"update_up_equip_fabricante_{equip_id}")
                
                col3, col4 = st.columns(2)
                up_modelo = col3.text_input("4. Modelo", value=current_equip.get('modelo', ''), key=f"update_up_equip_modelo_{equip_id}")
                
                opcoes_local = ["Sala de Ensaios", "Sala de Preparação", "Campo", "Depósito"]
                up_localizacao = col4.selectbox("5. Localização Atual", options=opcoes_local, 
                                                index=opcoes_local.index(current_equip.get('localizacao', opcoes_local[0])), 
                                                key=f"update_up_equip_localizacao_{equip_id}")
                
                opcoes_disp = ["Disponível", "Em Uso", "Em Manutenção", "Em Calibração"]
                up_disponibilidade = st.selectbox("6. Disponibilidade", options=opcoes_disp, 
                                                  index=opcoes_disp.index(current_equip.get('disponibilidade', opcoes_disp[0])), 
                                                  key=f"update_up_equip_disponibilidade_{equip_id}")
                
                up_descricao = st.text_area("7. Descrição/Especificações", value=current_equip.get('descricao', ''), key=f"update_up_equip_descricao_{equip_id}")
                
                col5, col6 = st.columns(2)
                # O Streamlit `date_input` espera um objeto date ou string 'YYYY-MM-DD'
                data_aquisicao_date = datetime.strptime(current_equip.get('data_aquisicao'), '%Y-%m-%d').date() if current_equip.get('data_aquisicao') else datetime.now().date()
                up_data_aquisicao = col5.date_input("8. Data de Aquisição", value=data_aquisicao_date, key=f"update_up_equip_data_aquisicao_{equip_id}")
                up_link_manual = col6.text_input("9. Link do Manual (URL)", value=current_equip.get('link_manual', ''), key=f"update_up_equip_link_manual_{equip_id}")

                st.markdown(f"**10. Data de Entrada no Sistema:** _{current_equip.get('data_de_entrada_sistema', 'N/A')}_")

                submitted_update = st.form_submit_button("Atualizar Equipamento", type="primary")
                
                if submitted_update:
                    update_data = {
                        'nome': up_nome, 
                        'fabricante': up_fabricante, 
                        'modelo': up_modelo,
                        'localizacao': up_localizacao,
                        'disponibilidade': up_disponibilidade,
                        'descricao': up_descricao,
                        'data_aquisicao': str(up_data_aquisicao),
                        'link_manual': up_link_manual
                    }
                    try:
                        update_equipamento(equip_id, update_data)
                        st.success(f"Equipamento '{up_nome}' atualizado com sucesso!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao atualizar: {e}")
        else:
            st.info("Selecione um equipamento para exibir o formulário de edição.")

    # --- TAB DELETAR ---
    with tab_delete:
        st.subheader("Deletar Equipamento")

        if df_equipamentos.empty:
            st.info("Nenhum equipamento para deletar.")
            return

        equip_names_del = df_equipamentos['nome'].tolist()
        selected_name_del = st.selectbox("Selecione o Equipamento para DELETAR:", equip_names_del, key="delete_select_equip_key")
        
        if selected_name_del:
            current_equip_del = df_equipamentos[df_equipamentos['nome'] == selected_name_del].iloc[0]
            equip_id_del = current_equip_del['id']
            
            st.warning(f"Confirme a exclusão do equipamento: **{selected_name_del}** (ID: {equip_id_del})")
            
            if st.button("🗑️ DELETAR IRREVERSIVELMENTE", type="secondary", key="delete_equip_button_final"):
                try:
                    delete_equipamento(equip_id_del)
                    st.success(f"Equipamento '{selected_name_del}' excluído com sucesso.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao deletar: {e}")

# =========================================================================
# CORPO PRINCIPAL DA PÁGINA
# =========================================================================

# 1. Obter e verificar a role do usuário
user_email = get_user_email_safely()
user_role = get_user_role(user_email) if user_email else None

if not user_email:
    st.error("Por favor, faça login para acessar a página de Equipamentos.")
    st.stop()
    
col1, col2, col3 = st.columns([1, 5, 1])
col2.title("🛠️ Catálogo de Equipamentos")

# 2. Carregar dados do DB
try:
    df = fetch_all_equipamentos()
    # Converte listas/objetos (se houver) para strings (similar à biblioteca)
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df[col] = df[col].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)

    df = df.dropna(axis=1, how="all")

except Exception as e:
    col2.info(f"Erro ao carregar o catálogo de equipamentos do banco de dados: {e}")
    df = pd.DataFrame() 

# 3. RENDERIZAÇÃO CONDICIONAL DO CRUD
if user_role in ["admin", "editor"]:
    col1, col2, col3, col4 = st.columns([1, 4, 1, 1])
    off = col3.toggle("Habilitar edição", value=False)
    if off:
        show_admin_interface_equipamentos(df, user_role)
        st.markdown("---") 

col1, col2, col3 = st.columns([1, 5, 1])
# 4. Interface de Consulta
if df.empty:
    col2.info("Nenhum equipamento cadastrado no acervo ainda.")
else:
    col2.header("🔍 Equipamentos para Consulta")
    
    # Colunas a serem exibidas na tabela de consulta
    colunas_exibicao = [
        "nome", "modelo", "fabricante", "localizacao", "disponibilidade",
        "data_aquisicao", "link_manual" 
    ]
    
    colunas = [c for c in colunas_exibicao if c in df.columns]
    df_exibicao = df[colunas]

    busca = col2.text_input("🔍 Buscar por nome, fabricante ou modelo:", key="search_equip_consulta")

    if busca:
        mask = (
            df_exibicao["nome"].astype(str).str.contains(busca, case=False, na=False) |
            df_exibicao["fabricante"].astype(str).str.contains(busca, case=False, na=False) |
            df_exibicao["modelo"].astype(str).str.contains(busca, case=False, na=False)
        )
        df_filtrado = df_exibicao[mask]
    else:
        df_filtrado = df_exibicao

    col2.dataframe(
        df_filtrado,
        hide_index=True,
        width="stretch",
    )