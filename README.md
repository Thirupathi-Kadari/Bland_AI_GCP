# Bland_AI
## Bland_AI Cloud Integration

This project involves deploying a Flask application on Google Cloud Platform (GCP) that interacts with the Bland AI API. It includes a webhook endpoint for receiving data from Bland AI, a method to manually trigger calls, and instructions for deploying the application to GCP.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [License](#license)

## Installation

### Prerequisites

- Python 3.9+
- `requests` library
- `flask` library
- `gunicorn` for serving the Flask app

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Thirupathi-Kadari/Bland_AI_GCP.git
    cd Bland_AI_GCP
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add your API key:
    ```ini
    API_KEY=your_bland_ai_api_key
    ```

## Usage

### Running the Flask Application Locally

To run the Flask application locally:
1. Start the Flask server:
    ```sh
    python app.py
    ```

2. Access the application at `http://localhost:5000`.

### Making a Reminder Call

To trigger a reminder call using the Bland AI API, navigate to the following endpoint:
- **GET /trigger_call**: Manually triggers a call using the Bland AI API.

### Retrieving Conversations

To view stored conversations:
- **GET /conversations**: Retrieves all stored conversations from `conversations.json`.

## Deployment

### Deploying to Google Cloud Platform (GCP)

1. **Install the Google Cloud SDK** if you haven't already: [Google Cloud SDK Installation](https://cloud.google.com/sdk/docs/install)

2. **Authenticate with Google Cloud:**
    ```sh
    gcloud auth login
    ```

3. **Set your project:**
    ```sh
    gcloud config set project your-project-id
    ```

4. **Deploy the application:**
    ```sh
    gcloud app deploy
    ```

   The application will be deployed and accessible at a URL provided by GCP.

## Configuration

### `app.yaml`

The `app.yaml` file configures the runtime and entrypoint for your Flask application. Update the `API_KEY` environment variable with your actual API key:
```yaml
runtime: python39
entrypoint: gunicorn -b :$PORT app:app

env_variables:
  API_KEY: "your_bland_ai_api_key"
```
## API Documentation

### POST /webhook

- **Description**: Handles incoming webhook data from the Bland AI API.
- **Method**: POST
- **Request Body**: JSON object with the data sent by the Bland AI API.
- **Response**: 
    - **Success**: `{"status": "success"}`
    - **Failure**: `{"status": "failure"}`

### GET /conversations

- **Description**: Retrieves stored conversations.
- **Method**: GET
- **Response**: 
    - **Success**: JSON array of conversations
    - **Failure**: `{"error": "No conversations found"}`

### GET /trigger_call

- **Description**: Manually triggers a call using the Bland AI API.
- **Method**: GET
- **Response**: JSON object containing the API response

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
