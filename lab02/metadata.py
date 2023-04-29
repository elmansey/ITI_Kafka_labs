import boto3
import json
import csv
# Create a client for the SQS service
sqs_client = boto3.client('sqs')
s3 = boto3.resource('s3')

# Set the name of the SQS queue to pull messages from
queue_name = 'secondqueue'

# Get the URL of the queue
queue_url = sqs_client.get_queue_url(QueueName=queue_name)['QueueUrl']

# Continuously poll the queue for new messages
while True:
    # Receive up to 10 messages at a time
    response = sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
    
    # Check if there are any messages to process
    if 'Messages' in response:
        # Process each message
        for message in response['Messages']:
            # Print the message body
            Message = json.loads(json.loads(message['Body'])['Message'])
            objMetaData = json.dumps(Message['Records'][0]['s3']['object'])
            bucket_name = 'testbucketfor-sns-sqs'

            with open('metadata.csv', 'a') as f:
                f.write(objMetaData + '\n')





            # Delete the message from the queue
            sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])



