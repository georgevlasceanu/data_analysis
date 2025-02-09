import streamlit as st
import pickle


st.title("Supravietuiai pe Titanic?")

QUESTIONS = [
    "In primul rand, trebuie sa imi spui ce varsta ai...", 
    "Spune-mi cu cate persoane de tip sot/sotie/sora/frate ai fi mers?",
    "Alege de unde ai fi plecat 1-Southhampton / 2-Queenstown"
]



if not st.session_state.get("messages"):
    st.session_state["messages"] = []
if not st.session_state.get("Q_index"):
    st.session_state["Q_index"] = 0

mesaj = st.chat_input("Raspunde")

with st.chat_message("ai") as msg:
    st.write(QUESTIONS[st.session_state.get("Q_index", 0)])


if mesaj:
    st.session_state["messages"].append((mesaj, "user"))
    if st.session_state.get("Q_index", 0) + 1 < len(QUESTIONS):
        st.session_state["Q_index"] += 1
        st.session_state["messages"].append((QUESTIONS[st.session_state.get("Q_index", 0)], "ai"))
    else:
        with open("model.pkl", "rb") as f_read:
            model = pickle.load(f_read)
            mesaje = st.session_state["messages"]
            mesaje_user = [m[0] for m in mesaje if m[1] == "user"]
            varsta, nr_frati, portul = mesaje_user
            print(varsta, nr_frati, portul)
            result = model.predict([[3,	int(varsta),	int(nr_frati),	0,	7.2500,	True,	7,	int(portul)]])[0]
            result = bool(result)
        st.session_state["messages"].append((f"Cel mai probabil nu supravietuiai {result}", "ai"))
    
        
for mesaj, role in st.session_state["messages"]:
    with st.chat_message(role) as msg:
        st.write(mesaj)