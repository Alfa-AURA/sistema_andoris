import streamlit as st
import requests  # A biblioteca que faz a conexão com o n8n

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sistema Andoris",
    page_icon="🛡️",
    layout="centered"
)

# --- ESTILO VISUAL (MANTIDO) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1 { color: #40E0D0 !important; text-align: center; }
    .stTextInput > label { color: #00FF7F !important; font-weight: bold; }
    div.stButton > button { background-color: #40E0D0; color: black; border-radius: 10px; border: none; }
    div.stButton > button:hover { background-color: #00FF7F; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🛡️ PROTOCOLO ANDORIS")
st.markdown("<h3 style='text-align: center; color: white;'>Base de Conhecimento Tático PCS - 2026</h3>", unsafe_allow_html=True)
st.divider()

# --- INPUT DO COMANDANTE ---
pergunta = st.text_input("Comandante, insira sua consulta operacional:")

# --- LÓGICA DE CONEXÃO ---
if st.button("PROCESSAR DADOS"):
    if pergunta:
        with st.spinner('📡 Andoris contatando base de dados...'):
            try:
                # 1. A URL do seu n8n (COLE AQUI A URL QUE VOCÊ COPIOU)
                webhook_url = "https://loboalpha.app.n8n.cloud/webhook-test/andoris-chat-pcs"
                # 2. O pacote de dados que vamos enviar (JSON)
                payload = {"pergunta": pergunta}
                
                # 3. Enviando para o n8n
                response = requests.post(webhook_url, json=payload)
                
                # 4. Recebendo a resposta
                if response.status_code == 200:
                    dados_resposta = response.json()
                    # Tenta pegar o texto da resposta (ajuste a chave 'output' conforme seu n8n)
                    resposta_texto = dados_resposta.get("output", "Resposta recebida, mas sem texto claro.")
                    
                    st.success("✅ Conexão Estabelecida!")
                    st.markdown(f"### 🛡️ Resposta da Andoris:\n\n{resposta_texto}")
                else:
                    st.error(f"⚠️ Erro no servidor: {response.status_code}")
            
            except Exception as e:
                st.error(f"⚠️ Falha na conexão: {e}")
    else:
        st.warning("⚠️ Alerta: Insira um comando válido.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Desenvolvido pelo Comandante Lobo Alfa | Powered by AURA & n8n</p>", unsafe_allow_html=True)