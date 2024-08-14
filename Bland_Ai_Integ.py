# Bland_Ai_Integ.py

import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def trigger_call():
    """
    Triggers a call using the Bland AI API.

    Constructs a payload with call parameters and sends a POST request
    to the Bland AI API endpoint to initiate the call.

    Returns:
        str: The response text from the API call.
    """
    
    # API endpoint for initiating a call
    url = "https://api.bland.ai/v1/calls"

    # Retrieve API key from environment variables
    api_key = os.environ.get("API_KEY")

    # Payload for the API request
    payload = {
        "phone_number": "+19797393588",
        "task": "Remind the Customer about their appointment",
        "voice": "maya",
        "first_sentence": "Hello! This is a reminder about your appointment.",
        "wait_for_greeting": True,
        "block_interruptions": False,
        "interruption_threshold": 123,
        "model": "enhanced",
        "temperature": 0.7,
        "keywords": ["reminder", "appointment"],
        "pronunciation_guide": [{}],
        "transfer_phone_number": "+15512008317",
        "transfer_list": {"default": "+15512008317"},
        "language": "en-US",
        "calendly": {},
        "timezone": "America/New_York",
        "request_data": {},
        "voicemail_message": "Hello, this is a test message",
        "voicemail_action": "leave_message",
        "retry": {
            "wait": 10,
            "voicemail_action": "leave_message",
            "voicemail_message": "Hello, this is a test message."
        },
        "max_duration": 30,
        "record": True,
        "webhook": "https://your_webhook_URL/webhook",
        "metadata": {},
        "summary_prompt": "Summarize the call with 'See you, have a good one'",
        "answered_by_enabled": True
    }

    # Headers for the API request
    headers = {
        "authorization": api_key,
        "Content-Type": "application/json"
    }

    # Send the POST request to the API endpoint
    response = requests.post(url, json=payload, headers=headers)
    
    # Return the response text for further processing
    return response.text
