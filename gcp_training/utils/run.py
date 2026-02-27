from google.cloud import storage,bigquery
from utils.gcp_operations import move_file
def run(envelope):
    input_bucket=envelope['test-bucket']
    output_bucket=envelope['stage-bucket']
    blob_name=envelope['file_name']
    move_file(input_bucket,output_bucket,blob_name)





