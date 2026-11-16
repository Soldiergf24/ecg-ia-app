from flask import Flask,  jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/diagnostico', methods=['GET'])
def diagnostico():
    resultado = {
        "bpm": 75, 
        "estado": "Normal", 
        ",ensaje": "Ritmo cardiaco normal. No se detectan arritmias"
    }
    return jsonify(resultado)
if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto,)

