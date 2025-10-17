import streamlit as st
import pandas as pd
from datetime import datetime


# ⚠️ ASSUMIMOS QUE database.py EXISTE E CONTÉM AS FUNÇÕES ABAIXO
from database import (
    fetch_all_items, 
    add_item, 
    update_item, 
    delete_item, 
    update_user_activity,
    get_user_email_safely
)

# Assumindo que app.py está acessível para as funções de role
# Isso pode falhar se não estiver na estrutura correta;
# o ideal é passar as informações de autenticação via st.session_state.

# Funções de CRUD Helper
@st.cache_data(ttl=60)
def fetch_all_livros():
    """Busca todos os livros do DB com cache."""
    # Retorna o conteúdo da coleção 'livros'
    return fetch_all_items("livros")

def add_livro(data):
    """Adiciona um livro e invalida o cache de dados."""
    st.cache_data.clear()
    return add_item("livros", data)

def update_livro(livro_id, data):
    """Atualiza um livro e invalida o cache de dados."""
    st.cache_data.clear()
    return update_item("livros", livro_id, data) 

def delete_livro(livro_id):
    """Deleta um livro e invalida o cache de dados."""
    st.cache_data.clear()
    return delete_item("livros", livro_id)

# =========================================================================
# COMPONENTES DE ADMINISTRAÇÃO (Formulários de CRUD)
# =========================================================================

def render_form_create():
    """Renderiza o formulário de criação completo."""
    st.subheader("➕ Cadastrar Novo Livro")
    
    # CHAVE FINAL ÚNICA para o formulário
    with st.form("form_create_livro_unique_key", clear_on_submit=True):
        
        # Campos de entrada
        col1, col2, col3 = st.columns(3)
        # Chaves dos campos (prefixo 'create_' para garantir unicidade)
        new_id = col1.text_input("1. ID Único (Chave Primária)", key="create_new_id_biblio_key") 
        new_titulo = col2.text_input("2. Título", key="create_new_titulo_biblio_key")
        new_autor = col3.text_input("3. Autor(es)", key="create_new_autor_biblio_key")
        
        col4, col5, col6, col7 = st.columns(4)
        new_ano = col4.number_input("4. Ano de Publicação", min_value=1000, max_value=datetime.now().year, value=datetime.now().year, key="create_new_ano_biblio_key")
        new_editora = col5.text_input("5. Editora", key="create_new_editora_biblio_key")
        new_isbn = col6.text_input("6. ISBN", help="Identificação Padrão Internacional do Livro", key="create_new_isbn_biblio_key")
        opcoes_idioma = ["Português", "Inglês", "Espanhol", "Outro"]
        new_idioma = col7.selectbox("7. Idioma", opcoes_idioma, key="create_new_idioma_biblio_key")

        col8, col9, col10 = st.columns(3)
        opcoes_categoria = ["Tese", "Artigo", "Manual", "Livro Didático", "Norma"]
        new_categoria = col8.selectbox("8. Categoria", opcoes_categoria, key="create_new_categoria_biblio_key")
        new_subcategoria = col9.text_input("9. Subcategoria (Opcional)", key="create_new_subcategoria_biblio_key")
        opcoes_material = ["Livro Físico", "E-book", "Periódico", "Relatório"]
        new_tipo_de_material = col10.selectbox("10. Tipo de Material", opcoes_material, key="create_new_tipo_de_material_biblio_key")
        
        new_palavras_chave_str = st.text_input("11. Palavras-Chave (Separadas por vírgula)", help="Ex: concreto, ensaios, materiais compósitos", key="create_new_palavras_chave_biblio_key")
        opcoes_nivel = ["Graduação", "Pós-Graduação", "Pesquisa", "Técnico"]
        new_nivel = st.selectbox("12. Nível", opcoes_nivel, key="create_new_nivel_biblio_key")
        
        col11, col12 = st.columns(2)
        new_localizacao_fisica = col11.text_input("13. Localização Física (Prateleira/Sala)", key="create_new_localizacao_fisica_biblio_key")
        opcoes_disp = ["Disponível", "Emprestado", "Em Manutenção", "Perdido"]
        new_disponibilidade = col12.selectbox("14. Disponibilidade", opcoes_disp, key="create_new_disponibilidade_biblio_key")

        new_resumo = st.text_area("15. Resumo/Descrição", key="create_new_resumo_biblio_key")
        col13, col14 = st.columns(2)
        new_imagem_capa_url = col13.text_input("16. URL Imagem da Capa (Opcional)", key="create_new_imagem_capa_url_biblio_key")
        new_link_externo = col14.text_input("17. Link Externo (E-book/PDF/Compra)", key="create_new_link_externo_biblio_key")
        
        new_data_de_entrada = str(datetime.now().date())
        st.markdown(f"**18. Data de Entrada no Sistema:** _{new_data_de_entrada}_")
        
        submitted = st.form_submit_button("Cadastrar Livro", type="primary", key="submit_create_livro_button")
        
        if submitted:
            new_data = {
                'id': new_id, 'titulo': new_titulo, 'autor': new_autor, 'ano': new_ano,
                'editora': new_editora, 'isbn': new_isbn, 'idioma': new_idioma,
                'categoria': new_categoria, 'subcategoria': new_subcategoria,
                'tipo_de_material': new_tipo_de_material, 'palavras_chave': new_palavras_chave_str,
                'nivel': new_nivel, 'localizacao_fisica': new_localizacao_fisica,
                'disponibilidade': new_disponibilidade, 'resumo': new_resumo,
                'imagem_capa_url': new_imagem_capa_url, 'link_externo': new_link_externo,
                'data_de_entrada': new_data_de_entrada
            }
            try:
                add_livro(new_data)
                st.success(f"Livro '{new_titulo}' cadastrado com sucesso!")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao cadastrar: {e}")

