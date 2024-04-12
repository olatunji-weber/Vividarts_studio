from flask import Flask, render_template, request
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.environ.get("aws_key_id")
AWS_SECRET_ACCESS_KEY = os.environ.get("aws_secret_key")
S3_BUCKET_NAME = 'vividbucket-beanstalk2'

s3 = boto3.client(S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.upload_fileobj(file, 'vividbucket-beanstalk2', file.filename)
    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
