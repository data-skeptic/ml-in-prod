import os
import ctypes
import boto3
import json
import random
import pandas as pd
from datetime import datetime
import pickle
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_boston

for d, _, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import numpy as np

s3_bucket = os.getenv('S3_BUCKET')

s3 = boto3.resource('s3')

def lambda_handler(event, context):
	print('========[START]========================================')
	print(event)

	print("--------[Configuration]--------------------------------")
	#
	# Not required for this demo, but here's a code example
	#
	#from influxdb import InfluxDBClient
	#influxdb_host = os.environ['host']
	#influxdb_database = os.environ['database']
	#influxdb_port = os.environ['port']
	#influxdb_user = os.environ['user']
	#influxdb_password = os.environ['password']
	#db_influx = InfluxDBClient(host=host, port=port, username=user, password=password, database=database, ssl=True)
	print("--------[Getting model]--------------------------------")
	bucket = event['bucket']
	s3key = event['s3key']
	observation = event['observation']
	fname = 'latest.pickle'
	s3.Bucket(bucket).download_file(s3key, fname)
	model = pickle.load(open(fname, 'rb'))
	obs = pd.DataFrame([observation])
	prediction = model.predict(obs)
	print("--------[Classification]-------------------------------")

	resp = {
		"label": prediction,
		"version": "v1.0.0"
	}
	print("--------[Persist result]-------------------------------")
	# Save here or let the caller handle it?
	return resp


test_obj = {'CRIM': 0.00632,
 'ZN': 18.0,
 'INDUS': 2.31,
 'CHAS': 0.0,
 'NOX': 0.538,
 'RM': 6.575,
 'AGE': 65.2,
 'DIS': 4.09,
 'RAD': 1.0,
 'TAX': 296.0,
 'PTRATIO': 15.3,
 'B': 396.9,
 'LSTAT': 4.98}

event = {"bucket": "ml-in-prod", "s3key": "models/latest.pickle", "observation": test_obj}

context = {}
result = lambda_handler(event, context)
print(result)