def render_form_update(df):
    """Renderiza o formulário de edição (com chaves dinâmicas)."""
    st.subheader("✏️ Editar Livro")
    
    if df.empty:
        st.info("Nenhum livro para editar.")
        return

    livro_titles = df['titulo'].tolist()
    title_to_id = {row['titulo']: row['id'] for index, row in df.iterrows()}
    
    # Chave estável para o selectbox
    selected_title = st.selectbox(
        "Selecione o Livro para Edição:", 
        livro_titles, 
        key="update_select_livro_static_key" 
    )
    
    livro_id = title_to_id.get(selected_title)

    if livro_id:
        # Garante que 'ano' é um inteiro para o number_input
        current_livro = df[df['id'] == livro_id].iloc[0].to_dict()
        current_livro['ano'] = int(current_livro['ano']) if pd.notna(current_livro.get('ano')) else datetime.now().year

        st.info(f"Editando livro com ID (não editável): **{livro_id}**")
        
        # CHAVE FINAL ÚNICA E DINÂMICA (depende do ID do livro selecionado)
        with st.form(f"form_update_livro_dynamic_key_{livro_id}"):
            
            # Campos de entrada (Chaves Dinâmicas)
            col1, col2, col3 = st.columns(3)
            # ATENÇÃO: Chaves DINÂMICAS com o ID do livro
            up_titulo = col1.text_input("2. Título", value=current_livro.get('titulo', ''), key=f"update_up_titulo_{livro_id}_dynamic")
            up_autor = col2.text_input("3. Autor(es)", value=current_livro.get('autor', ''), key=f"update_up_autor_{livro_id}_dynamic")
            up_ano = col3.number_input("4. Ano de Publicação", min_value=1000, max_value=datetime.now().year, value=current_livro.get('ano'), key=f"update_up_ano_{livro_id}_dynamic")
            
            col4, col5, col6, col7 = st.columns(4)
            up_editora = col4.text_input("5. Editora", value=current_livro.get('editora', ''), key=f"update_up_editora_{livro_id}_dynamic")
            up_isbn = col5.text_input("6. ISBN", value=current_livro.get('isbn', ''), key=f"update_up_isbn_{livro_id}_dynamic")
            opcoes_idioma = ["Português", "Inglês", "Espanhol", "Outro"]
            idioma_index = opcoes_idioma.index(current_livro.get('idioma')) if current_livro.get('idioma') in opcoes_idioma else 0
            up_idioma = col6.selectbox("7. Idioma", opcoes_idioma, index=idioma_index, key=f"update_up_idioma_{livro_id}_dynamic")
            opcoes_categoria = ["Tese", "Artigo", "Manual", "Livro Didático", "Norma"]
            categoria_index = opcoes_categoria.index(current_livro.get('categoria')) if current_livro.get('categoria') in opcoes_categoria else 0
            up_categoria = col7.selectbox("8. Categoria", opcoes_categoria, index=categoria_index, key=f"update_up_categoria_{livro_id}_dynamic")

            up_resumo = st.text_area("15. Resumo/Descrição", value=current_livro.get('resumo', ''), key=f"update_up_resumo_{livro_id}_dynamic")
            
            submitted_update = st.form_submit_button("Atualizar Livro", type="primary", key=f"submit_update_livro_button_{livro_id}")
            
            if submitted_update:
                update_data = {
                    'titulo': up_titulo,
                    'autor': up_autor,
                    'ano': up_ano,
                    'editora': up_editora,
                    'isbn': up_isbn,
                    'idioma': up_idioma,
                    'categoria': up_categoria,
                    'resumo': up_resumo
                    # Inclua todos os campos que deseja permitir a edição
                }
                try:
                    update_livro(livro_id, update_data)
                    st.success(f"Livro '{up_titulo}' atualizado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao atualizar: {e}")
    else:
        st.info("Selecione um livro para exibir o formulário de edição.")


