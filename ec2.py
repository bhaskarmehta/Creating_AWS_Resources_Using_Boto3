import boto3

ec2 = boto3.client('ec2', region_name = "us-east-1")
instance = ec2.run_instances(
      ImageId = "ami-053b0d53c279acc90",
      InstanceType = 't2.micro',
      KeyName = "nvkey",
      MaxCount = 1,
      MinCount = 1
        )

