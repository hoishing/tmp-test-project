import streamlit as st
from natal import Data

st.write("Natal")


data = Data("shing", "Hong Kong", "2024-12-21 12:00")
st.write(data)
