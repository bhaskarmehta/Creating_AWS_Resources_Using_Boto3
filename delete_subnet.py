import boto3

client = boto3.client('ec2', region_name='us-east-1')
response = client.delete_subnet(
         SubnetId = 'subnet-0871161ee13702414'
        )
