from flask import Flask
from flask_restful import Resource, Api
from E3DataAccess import e3comm

app = Flask(__name__)
api = Api(app)

class GetE3Tag(Resource):

    def get(self):
        e3 = e3comm()
        tagpath = "Dados.TagInterno1"
        temp = e3.getValue(e3path=tagpath)[3]

        return {'E3': tagpath +'Valor:'+temp}

api.add_resource(GetE3Tag, '/')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')