
# Reconhecimento Facial para Desbloqueio de Login

Este projeto foi desenvolvido como parte de um trabalho acadêmico e tem como objetivo implementar um sistema de reconhecimento facial para desbloqueio de login de maneira segura e eficiente.

## Funcionalidades
- Captura de imagem em tempo real utilizando a webcam.
- Upload de imagens para identificação facial.
- Processamento de imagens (rotação, conversão de formato, etc.) com a biblioteca Pillow.
- Reconhecimento facial robusto através da biblioteca DeepFace usando o modelo FaceNet.
- Identificação de rostos conhecidos por meio de comparação com uma base de dados de imagens.
- Interface intuitiva para seleção de arquivos via Tkinter.

## Tecnologias Utilizadas
- Linguagem: Python.
- Bibliotecas principais:- DeepFace para reconhecimento facial.
- Pillow para manipulação de imagens.
- OpenCV para captura de imagem pela webcam.
- Tkinter para interface gráfica.

- Estrutura modular para facilitar manutenções e expansões futuras.

## Como Funciona
- O usuário pode optar por capturar uma foto via webcam ou fazer upload de uma imagem.
- O sistema processa a imagem, converte para o formato correto e a compara com uma base de dados de rostos conhecidos.
- Caso o rosto seja reconhecido, o sistema identifica a pessoa e concede acesso.
- Em caso de falha, o sistema registra a tentativa e oferece opções adicionais.

## Aplicações
- Sistemas de segurança pessoais ou acadêmicos.
- Automação no controle de acesso por meio de inteligência artificial.

Instruções de Uso
- Clone o repositório: git clone https://github.com/seu_usuario/repositorio-reconhecimento-facial.git
- Instale as dependências listadas no requirements.txt.
- Configure os diretórios para imagens originais e processadas.
- Execute o script principal e escolha o método de identificação.



