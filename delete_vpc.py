import boto3
client = boto3.client('ec2', region_name='us-east-1')

response = client.delete_vpc(
         VpcId = 'vpc-060b243e5c26ed442'
        )
