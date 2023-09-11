from flask import Flask, jsonify
from flask_restful import Api, Resource
from datetime import datetime
import pytz


app = Flask(__name__)

api = Api(app)


class slack_name(Resource):
    name = "Sulaimon Taiwo Femi"
    current_day = "Sunday"
    current_time = datetime.now(pytz.utc)
    track = "backend"
    file = "https://github.com/badoolee/First-Task/blob/master/task.py"
    code = "https://github.com/badoolee/First-Task"
    status = 200

    def __init__(self, name=name, current_day=current_day, 
                 current_time=current_time, track=track, file=file, code=code, status=status):
        self.name = name
        self.current_day = current_day
        self.current_time = current_time
        self.track = track
        self.file = file
        self.code = code
        self.status = status
    
    def get(self):
        
        return {
            "name": self.name,
            "current_day": self.current_day,
            "current_time": str(self.current_time),
            "track": self.track,
            "file": self.file,
            "code": self.code,
            "status": self.status
        }

class track(Resource):
    name = "Sulaimon Taiwo Femi"
    current_day = "Sunday"
    current_time = datetime.now(pytz.utc)
    track = "backend"
    file = "file"
    code = "code"
    status = 200

    def __init__(self, name=name, current_day=current_day, 
                 current_time=current_time, track=track, file=file, code=code, status=status):
        self.name = name
        self.current_day = current_day
        self.current_time = current_time
        self.track = track
        self.file = file
        self.code = code
        self.status = status
    
    def get(self):
        
        return {
            "name": self.name,
            "current_day": self.current_day,
            "current_time": str(self.current_time),
            "track": self.track,
            "file": self.file,
            "code": self.code,
            "status": self.status
        }
    
        

api.add_resource(slack_name, "/Sulaimon_Taiwo_Femi")
api.add_resource(track, "/backend")

if __name__ == "__main__":
    app.run(port=5000, debug=True)