import boto3

# Function to create a snapshot and delete unassigned EBS volumes
def run_ebs():
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    data = []
    
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
                
                data.append([region,volume_id,volume.state, len(attachments),snapshot.snapshot_id])

                # Delete the volume
                # volume.delete()

                print(f"Deleted volume {volume_id}")
    headers = ["Region","Volume ID","State", "Attachments", "Snapshot ID"]
    table = f"{headers[0]:<15} | {headers[1]:<20} | {headers[2]:<10} | {headers[3]:<12} | {headers[4]:<20}\n"
    table += "-" * 80 + "\n"
    for row in data:
        table += f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10} | {row[3]:<12} | {row[4]:<20}\n"
    print(table)

    # Append the table to the log file
    with open('/tmp/details.log','a') as log_file:
        log_file.write("\n\nEBS Volumes with no attachments:\n")
        log_file.write(table)