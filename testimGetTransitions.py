# filepath: /c:/Users/jsteenkamp/Projects/testim/testimGetTransitions.py
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests
import json


# Load environment variables from .env file
load_dotenv()

# Jira credentials
jira_email = os.getenv("JIRA_EMAIL")
jira_api_token = os.getenv("JIRA_API_TOKEN")
jira_base_url = "https://mauriceblackburn.atlassian.net"

app = Flask(__name__)

@app.route('/get-transitions', methods=['POST'])
def get_transitions():
    # Get data from the request
    data = request.json
    issue_key = data.get('issue_key')
    
    
    # Jira API endpoint for getting available transitions
    url = f"{jira_base_url}/rest/api/2/issue/{issue_key}/transitions"
    
    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    # Make the GET request to get available transitions
    response = requests.get(url, headers=headers, auth=(jira_email, jira_api_token))

    if response.status_code == 200:
        transitions = response.json().get('transitions', [])
        return jsonify(transitions), 200
    else:
        return jsonify({"message": f"Failed to get transitions. Status code: {response.status_code}", "details": response.text}), response.status_code

if __name__ == '__main__':
    app.run(port=5000)

# curl -X POST http://localhost:5000/get-transitions -H "Content-Type: application/json" -d '{"issue_key": "TLC-3622"}'
