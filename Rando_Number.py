import streamlit as st
import random
import time
import io

st.set_page_config(page_title="😜 Perguntas Malucas", page_icon="🤯", layout="wide")

# Estado
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

# Perguntas uma por vez
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

# Final: gera txt para download
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

    # Criar conteúdo do arquivo .txt
    conteudo = "😈 Você foi hackeado! Isso é apenas uma simulação.\n\n0 e 1 são agora parte de você.\n\n— O Hacker"
    arquivo = io.BytesIO(conteudo.encode("utf-8"))

    # Botão de download
    st.download_button(
        label="📥 Baixar arquivo.txt",
        data=arquivo,
        file_name="hackeado.txt",
        mime="text/plain",
        on_click=lambda: st.session_state.update({"baixou": True})
    )

    # Só mostra os binários se ele já clicou no botão
    if st.session_state.baixou:
        placeholder = st.empty()
        while True:
            binarios = "\n".join(
                "".join(random.choice(["0", "1"]) for _ in range(200))
                for _ in range(30)
            )
            placeholder.markdown(f"<div class='binario'>{binarios}</div>", unsafe_allow_html=True)
            time.sleep(0.08)


