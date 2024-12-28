import json
import requests

def send_message_to_api(url, bid_data):
    headers = {'Content-type': 'application/json'}
    message = create_message("new_bid", bid_data)
    try:
        new_url = url.replace("/message", "")
        response = requests.post(f"{new_url}/new_bid", data=message, headers=headers)
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

def browse_freelancing_platforms(keywords, platform="Upwork"):
  print(f"Browsing '{platform}' for jobs with keywords: {keywords}")
  # Placeholder for web scraping or API calls
  jobs = []
  if platform == "Upwork":
     jobs = [
      {"title": "Data Entry Project", "description": "Simple data entry task.", "budget": 20, "platform":"Upwork"},
      {"title": "Copywriting Article", "description": "Writing an article for a blog.", "budget": 30, "platform":"Upwork"},
        ] # We can use a list of dictionaries for now.
  elif platform == "Fiverr":
    jobs = [
      {"title": "Social Media Manager", "description": "Automate posting on Social Media", "budget": 40, "platform":"Fiverr"},
       {"title": "Web Dev Project", "description": "A simple personal website.", "budget": 100, "platform":"Fiverr"},
        ]
  else:
      print("Platform not found")
  return jobs

def analyze_job_description(job_description):
    # Placeholder for natural language processing or keyword extraction
    print(f"Analyzing Job: {job_description}")
    relevant_data = {
        "required_skills": ["data entry", "copywriting"],
        "estimated_time": "1 hour",
    }
    # Simulate different results for different jobs
    if "data entry" in job_description.lower():
         relevant_data["required_skills"] = ["data entry"]
    if "copywriting" in job_description.lower():
          relevant_data["required_skills"] = ["copywriting"]
    if "social media" in job_description.lower():
          relevant_data["required_skills"] = ["social media", "marketing"]
    if "web dev" in job_description.lower():
       relevant_data["required_skills"] = ["web dev", "coding", "html"]
    return relevant_data


def generate_automated_response(relevant_data):
        # Placeholder: This is where the response is created.
        print(f"Generating automated response")
        skills = ", ".join(relevant_data['required_skills'])
        response_text = f"Hello, I saw that you need someone that has the skills {skills}, and I think I can help you. My hourly rate is $5, how does it sound?"
        return response_text

def store_bid(bid_data, url):
    #Placeholder: You will store the data on a file here
    send_bid_to_api(url, bid_data)
    print(f"Storing bid: {bid_data}")

def send_bid_to_api(url, bid_data):
    message = create_message("new_bid", bid_data)
    headers = {'Content-type': 'application/json'}
    try:
        new_url = url.replace("/message", "")
        response = requests.post(f"{new_url}", data=message, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        return None

if __name__ == "__main__":
        url = "https://samihil.pythonanywhere.com/message" # Replace with your actual PythonAnywhere URL
        keywords = ["data entry", "copywriting"]
        jobs_upwork = browse_freelancing_platforms(keywords, "Upwork")
        jobs_fiverr = browse_freelancing_platforms(keywords, "Fiverr")
        jobs = jobs_upwork + jobs_fiverr

        for job in jobs:
          relevant_data = analyze_job_description(job["description"])
          response = generate_automated_response(relevant_data)
          bid_data = {"job_title":job["title"], "response":response, "platform":job["platform"]}
          send_bid_to_api(url, bid_data)
        print("Process completed")