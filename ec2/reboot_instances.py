import boto3
from botocore.exceptions import ClientError


ec2 = boto3.resource('ec2')

def reboot(instance_id):
    instance = ec2.Instance(instance_id)
    try:
        instance.reboot(DryRun=True)
    except ClientError as e:
        print(e)
        if 'DryRunOperation' not in str(e):
            raise

    # Perform actual action 
    try:
        instance.reboot(DryRun=True)
        print(f'Instance {instance_id} rebooting...')
    except ClientError as e:
        print(e)