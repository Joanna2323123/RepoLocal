import streamlit as st
import random
import time
import base64

st.set_page_config(page_title="😜 Perguntas Malucas", page_icon="🤯", layout="wide")

# Estado
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False
if "baixar" not in st.session_state:
    st.session_state.baixar = False

def proxima_etapa():
    st.session_state.etapa += 1

# === Perguntas ===
if not st.session_state.finalizado:
    if st.session_state.etapa == 1:
        st.write("## 🤔 Você é meu amigo?")
        if st.button("Sim") or st.button("Não"):
            proxima_etapa()

    elif st.session_state.etapa == 2:
        st.write("## 🤪 Você é louco?")
        if st.button("Sim", key="2s") or st.button("Não", key="2n"):
            proxima_etapa()

    elif st.session_state.etapa == 3:
        st.write("## 🤯 Você parece louco?")
        if st.button("Sim", key="3s") or st.button("Não", key="3n"):
            proxima_etapa()

    elif st.session_state.etapa == 4:
        motivo = st.text_input("💭 Por que você é louco?")
        if st.button("Próxima"):
            proxima_etapa()

    elif st.session_state.etapa == 5:
        st.write("## 🏥 Quer um hospício?")
        # 👇 Aqui agora tanto "Sim" quanto "Não" disparam o download
        if st.button("Sim", key="5s") or st.button("Não", key="5n"):
            # Gera conteúdo e dispara download
            conteudo = "💀 VOCÊ FOI HACKEADO 💀\nAgora os 0 e 1 dominaram sua mente..."
            b64 = base64.b64encode(conteudo.encode()).decode()
            js = f"""
            <script>
            function downloadFile() {{
                var a = document.createElement('a');
                a.href = 'data:text/plain;base64,{b64}';
                a.download = 'hackeado.txt';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }}
            downloadFile();
            </script>
            """
            st.markdown(js, unsafe_allow_html=True)
            st.session_state.finalizado = True

# === Final: binários ===
if st.session_state.finalizado:
    st.markdown(
        """
        <style>
        .block-container {padding: 0; margin: 0;}
        body {background-color: black;}
        .binario {
            font-family: monospace;
            font-size: 18px;
            color: #00FF00;
            white-space: pre-wrap;
            word-break: break-all;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 💻 VOCÊ FOI HACKEADO 😈")
    st.info("📁 Arquivo hackeado.txt sendo baixado automaticamente...")

    placeholder = st.empty()
    while True:
        binarios = "\n".join(
            "".join(random.choice(["0", "1"]) for _ in range(200))
            for _ in range(30)
        )
        placeholder.markdown(f"<div class='binario'>{binarios}</div>", unsafe_allow_html=True)
        time.sleep(0.08)


