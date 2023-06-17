import boto3
client = boto3.client('ec2', region_name = "us-east-1")
response = client.terminate_instances(
    InstanceIds=[
        'i-0295b1bd749de7b9c',
    ]
)
