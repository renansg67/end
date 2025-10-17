import streamlit as st
import pandas as pd
from datetime import datetime

# Importa as funções de CRUD de Equipamentos do database.py
from database import (
    fetch_all_items, 
    add_item, 
    update_item, 
    delete_item,
    get_user_email_safely,
    update_user_activity
)

# =========================================================================
# FUNÇÕES DE ACESSO A DADOS (com cache)
# =========================================================================

@st.cache_data(ttl=60)
def fetch_all_equipamentos():
    """Busca todos os equipamentos do DB com cache."""
    return fetch_all_items("equipamentos")

def add_equipamento(data):
    """Adiciona um equipamento e invalida o cache de dados."""
    st.cache_data.clear()
    return add_item("equipamentos", data)

def update_equipamento(equip_id, data):
    """Atualiza um equipamento e invalida o cache de dados."""
    st.cache_data.clear()
    return update_item("equipamentos", equip_id, data)

def delete_equipamento(equip_id):
    """Deleta um equipamento e invalida o cache de dados."""
    st.cache_data.clear()
    return delete_item("equipamentos", equip_id)

# =========================================================================
# COMPONENTES DE ADMINISTRAÇÃO (Formulários de CRUD)
# =========================================================================

def render_form_create_equipamento():
    """Renderiza o formulário de criação."""
    st.subheader("➕ Cadastrar Novo Equipamento")
    
    # CHAVE FINAL ÚNICA: Garantia contra duplicação
    with st.form("form_create_equipamento_unique_key_equip", clear_on_submit=True):
        
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

        new_data_de_entrada_sistema = str(datetime.now().date())
        st.markdown(f"**10. Data de Entrada no Sistema:** _{new_data_de_entrada_sistema}_")
        
        submitted = st.form_submit_button("Cadastrar Equipamento", type="primary", key="submit_create_equip_button")
        
        if submitted:
            new_data = {
                'id': new_id, 'nome': new_nome, 'fabricante': new_fabricante, 'modelo': new_modelo,
                'localizacao': new_localizacao, 'disponibilidade': new_disponibilidade,
                'descricao': new_descricao, 'data_aquisicao': str(new_data_aquisicao), 
                'link_manual': new_link_manual, 'data_de_entrada_sistema': new_data_de_entrada_sistema
            }

            if not new_id or not new_nome:
                st.error("O ID Único e o Nome são campos obrigatórios.")
                return

            try:
                add_equipamento(new_data)
                st.success(f"Equipamento '{new_nome}' cadastrado com sucesso!")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao cadastrar: {e}")

