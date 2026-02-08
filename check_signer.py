import os
import requests
from dotenv import load_dotenv

def check_signer():
    load_dotenv()
    api_key = os.getenv('FARCASTER_API_KEY')
    signer_uuid = os.getenv('FARCASTER_SIGNER_UUID')
    
    url = f"https://api.neynar.com/v2/farcaster/signer?signer_uuid={signer_uuid}"
    headers = {"api_key": api_key}
    
    response = requests.get(url, headers=headers)
    print(f"Signer Check: {response.status_code}")
    print(response.text)

if __name__ == "__main__":
    check_signer()
