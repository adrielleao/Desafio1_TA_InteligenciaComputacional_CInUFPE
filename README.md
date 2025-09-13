# Jokenpô com Skynet  

Este projeto é a primeira atividade para a disciplina de **Tópicos Avançados em Inteligência Computacional** do **CIn-UFPE**. Ele demonstra a integração de um modelo de **Visão Computacional** com uma aplicação interativa.

A aplicação é um jogo de Jokenpô (pedra, papel e tesoura), onde o usuário joga contra um sistema batizado de **Skynet**. O modelo de classificação, treinado previamente com o **Google Teachable Machine**, identifica a jogada do usuário pela webcam e o resultado da rodada é definido em tempo real com escolha aleatória do sistema.

---

### Requisitos

Certifique-se de que você tenha instalado:
- **Python** (versões 3.9, 3.10 ou 3.11)  
- **Git**

---

### Instalação

1. Clone este repositório para o seu computador:
    ```bash
    git clone https://github.com/adrielleao/Desafio1_TA_InteligenciaComputacional_CInUFPE.git
    cd projeto-jokenpo
    ```

2. Crie e ative o ambiente virtual para o projeto:  
   - Linux/Mac:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

---

### Como Usar

1. Garanta que os arquivos do modelo (`keras_model.h5` e `labels.txt`) exportados do Teachable Machine estejam na pasta correta: `utils/`.

2. Execute o aplicativo com o Streamlit a partir da pasta raiz do projeto:
    ```bash
    streamlit run main.py
    ```

3. A aplicação será aberta automaticamente no seu navegador.  
   Siga as instruções na tela para jogar Jokenpô usando a sua webcam.

---

### Estrutura do Projeto

```text
projeto-jokenpo/
├── main.py                # Ponto de entrada do aplicativo
├── README.md              # Documentação principal
├── requirements.txt       # Dependências do projeto
├── src/                   # Diretório de código-fonte
│   ├── app.py             # Lógica principal da aplicação Streamlit
│   ├── regras.py          # Regras do jogo
│   └── ui.py              # Funções da interface
└── utils/                 # Utilitários e arquivos do modelo
    ├── __init__.py
    ├── modelo.py          # Funções para carregar e usar o modelo da IA
    ├── keras_model.h5     # Arquivo do modelo treinado
    └── labels.txt         # Rótulos das classes do modelo
```

---

### Tecnologias Utilizadas

- **Python**: Linguagem de programação principal  
- **Streamlit**: Framework para criar a interface web  
- **TensorFlow/Keras**: Para carregar e rodar o modelo de Deep Learning  
- **Pillow** e **NumPy**: Para o pré-processamento das imagens  
