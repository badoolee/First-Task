from flask import Flask, jsonify, request
from datetime import datetime


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        # Get query parameters
        slack_name = request.args.get("slack_name")
        track = request.args.get('backend')

        # Object Variable
        track = "backend"

        # Get the current day of the week
        current_day = datetime.utcnow().strftime('%A')

        # Get the current UTC time with validation of +/- 2 hours
        current_utc_time = datetime.utcnow()
        current_utc_time_str = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Define GitHub URLs
        github_file_url = "https://github.com/badoolee/First-Task/blob/master/task.py"
        github_repo_url = "https://github.com/badoolee/First-Task"

        # Create the JSON response
        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_utc_time_str,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)