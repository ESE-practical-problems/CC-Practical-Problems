# Deploy a Python Flask App on Google App Engine (Standard Environment)

This guide will walk you through deploying a simple Flask application on Google App Engine Standard Environment.

# Prerequisites


- A Google Cloud Platform (GCP) project with billing enabled.
- Google Cloud SDK installed on your local machine.
- Python 3 installed (Recommended: Python 3.7+).
- A basic understanding of command line operations.
Alternatively, you can use Google Cloud Shell which comes pre-installed with required tools.


# Setup Steps

## 1. Create an App Engine Application

```
gcloud init
gcloud app create --region=your-region
```
Replace 'your-region' with your preferred region (e.g., asia-south1 for Mumbai)

## 2. Write a Simple Flask Application

```
mkdir my-flask-app
cd my-flask-app
```
Creates a new folder and moves inside it

```
# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World from Google App Engine!'
```
A basic Flask application

## 3. Create `requirements.txt`

```
Flask==2.2.5
```
Mention dependencies needed to run the app

## 4. Create `app.yaml`

```
runtime: python39

entrypoint: gunicorn -b :$PORT main:app

instance_class: F1

automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 1
  max_instances: 2
```
Configurations for App Engine Deployment

## 5. Deploy the Application

```
gcloud app deploy --project=your-project-id -v=v01
```
Deploys your app to App Engine

## 6. Open the Deployed App

```
gcloud app browse
```
Opens the app URL in your default browser

# Common Errors & Debugging


- Billing Not Enabled Error:
  Make sure billing is enabled for your GCP project.

- Missing app.yaml Error:
  Ensure app.yaml is correctly placed in the project root directory.

- Module Not Found Error:
  Check if your requirements.txt correctly lists all dependencies.

- Port Errors (Locally Running Flask):
  Use gunicorn if deploying with custom entry points.


# Notes


- App Engine Standard only supports certain versions of Python (3.7, 3.8, 3.9).
- For testing locally, you can run:


```
python main.py
```
For local testing


- For production, App Engine handles running the server automatically via gunicorn.


# References


- Google Cloud App Engine Documentation: https://cloud.google.com/appengine/docs
- Flask Official Documentation: https://flask.palletsprojects.com/
- Yt video referred: https://youtu.be/c1R8itvI6JA?si=zjaDtO0fPipXU_S9

-Install the gcloud CLI: https://cloud.google.com/sdk/docs/install

