import json

from google.cloud import storage,bigquery,secretmanager
from google.oauth2 import service_account
from io import BytesIO
import pandas as pd
import logging


# credentials = service_account.Credentials.from_service_account_file(
# r"C:\Users\Windows 10\Downloads\service_account_dredentials.json")

# storage_client=storage.Client(credentials=credentials, project="develop-488306")
storage_client=storage.Client()
bq_client=bigquery.Client()
def move_file(input_bucket,output_bucket,blob_name):
    source_bucket = storage_client.bucket(input_bucket)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(output_bucket)
    try:
        source_bucket.copy_blob(
            source_blob, destination_bucket,blob_name
        )
        # source_bucket.delete_blob(blob_name)
    except Exception as e:
        print(e)

def read_file(input_bucket,file_name):
    try:
        source_bucket=storage_client.get_bucket(input_bucket)
        input_blob=source_bucket.get_blob(file_name)
        temp_xls=BytesIO(input_blob.download_as_string())
        temp_df=pd.read_excel(temp_xls)
        print(temp_df.columns())


    except Exception as e:
        print(e)
def convert_excel_to_csv(input_bucket,file_name):
    input_bucket = storage_client.get_bucket(input_bucket)
    input_blob = input_bucket.get_blob(file_name)
    temp_xls = BytesIO(input_blob.download_as_string())
    temp_df = pd.read_excel(temp_xls)
    stg_file_name = f"{file_name.split('.')[0]}_stg.csv"
    csv_delimiter = ','
    input_bucket.blob(stg_file_name).upload_from_string(
        temp_df.to_csv(sep=csv_delimiter, header=False, index=False, quotechar='"', escapechar='"'), 'text/csv')
    return stg_file_name

def load_file_to_table(file_name,stage_bucket,input_bucket):
    try:
        table_id='develop-488306.testing_datset.sample_data'
        stage_bucket=storage_client.get_bucket(stage_bucket)
        csv_file_name = convert_excel_to_csv(input_bucket,file_name)
        source_bucket=storage_client.get_bucket(input_bucket)
        schema_path=stage_bucket.get_blob(f'schema/sample_data.json')
        config_xls=BytesIO(schema_path.download_as_string())
        schema=bq_client.schema_from_json(config_xls)

        job_config=bigquery.LoadJobConfig(
            schema=schema,
            skip_leading_rows=0,
            allow_jagged_rows=True,
            allow_quoted_newlines=True
        )
        uri=f"gs://{input_bucket}/{csv_file_name}"
        load_job=bq_client.load_table_from_uri(uri,table_id,job_config=job_config)
        load_job.result()

        source_bucket.delete_blob(csv_file_name)

        table=bq_client.get_table(table_id)
        logging.info(f"loaded {str(load_job.output_rows)} rows to {table_id}.")
        print((f"loaded {str(load_job.output_rows)} rows to {table_id}."))
        return "success"

    except Exception as e:
        print(e)

def get_secret_value(project,secret_id,version='latest'):
    try:
        client=secretmanager.SecretManagerServiceClient()
        name=f"projects/{project}/secrets/{secret_id}/versions/{version}"
        response=client.access_secret_version(name=name)
        payload=response.payload.data.decode('UTF-8')
        secret_data=json.loads(payload)
        password=secret_data['secret']
        print(password)
        return "success"
    except Exception as e:
        print(e)
