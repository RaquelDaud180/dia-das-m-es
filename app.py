from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Lista de fotos com mensagens (pode ser modificada ou gerada dinamicamente)
fotos = [
    {"nome": "foto1.png", "mensagem": "Mãe, você é meu maior exemplo de amor e força! Feliz Dia das Mães!"},
    {"nome": "foto2.png", "mensagem": "Te amo mais do que as palavras podem dizer, minha rainha!"},
    {"nome": "foto3.png", "mensagem": "Obrigada por tudo, mãe! Você é meu porto seguro."},
    {"nome": "foto4.png", "mensagem": "Seu sorriso ilumina minha vida. Te amo!"},
    {"nome": "foto5.png", "mensagem": "Você é a melhor mãe do mundo!"},
    {"nome": "foto6.png", "mensagem": "Sua força me inspira todos os dias."},
    {"nome": "foto7.png", "mensagem": "Gratidão por seu amor incondicional."},
    {"nome": "foto8.png", "mensagem": "Você é meu anjo protetor!"},
    {"nome": "foto9.png", "mensagem": "Te amo para sempre, mãe!"},
    {"nome": "foto10.png", "mensagem": "Sua presença faz tudo melhor."},
    {"nome": "foto11.png", "mensagem": "Você é meu maior tesouro."},
    {"nome": "foto12.png", "mensagem": "Obrigada por ser tão especial."},
    {"nome": "foto13.png", "mensagem": "Seu carinho é meu refúgio."},
    {"nome": "foto14.png", "mensagem": "Você é simplesmente incrível!"},
    {"nome": "foto15.png", "mensagem": "Te amo mais a cada dia."},
    {"nome": "foto16.png", "mensagem": "Sua luz guia meu caminho."},
    {"nome": "foto17.png", "mensagem": "Feliz Dia das Mães, minha heroína!"},
    {"nome": "foto18.png", "mensagem": "Você é meu maior apoio!"},
]

# Rota para servir o index.html
@app.route('/')
def serve_index():
    return render_template('index.html', fotos=fotos)

# Rota para servir arquivos estáticos (imagens)
@app.route('/imagens/<path:path>')
def serve_static(path):
    return send_from_directory('imagens', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.py
    