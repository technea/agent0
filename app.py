from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'dashboard.html')

@app.route('/deployments.json')
def get_deployments():
    return send_from_directory('.', 'deployments.json')

@app.route('/agent0_metadata.json')
def get_metadata():
    return send_from_directory('.', 'agent0_metadata.json')

@app.route('/api/command', methods=['POST'])
def send_command():
    data = request.json
    command_type = data.get('type') # 'deploy' or 'post'
    params = data.get('params', {})
    
    command = {
        "type": command_type,
        "params": params,
        "timestamp": time.time(),
        "executed": False
    }
    
    # Save to commands.json for the agent to pick up
    try:
        commands = []
        if os.path.exists("commands.json"):
            with open("commands.json", "r") as f:
                commands = json.load(f)
        
        commands.append(command)
        
        with open("commands.json", "w") as f:
            json.dump(commands, f, indent=2)
            
        return jsonify({"status": "success", "message": f"Command {command_type} queued"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
