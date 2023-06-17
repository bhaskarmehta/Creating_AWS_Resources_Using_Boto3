import boto3
response = client.stop_instances(
    InstanceIds=[
        "i-0295b1bd749de7b9c"
    ]
)
