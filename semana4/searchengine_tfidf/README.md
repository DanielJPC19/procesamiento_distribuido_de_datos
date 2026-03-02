# Lab 4 - Week 4

## Student Information

**Name:** Daniel José Plazas Cortés

**Student Code:** A00400085

## `.env` Information

```
CREDENTIALS_FILE = "dev-prodatos-lab4-771a915d2031.json"
PROJECT_ID = "dev-prodatos-lab4"
BUCKET_NAME = "dev-lab4-tfidfdata"
WORKER1 = "https://tfidf-worker-408027501180.us-central1.run.app/map"
WORKER2 = "https://tfidf-worker2-408027501180.us-central1.run.app/map"
```

## Indications

First, create your own virtual environment and activate it, you can use the following prompt:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

Also, remember to create a `.env` file in the `searchengine_tfidf` directory with the content provided above and to download the json with the Credentials.

Finally, run the master script to execute the search engine:
```bash
python master.py
py master.py  # Windows or specific Python version
```