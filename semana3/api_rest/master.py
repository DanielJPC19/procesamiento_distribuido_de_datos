from flask import Flask, jsonify, request
import requests
from collections import Counter
from google.cloud import storage

app = Flask(__name__)

WORKERS = [
    "http://10.128.0.4:5000/map",
    "http://10.128.0.5:5000/map",   
]

def download_file():
    client = storage.Client()
    bucket = client.bucket('lab3-mapreduce-flask')
    blob = bucket.blob('archivo.txt')
    content = blob.download_as_text()
    return content

@app.route('/run', methods=['POST'])
def run_mapreduce():
    text = download_file()

    chunks = text.split('\n')
    size = len(chunks) // 3
    partitions = [
        "\n".join(chunks[:size]),
        "\n".join(chunks[size:2*size]),
        "\n".join(chunks[2*size:]),
    ]

    total_counts = Counter()
    for worker_url, part in zip(WORKERS, partitions):
        response = requests.post(worker_url, json={'data': part})
        partial_counts = Counter(response.json())
        total_counts.update(partial_counts)
    
    return jsonify(total_counts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)