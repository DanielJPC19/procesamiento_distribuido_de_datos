import requests
import math
from google.cloud import storage
from collections import defaultdict
from collections import Counter
import os
import re

# =====================================================================

# Configuración
CREDENTIALS_FILE = "dev-prodatos-lab4-771a915d2031.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_FILE

PROJECT_ID = "dev-prodatos-lab4"
BUCKET_NAME = "dev-lab4-tfidfdata"

WORKERS = [
    "https://tfidf-worker-408027501180.us-central1.run.app/map",
    "https://tfidf-worker2-408027501180.us-central1.run.app/map",
]

FILES = [
    "marie_curie.txt",
    "historia_quimica.txt",
    "fisica_moderna.txt",
    "biografia_cientificos.txt",
]

STOPWORDS = {
    "a", "al", "ante", "bajo", "con", "contra", "de", "del", "desde",
    "durante", "en", "entre", "hacia", "hasta", "mediante", "para",
    "por", "según", "sin", "sobre", "tras", "el", "la", "lo", "los",
    "las", "un", "una", "uno", "unos", "unas", "y", "e", "ni", "o",
    "u", "pero", "mas", "sino", "que", "como", "es", "fue", "ser",
    "son", "está", "están", "ha", "han", "se", "su", "sus", "este",
    "esta", "estos", "estas", "ese", "esa", "esos", "esas", "aquel",
    "aquella", "aquellos", "aquellas", "no", "si", "sí", "muy", "más",
    "ya", "también", "bien", "así", "donde", "cuando", "todo", "todos",
    "toda", "todas", "otro", "otra", "otros", "otras", "me", "te",
    "le", "nos", "les", "mi", "tu", "yo", "él", "ella", "ellos",
    "ellas", "nosotros", "cada", "cual", "quien",
}

# =====================================================================
def download_file(file="marie_curie.txt"):
    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(file)
    content = blob.download_as_text(encoding="utf-8")
    return content

def map(texts):
    # Para este enfoque separaremos los documentos entre los workers, no el contenido de estos
    responses = []
    number_assigned_files = {}
    docs_per_worker = len(FILES) // len(WORKERS)

    for i, worker_url in enumerate(WORKERS):
        number_assigned_files[worker_url] = FILES[i * docs_per_worker : (i + 1) * docs_per_worker]
        
        for document in number_assigned_files[worker_url]:
            payload = {
                "doc_id": document,
                "text": texts[document],
            }

            response = requests.post(worker_url, json=payload)
            if response.status_code == 200:
                data = response.json()
                responses.extend(data)

    return responses

def reduce(results):
    N = len(FILES)  # Número total de documentos
    # Primero calculamos el TF

    tf_list_visited = {}
    for record in results:
        doc_id = record["doc_id"]
        word = record["word"]
        count = record["count"]
        total_terms = record["total_terms"]

        if doc_id not in tf_list_visited:
            tf_list_visited[doc_id] = {}
        
        # Calculamos el TF para cada palabra en su respectivo documento
        tf = count / total_terms
        tf_list_visited[doc_id][word] = tf

    df = {}
    for doc_id, words in tf_list_visited.items():
        for word in words:
            if word not in df:
                df[word] = 0
            df[word] += 1

    idf = {}
    for word, count in df.items():
        idf[word] = math.log(N / count)

    tfidf = {}
    for doc_id, words in tf_list_visited.items():
        tfidf[doc_id] = {}
        for word, tf in words.items():
            tfidf[doc_id][word] = tf * idf[word]

    return tfidf

def preprocess_query(query):
    query = query.lower()
    words = query.split()
    return [word for word in words if word not in STOPWORDS]

def calculate_score(query_words, tfidf):
    scores = {}
    for doc_id, word_scores in tfidf.items():
        score = sum(word_scores.get(word, 0) for word in query_words)
        scores[doc_id] = score
    return scores

def main():
    print("Descargando documentos...")
    texts = {file: download_file(file) for file in FILES}

    print("Fase MAP...")
    # Para este enfoque separaremos los documentos entre los workers, no el contenido de estos
    results = map(texts)

    print("Fase REDUCE...")
    tfidf = reduce(results)

    query = input("\nIngrese términos de búsqueda: ")
    query_words = preprocess_query(query)
    scores = calculate_score(query_words, tfidf)

    print("\n===== Resultados =====")
    rank = 1
    for doc_id, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        if score > 0:
            print(f"{rank}. {doc_id} - Score: {score:.4f}")
        rank += 1

if __name__ == "__main__":
    main()