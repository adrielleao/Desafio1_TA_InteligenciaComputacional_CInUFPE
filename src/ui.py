import streamlit as st
from typing import Dict, Any, Tuple


def inicializar_estado() -> None:
    """Inicializa variáveis de sessão do Streamlit.

    Verifica a existência das chaves 'placar_voce', 'placar_sistema' e
    'jogada_processada' e as inicializa caso não existam.
    """
    if 'placar_voce' not in st.session_state:
        st.session_state.placar_voce = 0
    if 'placar_sistema' not in st.session_state:
        st.session_state.placar_sistema = 0
    if 'jogada_processada' not in st.session_state:
        st.session_state.jogada_processada = False


def configurar_pagina() -> None:
    """Configura o layout e título da página Streamlit."""
    st.set_page_config(page_title="Jokenpô com Reconhecimento de Imagem", page_icon="🤖", layout="centered")
    st.markdown("<h1 style='text-align: center; margin-top: -3rem;'>Jokenpô!</h1>", unsafe_allow_html=True)


def sidebar() -> None:
    """Exibe o conteúdo da barra lateral do aplicativo."""
    with st.sidebar:
        st.title("Sobre o Projeto")
        st.info(
            """
            Este projeto é a primeira atividade para a disciplina de Tópicos Avançados em Inteligência Computacional do CIn-UFPE. Ele demonstra a integração de um modelo de Visão Computacional com uma aplicação interativa.

A aplicação é um jogo de Jokenpô (pedra, papel e tesoura), onde o usuário joga contra o sistema, batizado de Skynet. O modelo de classificação, treinado previamente com o Google Teachable Machine, identifica a jogada do usuário pela webcam e o resultado da rodada é definido em tempo real.
            """
        )
        if st.button("Resetar Placar"):
            st.session_state.placar_voce = 0
            st.session_state.placar_sistema = 0
            st.session_state.jogada_processada = False
            st.rerun()


def mostrar_placar() -> None:
    """Exibe o placar atual do jogo."""
    st.subheader("Placar 🏆")
    col_placar1, col_placar2 = st.columns(2)
    with col_placar1:
        st.markdown("<h3 style='text-align: center;'>🌎 Você</h3>", unsafe_allow_html=True)
        st.markdown(
            f"<p style='text-align: center; font-size: 2.5em; font-weight: bold;'>{st.session_state.placar_voce}</p>",
            unsafe_allow_html=True
        )

    with col_placar2:
        st.markdown("<h3 style='text-align: center;'>💀 Skynet</h3>", unsafe_allow_html=True)
        st.markdown(
            f"<p style='text-align: center; font-size: 2.5em; font-weight: bold;'>{st.session_state.placar_sistema}</p>",
            unsafe_allow_html=True
        )

    st.write("")


def mostrar_jogadas(imagens_ia: Dict[str, str]) -> Tuple[Any, Any]:
    """Exibe os componentes da interface para as jogadas do usuário e da IA.

    Parameters
    ----------
    imagens_ia : dict[str, str]
        Um dicionário mapeando as jogadas da IA para URLs de imagens.

    Returns
    -------
    tuple[Any, Any]
        Uma tupla contendo o objeto de imagem da câmera (retorno de st.camera_input) e o placeholder para a jogada da IA.
    """
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align: center;'>Sua Jogada</h3>", unsafe_allow_html=True)
        camera_image = st.camera_input("Tire sua foto aqui", label_visibility="collapsed")
        if camera_image is None:
            st.session_state.jogada_processada = False

    with col2:
        st.markdown("<h3 style='text-align: center;'>Jogada da Skynet</h3>", unsafe_allow_html=True)
        placehoder_sistema = st.empty()
        if not st.session_state.jogada_processada:
            placehoder_sistema.markdown("<p style='text-align: center;'>Aguardando sua jogada...</p>", unsafe_allow_html=True)
        else:
            jogada_sistema = st.session_state.jogada_sistema
            imagem_jogada_sistema = imagens_ia[jogada_sistema]
            with placehoder_sistema.container():
                col_vazia_esquerda, col_centro, col_vazia_direita = st.columns([1, 2, 1])
                with col_centro:
                    st.image(imagem_jogada_sistema, width=200)

                # st.markdown(f"<h4 style='text-align: center;'>Skynet jogou {jogada_sistema.capitalize()}!</h4>", unsafe_allow_html=True)

    return camera_image, placehoder_sistema