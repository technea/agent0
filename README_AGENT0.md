# 🚀 OpenClaw Agent with Agent0 SDK (ERC-8004)

## Overview

**OpenClaw** is now fully integrated with the official **Agent0 SDK**! This enables:
- **On-chain Identity**: Your agent is represented by an NFT on Base Sepolia.
- **Verifiable Reputation**: Building a track record that other agents can trust.
- **Discoverability**: Registering with a global standard for AI agent coordination.

## Quick Setup

### 1. Install Dependencies

Ensure you have the latest requirements:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment

The agent requires **Base Sepolia ETH** for registration and reputation signals.

Edit `.env`:
```bash
# Required
RPC_URL=https://sepolia.base.org
PRIVATE_KEY=your_private_key_without_0x_prefix

# Optional (for social media)
FARCASTER_API_KEY=your_key
X_API_KEY=your_key
```

### 3. Run the Agent

**With Agent0/ERC-8004 integration:**
```bash
python agent.py --agent0
```

**Run once (test mode):**
```bash
python agent.py --once --agent0
```

## How It Works

### Identity (Identity Registry)
When you first run with `--agent0`, the agent checks `agent0_metadata.json`. If missing or not registered, it will:
1. Connect to the **Identity Registry** on Base Sepolia.
2. Mint a new Agent NFT.
3. Save the assigned `agentId` (e.g., `84532:42`).

### Reputation (Reputation Registry)
After every successful token deployment:
1. OpenClaw generates a reputation signal via the `agent0-sdk`.
2. A transaction is sent to the **Reputation Registry**.
3. Your agent's "Trust Score" (feedback count) increases.

### Verifying Results
You can check your agent's reputation on the [ERC-8004 Explorer](https://8004agents.ai) or by running:
```bash
python test_agent0.py
```

## File Structure

- `agent0_integration.py`: The bridge to the official Agent0 SDK.
- `agent0_metadata.json`: Stores your on-chain identity details.
- `proofs/`: Local records of submitted reputation signals.

## Registry Addresses (Base Sepolia)
- **Identity Registry**: `0x8004AA63c570c570eBF15376c0dB199918BFe9Fb`
- **Reputation Registry**: `0x8004bd8daB57f14Ed299135749a5CB5c42d341BF`

## Troubleshooting

### Connection Issues
If the agent fails to connect to the RPC, verify your `RPC_URL` is working. You can test it with `python check_rpc.py`.

### Registration Fails
- Ensure your wallet has at least **0.01 Base Sepolia ETH**.
- Verify your `PRIVATE_KEY` is a valid 64-character hex string (no `0x` prefix).

### API Errors
If you see `agent0_sdk` related errors, ensure the package is up to date:
```bash
pip install agent0-sdk --upgrade
```

---

**Welcome to the Agent0 ecosystem!** Your OpenClaw agent is now more than just a script; it's a verifiable on-chain actor. 🤖🚀
