# Bland_AI
## AI_Health_Monitoring Calls Project

This project uses the Bland API to make reminder calls and sets up a Flask server to handle webhooks and store conversations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Webhooks](#webhooks)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6+
- `requests` library
- `flask` library
- `ngrok` (for HTTPS tunneling)

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Thirupathi-Kadari/Bland_AI.git
    cd Bland_AI
    ```

2. Install the dependencies:
    ```sh
    pip install requests
    pip install flask
    ```

## Usage

### Making a Reminder Call

To make a reminder call using the Bland API, refer to the [Bland_Ai_Integ.py](https://github.com/Thirupathi-Kadari/Bland_AI/blob/main/Bland_Ai_Integ.py) file in the repository.

### Setting Up the Flask Server

To set up the Flask server to handle webhooks and store conversations, refer to the [Flask.py](https://github.com/Thirupathi-Kadari/Bland_AI/blob/main/Flask.py) file in the repository.

### Using ngrok for HTTPS

Since the `Bland_Ai_Integ.py` file requires an HTTPS URL but the Flask server provides only HTTP, you can use ngrok to create an HTTPS tunnel. Follow these steps:

1. Install ngrok:
    ```sh
    # On macOS
    brew install ngrok/ngrok/ngrok

    # On Windows
    choco install ngrok

    # On Linux
    snap install ngrok
    ```

2. Start the Flask server:
    ```sh
    python flask_server.py
    ```

3. In a new terminal, start ngrok to tunnel your Flask server:
    ```sh
    ngrok http 5000
    ```

4. Copy the HTTPS URL provided by ngrok (e.g., `https://<your-subdomain>.ngrok.io`) and use it as the webhook URL in your `Bland_Ai_Integ.py` file.

## Webhooks

### Setting Up the Webhook

To handle incoming webhook data from the Bland API, you'll need to set up a webhook URL in your application. This URL should be publicly accessible over HTTPS. Here’s how to obtain and use the webhook URL:

1. **Create a Webhook URL:**
   - Use ngrok to expose your local Flask server to the internet. After starting ngrok, it will provide an HTTPS URL (e.g., `https://<your-subdomain>.ngrok.io`).

2. **Update the Webhook URL:**
   - Copy the ngrok HTTPS URL and update it in your `Bland_Ai_Integ.py` file. This URL will be used by the Bland API to send data to your Flask server.

3. **Handle Webhook Requests:**
   - Implement logic in your Flask server to process incoming webhook requests. This typically involves parsing the JSON payload sent by the Bland API and taking appropriate action.

## API Documentation

### POST /webhook

- **Description**: Handles incoming webhook data.
- **Method**: POST
- **Request Body**: JSON object with the data sent by the Bland API.
- **Response**: 
    - Success: `{"status": "success"}`
    - Failure: `{"status": "failure"}`

### GET /conversations

- **Description**: Retrieves stored conversations.
- **Method**: GET
- **Response**: 
    - Success: JSON array of conversations
    - Failure: `{"error": "No conversations found"}`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
