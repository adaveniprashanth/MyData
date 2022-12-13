import boto3
import json
import sys
import string
import random

# access key ID --> AKIAXW2XUCTVON2CBKMC
# secret access key -->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
# Users with AWS Management Console access can sign-in at: https://530075358442.signin.aws.amazon.com/console
# dynamoDB guidance examples https://dynobase.dev/dynamodb-python-with-boto3/

print("hello world")
def generate_random_string(size):
    random_string = "".join(random.choice(string.ascii_lowercase) for i in range(size))
    return random_string

db = boto3.resource("dynamodb")  # connecting to dynamo DB
table = db.Table("employees")  # connecting to table

#put the data in the table
table.put_item(
    Item={
        "emp_id":2,
        'name':"ram",
        'age':23
    }
)
# getting the data from table
result =table.get_item(
    Key={
        "emp_id":2
    }
)

print(result)
print(result['Item'])
