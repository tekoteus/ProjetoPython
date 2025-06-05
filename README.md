
# 🔐 Sistema de Login com Reconhecimento Facial

Este é um projeto em Python utilizando [Streamlit](https://streamlit.io/) e [DeepFace](https://github.com/serengil/deepface) para autenticação por reconhecimento facial. O sistema permite que o usuário acesse uma área protegida ao ser reconhecido por uma imagem enviada via webcam ou upload.

---

## 🛠️ Requisitos

- Windows (com suporte a `.bat`)
- Python **3.10.11** instalado e disponível no PATH
- Acesso à câmera (para uso da webcam)
- Pasta `corrigidos/` com as imagens dos rostos conhecidos

---

## 📁 Estrutura do Projeto

```
Projeto_Python_2.3/
│
├── corrigidos/               # Pasta com imagens dos rostos autorizados
├── main.py                   # Código principal do Streamlit
├── requirements.txt          # Bibliotecas necessárias
├── setup.bat                 # Cria o ambiente virtual e instala dependências
├── start.bat                 # Ativa o ambiente virtual e executa o Streamlit
└── README.md                 # Instruções de uso (este arquivo)
```

---

## ▶️ Como usar

### 1. Clonar ou baixar o projeto

Baixe o projeto em sua máquina e certifique-se de que a pasta `corrigidos/` contém as imagens dos rostos autorizados para o login.

---

### 2. Executar o setup

Abra o terminal (CMD) na pasta do projeto e execute o script abaixo para:

- Criar um ambiente virtual (`venv`)
- Instalar todas as dependências do projeto

```bash
setup.bat
```

Esse processo pode demorar alguns minutos dependendo da sua conexão.

---

### 3. Iniciar a aplicação

Após a instalação, inicie a aplicação com:

```bash
start.bat
```

Isso irá:
- Ativar o ambiente virtual
- Rodar o `streamlit run main.py` automaticamente

O navegador abrirá com a interface do login facial.

---

## 🧠 Como funciona

1. O usuário escolhe enviar uma imagem **via webcam** ou **upload**.
2. A imagem é comparada com os rostos da pasta `corrigidos/` usando o modelo **Facenet** do DeepFace.
3. Se houver correspondência, o acesso é concedido.

---

## 📸 Dicas para melhor desempenho

- As imagens em `corrigidos/` devem estar bem iluminadas, com o rosto em posição frontal.
- Use arquivos `.jpg`, `.jpeg` ou `.png`.
- O modelo usado é `Facenet` com o detector `retinaface`, que oferece bom equilíbrio entre precisão e velocidade.

---

## 🐍 Ambiente Python

Este projeto usa:

- **Python** 3.10.11
- **Streamlit**
- **DeepFace**
- **OpenCV**
- **streamlit-webrtc**
- **Pillow (PIL)**

As dependências estão listadas no `requirements.txt`.

---

## ❗ Possíveis erros

- Se a webcam não for detectada, recarregue a página ou verifique permissões do navegador.
- Certifique-se de que a pasta `corrigidos/` existe e contém imagens válidas.
- Para problemas com `dlib` ou `tensorflow`, tente reinstalar manualmente no ambiente virtual.

---

## 📄 Licença

Este projeto é livre para fins educacionais e experimentais. Adaptável para sistemas de controle de acesso, segurança, ou autenticação biométrica.
