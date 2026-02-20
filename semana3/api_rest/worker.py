from flask import Flask, jsonify, request
from collections import Counter

app = Flask(__name__)

@app.route('/map', methods=['POST'])
def map_task():
    text = request.json['data']
    words = text.lower().split()
    counts = Counter(words)
    return jsonify(counts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)