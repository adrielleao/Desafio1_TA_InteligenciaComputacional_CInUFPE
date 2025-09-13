import streamlit as st


def definir_vencedor(sua_jogada: str, jogada_sistema: str) -> str:
    """Define o vencedor da rodada e atualiza o placar no session_state.

    Parameters
    ----------
    sua_jogada : str
        Jogada do usuário ("pedra", "papel" ou "tesoura").
    jogada_sistema : str
        Jogada escolhida pelo Sistema.

    Returns
    -------
    str
        Mensagem de resultado da rodada ("Empate! 🤝", "Você Venceu! 🎉" ou "Skynet Venceu! 🤖").
    """
    if sua_jogada == jogada_sistema:
        return "Empate! 🤝"
    elif (sua_jogada == "pedra" and jogada_sistema == "tesoura") or \
         (sua_jogada == "papel" and jogada_sistema == "pedra") or \
         (sua_jogada == "tesoura" and jogada_sistema == "papel"):
        st.session_state.placar_voce += 1
    else:
        st.session_state.placar_sistema += 1
