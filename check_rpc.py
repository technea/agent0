from web3 import Web3
import sys

def check():
    rpc = 'https://sepolia.base.org'
    print(f"Testing RPC: {rpc}")
    try:
        w3 = Web3(Web3.HTTPProvider(rpc))
        connected = w3.is_connected()
        print(f"Connected: {connected}")
        if connected:
            print(f"Latest block: {w3.eth.block_number}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check()
