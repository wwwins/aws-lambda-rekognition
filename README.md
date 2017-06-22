# aws-lambda-rekognition
When a user uploads a photo to a S3 bucket, aws invoke lambda function and uses rekognition APIs to detect faces.

## Setting
### Code
see lambda_function.py

### Configuration
Lambda entry point "lambda_handler"

Handler: lambda_function.lambda_handler

Permissions

Role: Choose an existing Role

### Trigger
S3 bucket-test images folder

arn:aws:s3:::bucket-test

Event type: ObjectCreated

## Log
check CloudWatch -> Logs

## Demo
```
aws s3 cp wonderwoman.jpg s3://bucket-test/images/ww.jpg
aws s3 cp wonderwoman.jpg s3://bucket-test/images/ww.jpg --profile default
python s3upload.py -b bucket -f images -i ww.jpg
```
