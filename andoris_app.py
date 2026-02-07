import streamlit as st
import requests

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Protocolo Andoris", page_icon="🛡️", layout="centered")

# --- ESTILO VISUAL AVANÇADO (TURQUESA & DARK) ---
st.markdown("""
    <style>
    /* Fundo principal */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Customização da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #40E0D0;
    }

    /* Títulos em Turquesa Neon */
    h1 {
        color: #40E0D0 !important;
        text-shadow: 0 0 10px rgba(64, 224, 208, 0.5);
        font-family: 'Courier New', Courier, monospace;
    }

    /* Estilização das Mensagens */
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid rgba(64, 224, 208, 0.1);
    }
    
    /* Botões e Inputs */
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR - MURAL DE HONRA) ---
with st.sidebar:
    # 1. Identidade Visual (Escudo & Árvore)
    col1, col2 = st.columns([1, 4])
    with col1:
        st.write("🛡️")
    with col2:
        st.write("🌳 **PROTOCOLO ANDORIS**")
    
    # 2. A Missão (Texto Oficial)
    st.info("""
    **Missão:** Inteligência de Conservação.
    
    A Andoris é o 'Cérebro Digital' que processa os dados vitais da Serra de Baturité para proteger o *Pyrrhura griseipectus*.
    """)
    
    st.markdown("---")
    
    # 3. MURAL DE HONRA (A Alma do Projeto)
    st.markdown("#### 🎖️ ESQUADRÃO DE ELITE (PCS)")
    st.caption("*A inteligência deste sistema é construída pelo esforço diário desta equipe:*")
    
    # Comando & Inteligência
    st.markdown("**🧠 Inteligência & Estratégia:**")
    st.text("• Lobo Alfa (Coord. Tática)")
    st.text("• Érica Demondes (Logística & Dados)") # <--- Ajuste realizado aqui!
    st.text("• AURA (Processamento AI)")

    # Agentes de Campo (A Força Operacional)
    st.markdown("**🔭 Operações de Campo (Coleta):**")
    st.text("• Carlos Jorge")
    st.text("• Werlyson Pinheiro")
    st.text("• Jonas Cruz")
    
    st.markdown("---")
    
    # 4. Status do Sistema
    st.markdown("#### 📡 STATUS DE REDE")
    st.success("Conexão Neural: **ESTÁVEL**")
    st.caption("Monitorando 90 Sítios na Serra.")

# --- CABEÇALHO CENTRAL ---
st.markdown("<h1 style='text-align: center;'>🛡️ PROTOCOLO ANDORIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF7F;'><b>Centro de Comando Tático PCS - Serra de Baturité</b></p>", unsafe_allow_html=True)

# --- CONFIGURAÇÃO DE SEGREDOS ---
try:
    webhook_url = st.secrets["WEBHOOK_URL"]
except:
    st.error("🚨 ERRO TÁTICO: Webhook não configurado.")
    st.stop()

# --- MEMÓRIA DO CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LÓGICA DE INTERAÇÃO ---
if prompt := st.chat_input("Solicitar relatório tático..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Acessando base de dados..."):
            try:
                # Payload correto para o n8n
                response = requests.post(webhook_url, json={"input": prompt})
                if response.status_code == 200:
                    data = response.json()
                    bot_reply = data.get("output", data.get("text", "Aguardando sinal..."))
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.error("Sinal interrompido. Verifique o n8n.")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
