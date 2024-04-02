from flask import Flask, render_template, request
import boto3
import os

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = 'vividart-studios-user-uploads'

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Upload file to S3
    s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)

    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
