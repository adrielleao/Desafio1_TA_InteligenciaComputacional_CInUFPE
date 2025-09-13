import os
from typing import Tuple, List, Any

import numpy as np
import streamlit as st
from PIL import Image, ImageOps

from tensorflow.keras.models import load_model


@st.cache_resource
def carregar_modelo() -> Tuple[Any, List[str]]:
    """Carrega o modelo Keras e os rótulos de forma eficiente.

    Returns
    -------
    tuple[Any, list[str]]
        Uma tupla contendo o modelo carregado e uma lista de strings com os nomes das classes.
        Retorna (None, None) em caso de erro.
    """
    
    try:
        caminho_dir = os.path.dirname(os.path.abspath(__file__))
        
        caminho_modelo = os.path.join(caminho_dir, "keras_model.h5")
        caminho_labels = os.path.join(caminho_dir, "labels.txt")
        
        model = load_model(caminho_modelo, compile=False)
        with open(caminho_labels, "r", encoding="utf-8") as f:
            class_names = f.readlines()
        return model, class_names
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        st.info("Verifique se os arquivos 'keras_model.h5' e 'labels.txt' estão na mesma pasta.")
        return None, None


def prever_jogada(image_data: st.runtime.uploaded_file_manager.UploadedFile, model: Any, class_names: List[str]) -> Tuple[str, np.float32]:
    """Processa a imagem da câmera e retorna a jogada prevista e a confiança.

    Parameters
    ----------
    image_data : UploadedFile
        O objeto de arquivo carregado pela câmera do Streamlit.
    model : Any
        O modelo Keras carregado.
    class_names : list[str]
        Uma lista com os nomes das classes.

    Returns
    -------
    tuple[str, np.float32]
        Uma tupla contendo o nome da classe prevista (string) e o score de confiança (float).
    """
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(image_data).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:].strip().lower(), confidence_score
