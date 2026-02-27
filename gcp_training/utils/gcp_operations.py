from google.cloud import storage,bigquery


def move_file(input_bucket,output_bucket,blob_name):
    storage_client=storage.Client()
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
