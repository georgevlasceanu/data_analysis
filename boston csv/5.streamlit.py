import streamlit as st
import enum
import pandas as pd


df = pd.read_csv("teams.csv", index_col=0)

class INTREBARI(enum.Enum):
    TROFEE_ECHIPA = 'Cate trofee are o anumita echipa?'
    TROFEE_TARA  = 'Cate trofee are o anumita tara?'
    TOP_X = 'Care este topul primelor x echipe'
    A_vs_B = 'Cine are mai multe trofee Echipa A vs Echipa B'

st.title("Castigatori Champion League")

optiuni = [i.value for i in INTREBARI]
select = st.selectbox("Alege una din optiuni", optiuni)
print("select=", select)
intrebare = INTREBARI(select)
print("intrebare=", intrebare)

if select == INTREBARI.TROFEE_ECHIPA.value:
    mesaj = "echipa"
elif select == INTREBARI.TROFEE_TARA.value:
    mesaj = "nationala"
elif select == INTREBARI.TOP_X.value:
    mesaj = "numar de echipe"  
elif select == INTREBARI.A_vs_B.value:
    mesaj = "cele doua echipe"  
    
    
with st.chat_message("ai") as msg:
    st.write(f"Alege {mesaj} despre care vrei sa afli mai multe")

keyword = st.chat_input(mesaj)

if intrebare == INTREBARI.TROFEE_ECHIPA:
    print(df['team'].unique())
    if keyword in df['team'].unique():
        with st.chat_message("user") as msg:
            st.write(f"{keyword}")
        reply = df[df['team'] == keyword]['trophies']
        with st.chat_message("ai") as msg:
            st.write(f"Echipa {keyword} are {reply.values} trofee")
    else:
        print("Nicio echipa") 
elif intrebare == INTREBARI.TROFEE_TARA:
    print(df['country'].unique())
    if keyword in df['country'].unique():
        with st.chat_message("user") as msg:
            st.write(f"{keyword}")
        reply = df[df['country'] == keyword]['trophies'].sum()
        with st.chat_message("ai") as msg:
            st.write(f"{keyword} are {reply} trofee")
    else:
        print("Nicio echipa") 

elif intrebare == INTREBARI.TOP_X:
    try:
        keyword = int(keyword)
        reply = df[:keyword]
        with st.chat_message("ai") as msg:
            st.dataframe(reply)

    except:
        print("Nu este o valoare valida")

elif intrebare == INTREBARI.A_vs_B:
    teams = keyword.split(' vs ')
    print(teams)
    if all([ team in df['team'].unique() for team in teams ]):
        # trofee0 = df[df['team'] == teams[0]]['trophies']
        # trofee1 = df[df['team'] == teams[1]]['trophies']
        reply_df = df[df['team'].isin(teams)]
        st.dataframe(reply_df)
        replay_team = reply_df[reply_df['trophies'] ==reply_df['trophies'].max()]['team']
        st.write(f"Echipa care are cele mai multe trofee din cele 2 este {replay_team}")

    else:
        print("echipele nu se afla in lista")