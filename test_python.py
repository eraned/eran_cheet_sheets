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


credentials = service_account.Credentials.from_service_account_file(
    'path/to/file.json')

project_id = 'my-bq'
dataset_id = ''
client = bigquery.Client(credentials=credentials, project=project_id)
dataset_ref = client.dataset(dataset_id)

sql = (
    """SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` 
    WHERE state = "TX" 
    LIMIT 100""")


def query_table(sql):
    query_job = client.query(sql)
    results = query_job.result()

    for row in results:
        print(row.name)


def gcp_2_df(sql):
    query_job = client.query(sql)
    results = query_job._result()
    return results.to_dataframe()


if __name__ == '__main__':
    print("edri")
