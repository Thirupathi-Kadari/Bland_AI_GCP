from flask import Flask, request, jsonify
import json
import os

# Import the function from Bland_Ai_Integ.py
from Bland_Ai_Integ import trigger_call

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received data:", data)
    
    with open('conversations.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    return jsonify({"status": "success"}), 200

@app.route('/conversations', methods=['GET'])
def get_conversations():
    if os.path.exists('conversations.json'):
        with open('conversations.json', 'r') as f:
            conversations = f.readlines()
        
        conversations = [json.loads(conv) for conv in conversations]
        return jsonify(conversations), 200
    else:
        return jsonify({"error": "No conversations found"}), 404

# New route to trigger the call
@app.route('/trigger_call', methods=['GET'])
def trigger_bland_ai_call():
    response = trigger_call()
    return jsonify({"response": response}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
