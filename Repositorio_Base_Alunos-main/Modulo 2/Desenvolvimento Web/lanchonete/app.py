import streamlit as st

#-------------python -m streamlit run app.py

st.set_page_config(page_title="Carrinho de Compras", layout="centered")
st.title('🥪 LANCHONETE E CONFEITARIA')

#---------------------CARRINHO DE COMPRAS

# Lista de produtos disponíveis
produtos = {
    "DOG COMPLETO DUPLO": 14.00 ,
    "DOG SIMPLES DUPLO":  12.00,
    "PASTEL DE CARNE": 10.00,
    "PASTEL CARNE C/QUEIJO": 10.00,
}

# Inicializa o carrinho no session_state
if "carrinho" not in st.session_state:
    st.session_state.carrinho = {}

st.header("🛍️ Adicione seu produto no carrinho")
st.subheader("ESCOLHA SEUS PRODUTOS:")

# Exibir lista de produtos
for produto, preco in produtos.items():
    col1, col2 = st.columns([3,1])
    with col1:
        st.write(f"**{produto}** - R$ {preco:.2f}")
    with col2:
        if st.button(f"Adicionar {produto}", key=produto):
            if produto in st.session_state.carrinho:
                st.session_state.carrinho[produto]["quantidade"] += 1
            else:
                st.session_state.carrinho[produto] = {"preco": preco, "quantidade": 1}

st.divider()
st.subheader("🛒 Seu Carrinho")

# Exibir itens no carrinho
if st.session_state.carrinho:
    total = 0
    for produto, dados in st.session_state.carrinho.items():
        subtotal = dados["quantidade"] * dados["preco"]
        total += subtotal
        st.write(f"- {produto} | {dados['quantidade']}x | Subtotal: R$ {subtotal:.2f}")

    st.write(f"### 💰 Total: R$ {total:.2f}")

    # Escolher forma de pagamento
    st.subheader("💳 Forma de Pagamento")
    forma_pagamento = st.radio(
        "Selecione uma forma de pagamento:",
        ["Cartão de Crédito", "Pix", "Boleto Bancário"]
    )

    if forma_pagamento == "Cartão de Crédito":
        num_cartao = st.text_input("Número do Cartão")
        validade = st.text_input("Validade (MM/AA)")
        cvv = st.text_input("CVV", type="password")

    elif forma_pagamento == "Pix":
        st.info("Use a chave PIX: **lanchonete@confeitaria.com**")

    elif forma_pagamento == "Boleto Bancário":
        st.info("O boleto será gerado após a finalização da compra.")

    # Botão finalizar compra
    if st.button("✅ Finalizar Compra"):
        st.success(f"Compra finalizada com sucesso! Pagamento via {forma_pagamento}.")
        st.session_state.carrinho = {}

    if st.button("🧹 Limpar Carrinho"):
        st.session_state.carrinho = {}

else:
    st.info("Seu carrinho está vazio. Adicione itens acima!")


for produto, dados in st.session_state.carrinho.items():
    col1, col2, col3, col4 = st.columns([4,1,1,2])
    subtotal = dados["quantidade"] * dados["preco"]

    with col1:
        st.write(f"**{produto}** - R$ {dados['preco']:.2f}")
    with col2:
        if st.button("➕", key=f"mais_{produto}"):
            st.session_state.carrinho[produto]["quantidade"] += 1
    with col3:
        if st.button("➖", key=f"menos_{produto}"):
            st.session_state.carrinho[produto]["quantidade"] -= 1
            if st.session_state.carrinho[produto]["quantidade"] <= 0:
                del st.session_state.carrinho[produto]
                st.experimental_rerun()
    with col4:
        st.write(f"{dados['quantidade']}x | Subtotal: R$ {subtotal:.2f}")    

