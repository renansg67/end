import streamlit as st

pages = {
    "Início": [
        st.Page("./inicio/apresentacao.py", title="Landing Page", icon="✈️")
    ],
    "Conteúdo": [
        st.Page("./conteudo/1_materiais_nao_metalicos.py", title="Materiais de Construção não Metálicos", icon="🧱"),
        st.Page("./conteudo/2_classificacao_madeira_estrutural.py", title="Classificação de Madeira Estrutural", icon="🧪"),
        st.Page("./conteudo/3_inspecao_concreto.py", title="Inspeção de Concreto", icon="🌳"),
        st.Page("./conteudo/4_inspecao_de_arvores.py", title="Inspeção de Árvores", icon="📊"),
        st.Page("./conteudo/5_matriz_de_rigidez.py", title="Matriz de Rigidez", icon="📚"),
        st.Page("./conteudo/6_propagacao_de_ondas_acusticas.py", title="Propagação de Ondas Acústicas", icon="🔊"),
        st.Page("./conteudo/7_atenuacao_de_ondas_acusticas.py", title="Atenuação de Ondas Acústicas", icon="🔊")
    ],
    "Empréstimos": [
        st.Page("./emprestimos/emprestimos.py", title="Formulário", icon="ℹ️")
    ],
    "Equipamentos": [
        st.Page("./equipamentos/equipamentos.py", title="Equipamentos", icon="🛠")
    ],
    "Biblioteca": [
        st.Page("./biblioteca/biblioteca.py", title="Biblioteca", icon="📚")
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
