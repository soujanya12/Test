import boto3
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2', region_name="us-east-1")
def lambda_handler(event, context):
    stopped_ec2 = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    List = ''
    for instance in stopped_ec2:
        List += instance.id + '\r\n'
    s3.Bucket('soujanyatesting').put_object(Key='lambda-stopped-instances.txt', Body=List)
    return "Success"

