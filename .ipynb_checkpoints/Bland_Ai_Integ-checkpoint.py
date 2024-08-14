import requests

url = "https://api.bland.ai/v1/calls"

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
    "voicemail_message": "Hello, this ia a test message",
    "voicemail_action": "leave_message",
    "retry": {"wait": 10,
    "voicemail_action": "leave_message",
    "voicemail_message": "Hello, this is a test message."},
    "max_duration": 30,
    "record": True,
    "webhook":"https://your-webhook-url",
    "metadata": {},
    "summary_prompt": "Summerize the call with See you Have a good one",
    "answered_by_enabled": True
}
headers = {
    "authorization": "YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.post( url, json=payload, headers=headers)

print(response.text)