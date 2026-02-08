# 🤖 OpenClaw: The Autonomous Creative Agent on Base 🟦

**OpenClaw** is a fully autonomous, no-human-in-the-loop AI agent built for the **Base** ecosystem. It doesn't just deploy code; it creates, visualizes, and engages on-chain and on social media using **AI Image Generation** and **Social Intelligence**.

---

## 🏆 5ETH Prize Competition Specs
- **Agent Type**: 100% Autonomous (No human in the loop)
- **On-chain Primitives**: 
    - **ERC20**: Autonomous Token Deployments (QuantumPay, ApexChain, etc.)
    - **ERC721**: Autonomous/Remote NFT Collection Deployments.
- **Novelty Factors**:
    - **AI Artist**: Generates unique futuristic visuals for every single deployment.
    - **Social Listening**: Scans Farcaster for user context to write original 'Hype' posts.
    - **Remote Control**: Responds to Warpcast commands (!deploy, !nft).
- **Compliance**: **ERC-8004** Standard via Agent0 SDK.

## ✨ Core Capabilities

### 1. 🟦 On-chain Mastery (Base)
OpenClaw continuously building on Base. It handles smart contract deployments for Tokens and NFTs autonomously.
- **Agent ID**: `84532:170729`
- **Verified Proofs**: Every transaction is logged and verified via Agent0 reputation signals.

### 2. 🎨 AI Visual Creativity
Unlike standard bots, OpenClaw is an artist. It uses **dynamic AI image generation** to create custom logos and artworks for its social announcements. Every token gets its own unique visual identity.

### 3. 📡 Socio-Autonomous Intelligence
OpenClaw "lives" on Farcaster. 
- **Listening**: It periodically checks the creator's profile (`furqan.base.eth`) for inspiration.
- **Engagement**: It writes its own posts based on the latest community vibes.
- **Execution**: Can be triggered by remote on-chain commands directly from a Warpcast post.

---

## 🛠️ Architecture
- `agent.py`: The "Brain" – handling the logic loop and social listening.
- `blockchain.py`: The "Hands" – deploying ERC20 and ERC721 contracts.
- `social.py`: The "Voice" – integrating Farcaster, X, and AI Image APIs.
- `agent0_integration.py`: The "Identity" – ERC-8004 feedback and registry.

## 🚀 Live Demo & Proof of Work
- **Live Dashboard**: [https://agent0-five.vercel.app/](https://agent0-five.vercel.app/)
- **Farcaster Profile**: [furqan.base.eth](https://warpcast.com/furqan.base.eth) (See live AI posts and deployments)

---

### 📂 Quick Start
1. `pip install -r requirements.txt`
2. Set `RPC_URL`, `PRIVATE_KEY`, `FARCASTER_API_KEY` in `.env`.
3. Run: `python agent.py --agent0 --interval 20`

*Built with ❤️ for the Base BBQ & Agent0 Ecosystem.*
