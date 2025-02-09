import streamlit as st
import requests

st.title("Tell me a joke")

# Input for keyword
mesaj = st.chat_input("Insert a keyword")

# Initialize the messages list in session state if it's not already there
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Default AI message asking for a keyword
if len(st.session_state["messages"]) == 0:
    with st.chat_message("ai"):
        st.write("Choose a keyword. I will tell you a joke about it")

# If a keyword is inserted, fetch and display a joke
if mesaj:
    st.session_state["messages"].append((mesaj, "user"))  # Append user message

    # Fetch joke with the keyword from the API (if no specific joke search, fetch general joke)
    response = requests.get("https://icanhazdadjoke.com/search", 
                            headers={"Accept": "application/json"}, 
                            params={"term": mesaj})
    jokes = response.json().get("results")
    
    # If jokes found, append the first one; otherwise, show a fallback message
    if jokes:
        joke = jokes[0]["joke"]
    else:
        joke = "I couldn't find a joke with that keyword. Try something else!"
    
    st.session_state["messages"].append((joke, "ai"))  # Append AI message with joke

# Display the messages from the session state
for mesaj, role in st.session_state['messages']:
    with st.chat_message(role):
        st.write(mesaj)

# import streamlit as st
# import requests

# st.title("Tell me a joke")
# mesaj = st.chat_input("Insert a keyword")

# if not st.session_state.get("messages"):
#     st.session_state["messages"] = []

# with st.chat_message("ai") as msg:
#     st.write("Choose a keyword. I will tell you a joke about it")

# print("st.session_state:", st.session_state, type(st.session_state))

# print(mesaj)
# if mesaj:
#     print("Mesaj nou venit")
#     st.session_state["messages"].append((mesaj, "user"))
#     print("st.session_state:", st.session_state, type(st.session_state))

#     response = requests.get("https://icanhazdadjoke.com/search", headers={"Accept":"text/plain"}, params={"term":mesaj, "limit":1})
#     print(response.request)
#     st.session_state["messages"].append((response.text, "ai"))


# for mesaj, role in st.session_state["messages"]:
#     with st.chat_message(role) as msg:
#         st.write(mesaj)

