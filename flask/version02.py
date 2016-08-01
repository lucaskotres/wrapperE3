from flask import Flask, request
from flask_restful import Resource, Api
from E3DataAccess import e3comm
import pythoncom
import datetime

#todo: melhorar parser de data
#todo: tratamento de erro
#todo: logs

app = Flask(__name__)
api = Api(app)

class E3Tag(Resource):


    def get(self,pathname):
        pythoncom.CoInitialize()
        e3 = e3comm()

        temp = e3.getValue(e3path=pathname)
        if temp == False:
            return 'Error! E3Server or pathname are unavailable',400

        return {'PathName':pathname,
                'Quality':str(temp[2]),
                'TimeStamp':str(temp[1]),
                'Value':temp[3]}


    def put(self,pathname):

        if request.json:
            data = request.json

            #convert string to timestamp
            timestamp = datetime.datetime.strptime(data.get("timestamp"),'%Y-%m-%d %H:%M:%S.%f')

            pythoncom.CoInitialize()
            e3 = e3comm()

            temp = e3.sendValue(e3path=pathname,Value=data.get("value"),Timestamp=timestamp,Quality=data.get("quality"))
            return pathname+' write!'
        else:
            return 'No json received!',400


api.add_resource(E3Tag, '/<string:pathname>')

if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0')