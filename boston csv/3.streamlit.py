import streamlit as st

st.title("User input")

mesaj = st.chat_input("Insereaza o valoare")

if not st.session_state.get("messages"):
    st.session_state["messages"] = []

print("session state:", st.session_state)


print(mesaj)
if mesaj:
    print("Mesaj nou venit")
    st.session_state["messages"].append(mesaj)
    print("session state:", st.session_state)

for mesaj in st.session_state['messages']:
    with st.chat_message("human") as msg:
        st.write(mesaj)

with st.chat_message("user") as msg:
    st.write(mesaj)

with st.chat_message("assistant") as msg:
    st.write("da da da")