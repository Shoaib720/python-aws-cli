import boto3
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

def terminate_instance(instance_id):
    instance = ec2.Instance(instance_id)
    try:
        instance.terminate(DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
        
    try:
        instance.terminate(DryRun=False)
        print(f"Terminating instances... with ids {instance_id}")
    except ClientError as e:
        print(e)