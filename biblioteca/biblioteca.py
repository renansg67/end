# biblioteca/biblioteca.py

import streamlit as st
import pandas as pd
from datetime import datetime

# 🚨 ALTERAÇÃO CRUCIAL 1: Importar as funções do DB 🚨
# Assumindo que database.py está no diretório raiz e acessível
from database import (
    fetch_all_items, 
    add_item, 
    update_item, 
    delete_item, 
)

from app import (
    get_user_email_safely, 
    get_user_role
)

def fetch_all_livros():
    return fetch_all_items("livros")

def add_livro(data):
    return add_item("livros", data)

def update_livro(livro_id, data):
    # O frontend envia a PK como 'id'
    return update_item("livros", livro_id, data) 

def delete_livro(livro_id):
    return delete_item("livros", livro_id)

# =========================================================================
# FUNÇÃO DE ADMIN/CRUD (Encapsula a lógica de formulários)
# =========================================================================

# biblioteca/biblioteca.py (Trecho da função show_admin_interface_livros)


def show_admin_interface_livros(df_livros, user_role):
    """Renderiza os formulários de CRUD para livros, cobrindo todos os 18 campos."""
    col1, col2, col3 = st.columns([1, 5, 1])    
    col2.header("🛠️ Administração de Livros (CRUD)")
    st.markdown("---") 
    
    tab_create, tab_update, tab_delete = col2.tabs(["➕ Criar Livro", "✏️ Editar Livro", "🗑️ Deletar Livro"])

    # --- TAB CRIAR: TODOS OS 18 CAMPOS ---
    with tab_create:
        st.subheader("Cadastrar Novo Livro")
        
        # O formulário é extenso, vamos usar 3 colunas para otimizar o espaço horizontal
        with st.form("form_create_livro", clear_on_submit=True):
            
            # 1. Campos principais (Linha 1)
            col1, col2, col3 = st.columns(3)
            new_id = col1.text_input("1. ID Único (Chave Primária)", key="create_new_id_key")
            new_titulo = col2.text_input("2. Título", key="create_new_titulo_key")
            new_autor = col3.text_input("3. Autor(es)", key="create_new_autor_key")
            
            # 2. Especificações do Material (Linha 2)
            col4, col5, col6, col7 = st.columns(4)
            new_ano = col4.number_input("4. Ano de Publicação", min_value=1000, max_value=datetime.now().year, value=datetime.now().year, key="create_new_ano_key")
            new_editora = col5.text_input("5. Editora", key="create_new_editora_key")
            new_isbn = col6.text_input("6. ISBN", help="Identificação Padrão Internacional do Livro", key="create_new_isbn_key")
            new_idioma = col7.selectbox("7. Idioma", ["Português", "Inglês", "Espanhol", "Outro"], key="create_new_idioma_key")

            # 3. Classificação (Linha 3)
            col8, col9, col10 = st.columns(3)
            new_categoria = col8.selectbox("8. Categoria", ["Tese", "Artigo", "Manual", "Livro Didático", "Norma"], key="create_new_categoria_key")
            new_subcategoria = col9.text_input("9. Subcategoria (Opcional)", key="create_new_subcategoria_key")
            new_tipo_de_material = col10.selectbox("10. Tipo de Material", ["Livro Físico", "E-book", "Periódico", "Relatório"], key="create_new_tipo_de_material_key")
            
            # 4. Palavras-Chave e Nível
            new_palavras_chave_str = st.text_input("11. Palavras-Chave (Separadas por vírgula)", help="Ex: concreto, ensaios, materiais compósitos", key="create_new_palavras_chave_key")
            new_nivel = st.selectbox("12. Nível", ["Graduação", "Pós-Graduação", "Pesquisa", "Técnico"], key="create_new_nivel_key")
            
            # 5. Localização e Disponibilidade (Linha 4)
            col11, col12 = st.columns(2)
            new_localizacao_fisica = col11.text_input("13. Localização Física (Prateleira/Sala)", key="create_new_localizacao_fisica_key")
            new_disponibilidade = col12.selectbox("14. Disponibilidade", ["Disponível", "Emprestado", "Em Manutenção", "Perdido"], key="create_new_disponibilidade_key")

            # 6. Links e Resumo (Linha 5)
            new_resumo = st.text_area("15. Resumo/Descrição", key="create_new_resumo_key")
            col13, col14 = st.columns(2)
            new_imagem_capa_url = col13.text_input("16. URL Imagem da Capa (Opcional)", key="create_new_imagem_capa_url_key")
            new_link_externo = col14.text_input("17. Link Externo (E-book/PDF/Compra)", key="create_new_link_externo_key")
            
            # 18. Data de Entrada (Campo interno, mas útil)
            new_data_de_entrada = str(datetime.now().date())
            st.markdown(f"**18. Data de Entrada no Sistema:** _{new_data_de_entrada}_")
            
            # Submissão
            submitted = st.form_submit_button("Cadastrar Livro", type="primary")
            
            if submitted:
                # 1. Reunir todos os 18 dados
                new_data = {
                    'id': new_id, 
                    'titulo': new_titulo, 
                    'autor': new_autor, 
                    'ano': new_ano,
                    'editora': new_editora,
                    'isbn': new_isbn,
                    'idioma': new_idioma,
                    'categoria': new_categoria,
                    'subcategoria': new_subcategoria,
                    'tipo_de_material': new_tipo_de_material,
                    'palavras_chave': new_palavras_chave_str, # Enviado como string
                    'nivel': new_nivel,
                    'localizacao_fisica': new_localizacao_fisica,
                    'disponibilidade': new_disponibilidade,
                    'resumo': new_resumo,
                    'imagem_capa_url': new_imagem_capa_url,
                    'link_externo': new_link_externo,
                    'data_de_entrada': new_data_de_entrada
                }

                try:
                    # Chama a função que insere no DB
                    add_livro(new_data)
                    st.success(f"Livro '{new_titulo}' cadastrado com sucesso!")
                    st.rerun()
                except Exception as e:
                    # O erro de chave primária duplicada (IntegrityError) será pego aqui.
                    st.error(f"Erro ao cadastrar: {e}")

    # --- TAB EDITAR: TODOS OS 18 CAMPOS ---
     # --- TAB EDITAR: TODOS OS 18 CAMPOS (REVISADO PARA RESPONSIVIDADE) ---
    if 'selected_livro_id' not in st.session_state:
        st.session_state['selected_livro_id'] = None

    # --- TAB EDITAR: TODOS OS 18 CAMPOS (REVISADO COM CHAVES DINÂMICAS) ---
    with tab_update:
        if df_livros.empty:
            st.info("Nenhum livro para editar.")
            return 
            
        # 1. Seleção do Livro para Edição
        livro_titles = df_livros['titulo'].tolist()
        title_to_id = {row['titulo']: row['id'] for index, row in df_livros.iterrows()}
        
        # Lógica para determinar o item inicial no selectbox (mantém a seleção após o rerun)
        initial_title = None
        if st.session_state['selected_livro_id'] is not None:
            id_to_title = {v: k for k, v in title_to_id.items()}
            initial_title = id_to_title.get(st.session_state['selected_livro_id'])

        if initial_title is None and livro_titles:
             initial_title = livro_titles[0]
        
        initial_index = livro_titles.index(initial_title) if initial_title in livro_titles else 0


        selected_title = st.selectbox(
            "Selecione o Livro para Edição:", 
            livro_titles, 
            index=initial_index,
            key="update_select_livro_key" 
        )
        
        # 2. Atualizar o estado de sessão e obter o ID
        if selected_title:
            livro_id = title_to_id.get(selected_title)
            # Armazenar o ID no estado (necessário para a lógica de chaves dinâmicas)
            st.session_state['selected_livro_id'] = livro_id
        else:
            livro_id = None

        # 3. Renderização do Formulário de Edição
        if livro_id:
            # Encontra o registro atual
            current_livro = df_livros[df_livros['id'] == livro_id].iloc[0].to_dict()

            # O ID é exibido, mas não pode ser alterado
            st.info(f"Editando livro com ID (não editável): **{livro_id}**")
            
            with st.form("form_update_livro"):
                
                # Campos de entrada
                col1, col2, col3 = st.columns(3)
                # CHAVES DINÂMICAS: f"update_up_titulo_{livro_id}"
                up_titulo = col1.text_input("2. Título", value=current_livro.get('titulo', ''), key=f"update_up_titulo_{livro_id}")
                up_autor = col2.text_input("3. Autor(es)", value=current_livro.get('autor', ''), key=f"update_up_autor_{livro_id}")
                up_ano = col3.number_input("4. Ano de Publicação", min_value=1000, max_value=datetime.now().year, value=current_livro.get('ano'), key=f"update_up_ano_{livro_id}")
                
                # Campos de seleção
                col4, col5, col6, col7 = st.columns(4)
                up_editora = col4.text_input("5. Editora", value=current_livro.get('editora', ''), key=f"update_up_editora_{livro_id}")
                up_isbn = col5.text_input("6. ISBN", value=current_livro.get('isbn', ''), key=f"update_up_isbn_{livro_id}")
                
                opcoes_idioma = ["Português", "Inglês", "Espanhol", "Outro"]
                up_idioma = col6.selectbox("7. Idioma", opcoes_idioma, index=opcoes_idioma.index(current_livro.get('idioma', 'Português')), key=f"update_up_idioma_{livro_id}")
                
                opcoes_material = ["Livro Físico", "E-book", "Periódico", "Relatório"]
                up_tipo_de_material = col7.selectbox("10. Tipo de Material", opcoes_material, index=opcoes_material.index(current_livro.get('tipo_de_material', 'Livro Físico')), key=f"update_up_tipo_de_material_{livro_id}")
                
                # Classificação
                col8, col9 = st.columns(2)
                opcoes_categoria = ["Tese", "Artigo", "Manual", "Livro Didático", "Norma"]
                up_categoria = col8.selectbox("8. Categoria", opcoes_categoria, index=opcoes_categoria.index(current_livro.get('categoria', 'Tese')), key=f"update_up_categoria_{livro_id}")
                up_subcategoria = col9.text_input("9. Subcategoria (Opcional)", value=current_livro.get('subcategoria', ''), key=f"update_up_subcategoria_{livro_id}")

                # Palavras-Chave e Nível
                up_palavras_chave_str = st.text_input("11. Palavras-Chave (Separadas por vírgula)", value=current_livro.get('palavras_chave', ''), key=f"update_up_palavras_chave_{livro_id}")
                
                opcoes_nivel = ["Graduação", "Pós-Graduação", "Pesquisa", "Técnico"]
                up_nivel = st.selectbox("12. Nível", opcoes_nivel, index=opcoes_nivel.index(current_livro.get('nivel', 'Graduação')), key=f"update_up_nivel_{livro_id}")
                
                # Localização e Disponibilidade 
                col10, col11 = st.columns(2)
                up_localizacao_fisica = col10.text_input("13. Localização Física (Prateleira/Sala)", value=current_livro.get('localizacao_fisica', ''), key=f"update_up_localizacao_fisica_{livro_id}")
                
                opcoes_disp = ["Disponível", "Emprestado", "Em Manutenção", "Perdido"]
                up_disponibilidade = col11.selectbox("14. Disponibilidade", opcoes_disp, index=opcoes_disp.index(current_livro.get('disponibilidade', 'Disponível')), key=f"update_up_disponibilidade_{livro_id}")

                # Links e Resumo 
                up_resumo = st.text_area("15. Resumo/Descrição", value=current_livro.get('resumo', ''), key=f"update_up_resumo_{livro_id}")
                col12, col13 = st.columns(2)
                up_imagem_capa_url = col12.text_input("16. URL Imagem da Capa (Opcional)", value=current_livro.get('imagem_capa_url', ''), key=f"update_up_imagem_capa_url_{livro_id}")
                up_link_externo = col13.text_input("17. Link Externo (E-book/PDF/Compra)", value=current_livro.get('link_externo', ''), key=f"update_up_link_externo_{livro_id}")
                
                # Data de Entrada (Não editável)
                st.markdown(f"**18. Data de Entrada no Sistema:** _{current_livro.get('data_de_entrada', 'N/A')}_")

                submitted_update = st.form_submit_button("Atualizar Livro", type="primary")
                
                if submitted_update:
                    # Lógica de atualização (Manter os nomes das variáveis criadas acima: up_titulo, up_autor, etc.)
                    update_data = {
                        'titulo': up_titulo, 
                        'autor': up_autor, 
                        'ano': up_ano,
                        'editora': up_editora,
                        'isbn': up_isbn,
                        'idioma': up_idioma,
                        'categoria': up_categoria,
                        'subcategoria': up_subcategoria,
                        'tipo_de_material': up_tipo_de_material,
                        'palavras_chave': up_palavras_chave_str,
                        'nivel': up_nivel,
                        'localizacao_fisica': up_localizacao_fisica,
                        'disponibilidade': up_disponibilidade,
                        'resumo': up_resumo,
                        'imagem_capa_url': up_imagem_capa_url,
                        'link_externo': up_link_externo
                    }
                    try:
                        update_livro(livro_id, update_data)
                        st.success(f"Livro '{up_titulo}' atualizado com sucesso!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao atualizar: {e}")
        else:
            st.info("Selecione um livro para exibir o formulário de edição.")

    # --- TAB DELETAR: (Mantida simples, focada apenas na exclusão) ---
    with tab_delete:
        if df_livros.empty:
            st.info("Nenhum livro para deletar.")
            return

        livro_titles_del = df_livros['titulo'].tolist()
        selected_title_del = st.selectbox("Selecione o Livro para DELETAR:", livro_titles_del, key="delete_select_livro_key")
        
        if selected_title_del:
            current_livro_del = df_livros[df_livros['titulo'] == selected_title_del].iloc[0]
            livro_id_del = current_livro_del['id']
            
            st.warning(f"Confirme a exclusão do livro: **{selected_title_del}** (ID: {livro_id_del})")
            
            if st.button("🗑️ DELETAR IRREVERSIVELMENTE", type="secondary", key="delete_button_final"):
                try:
                    delete_livro(livro_id_del)
                    st.success(f"Livro '{selected_title_del}' excluído com sucesso.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao deletar: {e}")

