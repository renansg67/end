import streamlit as st

def emprestimos():
    col1, col2, col3 = st.columns([1, 3, 1])

    col2.title("Formulário")
    col2.page_link("https://forms.gle/SdSBbfCuKk4C2yQC7", label="Formulário para Empréstimos", icon="🌎")

if __name__ == "__main__":
    emprestimos()