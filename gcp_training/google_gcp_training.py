import pandas as pd
from utils.run import run
import logging
from google.cloud import storage
import uuid

def main():
    print('flow is started')
    envelope={'test-bucket':'us-test-bucket1','file_name':'sample_data.xlsx','stage-bucket':'us-stage-bucket1'}
    run(envelope)

if __name__ == '__main__':
    PROJECT_SETTINGS= {
        'test-buckte': 'us-test-bucket1'
    }
    main()