from flask import Flask, jsonify
from flask_cors import CORS  # Thêm thư viện CORS

app = Flask(__name__)
CORS(app)  # Bật CORS cho toàn bộ ứng dụng


@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask API!", "status": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
