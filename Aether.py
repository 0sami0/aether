import json
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from freelance_module import send_message_to_api, create_message, browse_freelancing_platforms, analyze_job_description, generate_automated_response, store_bid


if __name__ == "__main__":
    print("Aether is Starting")
    url = "https://samihil.pythonanywhere.com/message" # Replace with your actual PythonAnywhere URL
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