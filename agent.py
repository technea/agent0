"""
agent.py - Main autonomous agent loop for OpenClaw
Coordinates blockchain operations and social media posting
"""

import os
import time
import logging
from datetime import datetime
from typing import Optional
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
    logger.warning("⚠️ Agent0 integration not available")

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
        
        Args:
            interval_minutes: Time interval between operations (default: 20 minutes)
            enable_agent0: Enable ERC-8004 Agent0 integration (default: False)
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
        
        # Initialize Agent0 integration (optional)
        self.agent0 = None
        if enable_agent0 and AGENT0_AVAILABLE:
            try:
                self.agent0 = Agent0Integration(self.blockchain.w3, self.blockchain.account)
                if not self.agent0.is_registered():
                    self.agent0.register_agent(
                        name="OpenClaw",
                        capabilities=["erc20_deployment", "social_posting", "autonomous_operation"]
                    )
                logger.info("✅ Agent0 integration enabled")
            except Exception as e:
                logger.warning(f"⚠️ Agent0 integration failed: {e}")
                self.agent0 = None
        
        self.interval_minutes = interval_minutes
        self.interval_seconds = interval_minutes * 60
        self.deployment_count = 0
        self.start_time = datetime.now()
        
        # Token name generation lists
        self.token_prefixes = [
            "Open", "Base", "Claw", "Auto", "Chain", "Mesh", "Cyber", "Meta",
            "Hyper", "Ultra", "Mega", "Nova", "Apex", "Quantum", "Nexus"
        ]
        self.token_suffixes = [
            "Token", "Coin", "Cash", "Finance", "Pay", "Network", "Protocol",
            "Chain", "Swap", "Vault", "DAO", "Labs"
        ]
        
        logger.info(f"✅ OpenClaw Agent initialized")
        logger.info(f"⏱️ Interval: {interval_minutes} minutes")
        logger.info(f"📍 Deployer Address: {self.blockchain.address}")
    
    def generate_token_name(self) -> tuple[str, str]:
        """
        Generate a random but meaningful token name and symbol
        
        Returns:
            Tuple of (name, symbol)
        """
        prefix = random.choice(self.token_prefixes)
        suffix = random.choice(self.token_suffixes)
        
        name = f"{prefix}{suffix}"
        
        # Generate symbol from name (2-5 characters)
        if len(name) <= 5:
            symbol = name.upper()
        else:
            # Take first letter of prefix and suffix, add random characters
            symbol = (prefix[0] + suffix[0:3]).upper()
        
        return name, symbol
    
    def generate_initial_supply(self) -> int:
        """
        Generate a random initial supply between 100k and 10M
        
        Returns:
            Initial supply amount
        """
        supplies = [100_000, 500_000, 1_000_000, 5_000_000, 10_000_000]
        return random.choice(supplies)
    
    def deploy_and_announce(self) -> bool:
        """
        Execute one cycle: deploy token and announce on social media
        
        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info("=" * 60)
            logger.info(f"🚀 Starting deployment cycle #{self.deployment_count + 1}")
            logger.info(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info("=" * 60)
            
            # Step 1: Check wallet balance
            balance = self.blockchain.get_balance()
            if balance < 0.001:
                logger.error(f"❌ Insufficient balance: {balance} ETH")
                logger.error("Please fund your wallet with Base Sepolia ETH")
                return False
            
            # Step 2: Generate token parameters
            token_name, token_symbol = self.generate_token_name()
            initial_supply = self.generate_initial_supply()
            
            logger.info(f"💎 Token: {token_name} (${token_symbol})")
            logger.info(f"💰 Supply: {initial_supply:,}")
            
            # Step 3: Deploy token
            logger.info("🔨 Deploying token contract...")
            deployment_result = self.blockchain.deploy_erc20_token(
                name=token_name,
                symbol=token_symbol,
                initial_supply=initial_supply
            )
            
            contract_address = deployment_result['contract_address']
            tx_hash = deployment_result['transaction_hash']
            explorer_url = self.blockchain.get_explorer_url(tx_hash)
            
            logger.info(f"✅ Deployment successful!")
            logger.info(f"📍 Contract: {contract_address}")
            logger.info(f"🔗 Explorer: {explorer_url}")
            
            # Step 4: Announce on social media
            logger.info("📢 Announcing deployment...")
            social_result = self.social.post_token_deployment(
                token_name=token_name,
                token_symbol=token_symbol,
                contract_address=contract_address,
                transaction_hash=tx_hash,
                initial_supply=initial_supply,
                explorer_url=explorer_url
            )
            
            # Log social media results
            for platform, result in social_result.items():
                if platform == 'message':
                    continue
                status = result.get('status', 'unknown')
                if status == 'success':
                    logger.info(f"✅ Posted to {platform}")
                elif status == 'skipped':
                    logger.warning(f"⚠️ Skipped {platform}: {result.get('reason', 'unknown')}")
                else:
                    logger.error(f"❌ Failed to post to {platform}: {result.get('error', 'unknown')}")
            
            # Step 5: Submit to Agent0 for reputation (if enabled)
            if self.agent0:
                try:
                    self.agent0.submit_reputation_proof(
                        task_type="erc20_deployment",
                        proof_data={
                            'contract_address': contract_address,
                            'transaction_hash': tx_hash,
                            'token_name': token_name,
                            'token_symbol': token_symbol,
                            'initial_supply': initial_supply,
                            'gas_used': deployment_result['gas_used'],
                            'social_posted': any(r.get('status') == 'success' for r in social_result.values() if isinstance(r, dict))
                        }
                    )
                    reputation = self.agent0.get_reputation_score()
                    logger.info(f"⭐ Agent reputation: {reputation}")
                except Exception as e:
                    logger.warning(f"Failed to submit Agent0 proof: {e}")
            
            # Step 6: Update statistics
            self.deployment_count += 1
            
            # Save deployment record
            self._save_deployment_record({
                'deployment_number': self.deployment_count,
                'timestamp': datetime.now().isoformat(),
                'token_name': token_name,
                'token_symbol': token_symbol,
                'contract_address': contract_address,
                'transaction_hash': tx_hash,
                'initial_supply': initial_supply,
                'explorer_url': explorer_url,
                'gas_used': deployment_result['gas_used'],
                'social_results': {
                    k: v.get('status') for k, v in social_result.items() if k != 'message'
                },
                'agent0_registered': self.agent0 is not None
            })
            
            logger.info("=" * 60)
            logger.info(f"✅ Cycle #{self.deployment_count} completed successfully!")
            logger.info(f"📊 Total deployments: {self.deployment_count}")
            logger.info(f"⏱️ Agent uptime: {self._get_uptime()}")
            logger.info("=" * 60)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error in deployment cycle: {str(e)}")
            logger.exception(e)
            return False
    
    def _save_deployment_record(self, record: dict):
        """Save deployment record to JSON file"""
        try:
            filename = 'deployments.json'
            
            # Load existing records
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    records = json.load(f)
            else:
                records = []
            
            # Add new record
            records.append(record)
            
            # Save updated records
            with open(filename, 'w') as f:
                json.dump(records, f, indent=2)
                
            logger.info(f"💾 Deployment record saved to {filename}")
            
        except Exception as e:
            logger.error(f"❌ Error saving deployment record: {str(e)}")
    
    def _get_uptime(self) -> str:
        """Get agent uptime as human-readable string"""
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}h {minutes}m {seconds}s"
    
    def run_once(self):
        """Execute one deployment cycle"""
        logger.info("🔄 Running single deployment cycle...")
        success = self.deploy_and_announce()
        if success:
            logger.info("✅ Single cycle completed successfully")
        else:
            logger.error("❌ Single cycle failed")
        return success
    
    def run_continuous(self):
        """
        Run the agent continuously on a schedule
        """
        logger.info("🔄 Starting continuous operation mode")
        logger.info(f"⏱️ Will deploy a new token every {self.interval_minutes} minutes")
        logger.info("Press Ctrl+C to stop")
        
        try:
            while True:
                # Execute deployment cycle
                self.deploy_and_announce()
                
                # Wait for next cycle
                logger.info(f"⏳ Waiting {self.interval_minutes} minutes until next deployment...")
                logger.info(f"⏰ Next deployment at: {self._get_next_run_time()}")
                
                time.sleep(self.interval_seconds)
                
        except KeyboardInterrupt:
            logger.info("\n⚠️ Agent stopped by user")
            logger.info(f"📊 Total deployments: {self.deployment_count}")
            logger.info(f"⏱️ Total uptime: {self._get_uptime()}")
            logger.info("👋 Goodbye!")
        except Exception as e:
            logger.error(f"❌ Fatal error: {str(e)}")
            logger.exception(e)
            raise
    
    def _get_next_run_time(self) -> str:
        """Get next scheduled run time"""
        next_time = datetime.now().timestamp() + self.interval_seconds
        return datetime.fromtimestamp(next_time).strftime('%Y-%m-%d %H:%M:%S')


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='OpenClaw Autonomous Agent')
    parser.add_argument(
        '--interval',
        type=int,
        default=20,
        help='Interval between deployments in minutes (default: 20)'
    )
    parser.add_argument(
        '--once',
        action='store_true',
        help='Run once and exit (useful for testing)'
    )
    parser.add_argument(
        '--agent0',
        action='store_true',
        help='Enable Agent0/ERC-8004 integration for on-chain identity and reputation'
    )
    
    args = parser.parse_args()
    
    try:
        # Create agent
        agent = OpenClawAgent(
            interval_minutes=args.interval,
            enable_agent0=args.agent0
        )
        
        # Run mode
        if args.once:
            agent.run_once()
        else:
            agent.run_continuous()
            
    except Exception as e:
        logger.error(f"Failed to start agent: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
