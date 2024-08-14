# Bland_Ai_Integ.py

import requests
from dotenv import load_dotenv
import os

load_dotenv()

def trigger_call():
    url = "https://api.bland.ai/v1/calls"
    api_key = os.environ.get("API_KEY")

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
        "webhook": "https://bland-ai-431701.ts.r.appspot.com/webhook",
        "metadata": {},
        "summary_prompt": "Summarize the call with 'See you, have a good one'",
        "answered_by_enabled": True
    }

    headers = {
        "authorization": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    # Returning the response for further use
    return response.text
