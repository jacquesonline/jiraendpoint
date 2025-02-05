from flask import Flask, request
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/testim-webhook', methods=['POST'])
def testim_webhook():
    data = request.json
    test_name = data.get('test_name')
    test_status = data.get('status')
    jira_issue_key = data.get('jira_issue_key')

    jira_url = f"https://mauriceblackburn.atlassian.net/rest/api/2/issue/{jira_issue_key}/comment"
    jira_email = os.getenv("JIRA_EMAIL")
    jira_api_token = os.getenv("JIRA_API_TOKEN")
    auth = (jira_email, jira_api_token)

    headers = {
        "Content-Type": "application/json"
    }

    comment_data = {
        "body": f"Testim test case '{test_name}' has been run with status: {test_status}."
    }

    print(f"Received webhook data: {comment_data}")

    response = requests.post(jira_url, headers=headers, auth=auth, data=json.dumps(comment_data))

    if response.status_code == 201:
        return "Comment added successfully.", 201
    else:
        return f"Failed to add comment. Status code: {response.status_code}", response.status_code

if __name__ == '__main__':
    app.run(port=5000)
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     print(f"Received webhook data: {data}")
#     return jsonify({"status": "success"}), 200

# if __name__ == '__main__':
#     app.run(port=5000)


# curl -X POST http://localhost:5000/testim-webhook \
#      -H "Content-Type: application/json" \
#      -d '{
#            "test_name": "Sample Test Case",
#            "status": "Passed",
#            "jira_issue_key": "TLC-3622"
#          }'

# https://mauriceblackburn.atlassian.net/rest/api/2/issue/TLC-3622/comment