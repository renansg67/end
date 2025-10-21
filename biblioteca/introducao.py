import streamlit as st
import time

CARL_SAGAN_VIDEO_URL = "https://www.youtube.com/embed/Uc1O_TrXKQU?cc_load_policy=1&cc_lang_pref=pt" # Substitua pelo URL do vídeo real
INTRO_QUOTE = "> \"O livro é a prova de que os humanos são capazes de fazer magia.\" — Carl Sagan"
INTRO_TEXT = """
Embarque conosco em uma jornada através das páginas.
Assim como uma estrela guia ilumina o caminho em um universo vasto, cada título aqui é um farol de conhecimento e descoberta. 
Reserve um momento para inspirar-se, e então siga adiante para o Catálogo. **Explore os mundos, absorva as ideias e não se contente com menos do que a vastidão do saber.**
"""

def display_themed_intro():
    """Exibe o cabeçalho temático e o vídeo."""
    col1, col2, col3, col4 = st.columns([1, 2.5, 2.5, 1])
    # Saudação personalizada
    
    col2.markdown(f"## 🔭 Seja Bem-vindo(a) à Biblioteca, {st.user.given_name}! ✨")
    
    col3.video(CARL_SAGAN_VIDEO_URL)

    col3.markdown(INTRO_QUOTE)
    col2.markdown(INTRO_TEXT)
    
    col1, col2, col3 = st.columns([1, 5, 1])
    col2.markdown("---")


# --- Lógica Principal da Página ---

def run_bem_vindo_page():
    """Função que executa a página de Boas-Vindas."""
    
    # 2. Rede de Segurança (Verificação de Autenticação)
    # A verificação deve garantir que o email e a role (que é definida após o login) existam.

    if 'user_role' not in st.session_state:
        st.error("🔒 Acesso negado. Por favor, volte para a Página Principal e faça login para continuar.")
        st.stop()
    
    # 3. Exibição da Introdução Temática
    display_themed_intro()
    
    # 4. Botão de Redirecionamento
    col1, col2, col3 = st.columns([1, 5, 1]) 
    # O botão faz o switch para o arquivo da próxima página.
    if col2.button("🚀 Iniciar a Jornada: Ver o Catálogo Completo", use_container_width=True, type="primary"):
        st.toast("Preparando o lançamento...", icon="🌌")
        time.sleep(0.5) # Dá tempo para a toast aparecer antes do switch
        
        # O Streamlit procura o arquivo '2_Catálogo.py' na pasta 'pages'
        st.switch_page("./biblioteca/biblioteca.py") 

# Execução da página
if __name__ == '__main__':
    run_bem_vindo_page()