import streamlit as st
import pandas as pd

st.title("Bine ati venit la cursul streamlit")

st.text("Acesta este un text descriptiv")

st.image("7 mare.png")

df = pd.read_csv("boston.csv", index_col=0)

st.dataframe(df)