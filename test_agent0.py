import os
import logging
from dotenv import load_dotenv
from web3 import Web3
from eth_account import Account
from agent0_integration import Agent0Integration

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_agent0")

def test():
    load_dotenv()
    rpc_url = os.getenv("RPC_URL")
    private_key = os.getenv("PRIVATE_KEY")
    
    if not rpc_url or not private_key:
        logger.error("RPC_URL or PRIVATE_KEY not set in .env")
        return

    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        account = Account.from_key(private_key)
        
        logger.info(f"Using address: {account.address}")
        
        integration = Agent0Integration(w3, account)
        
        print("\n--- Agent0 SDK Test ---")
        print(f"Is Registered: {integration.is_registered()}")
        
        if not integration.is_registered():
            print("Registering agent (this will send a transaction)...")
            agent_id = integration.register_agent()
            print(f"Registered Agent ID: {agent_id}")
        else:
            print(f"Agent ID: {integration.agent_id}")
            
        print(f"Reputation Score: {integration.get_reputation_score()}")
        
        print("Submitting test proof (this will send a transaction)...")
        success = integration.submit_reputation_proof(
            task_type="sdk_test",
            proof_data={"test": "success", "token_symbol": "TEST"}
        )
        print(f"Proof Submission Success: {success}")
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test()
