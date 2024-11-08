import boto3
from ec2_optimizer import run_ec2
from ebs import run_ebs
from constants import resource_list

def lambda_handler(event, context):
    if "EC2" in resource_list:
        run_ec2()
        print()
    if "EBS" in resource_list:
        run_ebs()
        print()
    return f"The following resources {resource_list} are optimized."
