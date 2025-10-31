# pylint: disable=broad-exception-caught
"""
This moodule is meant for working with AWS services like S3
"""
from flask import Flask, render_template
import boto3

app = Flask(__name__)

# Initialize the S3 client
s3 = boto3.client('s3')

# Your S3 bucket name
BUCKET_NAME = 'your-s3-bucket-name'

@app.route('/')
def list_s3_objects():
      """
    List objects from a given bucket
    """
    try:
        # Get the list of objects in the S3 bucket
        objects = s3.list_objects_v2(Bucket=BUCKET_NAME)
        # Get the object keys (file names)
        files = [obj['Key'] for obj in objects.get('Contents', [])]
    except Exception as e:
        return f"Error: {str(e)}"

    # Pass the list of files to the HTML template for rendering
    return render_template('list_s3.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
