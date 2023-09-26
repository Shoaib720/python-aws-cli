import boto3
import sys
from botocore.exceptions import ClientError


ec2 = boto3.resource('ec2')

def start(instance_id):
    instance = ec2.Instance(instance_id)
    try:
        instance.start(DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Perform actual action 
    try:
        instance.start(DryRun=False)
        print(f'Instance {instance_id} starting.')
    except ClientError as e:
        print(e)

def stop(instance_id):
    instance = ec2.Instance(instance_id)
    try:
        instance.stop(DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Perform actual action 
    try:
        instance.stop(DryRun=False)
        print(f'Instance {instance_id} stopping.')
    except ClientError as e:
        print(e)