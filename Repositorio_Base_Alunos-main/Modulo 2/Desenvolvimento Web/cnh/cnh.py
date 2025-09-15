import streamlit as st

st.set_page_config(page_title="Verificador de Habilitação", layout="centered")

st.title("🚗 Verificador de quem pode dirigir")

# Entrada de dados
idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1)
tem_cnh = st.radio("Você possui CNH?", ["Sim", "Não"])

# Botão para verificar
if st.button("Verificar"):
    if idade >= 18 and tem_cnh == "Sim":
        st.success("✅ Você pode dirigir!")
    elif idade >= 18 and tem_cnh == "Não":
        st.warning("⚠️ Você tem idade, mas precisa tirar a CNH.")
    else:
        st.error("❌ Você ainda não pode dirigir.")