# =========================================================================
# CORPO PRINCIPAL DA PÁGINA
# =========================================================================

# 1. 🚨 Obter e verificar a role do usuário 🚨
user_email = get_user_email_safely()
user_role = get_user_role(user_email) if user_email else None

# Se esta página é uma página do menu, assumimos que o app.py já verificou o login,
# mas uma checagem de segurança básica é sempre recomendada.
if not user_email:
    st.error("Por favor, faça login para acessar o catálogo.")
    # st.stop() # Pode ser necessário se você quiser interromper o carregamento.

col1, col2, col3 = st.columns([1, 5, 1])
col2.title("📚 Biblioteca de Referências")

# 2. 🚨 Mudar a fonte de dados para o DB 🚨
try:
    df = fetch_all_livros() # Puxa dados do SQLite
    
    # Processamento para converter colunas-lista (se houver, como palavras_chave) para string
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df[col] = df[col].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)

    # Remove colunas completamente vazias
    df = df.dropna(axis=1, how="all")

except Exception as e:
    col2.info(f"Erro ao carregar o acervo do banco de dados: {e}")
    df = pd.DataFrame() # DataFrame vazio em caso de erro


# 3. 🚨 RENDERIZAÇÃO CONDICIONAL DO CRUD 🚨
if user_role in ["admin", "editor"]:
    col1, col2, col3, col4 = st.columns([1, 4, 1, 1])
    off = col3.toggle("Habilitar edição", value=False)
    if off:
        show_admin_interface_livros(df, user_role)
        st.markdown("---") # Separador visual entre Admin e Consulta

col1, col2, col3 = st.columns([1, 5, 1])

# 4. Interface de Consulta (Abaixo, visível a todos os logados)
if df.empty:
    col2.info("Nenhum livro cadastrado no acervo ainda.")
else:
    # Restante da sua lógica de consulta (Filtros e exibição do DataFrame)
    
    # ... (Seu código de ordenação de colunas) ...
    colunas_ordenadas = ["titulo", "autor", "ano", "editora", "categoria", 
                         # ... (o resto das colunas) ...
                         "link_externo"]
    colunas = [c for c in colunas_ordenadas if c in df.columns]
    df_exibicao = df[colunas]

    busca = col2.text_input("🔍 Buscar por título ou autor:", key="search_consulta")

    if busca:
        mask = (
            df_exibicao["titulo"].str.contains(busca, case=False, na=False) |
            df_exibicao["autor"].str.contains(busca, case=False, na=False) |
            df_exibicao["editora"].str.contains(busca, case=False, na=False)
        )
        df_filtrado = df_exibicao[mask]
    else:
        df_filtrado = df_exibicao

    col2.dataframe(
        df_filtrado,
        hide_index=True,
        width="stretch"
    )