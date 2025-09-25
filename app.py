from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('3.249.94.36/health')
def health_check():
    return jsonify(status="ok"), 200

@app.route('3.249.94.36/data')
def get_data():
    return jsonify(message="Yo this is tesa")

@app.route('3.249.94.36/user')
def get_user():
    return jsonify(message="We are the best cloud engineers in the world")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
