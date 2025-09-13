import random
from typing import Dict, List, Any

import streamlit as st

from src.regras import definir_vencedor
from src.ui import (inicializar_estado,   
                    configurar_pagina, 
                    sidebar, 
                    mostrar_placar, 
                    mostrar_jogadas)
from utils.modelo import carregar_modelo, prever_jogada


def app() -> None:
    """
    Função principal do aplicativo Streamlit.

    Orquestra a inicialização do estado, a configuração da interface do usuário e a lógica do jogo.
    Detecta a jogada do usuário via webcam, faz a previsão usando o modelo de IA e define o vencedor
    de cada rodada de Jokenpô.
    """

    inicializar_estado()
    configurar_pagina()
    sidebar()

    opcoes_sistema: List[str] = ["pedra", "papel", "tesoura"]
    imagens_ia: Dict[str, str] = {
        "pedra": "https://static.vecteezy.com/system/resources/previews/019/527/056/non_2x/an-8-bit-retro-styled-pixel-art-illustration-of-a-stone-rock-free-png.png",
        "papel": "https://art.ngfiles.com/images/5739000/5739581_835822_clumsyslime_untitled-5739581.be8e4a5e272f52f9aacb8c636445114b.webp?f1717002910",
        "tesoura": "https://img.freepik.com/premium-vector/pixel-art-illustration-scissors-pixelated-scissors-tools-scissors-cutter-pixelated_1038602-773.jpg"
    }

    mostrar_placar()

    camera_image: Any
    camera_image, _ = mostrar_jogadas(imagens_ia)
    
    model: Any
    class_names: List[str]
    model, class_names = carregar_modelo()

    if model is not None and camera_image is not None and not st.session_state.jogada_processada:
        sua_jogada: str
        confianca: float
        sua_jogada, confianca = prever_jogada(camera_image, model, class_names)

        if sua_jogada in opcoes_sistema and confianca > 0.85:
            jogada_sistema: str = random.choice(opcoes_sistema)
            st.session_state.jogada_sistema = jogada_sistema

            resultado: str = definir_vencedor(sua_jogada, jogada_sistema)
            st.session_state.jogada_processada = True

            st.subheader(f"Você jogou: **{sua_jogada.capitalize()}** (Confiança: {confianca:.1%})")
            st.header(resultado)
            st.rerun()

        elif sua_jogada not in opcoes_sistema:
            st.warning(f"Gesto não reconhecido como Pedra, Papel ou Tesoura. (Detectado: {sua_jogada})")
        else:
            st.warning(f"Gesto não reconhecido com clareza (Confiança: {confianca:.0%}). Por favor, tente novamente.")