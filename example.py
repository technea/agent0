"""
Example usage script for OpenClaw agent
Demonstrates how to use each module independently
"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("=" * 60)
print("OpenClaw Agent - Example Usage")
print("=" * 60)

# Example 1: Blockchain Operations
print("\n1️⃣ BLOCKCHAIN MODULE EXAMPLE")
print("-" * 60)

try:
    from blockchain import BlockchainManager
    
    # Initialize blockchain manager
    bm = BlockchainManager()
    print(f"✅ Connected to blockchain")
    print(f"📍 Address: {bm.address}")
    
    # Check balance
    balance = bm.get_balance()
    print(f"💰 Balance: {balance} ETH")
    
    # Deploy a test token (commented out - uncomment to actually deploy)
    # result = bm.deploy_erc20_token(
    #     name="Example Token",
    #     symbol="EXMP",
    #     initial_supply=1000000
    # )
    # print(f"✅ Token deployed at: {result['contract_address']}")
    # print(f"🔗 Explorer: {bm.get_explorer_url(result['transaction_hash'])}")
    
except Exception as e:
    print(f"❌ Blockchain example failed: {str(e)}")

# Example 2: Social Media Operations
print("\n2️⃣ SOCIAL MEDIA MODULE EXAMPLE")
print("-" * 60)

try:
    from social import SocialMediaManager
    
    # Initialize social media manager
    sm = SocialMediaManager()
    print("✅ Social media manager initialized")
    
    # Post a test message (commented out - uncomment to actually post)
    # result = sm.post_status_update("Testing OpenClaw agent! 🤖")
    # print(f"✅ Posted to platforms: {len([r for r in result.values() if isinstance(r, dict) and r.get('status') == 'success'])}")
    
except Exception as e:
    print(f"❌ Social media example failed: {str(e)}")

# Example 3: Full Agent Cycle
print("\n3️⃣ AGENT MODULE EXAMPLE")
print("-" * 60)

try:
    from agent import OpenClawAgent
    
    # Initialize agent
    agent = OpenClawAgent(interval_minutes=20)
    print(f"✅ Agent initialized")
    print(f"⏱️ Interval: {agent.interval_minutes} minutes")
    print(f"📊 Deployments so far: {agent.deployment_count}")
    
    # Run single deployment (commented out - uncomment to deploy)
    # print("\n🚀 Running single deployment cycle...")
    # success = agent.run_once()
    # if success:
    #     print("✅ Deployment successful!")
    # else:
    #     print("❌ Deployment failed")
    
except Exception as e:
    print(f"❌ Agent example failed: {str(e)}")

# Example 4: Read Deployment History
print("\n4️⃣ DEPLOYMENT HISTORY")
print("-" * 60)

try:
    import json
    
    if os.path.exists('deployments.json'):
        with open('deployments.json', 'r') as f:
            deployments = json.load(f)
        
        print(f"📊 Total deployments: {len(deployments)}")
        
        if deployments:
            latest = deployments[-1]
            print(f"\nLatest deployment:")
            print(f"  Token: {latest['token_name']} ({latest['token_symbol']})")
            print(f"  Contract: {latest['contract_address']}")
            print(f"  Time: {latest['timestamp']}")
            print(f"  Supply: {latest['initial_supply']:,}")
    else:
        print("No deployment history yet. Run the agent to create deployments!")
        
except Exception as e:
    print(f"❌ Failed to read history: {str(e)}")

print("\n" + "=" * 60)
print("Examples complete!")
print("=" * 60)
print("\n💡 TIP: Edit this file to uncomment and test specific features")
print("📖 See README.md for full documentation")
