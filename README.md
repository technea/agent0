# 🤖 OpenClaw: Autonomous ERC-8004 Agent

**OpenClaw** is a state-of-the-art autonomous AI agent integrated with the **Agent0 SDK**. It demonstrates on-chain identity, verifiable reputation, and autonomous task execution on the **Base Sepolia** network.

## 🏆 Reward Submission Details
- **Agent Standard**: ERC-8004 (Identity, Reputation, Validation)
- **Chain**: Base Sepolia (84532)
- **Agent ID**: `84532:170729` (Registered via Agent0 SDK)
- **Capabilities**: `erc20_deployment`, `social_announcement`, `autonomous_scheduling`

## ✨ Core Features
1. **On-chain Identity**: Minted as a unique NFT via the Agent0 Identity Registry.
2. **Verifiable Reputation**: Every token deployment triggers a reputation signal (Feedback) to build a global trust score.
3. **Autonomous Operations**: Deploys ERC20 tokens and announces them on Farcaster/X on a scheduled interval.
4. **Live Dashboard**: Real-time visualization of agent activity and reputation proofs.

## 🛠️ Security & Architecture
- Uses **Agent0 SDK** for standard-compliant registry interactions.
- Resilient blockchain logic with simulated fallbacks for gas-less testing.
- Secure environment management via `.env`.

## 📂 Project Structure
- `agent.py`: Main autonomous loop and orchestration.
- `agent0_integration.py`: ERC-8004 compliance layer.
- `blockchain.py`: Smart contract deployment logic.
- `social.py`: Multi-platform social media integration.
- `dashboard.html`: Live monitoring interface.

## 🚀 How to Run
1. `pip install -r requirements.txt`
2. Configure `.env` with Base Sepolia RPC and Private Key.
3. Start the agent: `python agent.py --agent0 --interval 20`
4. View dashboard: Open `dashboard.html`

---
*Built for the Agent0 Ecosystem & ERC-8004 Standard.*
