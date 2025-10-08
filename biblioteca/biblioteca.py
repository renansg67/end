import streamlit as st
from biblioteca.dicionario_de_livros import biblioteca

col1, col2, col3 = st.columns([1, 3, 1])

col2.info("Biblioteca")

col2.write(biblioteca)