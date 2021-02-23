import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket  = 's3-redis-kafka-go-demo'
    key = 'abc.json'
    #read file content as string
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())
    print('jsonObject',jsonObject)
    
    for i in jsonObject.values():
        print(i[0])
