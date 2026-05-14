# Título
# Input do chat(Mensagem do usuário)
# Cada mensagem que o usuário enviar:
  # - Mostrar a mensagem do usuário
  # - Mandar a mensagem para o modelo de linguagem
  # - Mostrar a resposta do modelo de linguagem
# StreamLit permite criar o frontend e backend de forma simples, usando somente Python.
import streamlit as st
from openai import OpenAI

# Cliente OpenRouter
client = OpenAI(
    api_key="API_KEY_AQUI",
    base_url="https://openrouter.ai/api/v1"
)

# Título
st.title("Chatbot do Ulisses")

# Histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Mostrar mensagens
for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
prompt = st.chat_input("Digite sua mensagem")

if prompt:

    # Mostrar usuário
    st.chat_message("user").write(prompt)

    # Salvar mensagem
    st.session_state.mensagens.append({
        "role": "user",
        "content": prompt
    })

    try:

        # Resposta IA
        resposta = client.chat.completions.create(
            model="inclusionai/ring-2.6-1t:free",
            messages=st.session_state.mensagens
        )

        texto = resposta.choices[0].message.content

    except Exception as erro:

        texto = f"Erro: {erro}"

    # Mostrar resposta
    st.chat_message("assistant").write(texto)

    # Salvar resposta
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": texto
    })