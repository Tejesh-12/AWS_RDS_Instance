import boto3


# aws configuration
access_id_key = ""
secret_access_key = ""
session_token_key = ""

rdsClient = boto3.client(
    "rds",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

response = rdsClient.create_db_instance(
    DBName="Tejesh",
    DBInstanceIdentifier="Tejesh",
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    Engine="MySQL",
    MasterUsername="",
    MasterUserPassword="",
    PubliclyAccessible=True,
)
