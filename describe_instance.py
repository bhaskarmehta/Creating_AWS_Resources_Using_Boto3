import boto3
client = boto3.client('ec2', region_name='us-east-1')
response = client.describe_instances(
    InstanceIds=[
        'i-07b997ced770a7ed3'
    ]
        )


print(response['Reservations'][0]['Instances'][0]['Tags'])
