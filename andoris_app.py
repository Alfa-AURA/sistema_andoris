import streamlit as st
import requests

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Protocolo Andoris", page_icon="🛡️", layout="centered")

# --- ESTILO VISUAL (DARK MODE + TURQUESA) ---
st.markdown("""
    <style>
    /* Fundo escuro */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Texto geral claro (para corrigir modo claro de celulares) */
    .stApp p, .stApp div, .stApp li, .stApp span, .stMarkdown {
        color: #E0E0E0;
    }

    /* Títulos: BLINDADOS com !important para vencer o branco */
    h1, h1 span, h2, h2 span, h3, h3 span {
        color: #40E0D0 !important; 
        text-align: center;
    }
    
    /* Labels dos inputs em Verde */
    .stTextInput > label, .stTextInput > label > span {
        color: #00FF7F !important;
        font-weight: bold;
    }
    
    /* Botões */
    div.stButton > button {
        background-color: #40E0D0;
        color: black !important;
        border-radius: 10px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #00FF7F;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1 style='text-align: center; color: #40E0D0 !important;'>🛡️ PROTOCOLO ANDORIS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Base de Conhecimento Tático PCS - 2026</h3>", unsafe_allow_html=True)

# --- SEGREDOS E CONFIGURAÇÃO ---
# Tenta pegar o Segredo. Se não achar, avisa o erro amigavelmente.
try:
    webhook_url = st.secrets["WEBHOOK_URL"]
except Exception:
    st.error("🚨 ERRO TÁTICO: O segredo 'WEBHOOK_URL' não foi encontrado. Verifique o Streamlit Cloud.")
    st.stop()

# --- INICIALIZAÇÃO DO CHAT (MEMÓRIA) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- EXIBIR HISTÓRICO NA TELA ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LÓGICA DE ENVIO (O CÉREBRO) ---
if prompt := st.chat_input("Digite sua mensagem para a Andoris..."):
    
    # 1. Mostra a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    # Salva no histórico
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Envia para a IA
    with st.chat_message("assistant"):
        with st.spinner("Analisando dados táticos..."):
            try:
                # Payload correto para o n8n
                payload = {"input": prompt}
                
                response = requests.post(webhook_url, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    # Tenta pegar a resposta do campo 'output' ou 'text'
                    bot_reply = data.get("output", data.get("text", "⚠️ A base de dados retornou vazio."))
                    
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.error(f"Falha na comunicação: Código {response.status_code}")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")


# --- RODAPÉ ---
st.markdown("---")

st.markdown("<p style='text-align: center; color: gray;'>Desenvolvido pelo Comandante Lobo Alfa | Powered by AURA & n8n</p>", unsafe_allow_html=True)




