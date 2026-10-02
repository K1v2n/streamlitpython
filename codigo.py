import streamlit as st
from  openai import OpenAI 

modelo_ai = OpenAI(api_key="AQ.Ab8RN6IeEdELm78T4MxbHdYyUtzNwaPAqZA0TpFcdw9xFDgIPw",
                    base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.write("## CHATBOT DE AI")

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []


msg_usuario = st.chat_input('escreva sua mensagem aqui')

for mensagem in st.session_state["lista_mensagem"]:
    quem_enviou = mensagem["role"]
    txt = mensagem["content"]
    st.chat_message("role").write(txt)


if msg_usuario:
    st.chat_message("user").write(msg_usuario)
    msg = {"role": "user", "content": msg_usuario}
    st.session_state["lista_mensagem"].append(msg)
    

    resposta_modelo = modelo_ai.chat.completions.create(
        messages= st.session_state["lista_mensagem"],
        model="gemini-flash-lite-latest"
    )


    resposta_ai = resposta_modelo.choices[0].message.content


    st.chat_message("assistant").write(resposta_ai)
    msg2 = {"role": "assistant", "content": resposta_ai}
    st.session_state["lista_mensagem"].append(msg2)
