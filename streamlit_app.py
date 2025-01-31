import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.write(df)

number = st.slider("Vyberte číslo", 0, 100, 3)
st.write(f"Vybrané číslo: {number}")