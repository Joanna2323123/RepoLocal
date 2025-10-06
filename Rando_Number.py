import streamlit as st
import random
import time
import base64

st.set_page_config(page_title="😜 Perguntas Malucas", page_icon="🤯", layout="wide")

# Estado da aplicação
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False
if "baixou" not in st.session_state:
    st.session_state.baixou = False

def proxima_etapa():
    st.session_state.etapa += 1

def finalizar():
    st.session_state.finalizado = True

# === Perguntas uma por vez ===
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
        if st.button("Sim", key="5s"):
            finalizar()
        elif st.button("Não", key="5n"):
            finalizar()

# === Final: Hackeado + download automático ===
else:
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

    # Gera conteúdo do TXT
    conteudo = "😈 Você foi hackeado!\nAgora você faz parte do mundo dos 0 e 1.\n— O Hacker"
    b64 = base64.b64encode(conteudo.encode()).decode()

    # Injetar JS para baixar automaticamente no último "Sim"
    if not st.session_state.baixou:
        st.session_state.baixou = True
        js = f"""
        <script>
        function downloadFile() {{
            var element = document.createElement('a');
            element.setAttribute('href', 'data:text/plain;base64,{b64}');
            element.setAttribute('download', 'hackeado.txt');
            document.body.appendChild(element);
            element.click();
            document.body.removeChild(element);
        }}
        downloadFile();
        </script>
        """
        st.markdown(js, unsafe_allow_html=True)

    # Mostrar binários infinitos na tela
    placeholder = st.empty()
    while True:
        binarios = "\n".join(
            "".join(random.choice(["0", "1"]) for _ in range(200))
            for _ in range(30)
        )
        placeholder.markdown(f"<div class='binario'>{binarios}</div>", unsafe_allow_html=True)
        time.sleep(0.08)

