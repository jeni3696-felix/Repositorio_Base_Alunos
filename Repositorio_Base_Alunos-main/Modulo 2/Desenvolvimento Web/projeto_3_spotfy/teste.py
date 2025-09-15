import streamlit as st

# Dados de exemplo
generos = ["GOSPEL", "POP INTERNACIONAL", "TRAP", "DISNEY"]

# Dicionário relacionando gêneros das suas musicas
musica_por_genero = {
    "GOSPEL": ["QUEM È ESSE", "EM MEIO AO VENDAVAL", "TOCA-ME"],
    "POP INTERNACIONAL": [ "Die With A Smile","Treat you Better","WHEN|WAS YOUR MAN"],
    "TRAP": ["SUPERMAN", "SMACK THAT", "BUTTERFLY EFFECT"],
    "DISNEY": ["VEJO EM FIM A LUZ BRILHAR", "UM MUNDO IDEAL", "VEJO UMA PORTA ABRIR"]
}

# Selectbox para escolher o gênero                
st.sidebar.image("logo.png")
genero_selecionado = st.sidebar.selectbox("Selecione o gênero musical:", generos)

# Selectbox para escolher a musica (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionada= st.sidebar.selectbox(
        "Selecione o livro:", 
        musica_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionada:
    st.write(f"**MUSICA SELECIONADA:** {musica_selecionada}")
    st.write(f"**gênero:** {genero_selecionado}")
    st.image(f"{musica_selecionada}.png")
    st.video()