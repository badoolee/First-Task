from flask import Flask, jsonify
from flask_restful import Api, Resource
from datetime import datetime
import pytz


app = Flask(__name__)

api = Api(app)


class slack_name(Resource):
    
    def get(self):
        name = "Sulaimon Taiwo Femi"
        current_day = "Sunday"
        current_time = datetime.now(pytz.utc)
        track = "backend"
        file = "https://github.com/badoolee/First-Task/blob/master/task.py"
        code = "https://github.com/badoolee/First-Task"
        status = 200

        return {
            "name": name,
            "current_day": current_day,
            "current_time": str(current_time),
            "track": track,
            "file": file,
            "code": code,
            "status": status
        }

class track(Resource):
    
    def get(self):
        name = "Sulaimon Taiwo Femi"
        current_day = "Sunday"
        current_time = datetime.now(pytz.utc)
        track = "backend"
        file = "file"
        code = "code"
        status = 200

        return {
            "name": name,
            "current_day": current_day,
            "current_time": str(current_time),
            "track": track,
            "file": file,
            "code": code,
            "status": status
        }
    
        

api.add_resource(slack_name, "/Sulaimon_Taiwo_Femi")
api.add_resource(track, "/backend")

if __name__ == "__main__":
    app.run(port=5000, debug=True)