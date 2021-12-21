import boto3


access_id_key = "ASIAWTQ2NIW57NQOSBUM"
secret_access_key = "rcmiIg/nBKI/P574YF/tjz2P2b2j4AP5DDmpp4BO"
session_token_key = "FwoGZXIvYXdzEKr//////////wEaDM8dXbrKwomP5FS0hyLLAc18S0oQIsUS7OBmS9TzV281pcKaOYf1kEc2J+G6ICmZLuQj4IhcI1p9NyQngSF2CFq+JIQjqdhZ6X9m2mvIE9ZhQriDIwx1R7SmPwq22IeBF7+tBKGuP7Nden2IrwSVYK8PCIcxwgw4xt2whP63jCISbQ0QgF6apt6Zlr2rW5dbg0CEiQKrJGl8SnewtIU2lcpK9seiPnYTCE2Yl0BMev94JDy8M8nDUmgy3C4Tk0G7r7tPWQTdAbPT7J8P0CgIlOh6QZvOsmEOx1QSKO+LqIoGMi0VtX3Bi6nhDSZoDZmTgC6HTAXznYNV+t07TXfFQSCL8ID/s6hLRUCNZuMXCmA="


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
    UserData=open("C:/Users/bhara/Downloads/script (1).sh").read(),
)


print(instances)


instance = instances[0]
instance.wait_until_running()
instance.load()

print(instance.public_dns_name)