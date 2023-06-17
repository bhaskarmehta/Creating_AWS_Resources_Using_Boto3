def create_subnet():
  #open file2 in reading mode
  file2 = open('vpc_id.txt','r')

  #print the file2 content
  vpcId=file2.read()
  print(vpcId)

  import boto3
  client = boto3.client('ec2', region_name="us-east-1")
  response = client.create_subnet(
    CidrBlock='10.0.1.0/24',
    
    AvailabilityZone='us-east-1a',
    VpcId=vpcId
            )
  return response['Subnet']['SubnetId']

subnet_id=create_subnet()
with open('subnet_id.txt', 'w') as file:
        file.write(subnet_id)

