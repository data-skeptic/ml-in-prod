from flask import Response
from flask import jsonify
from flask_restful import Resource
import json

def get_header():

    f = open('api/header.htm', 'r')
    s = f.read()
    f.close()
    return s


def get_footer():
    f = open('api/footer.htm', 'r')
    s = f.read()
    f.close()
    return s


class Dashboard(Resource):
    """Provide a simple HTML user interface"""
    def __init__(self, models_collection):
        self.models_collection = models_collection
    
    def get(self):
        inner = "Available models: " + ",".join(self.models_collection.keys())
        body = get_header() + inner + get_footer()
        return Response(body, status=200, mimetype='text/html')


