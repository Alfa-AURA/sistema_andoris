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

# --- BARRA LATERAL (SIDEBAR) ---
# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # 1. Identidade Visual
    st.image("https://img.icons8.com/neon/96/shield.png", width=80)
    st.markdown("### 🛡️ PROTOCOLO ANDORIS")
    
    # 2. A Descrição Oficial (Nova!)
    st.info("""
    **Missão:** Inteligência Tática para Conservação.
    
    A Andoris atua como o 'Cérebro Digital' do **Projeto Cara-Suja**, processando dados de campo da Serra de Baturité para monitorar a reprodução do *Pyrrhura griseipectus*.
    
    **Objetivo:** Garantir que cada ninho, ovo e filhote seja contabilizado na luta contra a extinção.
    """)
    
    st.markdown("---")
    
    # 3. Status e Regras
    st.markdown("#### 📡 STATUS OPERACIONAL")
    st.success("Conexão Neural: **ESTÁVEL**")
    st.warning("Próxima Sincronização: **08/02**") # Exemplo de data futura
    
    st.markdown("---")
    
    # 4. Créditos
    st.caption("🛠️ **Operadores do Sistema:**")
    st.caption("Cmte. Lobo Alfa (Estratégia)")
    st.caption("Agente AURA (Processamento)")

# --- CABEÇALHO CENTRAL ---
st.markdown("<h1 style='text-align: center;'>🛡️ PROTOCOLO ANDORIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF7F;'><b>Centro de Comando Tático PCS - Serra de Baturité</b></p>", unsafe_allow_html=True)

# --- CONFIGURAÇÃO DE SEGREDOS ---
try:
    webhook_url = st.secrets["WEBHOOK_URL"]
except:
    st.error("🚨 ERRO: Webhook não configurado.")
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
                # O payload que você validou como funcional!
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