def render_form_update_equipamento(df_equipamentos):
    """Renderiza o formulário de edição (com chaves dinâmicas)."""
    st.subheader("✏️ Editar Equipamento Existente")

    if df_equipamentos.empty:
        st.info("Nenhum equipamento para editar.")
        return 
            
    # O DataFrame passado aqui já teve a coluna 'id' convertida para string
    # na função principal (equipamentos_main_page), evitando o SettingWithCopyWarning.
    
    equip_names = df_equipamentos['nome'].tolist()
    name_to_id = {row['nome']: row['id'] for index, row in df_equipamentos.iterrows()}
    
    # Chave ESTÁTICA única para o selectbox de seleção
    selected_name = st.selectbox(
        "Selecione o Equipamento para Edição:", 
        equip_names, 
        key="update_select_equip_name_static_key" 
    )
    
    equip_id = name_to_id.get(selected_name)

    # 3. Renderização do Formulário de Edição (Somente se um ID for selecionado)
    if equip_id:
        current_equip = df_equipamentos[df_equipamentos['id'] == equip_id].iloc[0].to_dict()

        st.info(f"Editando equipamento com ID (não editável): **{equip_id}**")
        
        # CHAVE FINAL DINÂMICA (depende do ID do equipamento)
        with st.form(f"form_update_equipamento_dynamic_key_{equip_id}"):
            
            # CHAVES DINÂMICAS: f"update_up_nome_{equip_id}"
            col1, col2 = st.columns(2)
            up_nome = col1.text_input("2. Nome do Equipamento", value=current_equip.get('nome', ''), key=f"update_up_equip_nome_{equip_id}")
            up_fabricante = col2.text_input("3. Fabricante", value=current_equip.get('fabricante', ''), key=f"update_up_equip_fabricante_{equip_id}")
            
            col3, col4 = st.columns(2)
            up_modelo = col3.text_input("4. Modelo", value=current_equip.get('modelo', ''), key=f"update_up_equip_modelo_{equip_id}")
            
            opcoes_local = ["Sala de Ensaios", "Sala de Preparação", "Campo", "Depósito"]
            local_index = opcoes_local.index(current_equip.get('localizacao', opcoes_local[0])) if current_equip.get('localizacao') in opcoes_local else 0
            up_localizacao = col4.selectbox("5. Localização Atual", options=opcoes_local, 
                                            index=local_index, 
                                            key=f"update_up_equip_localizacao_{equip_id}")
            
            opcoes_disp = ["Disponível", "Em Uso", "Em Manutenção", "Em Calibração"]
            disp_index = opcoes_disp.index(current_equip.get('disponibilidade', opcoes_disp[0])) if current_equip.get('disponibilidade') in opcoes_disp else 0
            up_disponibilidade = st.selectbox("6. Disponibilidade", options=opcoes_disp, 
                                            index=disp_index, 
                                            key=f"update_up_equip_disponibilidade_{equip_id}")
            
            up_descricao = st.text_area("7. Descrição/Especificações", value=current_equip.get('descricao', ''), key=f"update_up_equip_descricao_{equip_id}")
            
            col5, col6 = st.columns(2)
            # Converte a data de aquisição para o formato date (se existir)
            data_aquisicao_date = datetime.strptime(current_equip.get('data_aquisicao'), '%Y-%m-%d').date() if current_equip.get('data_aquisicao') and current_equip.get('data_aquisicao') != 'N/A' else datetime.now().date()
            up_data_aquisicao = col5.date_input("8. Data de Aquisição", value=data_aquisicao_date, key=f"update_up_equip_data_aquisicao_{equip_id}")
            up_link_manual = col6.text_input("9. Link do Manual (URL)", value=current_equip.get('link_manual', ''), key=f"update_up_equip_link_manual_{equip_id}")

            st.markdown(f"**10. Data de Entrada no Sistema:** _{current_equip.get('data_de_entrada_sistema', 'N/A')}_")

            submitted_update = st.form_submit_button("Atualizar Equipamento", type="primary", key=f"submit_update_equip_button_{equip_id}")
            
            if submitted_update:
                update_data = {
                    'nome': up_nome, 'fabricante': up_fabricante, 'modelo': up_modelo,
                    'localizacao': up_localizacao, 'disponibilidade': up_disponibilidade,
                    'descricao': up_descricao, 'data_aquisicao': str(up_data_aquisicao),
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

def render_form_delete_equipamento(df_equipamentos):
    """Renderiza o componente de deleção."""
    st.subheader("🗑️ Deletar Equipamento")

    if df_equipamentos.empty:
        st.info("Nenhum equipamento para deletar.")
        return

    equip_names_del = df_equipamentos['nome'].tolist()
    
    # Chave ESTÁTICA única para o selectbox de deleção
    selected_name_del = st.selectbox("Selecione o Equipamento para DELETAR:", equip_names_del, key="delete_select_equip_static_key")
    
    if selected_name_del:
        current_equip_del = df_equipamentos[df_equipamentos['nome'] == selected_name_del].iloc[0]
        equip_id_del = current_equip_del['id']
        
        st.warning(f"Confirme a exclusão do equipamento: **{selected_name_del}** (ID: {equip_id_del})")
        
        # CHAVE ÚNICA para o botão de deleção
        if st.button("🗑️ DELETAR IRREVERSIVELMENTE", type="secondary", key="delete_equip_button_final_unique"):
            try:
                delete_equipamento(equip_id_del)
                st.success(f"Equipamento '{selected_name_del}' excluído com sucesso.")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao deletar: {e}")

# =========================================================================
# CORPO PRINCIPAL DA PÁGINA
# =========================================================================

def equipamentos_main_page():
    
    # 1. Obter e verificar a role do usuário (usando funções autônomas)
    user_email = get_user_email_safely()
    user_role = st.session_state['user_role']

    update_user_activity(user_email, user_role, 'equipamentos')

    if not user_email:
        st.error("Por favor, faça login para acessar a página de Equipamentos.")
        st.stop()
        
    col1, col2, col3 = st.columns([1, 5, 1])
    col2.title("🛠️ Catálogo de Equipamentos")

    # 2. Carregar dados do DB
    with st.spinner("Carregando acervo de equipamentos do banco de dados..."):
        try:
            df = fetch_all_equipamentos()
            if not df.empty:
                
                # --- CORREÇÃO DO SETTINGWITHCOPYWARNING ---
                # Garante que 'id' é string usando .loc no DataFrame original
                df.loc[:, 'id'] = df['id'].astype(str)
                # ------------------------------------------

                # Converte listas/objetos (se houver) para strings
                for col in df.columns:
                    if df[col].apply(lambda x: isinstance(x, list)).any():
                        # Usando .loc também aqui para ser consistente
                        df.loc[:, col] = df[col].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
                        
                df = df.dropna(axis=1, how="all")
            else:
                 df = pd.DataFrame(columns=['id', 'nome', 'fabricante', 'modelo'])
        except Exception as e:
            col2.info(f"Erro ao carregar o catálogo de equipamentos do banco de dados: {e}")
            df = pd.DataFrame() 

    # 3. RENDERIZAÇÃO CONDICIONAL DO CRUD (Toggle e Tabs)
    if user_role in ["admin", "editor"]:
        
        # Toggle switch para mostrar/esconder a interface de administração
        show_admin = col2.toggle(
            "🛠️ Mostrar Interface de Administração (CRUD)", 
            value=False, # Começa desligado
            key="toggle_equip_admin_crud_unique_key"
        )
        
        if show_admin:
            
            # Usando st.tabs para organizar as operações
            tab_create, tab_update, tab_delete = col2.tabs(
                ["➕ Criar Equipamento", "✏️ Editar Equipamento", "🗑️ Deletar Equipamento"]
            )

            with tab_create:
                render_form_create_equipamento()

            with tab_update:
                # Cria uma cópia limpa antes de passar (embora a correção já resolva)
                render_form_update_equipamento(df.copy()) 

            with tab_delete:
                render_form_delete_equipamento(df.copy())

            st.markdown("---") 

    # 4. Interface de Consulta (Sempre visível)
    col1, col2, col3 = st.columns([1, 5, 1])
    col2.subheader("Acervo de Equipamentos")

    if df.empty:
        col2.info("Nenhum equipamento cadastrado no acervo ainda.")
    else:
        # Colunas a serem exibidas na tabela de consulta
        colunas_exibicao = [
            "nome", "modelo", "fabricante", "localizacao", "disponibilidade",
            "data_aquisicao", "link_manual", "id"
        ]
        
        colunas = [c for c in colunas_exibicao if c in df.columns]
        df_exibicao = df[colunas]

        busca = col2.text_input("🔍 Buscar por nome, fabricante, modelo ou ID:", key="search_equip_consulta_unique")

        if busca:
            mask = (
                df_exibicao["nome"].astype(str).str.contains(busca, case=False, na=False) |
                df_exibicao["fabricante"].astype(str).str.contains(busca, case=False, na=False) |
                df_exibicao["modelo"].astype(str).str.contains(busca, case=False, na=False) |
                df_exibicao["id"].astype(str).str.contains(busca, case=False, na=False)
            )
            df_filtrado = df_exibicao[mask]
        else:
            df_filtrado = df_exibicao

        col2.dataframe(
            df_filtrado,
            hide_index=True,
            width="stretch"
        )

# =========================================================================
# PONTO DE EXECUÇÃO
# =========================================================================
if __name__ == "__main__":
    equipamentos_main_page()
