import streamlit as st  

st.title("Ce mai poate face streamlit")
valoarea_inserata = st.number_input("Alege o valoare", 0, 10)
st.write(f"Valoarea inserata este {valoarea_inserata}")

st.sidebar.text("Aici va fi sidebar-ul")

valoarea_inserata_sidebar = st.sidebar.number_input("Alege o alta valoare", 0, 2)

print(valoarea_inserata, valoarea_inserata_sidebar)