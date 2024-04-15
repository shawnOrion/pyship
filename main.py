import requests
import json

base_url = 'https://pyship-backend-e8043b7ed140.herokuapp.com/'


def make_post_request(endpoint, data):
    url = base_url + endpoint
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # log
    print("Response status code:", response.status_code)
    return response.json()


# Create data list of python messages
data = {
    "messages": [
        {'role': 'user', 'content': 'Hello'},
        {'role': 'assistant', 'content': 'Hi, how can I assist you?'},
        {'role': 'user', 'content': 'I need help with my code'},
        {'role': 'assistant', 'content': 'Sure, I\'ll do my best to help you'},
        {'role': 'user', 'content': 'Thank you'},
        {'role': 'assistant', 'content': 'You\'re welcome!'},
    ]
}
# make a request to "message (function takes data
response = make_post_request('message', data)
# print response.message role and content
print(f'Response: {response}')
if 'message' in response:
    message = response['message']
    print(f"Message\n{message['role']}: {message['content']}")
