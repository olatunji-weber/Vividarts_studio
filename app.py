from flask import Flask, render_template, request
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = 'vividart-studios-user-uploads'

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method =='POST':
        img = request.files['file']
        if img:
            filename = secure_filename(img.filename)
            img.save(filename)
            s3.upload_file(Bucket=S3_BUCKET_NAME, Filename=filename, Key=filename)
            msg = "File Uploaded Successfully"
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
