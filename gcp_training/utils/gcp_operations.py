from google.cloud import storage,bigquery
from io import BytesIO
import pandas as pd
import logging

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

def load_file_to_table(uri,stage_bucket):
    try:
        table_id='develop-488306.testing_datset.sample_data'
        stage_bucket=storage_client.get_bucket(stage_bucket)
        schema_path=stage_bucket.get_blob(f'schema/sample_data.json')
        config_xls=BytesIO(schema_path.download_as_string())
        schema=bq_client.schema_from_json(config_xls)

        job_config=bigquery.LoadJobConfig(
            schema=schema,
            skip_leading_rows=1,
            allow_jagged_rows=True,
            allow_quoted_newlines=True
        )
        load_job=bq_client.load_table_from_uri(uri,table_id,job_config=job_config)
        load_job.result()

        table=bq_client.get_table(table_id)
        logging.info(f"loaded {str(load_job.output_rows)} rows to {table_id}.")


    except Exception as e:
        print(e)