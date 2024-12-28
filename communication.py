import json
import requests

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
    url = "https://samihil.pythonanywhere.com/message"
    test_message = create_message("test_command", {"value": "test_data"})
    print(f"Created message: {test_message}")
    response = send_message_to_api(url,test_message)
    print(f"Received message: {response}")