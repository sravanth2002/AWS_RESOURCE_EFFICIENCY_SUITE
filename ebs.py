import boto3

# Function to create a snapshot and delete unassigned EBS volumes
def run_ebs():
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])

        for volume in volumes:
            volume_id = volume.volume_id
            attachments = volume.attachments
            
            print(f"Region: {region}, VolumeId: {volume_id}, State: {volume.state}, Attachments: {len(attachments)}")
            
            if len(attachments) == 0 and volume.state == 'available':
                # Take a snapshot of the volume
                snapshot = volume.create_snapshot(Description=f"Snapshot of {volume_id} before deletion")
                print(f"Created snapshot {snapshot.snapshot_id} for volume {volume_id}")
                
                # Delete the volume
                volume.delete()
                print(f"Deleted volume {volume_id}")
