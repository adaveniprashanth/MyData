import boto3
import uuid
import boto3
import botocore

# for configuration reference --> https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration
# for reference --> https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/iam-example-managing-access-keys.html
# Let's use Amazon S3
if 1:
    # list all buckets
    if 0:  #working fine
        # Create an S3 client
        s3 = boto3.client('s3')
        # Call S3 to list current buckets
        response = s3.list_buckets()
        # Get a list of all bucket names from the response
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print(buckets)
        for bucket in response['Buckets']:print(bucket['Name'])
    # create bucket
    if 0: #working fine
        s3 = boto3.client('s3')
        # s3.create_bucket(Bucket='my-buckets-123')
        s3.create_bucket(Bucket="".join(['1222', str(uuid.uuid4())]))
    # upload file into bucket
    if 0:
        s3 =boto3.client("s3")
        file_name='aws_training.py';bucket_name="abcdpj"
        s3.upload_file(file_name,bucket_name,file_name)
    #download file from bucket
    if 0:
        BUCKET_NAME = 'abcdpj' # replace with your bucket name
        KEY = 'aws_training.py' # replace with your object key
        s3 = boto3.resource('s3')
        try:
            s3.Bucket(BUCKET_NAME).download_file(KEY, 'aws_training1.py')
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise
if 1:
    #create user
    if 0:
        iam=boto3.client("iam")
        response=iam.create_user(UserName="admin1")
        print(response)
    #list users
    if 0:
        iam = boto3.client("iam")
        paginator=iam.get_paginator('list_users')
        for i in paginator.paginate():
            print(i)
    # update user
    if 0:
        iam=boto3.client("iam")
        iam.update_user(UserName="admin1",NewUserName="admin2")
    #delete user
    if 0:
        iam =boto3.client("iam")
        iam.delete_user(UserName="admin2")





if 0: #working fine
    s3_resource = boto3.resource('s3')
    # Print out bucket names
    for bucket in s3_resource.buckets.all():
        print(bucket.name)





if 0:
    # creating the bucket

    def create_bucket_name(bucket_name):
        return "".join([bucket_name,str(uuid.uuid4())])

    def create_bucket(bucket_prefix,s3_connection):
        session=boto3.session.Session()
        current_region=session.region_name #collcting the region name from aws config data
        bucket_name=create_bucket_name(bucket_prefix)
        bucket_response=s3_connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'})
        print(bucket_name,bucket_response)
        return bucket_name,bucket_response

    # creating bucket using client
    # client_bucket,client_response = create_bucket('clientbucket',s3_resource.meta.client)
    # print(client_response)
    # s3_resource.create_bucket(Bucket=create_bucket_name('firstbucket'),
    #                           CreateBucketConfiguration={
    #                               'LocationConstraint': 'us-east-1'})
    #
    # # Replace 'your_region' with the desired AWS region
    # region = 'your_region'
    # bucket_name = 'your_bucket_name'
    #
    # s3 = boto3.client('s3', region_name=region)
    #
    # # Create S3 bucket
    # s3.create_bucket(Bucket=bucket_name)