import streamlit as st
from chatbot import predict_class, get_response, intents


st.title("🤖 Margo")



# Sesion
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar msg del historial 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# variable del prompt
prompt = st.chat_input("Escribe aquí")

#comprobar que el prompt esté lleno
if prompt:
    #Como usuario pinto lo que está en el prompt
    with st.chat_message(name="user", avatar="😊"):
        st.markdown(f"Tú: {prompt}")

    st.session_state.messages.append({"role": "user", "content": prompt})

    # que devuelva lo mismo el chatbot
    insts = predict_class(prompt)
    res = get_response(insts,intents)

    with st.chat_message(name="assistant",avatar="🤖"):
      st.markdown(res)
    st.session_state.messages.append({"role":"assistant","content":res})