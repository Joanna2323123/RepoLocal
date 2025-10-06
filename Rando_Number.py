import streamlit as st
import random
import time
import io
import base64

st.set_page_config(page_title="😜 Perguntas Malucas", page_icon="🤯", layout="wide")

if "etapa" not in st.session_state:
    st.session_state.etapa = 1
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False
if "download_ok" not in st.session_state:
    st.session_state.download_ok = False

def proxima_etapa():
    st.session_state.etapa += 1

def finalizar():
    st.session_state.finalizado = True

# Perguntas
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
        if st.button("Sim", key="5s") or st.button("Não", key="5n"):
            finalizar()

# Final: hackeado + download automático
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

    # Gera o conteúdo do arquivo
    conteudo = "😈 Você foi hackeado!\nAgora o mundo dos 0 e 1 faz parte de você.\n— O Hacker"
    b64 = base64.b64encode(conteudo.encode()).decode()

    # Script JS para forçar download automático
    js = f"""
    <script>
    function downloadFile() {{
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;base64,{b64}');
        element.setAttribute('download', 'hackeado.txt');
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }}
    downloadFile();
    </script>
    """

    # Injetar o script apenas uma vez
    if not st.session_state.download_ok:
        st.session_state.download_ok = True
        st.markdown(js, unsafe_allow_html=True)

    # Mostrar os binários ocupando a tela toda
    placeholder = st.empty()
    while True:
        binarios = "\n".join(
            "".join(random.choice(["0", "1"]) for _ in range(200))
            for _ in range(30)
        )
        placeholder.markdown(f"<div class='binario'>{binarios}</div>", unsafe_allow_html=True)
        time.sleep(0.08)



