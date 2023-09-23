## 🚀 ChatGPT Proxy API
This project provides a proxy for the ChatGPT API using Flask and Heroku. It allows you to send requests from your local environment to your deployed Heroku app, which then forwards those requests to OpenAI's ChatGPT API.

## 🛠 Setup and Configuration
### 1️⃣ Heroku Setup
Step 1: Install the Heroku CLI if you haven't already.
Step 2: Authenticate with Heroku:
```shell=
heroku login
```
### 2️⃣ Local Setup
Step 1: Install the necessary Python packages:

```shell=
pip install flask requests
```
Step 2: Save the provided server side code as proxy_server.py.

Step 3: Save the provided local code as local_request.py.

### 3️⃣ Deploying to Heroku
Step 1: In your project directory, initialize git and create a Heroku app:

```shell=
git init
heroku create your-heroku-app-name
```
Step 2: Commit all files:
```shell=
git add .
git commit -m "Initial commit"
```
Step 3: Push the code to Heroku:

```shell=
git push heroku master
```
Step 4: Start a Heroku dyno:

```shell=
heroku ps:scale web=1
```

## 🚀 Usage
Step 1: In local_request.py, replace YOUR_OPENAI_API_KEY_HERE with your OpenAI API key.
Step 2: Replace https://your-heroku-app-name.herokuapp.com with the URL of your app on Heroku.
Step 3: Run local_request.py and follow the prompts to input text.
## 🔎 Notes
### 🔒 Security: Make sure to keep your OpenAI API key confidential. Do not publicize or share it.
### 💡 Debugging: In case of any issues or errors, review the Heroku logs:
```shell=
heroku logs --tail
```