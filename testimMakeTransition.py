from flask import Flask, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Jira credentials
jira_email = os.getenv("JIRA_EMAIL")
jira_api_token = os.getenv("JIRA_API_TOKEN")
jira_base_url = "https://mauriceblackburn.atlassian.net"

app = Flask(__name__)

@app.route('/transition-issue', methods=['POST'])
def transition_issue():
    # Get data from the request
    data = request.json
    issue_key = data.get('issue_key')
    transition_id = data.get('transition_id')

    # Jira API endpoint for transitioning an issue
    url = f"{jira_base_url}/rest/api/2/issue/{issue_key}/transitions"

    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    # Data for the transition
    transition_data = {
        "transition": {
            "id": transition_id
        }
    }

    # Make the POST request to transition the issue
    response = requests.post(url, headers=headers, auth=(jira_email, jira_api_token), data=json.dumps(transition_data))

    # Check the response
    if response.status_code == 204:
        return jsonify({"message": "Issue transitioned successfully."}), 204
    else:
        return jsonify({"message": f"Failed to transition issue. Status code: {response.status_code}", "details": response.text}), response.status_code

if __name__ == '__main__':
    app.run(port=5000)

# curl -X POST http://localhost:5000/transition-issue \
#      -H "Content-Type: application/json" \
#      -d '{
#            "issue_key": "TLS-3622",
#            "transition_id": "10152"
#          }'
# curl -X POST http://localhost:5000/transition-issue \
#      -H "Content-Type: application/json" \
#      -d '{
#            "issue_key": "TLS-3622",
#            "transition_id": "10152"
#          }'