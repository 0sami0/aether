import json
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from freelance_module import send_bid_to_api, create_message, browse_freelancing_platforms, analyze_job_description, generate_automated_response, store_bid

def send_message_to_api(url, message):
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post(url, data=message, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        return None

def create_message(command, data):
    message = {
        "command": command,
        "data": data
    }
    return json.dumps(message)

def receive_message(json_message):
    try:
       message = json.loads(json_message)
       return message
    except json.JSONDecodeError:
        return None

if __name__ == "__main__":
    print("Aether is Starting")
    url = "http://127.0.0.1:8080/new_bid" # Replace with your actual PythonAnywhere URL
    test_message = create_message("start_up", {"message": "aether is starting"})
    response = send_message_to_api(url, test_message)
    print(f"Response from API {response}")
    
    keywords = ["data entry", "copywriting"]
    jobs_upwork = browse_freelancing_platforms(keywords, "Upwork")
    jobs_fiverr = browse_freelancing_platforms(keywords, "Fiverr")
    jobs = jobs_upwork + jobs_fiverr

    for job in jobs:
        relevant_data = analyze_job_description(job["description"])
        response = generate_automated_response(relevant_data)
        bid_data = {"job_title":job["title"], "response":response, "platform":job["platform"]}
        store_bid(bid_data, url)
    print("Aether has finished initialization")