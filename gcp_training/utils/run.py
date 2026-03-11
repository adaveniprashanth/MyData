from google.cloud import storage,bigquery
from utils.gcp_operations import move_file,read_file,load_file_to_table,get_secret_value
def run(envelope):
    try:
        input_bucket=envelope['test-bucket']
        output_bucket=envelope['stage-bucket']
        filename=envelope['file_name']
        stage_bucket=envelope['stage-bucket']
        secret_name=envelope['secret-name']
        project=envelope['project']

        # move_file(input_bucket,output_bucket,filename)
        # read_file(input_bucket,filename)

        status=load_file_to_table(filename,stage_bucket,input_bucket)

        # status=get_secret_value(project,secret_name)
    except Exception as e:
        print(e)





