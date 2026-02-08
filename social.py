"""
social.py - Social media integration module for OpenClaw agent
Handles posting updates to Farcaster and X (Twitter)
"""

import os
import logging
import requests
from typing import Dict, Optional
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SocialMediaManager:
    """Manages social media posting for Farcaster and X"""
    
    def __init__(
        self, 
        farcaster_api_key: Optional[str] = None,
        x_api_key: Optional[str] = None,
        x_api_secret: Optional[str] = None,
        x_access_token: Optional[str] = None,
        x_access_secret: Optional[str] = None
    ):
        """
        Initialize social media manager
        
        Args:
            farcaster_api_key: Farcaster API key (Neynar or Warpcast)
            x_api_key: X API key
            x_api_secret: X API secret
            x_access_token: X access token
            x_access_secret: X access token secret
        """
        # Farcaster credentials
        self.farcaster_api_key = farcaster_api_key or os.getenv('FARCASTER_API_KEY')
        
        # X (Twitter) credentials
        self.x_api_key = x_api_key or os.getenv('X_API_KEY')
        self.x_api_secret = x_api_secret or os.getenv('X_API_SECRET')
        self.x_access_token = x_access_token or os.getenv('X_ACCESS_TOKEN')
        self.x_access_secret = x_access_secret or os.getenv('X_ACCESS_SECRET')
        
        logger.info("🔗 Social Media Manager initialized")
        if self.farcaster_api_key:
            logger.info("✅ Farcaster API key configured")
        else:
            logger.warning("⚠️ Farcaster API key not configured")
        
        if all([self.x_api_key, self.x_api_secret, self.x_access_token, self.x_access_secret]):
            logger.info("✅ X (Twitter) credentials configured")
        else:
            logger.warning("⚠️ X (Twitter) credentials not fully configured")
            
    def generate_ai_image(self, prompt: str) -> str:
        """
        Generates a dynamic AI image URL based on the prompt.
        Uses Pollinations.ai for stable, high-quality on-the-fly generation.
        """
        # Clean prompt for URL
        clean_prompt = prompt.replace(" ", "%20").replace("$", "")
        # Parameters for premium look
        params = "width=1024&height=1024&nologo=true&enhance=true"
        image_url = f"https://pollinations.ai/p/{clean_prompt}?{params}"
        logger.info(f"🎨 Generated AI Image URL: {image_url}")
        return image_url
    
    def post_to_farcaster(self, message: str, image_url: Optional[str] = None) -> Dict[str, any]:
        """
        Post a message to Farcaster using Neynar API with optional image
        """
        try:
            if not self.farcaster_api_key:
                logger.warning("⚠️ Farcaster API key not configured. Skipping post.")
                return {'status': 'skipped', 'reason': 'no_api_key'}
            
            logger.info(f"📤 Posting to Farcaster: {message[:30]}...")
            
            url = "https://api.neynar.com/v2/farcaster/cast"
            headers = {
                "accept": "application/json",
                "api_key": self.farcaster_api_key,
                "content-type": "application/json"
            }
            
            payload = {
                "signer_uuid": os.getenv('FARCASTER_SIGNER_UUID', ''),
                "text": message
            }
            
            if image_url:
                payload["embeds"] = [{"url": image_url}]
            
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"✅ Successfully posted to Farcaster!")
                return {'status': 'success', 'platform': 'farcaster', 'response': data}
            else:
                logger.error(f"❌ Failed to post to Farcaster: {response.status_code}")
                return {'status': 'error', 'platform': 'farcaster', 'error': response.text}
                
        except Exception as e:
            logger.error(f"❌ Error posting to Farcaster: {str(e)}")
            return {'status': 'error', 'platform': 'farcaster', 'error': str(e)}
    
    def get_latest_casts(self, fid: int, limit: int = 5) -> List[Dict]:
        """
        Fetch latest casts for a specific FID to look for commands
        """
        try:
            if not self.farcaster_api_key:
                return []
            
            url = f"https://api.neynar.com/v2/farcaster/feed/user/casts?fid={fid}&limit={limit}"
            headers = {
                "accept": "application/json",
                "api_key": self.farcaster_api_key
            }
            
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get('casts', [])
            return []
        except Exception as e:
            logger.error(f"❌ Error fetching casts: {e}")
            return []

    def post_to_x(self, message: str) -> Dict[str, any]:
        """
        Post a message to X (Twitter) using API v2
        
        Args:
            message: Tweet content
        
        Returns:
            Response data from X API
        """
        try:
            if not all([self.x_api_key, self.x_api_secret, self.x_access_token, self.x_access_secret]):
                logger.warning("⚠️ X credentials not fully configured. Skipping post.")
                return {'status': 'skipped', 'reason': 'missing_credentials'}
            
            logger.info("📤 Posting to X (Twitter)...")
            
            # Using Tweepy or direct API v2 call
            # For simplicity, we'll use requests with OAuth 1.0a
            try:
                from requests_oauthlib import OAuth1Session
                
                # Create OAuth1 session
                oauth = OAuth1Session(
                    self.x_api_key,
                    client_secret=self.x_api_secret,
                    resource_owner_key=self.x_access_token,
                    resource_owner_secret=self.x_access_secret
                )
                
                # X API v2 endpoint
                url = "https://api.twitter.com/2/tweets"
                
                payload = {"text": message}
                
                response = oauth.post(url, json=payload)
                
                if response.status_code == 201:
                    data = response.json()
                    logger.info(f"✅ Successfully posted to X!")
                    logger.info(f"Tweet ID: {data.get('data', {}).get('id', 'N/A')}")
                    return {
                        'status': 'success',
                        'platform': 'x',
                        'response': data
                    }
                else:
                    logger.error(f"❌ Failed to post to X: {response.status_code}")
                    logger.error(f"Response: {response.text}")
                    return {
                        'status': 'error',
                        'platform': 'x',
                        'error': response.text
                    }
                    
            except ImportError:
                logger.error("❌ requests-oauthlib not installed. Install with: pip install requests-oauthlib")
                return {
                    'status': 'error',
                    'platform': 'x',
                    'error': 'requests-oauthlib not installed'
                }
                
        except Exception as e:
            logger.error(f"❌ Error posting to X: {str(e)}")
            return {
                'status': 'error',
                'platform': 'x',
                'error': str(e)
            }
    
    def post_token_deployment(
        self, 
        token_name: str,
        token_symbol: str,
        contract_address: str,
        transaction_hash: str,
        initial_supply: int,
        explorer_url: str
    ) -> Dict[str, any]:
        """
        Post token deployment announcement to all configured platforms
        
        Args:
            token_name: Name of the deployed token
            token_symbol: Symbol of the token
            contract_address: Contract address
            transaction_hash: Transaction hash
            initial_supply: Initial token supply
            explorer_url: Block explorer URL
        
        Returns:
            Dictionary with results from all platforms
        """
        try:
            # Craft announcement message
            message = self._create_deployment_message(
                token_name=token_name,
                token_symbol=token_symbol,
                contract_address=contract_address,
                initial_supply=initial_supply,
                explorer_url=explorer_url
            )
            
            logger.info("📢 Announcing token deployment...")
            logger.info(f"Message: {message}")
            
            # Generate a dynamic AI image for the token
            image_prompt = f"Futuristic crypto token logo for {token_name} on Base blockchain, high tech, glowing blue and purple, 3d render"
            image_url = self.generate_ai_image(image_prompt)
            
            results = {
                'message': message,
                'farcaster': self.post_to_farcaster(message, image_url=image_url),
                'x': self.post_to_x(message)
            }
            
            # Log summary
            success_count = sum(1 for r in [results['farcaster'], results['x']] if r.get('status') == 'success')
            logger.info(f"📊 Posted to {success_count}/2 platforms successfully")
            
            return results
            
        except Exception as e:
            logger.error(f"❌ Error announcing token deployment: {str(e)}")
            raise
    
    def _create_deployment_message(
        self,
        token_name: str,
        token_symbol: str,
        contract_address: str,
        initial_supply: int,
        explorer_url: str
    ) -> str:
        """
        Create a formatted deployment announcement message
        
        Args:
            token_name: Token name
            token_symbol: Token symbol
            contract_address: Contract address
            initial_supply: Initial supply
            explorer_url: Explorer URL
        
        Returns:
            Formatted message string
        """
        message = f"""🚀 New Token Deployed by OpenClaw Agent!

💎 {token_name} (${token_symbol})
📍 {contract_address[:8]}...{contract_address[-6:]}
💰 Supply: {initial_supply:,}
🔗 {explorer_url}

#Base #Crypto #DeFi #OpenClaw"""
        
        return message
    
    def post_status_update(self, message: str) -> Dict[str, any]:
        """
        Post a general status update to all platforms
        
        Args:
            message: Status message
        
        Returns:
            Results from all platforms
        """
        try:
            logger.info("📢 Posting status update...")
            
            results = {
                'message': message,
                'farcaster': self.post_to_farcaster(message),
                'x': self.post_to_x(message)
            }
            
            return results
            
        except Exception as e:
            logger.error(f"❌ Error posting status update: {str(e)}")
            raise


if __name__ == "__main__":
    # Test the social media manager
    from dotenv import load_dotenv
    load_dotenv()
    
    try:
        sm = SocialMediaManager()
        
        # Example: Post a test message (uncomment to test)
        # result = sm.post_status_update("Testing OpenClaw agent! 🤖")
        # print(json.dumps(result, indent=2))
        
    except Exception as e:
        logger.error(f"Error: {e}")
