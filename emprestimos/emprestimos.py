import streamlit as st
from database import (
    get_user_email_safely,
    update_user_activity
)


def emprestimos():
    user_email = get_user_email_safely()
    user_role = st.session_state['user_role']

    update_user_activity(user_email, user_role, 'empréstimos')
    col1, col2, col3 = st.columns([1, 3, 1])

    col2.title("Formulário")
    col2.page_link("https://forms.gle/SdSBbfCuKk4C2yQC7", label="Formulário para Empréstimos", icon="🌎")

if __name__ == "__main__":
    emprestimos()