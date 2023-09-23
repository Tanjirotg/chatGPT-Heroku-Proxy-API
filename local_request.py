import requests

# Replace with your Heroku app name
HEROKU_ENDPOINT = "https://your-heroku-app-name.herokuapp.com/complete"
# Replace with your API Key
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"


def send_prompt(messages):
    # limit the number of tokens to 15000
    max_tokens = 15000
    for message in messages:
        max_tokens -= len(message)*4

    # set the headers
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    # send the request
    response = requests.post(HEROKU_ENDPOINT, headers=headers, json={
                             "messages": [{'role': 'user', 'content': messages}], "max_tokens": max_tokens, "temperature": 0.9, "model": "gpt-3.5-turbo-16k"})
    return response.json()


if __name__ == "__main__":
    messages = "Hi"
    result = send_prompt(messages)
    # error handling
    if result.get("error"):
        print(result.get("error"))
        exit()
    # print the response
    print(result.get("choices")[0].get("message").get("content"))
