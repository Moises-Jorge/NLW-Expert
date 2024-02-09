from flask import Flask, request, jsonify
from barcode import Code128 # para criar o codigo de barra
from barcode.writer import ImageWriter # para criar a imagem do codigo de barra

app = Flask(__name__) #Criando o Servidor python com o Flask

@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    tag = Code128(product_code, writer=ImageWriter()) # Codificando o valor recebido da request e criando a imagem do seu codigo
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jsonify({ "tag path": path_from_tag})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
