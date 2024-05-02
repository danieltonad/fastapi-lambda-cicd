**FastAPI-Lambda-CICD README**
=============================

**Introduction**
---------------

This project is a demonstration of a FastAPI application deployed on AWS Lambda using a CI/CD pipeline with GitHub Actions.

**Installation**
---------------

### Prerequisites

* Python 3.9+
* pip
* AWS Lambda and API Gateway setup

### Installation Steps

1. Clone the repository: `git clone https://github.com/danieltonad/fastapi-lambda-cicd`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure AWS credentials: set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables

**Usage Guide**
--------------

### Running the Application Locally

1. Run the application: `uvicorn main:app --host 0.0.0.0 --port 8000`
2. Open a web browser and navigate to `http://localhost:8000/`


**CI/CD Configuration**
-------------------------

The CI/CD pipeline is configured using GitHub Actions. The workflow file `main.yml` is located in the `.github/workflows` directory.

**Configuration Files**
---------------------

### `fastapi-lambda-cicd/.github/workflows/main.yml`

This file contains the workflow configuration for the CI/CD pipeline.

### `main.py`

This file contains the FastAPI application code.

**Troubleshooting**
---------------

* Check the GitHub Actions workflow logs for deployment errors
* Verify AWS credentials and Lambda function configuration

**License**
-------

This project is licensed under the MIT License.
