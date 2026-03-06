import pandas as pd
from utils.run import run
import logging
from google.cloud import storage
import uuid

def main():
    print('flow is started')
    envelope={'project':'develop-488306',
              'test-bucket':'us-test-bucket1',
              'stage-bucket':'us-stage-bucket1',
              'file_name': 'sample_data.xlsx',
              'secret-name':'secret_manager_value'}
    run(envelope)

if __name__ == '__main__':
    PROJECT_SETTINGS= {
        'test-bucktet': 'us-test-bucket1'
    }
    main()