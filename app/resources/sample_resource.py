from flask_restful import Resource
# from app.app import bq_client
from app.config import bq_client

class SampleResource(Resource):
    def get(self):
        return {'data': 'rows'}


    def post(self):
        return {'message': 'POST request to sample received'}
