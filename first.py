import boto3

# Initialize the EC2 resource
ec2 = boto3.resource('ec2')

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0f403e3180720dd7e',  # Specify the Amazon Machine Image (AMI) ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Choose the instance type (e.g., t2.micro)
)

# Print the instance ID
print(f"Instance ID: {instance[0].id}")
#print(f"Instance ID: {instance[0].id}")
