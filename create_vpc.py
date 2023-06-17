def create_vpc():
  import boto3
  vpc =boto3.client('ec2', region_name="us-east-1")
  response = vpc.create_vpc(
    CidrBlock='10.0.0.0/16',
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags':[ {
                  'Key': 'Name',
                  'Value': 'myvpc'
                }]
            }]
        )
  return response['Vpc']['VpcId']


vpc_id=create_vpc()
with open('vpc_id.txt', 'w') as file:
        file.write(vpc_id)

