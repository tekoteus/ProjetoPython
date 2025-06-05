import streamlit as st
from deepface import DeepFace
from PIL import Image
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import os
import tempfile
import cv2
import numpy as np

# Silenciar logs do TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Configuração do Streamlit
st.set_page_config(page_title="Reconhecimento Facial", layout="centered")
st.title("🔐 Login com Reconhecimento Facial")

# Caminho para a pasta corrigida (rostos conhecidos)
PASTA_ROSTOS = os.path.join("C:/Projeto_Python_2.3", "corrigidos")
if not os.path.exists(PASTA_ROSTOS):
    st.warning("⚠️ Pasta 'corrigidos' não encontrada.")

# Inicializar variáveis de sessão
if "imagem_usuario" not in st.session_state:
    st.session_state["imagem_usuario"] = None
if "acesso_liberado" not in st.session_state:
    st.session_state["acesso_liberado"] = False

# Função de reconhecimento facial
def reconhecer_rosto(img_path):
    try:
        st.info("🔍 Verificando rosto...")
        resultado = DeepFace.find(
            img_path=img_path,
            db_path=PASTA_ROSTOS,
            model_name="Facenet",
            detector_backend="retinaface",
            enforce_detection=False
        )

        if not resultado[0].empty:
            identity = resultado[0].iloc[0]['identity']
            nome = os.path.splitext(os.path.basename(identity))[0]
            st.success(f"✅ Rosto reconhecido: {nome}")
            st.session_state["acesso_liberado"] = True
        else:
            st.warning("❌ Rosto não reconhecido.")
            st.session_state["acesso_liberado"] = False
    except Exception as e:
        st.error(f"Erro ao reconhecer rosto: {e}")
        st.session_state["acesso_liberado"] = False

# Conteúdo protegido
if st.session_state["acesso_liberado"]:
    st.success("🔓 Acesso concedido. Bem-vindo!")
    st.write("🎯 Painel confidencial ou conteúdo protegido.")
    
    if st.button("Logout"):
        st.session_state["imagem_usuario"] = None
        st.session_state["acesso_liberado"] = False
        st.experimental_rerun()

else:
    modo = st.radio("Como deseja enviar a imagem?", ["📷 Webcam", "📁 Upload"])

    # Upload de imagem
    if modo == "📁 Upload":
        uploaded_file = st.file_uploader("Escolha uma imagem JPG/PNG", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            img = Image.open(uploaded_file).convert("RGB")
            temp_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
            img.save(temp_path, format="JPEG")
            st.session_state["imagem_usuario"] = temp_path
            st.image(img, caption="Imagem enviada", width=300)

    # Captura via webcam
    if modo == "📷 Webcam":
        class VideoProcessor(VideoTransformerBase):
            def __init__(self):
                self.frame = None

            def transform(self, frame):
                img = frame.to_ndarray(format="bgr24")
                self.frame = img
                return img

        ctx = webrtc_streamer(
            key="webcam",
            video_processor_factory=VideoProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )

        if ctx.video_processor:
            st.info("📸 Clique abaixo para capturar a imagem.")
            if st.button("Capturar imagem"):
                frame = ctx.video_processor.frame
                if frame is not None:
                    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(img_rgb)
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
                    pil_img.save(temp_file.name, format="JPEG")
                    st.session_state["imagem_usuario"] = temp_file.name
                    st.image(pil_img, caption="Imagem capturada", width=300)
                else:
                    st.warning("❗ Nenhum frame da webcam ainda.")

    # Botão de verificação
    if st.session_state["imagem_usuario"]:
        st.image(Image.open(st.session_state["imagem_usuario"]), caption="Imagem pronta para verificação", width=300)
        if st.button("🔍 Verificar rosto"):
            reconhecer_rosto(st.session_state["imagem_usuario"])
