import streamlit as st
import pandas as pd
# python -m streamlit run app.py

# ------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('JENIFFER FELIX MOTORS')


carros = ['BMW','Mustang', 'Porsche', 'corvette', 'bugatti','honda civic G10','honda civic type R']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)



# ----------------------------------------------- Principal 
st.title('Sua jornada merece adrenalina- Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias oª {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')


if opcao == 'BMW':
    diaria = 1000

elif opcao == 'Mustang':
    diaria = 2000

elif opcao == 'Porsche':
    diaria = 1800

elif opcao == 'corvette':
    diaria = 2500

elif opcao == 'bugatti':
    diaria = 4000

elif opcao == 'honda civic G10':
    diaria = 670

elif opcao == 'honda civic type R':
    diaria = 900 




if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')
