import requests
import json
import datetime
from datetime import date
import pandas as pd
import numpy as np
import time
import csv
import os
from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file('path/to/file.json')

project_id = 'my-bq'
client = bigquery.Client(credentials=credentials, project=project_id)

QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)
rows = query_job.result()

for row in rows:
    print(row.name)


# if __name__ == '__main__':
#     print("edri")
