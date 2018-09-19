from flask import Response
from flask import jsonify
from flask_restful import Resource

class Health(Resource):
    """Provide a status check and details about what model versions are in memory"""
    def __init__(self, models_collection):
        self.models_collection = models_collection
    
    def get(self):
        status = "healthy"
        resp = {
            "status": status,
            "num_models": len(self.models_collection.keys())
        }
        return jsonify(resp)
