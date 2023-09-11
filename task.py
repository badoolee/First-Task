from flask import Flask, jsonify
from flask_restful import Api, Resource
from datetime import datetime
import pytz


app = Flask(__name__)

api = Api(app)


class slack_name(Resource):
    
    def get(self):
        slack_name = "Sulaimon Taiwo Femi"
        utc_time = datetime.now(pytz.utc)
        track = "backend"
        github_file_url = "https://github.com/badoolee/First-Task/blob/master/task.py"
        github_repo_url = "https://github.com/badoolee/First-Task"
        current_day = "Sunday"
        status_code = 200

        return {
            "slack_name": slack_name,
            "utc_time": str(utc_time),
            "track": track,
            "github_file_repo": github_file_url,
            "github_repo_url": github_repo_url,
            "current_day": current_day,
            "status_code": status_code
        }
    

class track(Resource):
    
    def get(self):
        slack_name = "Sulaimon Taiwo Femi"
        utc_time = datetime.now(pytz.utc)
        track = "backend"
        github_file_url = "https://github.com/badoolee/First-Task/blob/master/task.py"
        github_repo_url = "https://github.com/badoolee/First-Task"
        current_day = "Sunday"
        status_code = 200

        return {
            "slack_name": slack_name,
            "utc_time": str(utc_time),
            "track": track,
            "github_file_repo": github_file_url,
            "github_repo_url": github_repo_url,
            "current_day": current_day,
            "status_code": status_code
        }

    
        

api.add_resource(slack_name, "/Sulaimon_Taiwo_Femi")
api.add_resource(track, "/backend")

if __name__ == "__main__":
    app.run(port=5000, debug=True)