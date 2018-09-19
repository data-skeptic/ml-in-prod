from flask import Response
from flask import jsonify
from flask_restful import Resource, request
import pandas as pd

class Predict(Resource):
    """Score an Opportunity"""
    def __init__(self, models_collection):
        self.models_collection = models_collection
    
    def post(self, model_id):
        raw_input = dict(request.form)
        features = {}
        for datum in raw_input:
            features[datum] = raw_input[datum][0]
        resp = {"model_id": model_id, "features": features, "status": 200, "msg": "", "prediction": -1}
        model = self.models_collection[model_id]
        if model is None:
            sc = 400
            resp['msg'] = 'Model not found'
            resp['status'] = sc
            response = jsonify(message=resp)
            response.status_code = 500
            return response
        else:
            results = model.predict(pd.DataFrame([features]))
            prediction = results[0]
            resp['prediction'] = str(prediction)
            print(resp)
            return jsonify(resp)
