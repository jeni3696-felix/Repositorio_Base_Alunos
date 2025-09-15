import streamlit as st

# Dados de exemplo
generos = ["GOSPEL", "POP INTERNACIONAL", "TRAP", "DISNEY"]

# Dicionário relacionando gêneros aos seus livros
musica_por_genero = {
    "GOSPEL": ["QUEM È ESSE", "EM MEIO AO VENDAVAL", "TOCA-ME"],
    "POP INTERNACIONAL": [ "Die With A Smile","Treat you Better","WHEN|WAS YOUR MAN"],
    "TRAP": ["SUPERMAN", "SMACK THAT", "BUTTERFLY EFFECT"],
    "DISNEY": ["VEJO EM FIM A LUZ BRILHAR", "UM MUNDO IDEAL", "VEJO UMA PORTA ABRIR"]
}

# Selectbox para escolher o gênero 

st.sidebar.image('logo.png')

genero_selecionado = st.sidebar.selectbox("Selecione o gênero musical:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionada= st.sidebar.selectbox(
        "Selecione o livro:", 
        musica_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionada:
    st.write(f"**MUSICA SELECIONADA:** {musica_selecionada}")
    st.write(f"**gênero:** {genero_selecionado}")
    # st.image(f"{musica_selecionada}.png")



if genero_selecionado == "GOSPEL" and musica_selecionada == "QUEM È ESSE" :
    st.video('https://www.youtube.com/watch?v=0ZF5em0MTwY&list=RD0ZF5em0MTwY&start_radio=1')
    st.link_button(url='https://open.spotify.com/intl-pt/artist/0d71FlLkqZzdpEQifcngQq', label="Spotify", icon="🔊")   #st.link_button = link dentro do butao |  label= coloca o nome dentro do butao |  icon= coloca um simbulo dentro do butao

elif genero_selecionado == "GOSPEL" and musica_selecionada == "EM MEIO AO VENDAVAL" :
    st.video("https://www.youtube.com/watch?v=peitGcdyukA")
    st.link_button(url='https://open.spotify.com/intl-pt/album/3iALD5FS2raKNCjouli13t', label="Spotify", icon="🔊")  

elif genero_selecionado == "GOSPEL" and musica_selecionada == "TOCA-ME" :
    st.video("https://www.youtube.com/watch?v=Ul4dgaXy4Ps&list=RDUl4dgaXy4Ps&start_radio=1")
    st.link_button(url='https://open.spotify.com/intl-pt/artist/0mY88nlaku0dS8oNbON0uB', label="Spotify", icon="🔊") 

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "Die With A Smile" :
    st.video("https://www.youtube.com/watch?v=kPa7bsKwL-c&list=RDkPa7bsKwL-c&start_radio=1")
    st.link_button(url='https://open.spotify.com/intl-pt/track/2plbrEY59IikOBgBGLjaoe?si=dd5a97516d444a65', label="Spotify", icon="🔊") 

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "Treat you Better" :
    st.video("https://www.youtube.com/watch?v=lY2yjAdbvdQ&list=RDlY2yjAdbvdQ&start_radio=1")
    st.link_button(url='https://open.spotify.com/intl-pt/track/3QGsuHI8jO1Rx4JWLUh9jd?si=10d846d92e6d41f4', label="Spotify", icon="🔊")

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "WHEN|WAS YOUR MAN" :
    st.video("https://www.youtube.com/watch?v=ekzHIouo8Q4&list=RDekzHIouo8Q4&start_radio=1")
    st.link_button(url='https://open.spotify.com/intl-pt/track/0nJW01T7XtvILxQgC5J7Wh?si=ed8bb322608742c2', label="Spotify", icon="🔊")

elif genero_selecionado == "TRAP" and musica_selecionada == "SUPERMAN" :
    st.video("http://youtube.com/watch?v=lPlePBCS6Ic&list=RDlPlePBCS6Ic&start_radio=1")
    st.link_button(url='https://open.spotify.com/intl-pt/artist/7dGJo4pcD2V6oG8kP0tJRR?si=271ee7445b8840f7', label="Spotify", icon="🔊")


elif genero_selecionado == "TRAP" and musica_selecionada == "BUTTERFLY EFFECT" :
    st.video("https://www.youtube.com/watch?v=_EyZUTDAH0U&list=RD_EyZUTDAH0U&start_radio=1")
    st.link_button(url='https://open.spotify.com/search/%22BUTTERFLY%20EFFECT%22', label="Spotify", icon="🔊")

elif genero_selecionado == "TRAP" and musica_selecionada == "SMACK THAT" :
    st.video("https://www.youtube.com/watch?v=bKDdT_nyP54&list=RDbKDdT_nyP54&start_radio=1")
    st.link_button(url='https://open.spotify.com/intl-pt/artist/0z4gvV4rjIZ9wHck67ucSV', label="Spotify", icon="🔊")   



