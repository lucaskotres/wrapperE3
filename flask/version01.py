from flask import Flask
from flask_restful import Resource, Api
from E3DataAccess import e3comm
import pythoncom



app = Flask(__name__)
api = Api(app)

class GetE3Tag(Resource):


    def get(self):
        pythoncom.CoInitialize()
        e3 = e3comm()
        tagpath = "Dados.TagInterno1"
        temp = e3.getValue(e3path=tagpath)


        return {'PathName':'Dados.TagInterno1',
                'Quality':str(temp[2]),
                'TimeStamp':str(temp[1]),
                'Value':temp[3]}

api.add_resource(GetE3Tag, '/')

if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0')