from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io
import voice as voice
from retornoapi import RetornoApi
import json

app = Flask(__name__)

@app.route('/image-read-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem foi fornecida'}), 400
    
    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'Nenhuma imagem selecionada'}), 400
    
    # Lê a imagem e converte para formato PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # Extrai o texto da imagem usando pytesseract e envia para a classe audio ler
    try:
        textFromImage = pytesseract.image_to_string(image)
        voice.cria_audio(textFromImage)
        # TODO demais funcoes Classe de banco de dados, persistir audio, catalogar texto.
        retorno = RetornoApi(textFromImage, None)
        return json.dumps(retorno.__dict__) , 200
    except AssertionError as error:
        return jsonify({'error': 'Nenhum texto para processar'}), 400

if __name__ == '__main__':
    app.run(debug=True)
