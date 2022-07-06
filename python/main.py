from flask import Flask,send_file
import boto3
import botocore
app = Flask(__name__)
@app.route('/<string:fname>/')
def gets3file(fname):
    s3_client =boto3.client('s3')
    s3 = boto3.resource('s3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
    bucket = s3.Bucket('dcdevopstask')
    dfile = None
    for obj in bucket.objects.all():
        if fname in obj.key:
            dfile = obj.key
        elif fname == obj.key:
            dfile = obj.key
    if dfile is None:
       return "no luck finding "+fname
    try:
        s3.Object('dcdevopstask', dfile).download_file('/tmp/'+fname)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return "no luck finding "+fname
    else:
        return send_file("/tmp/"+fname, as_attachment=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
