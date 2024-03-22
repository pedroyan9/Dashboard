import streamlit as st
import pandas as pd
import numpy as np



data = pd.read_csv("dadosvenda.csv", delimiter=",")


st.bar_chart(data)
st.bokeh_chart(p, use_container_width=True)