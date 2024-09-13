# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


# Define a route for the API
@app.route('/api/send_data', methods=['POST'])
def send_data():
    data = request.json
    # Here you can process the data and send it as needed (e.g., to a Telegram Bot)

    # For example, just echo the data back
    response = {
        "message": "Data received successfully",
        "data": data
    }
    return jsonify(response), 200


# Health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
