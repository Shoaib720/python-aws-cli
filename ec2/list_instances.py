import boto3
from tabulate import tabulate

ec2 = boto3.resource('ec2')

def list_instances():
    response = ec2.instances.all()
    instances = []
    for instance in response:
        instance_data = {
            "id": instance.id,
            "instance_type": instance.instance_type,
            "private_ip_address": instance.private_ip_address,
            "public_ip_address": instance.public_ip_address,
            "state": instance.state["Name"]
        }
        instances.append(instance_data)
    headers = instances[0].keys()
    rows = [instance.values() for instance in instances]
    print(tabulate(rows, headers, tablefmt='grid'))