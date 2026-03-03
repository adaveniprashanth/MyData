from google.cloud import storage,bigquery
from utils.gcp_operations import move_file,read_file,load_file_to_table
def run(envelope):
    try:
        input_bucket=envelope['test-bucket']
        output_bucket=envelope['stage-bucket']
        filename=envelope['file_name']
        stage_bucket=envelope['stage-bucket']

        # move_file(input_bucket,output_bucket,filename)
        # read_file(input_bucket,filename)
        uri=f"gs://us-test-bucket1/{filename}"
        load_file_to_table(uri,stage_bucket)
    except Exception as e:
        print(e)





