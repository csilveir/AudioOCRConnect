### Projeto responsável por capturar texto de uma imagem ### utilizando a câmera de um celular e reproduzir o texto em ### forma de áudio, catalogando tanto o texto quanto o áudio.
### Para começar, ative o ambiente virtual:

source env/bin/activate


### Em seguida, instale as dependências necessárias:

brew install tesseract
pip3 install gtts playsound PyObjC

### Este projeto utiliza o Tesseract para reconhecimento ### óptico de caracteres (OCR), a biblioteca gtts para síntese de ### fala em áudio, e PyObjC para interagir com a câmera do dispositivo.

### Exemplo de Comando para envio de uma API simulando a captura da Camera pelo aplicativo do usuário.


curl -F 'image=@/Users/cleber/CDSOFT/projetos/ImageTextVoice/imagens/aprendizado.png' http://127.0.0.1:5000/image-read-text

