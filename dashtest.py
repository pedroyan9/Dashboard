import streamlit as st
import pandas as pd
import numpy as np

# carrega o arquivo CSV

tabela = pd.read_csv('tabela.csv', delimiter=',')

st.subheader('tabela')

# Selecionando apenas as colunas 'Estados' e 'títulos'
tabela_simplificada = tabela[['Estado', 'Titulos']]

# Exibindo a tabela simplificada
st.write(tabela_simplificada)
