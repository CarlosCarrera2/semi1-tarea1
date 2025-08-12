from flask import Flask, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route('/check', methods=['GET'])
def check():
    return "OK", 200

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "Instancia": "Maquina 2 - Api 2",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo 4"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
