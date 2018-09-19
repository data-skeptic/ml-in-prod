import os
import sys
import time
import json
import logging
import glob
import boto3
import pickle
from logging.handlers import TimedRotatingFileHandler
import threading
import schedule
from api.Predict import Predict
from api.Health import Health
from api.UI import Dashboard
from flask import Flask
from flask import Response
from flask import jsonify
from flask_restful import reqparse, Resource, Api, request
from flask import Markup

accountname = os.getenv('USER')
accountkey = os.getenv('PASSWORD')
aws_access_key = os.getenv('AWS_ACCESS_KEY')
aws_secret_key = os.getenv('AWS_SECRET_KEY')
s3_bucket = os.getenv('S3_BUCKET')        
env = os.getenv('MODE').lower()

s3_resource = boto3.resource('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
models_collection = {}

def worker():
    s = 60
    schedule.every(s).seconds.do(lambda: heartbeat(s3_resource, models_collection))
    while True:
        schedule.run_pending()
        time.sleep(s)

def heartbeat(s3_resource, models_collection):
    # TODO: Deep parse results and load many models
    model_id = 'latest'
    print("GOING TO LOAD " + model_id)
    fname = model_id + '.pickle'
    if not(os.path.exists(fname)):
        key = 'models/' + fname
        s3_resource.Bucket(s3_bucket).download_file(key, fname)
    model = pickle.load(open(fname, 'rb'))
    models_collection[model_id] = model
    # A nice place to do log rotation, save system telemetry, etc.
    print("Load complete!")

if __name__ == '__main__':
    print("-----[Loading Config]-------------------------------------------")
    if env == 'api':
        env = 'prod'
    app = Flask(__name__)
    api = Api(app)
    print("-----[Initialization]-------------------------------------------")
    heartbeat(s3_resource, models_collection)
    rck = {'models_collection': models_collection}
    api.add_resource(Dashboard, '/',                              resource_class_kwargs=rck)
    api.add_resource(Health,    '/api/health',                    resource_class_kwargs=rck)
    api.add_resource(Predict,   '/api/predict/<string:model_id>', resource_class_kwargs=rck)
    t = threading.Thread(target=worker)
    t.start()
    parser = reqparse.RequestParser()
    print("-----[Ready]----------------------------------------------------")
    app.run(host='0.0.0.0', debug=False, port=9988)
