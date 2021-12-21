import boto3


access_id_key = ""
secret_access_key = ""
session_token_key = ""
ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

instances = ec2.create_instances(
    ImageId="ami-0c2b8ca1dad447f8a",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="Cs351-2021",
    SecurityGroupIds=["sg-00b8d4fc8d0362232"],
    UserData=open("C:/Users/tejes/Downloads/script.sh").read(),
)


print(instances)


instance = instances[0]
instance.wait_until_running()
instance.load()

print(instance.public_dns_name)
