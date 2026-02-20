# Step by step

1. Create the Google Bucket

```bash
gsutil mb -l us-central1 gs://lab3-mapreduce-flask
```

2. Create the local file

```bash
echo "hola mundo mapreduce flask python" > archivo.txt
```

3. Upload the file to the Bucket

```bash
gsutil cp archivo.txt gs://lab3-mapreduce-flask/
```

4. Create firewall rule

```bash
gcloud compute firewall-rules create allow-flask \
 --allow tcp:5000 \
 --source-ranges=10.128.0.0/24 \
 --description="Allow internal Flask traffic"
```