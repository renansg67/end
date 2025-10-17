import streamlit as st

from database import (
    get_user_email_safely,
    update_user_activity
)

def apresentacao_page():
    user_email = get_user_email_safely()
    user_role = st.session_state['user_role']

    update_user_activity(user_email, user_role, 'apresentação')
    
    col1, col2, col3 = st.columns([1, 3, 1])

    col2.markdown("# 🔬 LabEND | Portal de Ensaios Não Destrutivos")
    col2.markdown("## Onde a ciência encontra a segurança das estruturas")

    col2.markdown("---")

    col2.header(f":rainbow[Olá,] :blue[{st.user.name.split(" ")[0]}]")

    with col1.expander("Ultrassom para inspeção de árvores", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Abstract_pattern_on_a_tree_stump.jpg/330px-Abstract_pattern_on_a_tree_stump.jpg")
        if st.button("Saiba mais", key="us"):
            st.switch_page("./conteudo/4_inspecao_de_arvores.py")

    with col1.expander("Carbonatação como ensaio complementar a outros ENDs", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Betonkorrosion_unter_Autobahnbruecke_%2802%29.JPG/330px-Betonkorrosion_unter_Autobahnbruecke_%2802%29.JPG")
        if st.button("Saiba mais", key="carbonatacao"):
            st.switch_page("./conteudo/3_inspecao_de_estruturas_de_concreto_e_madeira.py")

    with col1.expander("Termografia para inspeção de fachadas", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Infrared_thermal_imaging_during_a_yacht_survey.jpg/500px-Infrared_thermal_imaging_during_a_yacht_survey.jpg")
        if st.button("Saiba mais", key="termografia"):
            st.switch_page("./conteudos/3_inspecao_de_estruturas_de_concreto_e_madeira.py")

    with col3.expander("Ensaio de flexão estática conforme ABNT NBR 7190", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Stacked_Timber_Displaying_Growth_Rings.jpg/330px-Stacked_Timber_Displaying_Growth_Rings.jpg")
        if st.button("Saiba mais", key="flexao_estatica"):
            #st.switch_page("./conteudo/2_classificacao_madeira_estrutural.py")
            st.switch_page("./conteudo/2_classificacao_madeira_estrutural.py")

    with col3.expander("Livros e materiais para consulta", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Christen_Dalsgaard_-_In_a_pine_wood._Study_-_Google_Art_Project.jpg/500px-Christen_Dalsgaard_-_In_a_pine_wood._Study_-_Google_Art_Project.jpg")
        if st.button("Saiba mais", key="intro"):
            st.switch_page("./biblioteca/introducao.py")
            

if __name__ == "__main__":
    apresentacao_page()