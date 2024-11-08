import boto3
from datetime import datetime, timedelta


# Get CPU and Network metrics for each instance
def get_metrics(instance_id, region):
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=24)
    
    # Fetch CPU Utilization
    cpu_response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )
    
    # Fetch Network In
    network_in_response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='NetworkIn',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Sum']
    )

    cpu_util = cpu_response['Datapoints'][0]['Average'] if cpu_response['Datapoints'] else None
    network_in = network_in_response['Datapoints'][0]['Sum'] if network_in_response['Datapoints'] else None

    return cpu_util, network_in
    
    
# def format_data(data):
#     headers = ["Instance ID", "Region", "CPUUtilization (%)", "Network In (bytes)"]
#     table = f"{' | '.join(headers)}\n" + "-" * 40 + "\n"
#     for row in data:
#         table += " | ".join(str(cell) for cell in row) + "\n"
#     return table
    
def run_ec2():
        # Initialize the list of regions to check
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    data = []
    # Iterate over each region and list running instances
    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                cpu_util, network_in = get_metrics(instance_id, region)
                
                data.append([instance_id,region,cpu_util,network_in])
                
                print(f"Instance ID: {instance_id}, Region: {region}")
                print(f"  CPU Utilization: {cpu_util}%")
                print(f"  Network In: {network_in} bytes")
                
                # Example condition to stop instance if CPU usage is low and network I/O is minimal
                if cpu_util is not None and cpu_util < 10 and network_in is not None and network_in < 1000000:
                    print(f"  Stopping instance {instance_id} due to low usage.")
                    # Uncomment below to stop the instance
                    ec2.stop_instances(InstanceIds=[instance_id])