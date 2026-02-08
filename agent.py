"""
agent.py - Main autonomous agent loop for OpenClaw
Coordinates blockchain operations and social media posting
"""

import os
import time
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import random
import json
from dotenv import load_dotenv

from blockchain import BlockchainManager
from social import SocialMediaManager

# Agent0 integration (optional)
try:
    from agent0_integration import Agent0Integration
    AGENT0_AVAILABLE = True
except ImportError:
    AGENT0_AVAILABLE = False
    logging.warning("⚠️ Agent0 integration not available")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('openclaw_agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class OpenClawAgent:
    """
    Autonomous agent that deploys ERC20 tokens and posts updates
    """
    
    def __init__(self, interval_minutes: int = 20, enable_agent0: bool = False):
        """
        Initialize the OpenClaw agent
        """
        logger.info("🤖 Initializing OpenClaw Agent...")
        
        # Load environment variables
        load_dotenv()
        
        # Initialize managers
        try:
            self.blockchain = BlockchainManager()
            self.social = SocialMediaManager()
        except Exception as e:
            logger.error(f"❌ Failed to initialize managers: {str(e)}")
            raise
        
        # Initialize Agent0 integration
        self.agent0 = None
        if enable_agent0 and AGENT0_AVAILABLE:
            try:
                self.agent0 = Agent0Integration(self.blockchain.w3, self.blockchain.account)
                if not self.agent0.is_registered():
                    self.agent0.register_agent(name="OpenClaw")
                logger.info("✅ Agent0 integration enabled")
            except Exception as e:
                logger.warning(f"⚠️ Agent0 integration failed: {e}")
                self.agent0 = None
        
        self.interval_minutes = interval_minutes
        self.deployment_count = 0
        self.deployment_history = []
        self.start_time = datetime.now()
        self.last_deployment = datetime.now() - timedelta(minutes=interval_minutes)
        
        # Token name generation lists
        self.token_prefixes = ["Open", "Base", "Claw", "Auto", "Chain", "Mesh", "Cyber", "Meta", "Hyper", "Ultra", "Mega", "Nova", "Apex", "Quantum", "Nexus"]
        self.token_suffixes = ["Token", "Coin", "Cash", "Finance", "Pay", "Network", "Protocol", "Chain", "Swap", "Vault", "DAO", "Labs"]

    def check_for_commands(self):
        """Check for interactive commands from dashboard"""
        if not os.path.exists("commands.json"):
            return None
        try:
            with open("commands.json", "r") as f:
                commands = json.load(f)
            for cmd in commands:
                if not cmd.get("executed", False):
                    cmd["executed"] = True
                    with open("commands.json", "w") as f:
                        json.dump(commands, f, indent=2)
                    return cmd
            return None
        except: return None

    def deploy_and_announce(self, custom_name=None, custom_symbol=None) -> bool:
        """Execute one cycle: deploy token and announce"""
        try:
            logger.info("=" * 60)
            logger.info(f"🚀 Starting cycle #{self.deployment_count + 1}")
            
            # Parameters
            token_name = custom_name or random.choice(self.token_prefixes) + random.choice(self.token_suffixes)
            token_symbol = custom_symbol or (token_name[0] + token_name[-2:]).upper()
            initial_supply = random.choice([100000, 500000, 1000000])
            
            logger.info(f"💎 Token: {token_name} (${token_symbol})")
            
            # Deploy
            deployment = self.blockchain.deploy_erc20_token(token_name, token_symbol, initial_supply)
            contract_address = deployment['contract_address']
            tx_hash = deployment['transaction_hash']
            explorer_url = f"https://sepolia.basescan.org/tx/{tx_hash}"
            
            # Announce
            social_result = self.social.post_token_deployment(
                token_name=token_name, token_symbol=token_symbol,
                contract_address=contract_address, transaction_hash=tx_hash,
                initial_supply=initial_supply, explorer_url=explorer_url
            )
            
            # Reputation
            if self.agent0:
                self.agent0.submit_reputation_proof(
                    task_type="erc20_deployment",
                    proof_data={'token_symbol': token_symbol, 'transaction_hash': tx_hash}
                )
            
            # Save Record
            record = {
                'deployment_number': self.deployment_count + 1,
                'timestamp': datetime.now().isoformat(),
                'token_name': token_name,
                'token_symbol': token_symbol,
                'contract_address': contract_address,
                'transaction_hash': tx_hash,
                'initial_supply': initial_supply,
                'explorer_url': explorer_url
            }
            self.deployment_history.append(record)
            self._save_record(record)
            self.deployment_count += 1
            self.last_deployment = datetime.now()
            return True
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return False

    def _save_record(self, record):
        filename = 'deployments.json'
        records = []
        if os.path.exists(filename):
            with open(filename, 'r') as f: records = json.load(f)
        records.append(record)
        with open(filename, 'w') as f: json.dump(records, f, indent=2)

    def run(self, once=False):
        """Continuous Loop"""
        if once:
            self.deploy_and_announce()
            return

        logger.info("🔄 Agent Active - Waiting for instructions...")
        while True:
            cmd = self.check_for_commands()
            if cmd:
                if cmd['type'] == 'deploy':
                    self.deploy_and_announce(cmd['params'].get('name'), cmd['params'].get('symbol'))
                elif cmd['type'] == 'post':
                    custom_text = cmd['params'].get('text')
                    if custom_text:
                        logger.info(f"📤 Custom Manual Post: {custom_text}")
                        self.social.post_to_farcaster(custom_text)
                    elif self.deployment_history:
                        latest = self.deployment_history[-1]
                        self.social.post_to_farcaster(f"Manual Verified Update: Agent just verified {latest['token_name']} on-chain! 🤖")
                continue

            # Regular interval check
            if (datetime.now() - self.last_deployment).total_seconds() >= self.interval_minutes * 60:
                self.deploy_and_announce()
            
            time.sleep(5)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', type=int, default=20)
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--agent0', action='store_true')
    args = parser.parse_args()
    
    agent = OpenClawAgent(interval_minutes=args.interval, enable_agent0=args.agent0)
    agent.run(once=args.once)

if __name__ == "__main__":
    main()
