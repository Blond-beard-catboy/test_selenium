from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify({"status": "success", "message": "Hello from API!"})

@app.route('/api/check/<int:value>')
def check_value(value):
    return jsonify({"is_even": value % 2 == 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
