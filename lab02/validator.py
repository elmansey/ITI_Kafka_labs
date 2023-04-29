import boto3
import json
import csv
# Create a client for the SQS service
sqs_client = boto3.client('sqs')
s3 = boto3.resource('s3')

# Set the name of the SQS queue to pull messages from
queue_name = 'firstqueue'

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
            key = Message['Records'][0]['s3']['object']['key']
            bucket_name = 'testbucketfor-sns-sqs'
            fileName = key.split('/')[-1]
            s3.Bucket(bucket_name).download_file(key, f'{fileName}')
            with open(f'{fileName}', 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                rows=[]
                for row in reader:
                    rows.append(row)

            with open(f'{fileName}', 'w') as csv_file:
                for item in rows:
                    for elm in item: 
                        csv_file.write(elm + '\n')



            # upload file 
            file_name = f'after/{fileName}'
            boto3.client('s3').upload_file(f'./{fileName}', bucket_name, file_name)

            # Delete the message from the queue
            sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])



