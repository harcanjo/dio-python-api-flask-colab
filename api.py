# Importe os módulos necessários
from flask import Flask, jsonify

# Crie uma instância do Flask
app = Flask(__name__)

# Defina a rota /index que será o seu endpoint
@app.route('/index')
def index():
    # Aqui você deve ler a planilha de dados no formato JSON
    # e transformá-la em um objeto Python (por exemplo, uma lista de dicionários)
    
    # Exemplo de leitura de uma planilha JSON fictícia
    data = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 30},
        {"nome": "Pedro", "idade": 35}
    ]
    
    # Retorne a planilha de dados como uma resposta JSON
    return jsonify(data)

# Inicie o servidor Flask
if __name__ == '__main__':
    app.run()


# Para executar:
# pip install flask

# Para executar o script api.py
# Acesse o endpoint http://localhost:5000/index em seu navegador para obter a planilha de dados JSON (substitua localhost pelo IP ou nome de domínio do seu servidor COLAB, se necessário).