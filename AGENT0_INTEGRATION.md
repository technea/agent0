# 🚀 Integrating OpenClaw with Agent0 SDK (ERC-8004)

## What is ERC-8004?

**ERC-8004** is an Ethereum standard for **AI Agent Coordination** that provides:

1. **Identity Registry** - On-chain identity for agents (ERC-721 based)
2. **Reputation Registry** - Collects and distributes feedback/reputation signals
3. **Validation Registry** - Verifies agent execution integrity

## Implementation with Office Agent0 SDK

The OpenClaw agent now uses the official `agent0-sdk` to interact with ERC-8004 registries on **Base Sepolia**.

### Key Components

*   **Identity**: Agents are minted as NFTs on the Identity Registry.
*   **Reputation**: Agents build reputation by submitting feedback/signals to the Reputation Registry.
*   **Validation**: Each task completion is recorded on-chain.

## Configuration

Update your `.env` file with Base Sepolia credentials:

```bash
RPC_URL=https://sepolia.base.org
PRIVATE_KEY=your_private_key_here
```

## How to Use

### 1. Installation

```bash
pip install -r requirements.txt
```

### 2. Registration

When running with the `--agent0` flag, the agent automatically checks if it's already registered via a local `agent0_metadata.json` file. If not, it performs an on-chain registration (mints an identity NFT).

```python
# From agent0_integration.py
agent = sdk.createAgent(name="OpenClaw", description="...")
handle = agent.register(agentUri="")
handle.wait() # Waits for transaction confirmation
```

### 3. Submitting Reputation

After each successful token deployment, the agent submits a reputation signal to itself. This represents a "proof of work" that other agents can verify.

```python
# From agent0_integration.py
sdk.giveFeedback(
    agentId=self.agent_id,
    value=1.0, 
    tag1="erc20_deployment",
    tag2="SYMBOL"
)
```

## Advanced Example: Custom Integration

If you want to use the SDK manually:

```python
from agent0_sdk import SDK
from web3 import Web3
from eth_account import Account

# Initialize
w3 = Web3(Web3.HTTPProvider(rpc_url))
account = Account.from_key(private_key)

sdk = SDK(
    chainId=84532, 
    rpcUrl=rpc_url,
    signer=account,
    registryOverrides={
        84532: {
            "IDENTITY": "0x8004AA63c570c570eBF15376c0dB199918BFe9Fb",
            "REPUTATION": "0x8004bd8daB57f14Ed299135749a5CB5c42d341BF"
        }
    }
)

# Search for agents
agents = sdk.searchAgents(name="OpenClaw")
for agent in agents:
    print(f"Found agent: {agent.name} ID: {agent.agentId}")

# Get reputation summary
reputation = sdk.getReputationSummary("84532:123")
print(f"Agent score: {reputation['count']}")
```

## Architecture

1.  **OpenClaw** performs a task (e.g., deploys a token).
2.  **BlockchainManager** returns the transaction results.
3.  **Agent0Integration** takes these results and submits a "Feedback" transaction to the **Reputation Registry**.
4.  The agent's reputation score increases on-chain, verifiable by anyone using the `agent0-sdk` or the [8004 Explorer](https://8004agents.ai).

## Benefits

*   **Trustless Discovery**: Other agents can find OpenClaw via the registry.
*   **Verifiable History**: Every deployment is backed by an on-chain reputation signal.
*   **Interoperability**: Works with any other ERC-8004 compliant agent or tool.
