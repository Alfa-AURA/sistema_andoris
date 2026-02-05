import streamlit as st
import requests  # A biblioteca que faz a conexão com o n8n

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sistema Andoris",
    page_icon="🛡️",
    layout="centered"
)

# --- ESTILO VISUAL (MANTIDO) ---
# --- ESTILO VISUAL (CORRIGIDO: TURQUESA BLINDADO) ---
st.markdown("""
    <style>
    /* Fundo escuro */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Texto geral branco/cinza (para corrigir celular no modo claro) */
    .stApp p, .stApp div, .stApp li, .stApp span, .stMarkdown {
        color: #E0E0E0;
    }

    /* TÍTULOS: Força Turquesa no H1 e nos SPANS dentro dele */
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
# --- TÍTULO (COM COR TURQUESA FORÇADA) ---
st.markdown("<h1 style='text-align: center; color: #40E0D0 !important;'>🛡️ PROTOCOLO ANDORIS</h1>", unsafe_allow_html=True)

# --- SUBTÍTULO ---
st.markdown("<h3 style='text-align: center; color: white;'>Base de Conhecimento Tático PCS - 2026</h3>", unsafe_allow_html=True)
st.divider()

# --- INPUT DO COMANDANTE ---
pergunta = st.text_input("Comandante, insira sua consulta operacional:")

# --- LÓGICA DE CONEXÃO ---
if st.button("PROCESSAR DADOS"):
    if pergunta:
        with st.spinner('📡 Andoris contatando base de dados...'):
            try:
                # Pega o link do cofre secreto do Streamlit
                webhook_url = st.secrets["WEBHOOK_URL"]

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









