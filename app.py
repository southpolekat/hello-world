import os
from flask import Flask, send_file
from google.cloud import storage

app = Flask(__name__)

# Set up Google Cloud Storage client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./livelucky-3c45a0fb85db.json"
storage_client = storage.Client()

@app.route('/')
def hello_world():
    return 'Hello, World! This is my Python web server deployed on Cloud Run.'

@app.route('/read_file/<bucket>/<file_path>')
def read_file(bucket, file_path):
    # Get bucket and file path from URL
    bucket = storage_client.bucket(bucket)
    blob = bucket.blob(file_path)
    
    # Download file to a temporary location
    temp_file = f'/tmp/{file_path}'
    blob.download_to_filename(temp_file)
    
    # Return the file to the client
    return send_file(temp_file)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
