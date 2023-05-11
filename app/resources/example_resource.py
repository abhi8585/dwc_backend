from flask_restful import Resource

class ExampleResource(Resource):
    def get(self):
        return {'message': 'GET request received'}

    def post(self):
        return {'message': 'POST request received'}
