gcloud config set project livelucky
docker build -t gcr.io/livelucky/idx-server .
docker push gcr.io/livelucky/idx-server
gcloud run deploy my-python-web-server --image gcr.io/livelucky/idx-server --platform managed --region us-central1
