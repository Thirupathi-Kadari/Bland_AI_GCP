from flask import Flask, request, jsonify
import json
import os

# Import the function to trigger calls from Bland_Ai_Integ.py
from Bland_Ai_Integ import trigger_call

# Initialize Flask application
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Handles incoming webhook data from the Bland AI API.

    The webhook endpoint receives JSON data from the Bland AI API,
    logs the data to a file, and returns a success response.

    Returns:
        JSON response with status of success.
    """
    # Retrieve JSON data from the request
    data = request.json
    print("Webhook received data:", data)
    
    # Append the incoming data to 'conversations.json'
    with open('conversations.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    # Return a success response
    return jsonify({"status": "success"}), 200

@app.route('/conversations', methods=['GET'])
def get_conversations():
    """
    Retrieves and returns stored conversations.

    This endpoint reads the 'conversations.json' file and returns
    the stored conversations as a JSON array.

    Returns:
        JSON response with stored conversations or error message if no data found.
    """
    if os.path.exists('conversations.json'):
        # Read all lines from 'conversations.json'
        with open('conversations.json', 'r') as f:
            conversations = f.readlines()
        
        # Parse each line as JSON
        conversations = [json.loads(conv) for conv in conversations]
        return jsonify(conversations), 200
    else:
        # Return an error message if no data found
        return jsonify({"error": "No conversations found"}), 404

@app.route('/trigger_call', methods=['GET'])
def trigger_bland_ai_call():
    """
    Manually triggers a call using the Bland AI API.

    This endpoint invokes the trigger_call function from the Bland_Ai_Integ.py file
    and returns the response from the Bland AI API.

    Returns:
        JSON response containing the API response.
    """
    # Call the function to trigger a Bland AI call
    response = trigger_call()
    return jsonify({"response": response}), 200

# Run the Flask application on port 5000 with debug mode enabled
if __name__ == '__main__':
    app.run(port=5000, debug=True)