def render_form_delete(df):
    """Renderiza o componente de deleção."""
    st.subheader("🗑️ Deletar Livro")
    
    if df.empty:
        st.info("Nenhum livro para deletar.")
        return

    livro_titles_del = df['titulo'].tolist()
    title_to_id_del = {row['titulo']: row['id'] for index, row in df.iterrows()}
    
    # Chave estável para o selectbox
    selected_title_del = st.selectbox(
        "Selecione o Livro para DELETAR:", 
        livro_titles_del, 
        key="delete_select_livro_static_key"
    )
    
    livro_id_del = title_to_id_del.get(selected_title_del)
    
    if selected_title_del and livro_id_del:
        st.warning(f"Confirme a exclusão do livro: **{selected_title_del}** (ID: {livro_id_del})")
        
        # CHAVE FINAL ÚNICA para o botão de deleção
        if st.button("🗑️ DELETAR IRREVERSIVELMENTE", type="secondary", key="delete_button_unique_biblio"):
            try:
                delete_livro(livro_id_del)
                st.success(f"Livro '{selected_title_del}' excluído com sucesso.")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao deletar: {e}")
    else:
        st.info("Selecione um livro.")


# =========================================================================
# FUNÇÃO PRINCIPAL DA PÁGINA
# =========================================================================

def biblioteca_main_page():
    
    # 1. Obter e verificar a role do usuário (usando a função do app.py)
    user_email = get_user_email_safely()
    
    if not user_email or 'user_role' not in st.session_state:
        # Redirecionamento ou mensagem de erro se a sessão não estiver estável (improvável com o app.py corrigido)
        st.error("Por favor, volte para a 'Página Inicial' e faça login para acessar o catálogo.")
        st.stop()
        
    user_role = st.session_state['user_role']
    
    update_user_activity(user_email, user_role, 'biblioteca')
        
    # 2. Título da Página 
    col1, col2, col3 = st.columns([1, 5, 1])
    col2.title("📚 Biblioteca de Referências")

    # 3. Carregamento dos Dados
    with st.spinner("Carregando acervo do banco de dados..."):
        try:
            df = fetch_all_livros() 
            # Conversão de tipos/formato para exibição
            if not df.empty:
                for col in df.columns:
                    # Garantir que ID seja string
                    if col == 'id':
                         df[col] = df[col].astype(str)
                    # Lidar com listas de Palavras-Chave, se existirem
                    if df[col].apply(lambda x: isinstance(x, list)).any():
                        df[col] = df[col].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
                # Remove colunas totalmente vazias, se for o caso
                df = df.dropna(axis=1, how="all")
            else:
                 df = pd.DataFrame(columns=['id', 'titulo', 'autor', 'ano']) # Garante colunas mínimas
        except Exception as e:
            st.error(f"Erro ao carregar o acervo do banco de dados: {e}")
            df = pd.DataFrame() 

    # 4. RENDERIZAÇÃO CONDICIONAL DO CRUD/ADMIN (NOVO: Toggle e Tabs)
    if user_role in ["admin", "editor"]:
        
        # Toggle switch para mostrar/esconder a interface de administração
        show_admin = col2.toggle(
            "🛠️ Mostrar Interface de Administração (CRUD)", 
            value=False, # Começa desligado
            key="toggle_admin_crud_unique_key"
        )
        
        if show_admin:
            
            # Usando st.tabs para organizar as operações
            tab_create, tab_edit, tab_delete = col2.tabs(
                ["➕ Criar Livro", "✏️ Editar Livro", "🗑️ Deletar Livro"]
            )

            with tab_create:
                render_form_create()

            with tab_edit:
                render_form_update(df)

            with tab_delete:
                render_form_delete(df)

            st.markdown("---") 

    # 5. Interface de Consulta (Sempre visível)
    col2.subheader("Acervo Completo")
    
    if df.empty:
        col2.info("Nenhum livro cadastrado no acervo ainda.")
    else:
        # Colunas a serem exibidas na tabela
        colunas_ordenadas = ["titulo", "autor", "ano", "editora", "categoria", 
                             "disponibilidade", "resumo", "id"] 
        colunas = [c for c in colunas_ordenadas if c in df.columns]
        df_exibicao = df[colunas]

        busca = col2.text_input("🔍 Filtrar por Título/Autor/Editora/ID:", key="search_consulta_unique_key")

        if busca:
            mask = (
                df_exibicao["titulo"].str.contains(busca, case=False, na=False) |
                df_exibicao["autor"].str.contains(busca, case=False, na=False) |
                df_exibicao["editora"].str.contains(busca, case=False, na=False) |
                df_exibicao["id"].str.contains(busca, case=False, na=False)
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
    biblioteca_main_page()
