from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class E3WebAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(E3WebAPI, '/api/<string:pathname>', endpoint = 'user')