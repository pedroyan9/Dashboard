import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Alinhe o título no centro e defina a cor vermelha
st.markdown("<h1 style='text-align: center; color: red;'>Titulos Copa Do Brasil</h1>", unsafe_allow_html=True)

#st.sidebar.title('Titulo Copa Do Brasil')
#st.sidebar.write('ano')

# Carregue os dados do CSV (substitua pelo seu caminho)
df = pd.read_csv('hall.csv')

# Variável para controlar a exibição do gráfico
show_campeao = st.button("Campeão")
show_vice = st.button("Vice")

# Exiba o gráfico com base na seleção
if show_campeao:
    st.dataframe(df['Campeão'])
elif show_vice:
    st.dataframe(df['Vice'])

# Carregue os dados do CSV (substitua pelo seu caminho)
df = pd.read_csv('hall.csv')

# Create a variable for your "Vice" data
vice_data = df['Vice']


# Crie um gráfico de barras com pontos
fig = px.bar(df, x='Campeão')

# Adicione os pontos sobre as barras
fig.update_traces(marker=dict(size=10, color='red'), selector=dict(mode='markers'))

# Crie um layout para o dashboard
fig.update_layout(
    xaxis_title='Campeão',
    yaxis_title='titulos',
    font=dict(size=14),
    showlegend=False
)

# Mostre o dashboard
st.plotly_chart(fig)

# Adicione uma cor de fundo à página
st.markdown(
    """
    <style>
        body {
            background-color: #00008B; /* Substitua pela cor desejada */
        }
    </style>
    """,
    unsafe_allow_html=True
)

