import os
import ctypes
import boto3
import json
import random
import pandas as pd
from datetime import datetime

for d, _, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import numpy as np

s3r = boto3.resource('s3')

def lambda_handler(event, context):
	print('========[START]========================================')
	print(event)

	print("--------[Configuration]--------------------------------")
	#
	# Not required for this demo, but here's a code example
	#
	#from influxdb import InfluxDBClient
	#influxdb_host = os.environ['influxdb_host']
	#influxdb_database = os.environ['influxdb_database']
	#influxdb_port = os.environ['influxdb_port']
	#influxdb_user = os.environ['influxdb_user']
	#influxdb_password = os.environ['influxdb_password']
	#db_influx = InfluxDBClient(host=influxdb_host, port=influxdb_port, username=influxdb_user, password=influxdb_password, database=influxdb_database, ssl=True)
	print("--------[Getting data]---------------------------------")
	bucket = event['bucket']
	s3key = event['s3key']	
	obj = s3r.Object(bucket, s3key)
	s = obj.get()['Body'].read().decode('utf-8') 
	resp = json.loads(s)
	print("--------[Classification]-------------------------------")

	resp = {
		"label": label,
		"version": "v1.0.0", 
		"bucket": bucket,
		"s3key": s3key
	}
	print("--------[Persist result]-------------------------------")
	# Save here or let the caller handle it?
	return resp


#s3key = 'stub/sample.vega'

event = {"bucket": "blah", "s3key": "test"}

context = {}
result = lambda_handler(event, context)
print(result)
