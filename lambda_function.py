# -*- coding: utf-8 -*-
from __future__ import print_function

import boto3
import json
import urllib
import logging

print('Loading function')

rekognition = boto3.client('rekognition')

# --------------- Helper Functions to call Rekognition APIs ------------------

def detect_faces(bucket, key):
    response = rekognition.detect_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}}, Attributes=['ALL'])
    return response

def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response

def index_faces(bucket, key):
    response = rekognition.index_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}}, CollectionId="BLUEPRINT_COLLECTION")
    return response

# --------------- Main handler ------------------

def lambda_handler(event, context):
    # setup logger
    logger= logging.getLogger()
    logger.setLevel(logging.INFO)
    # logger.debug('this is debug message')
    # logger.error('this is error message')
    # logger.critical('中英文測試')

    '''
    Demonstrates S3 trigger that uses
    Rekognition APIs to detect faces, labels and index faces in S3 Object.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    print("bucket:"+bucket)
    print("key:"+key)
    try:
        # Calls rekognition DetectFaces API to detect faces in S3 object
        response = detect_faces(bucket, key)

        # Calls rekognition DetectLabels API to detect labels in S3 object
        #response = detect_labels(bucket, key)

        # Calls rekognition IndexFaces API to detect faces in S3 object and index faces into specified collection
        #response = index_faces(bucket, key)

        # Print response to console.
        print(response)

        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e
