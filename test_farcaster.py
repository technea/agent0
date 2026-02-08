import os
import requests
from dotenv import load_dotenv

def test_farcaster():
    load_dotenv()
    api_key = os.getenv('FARCASTER_API_KEY')
    signer_uuid = os.getenv('FARCASTER_SIGNER_UUID')
    
    print(f"Testing Farcaster with API Key: {api_key[:10]}...")
    print(f"Signer UUID: {signer_uuid}")
    
    url = "https://api.neynar.com/v2/farcaster/cast"
    headers = {
        "accept": "application/json",
        "api_key": api_key,
        "content-type": "application/json"
    }
    payload = {
        "signer_uuid": signer_uuid,
        "text": "Hello from OpenClaw Agent! 🤖 #Base"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        if response.status_code == 200:
            print("✅ Success! Farcaster post confirmed.")
        else:
            print("❌ Failed. Check API Key and Signer UUID.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_farcaster()
