# 🚀 OpenClaw Quick Start Guide

## Complete Setup in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment
```bash
# Copy template
cp .env.example .env

# Edit with your credentials
# Windows: notepad .env
# Mac/Linux: nano .env
```

### Step 3: Get Free Test ETH
Visit: https://www.coinbase.com/faucets/base-ethereum-goerli-faucet
- Enter your wallet address
- Receive Base Sepolia ETH (free)

### Step 4: Get API Keys (Optional)

**Farcaster (via Neynar):**
- Sign up: https://neynar.com/
- Get API key + Signer UUID

**X (Twitter):**
- Apply: https://developer.twitter.com/
- Get API credentials

### Step 5: Run!

**Test run (deploys once):**
```bash
python agent.py --once
```

**Continuous mode (every 20 min):**
```bash
python agent.py
```

**Custom interval (every 60 min):**
```bash
python agent.py --interval 60
```

## 🌐 Replit Setup

1. Create new Repl
2. Upload all files
3. Click 🔒 Secrets and add:
   - `RPC_URL`
   - `PRIVATE_KEY`
   - `FARCASTER_API_KEY` (optional)
   - `X_API_KEY` (optional)
4. Run: `python agent.py`

## 🎯 What Happens

Every cycle:
1. ✅ Generates random token name & symbol
2. ✅ Deploys ERC20 contract to Base Sepolia
3. ✅ Posts announcement to Farcaster & X
4. ✅ Saves deployment to `deployments.json`
5. ✅ Waits for next interval

## 📊 Monitor Progress

- **Console**: Real-time logs
- **openclaw_agent.log**: Full history
- **deployments.json**: All deployments

## ⚠️ Minimum Requirements

- Python 3.8+
- 0.001 ETH per deployment (gas)
- Base Sepolia RPC URL
- Wallet private key

## 🆘 Quick Fixes

**"Module not found"**
```bash
pip install -r requirements.txt
```

**"Failed to connect"**
- Check RPC_URL in .env
- Try: `https://sepolia.base.org`

**"Insufficient balance"**
- Get more ETH from faucet
- Need ~0.003 ETH per deployment

## 📞 Need Help?

Check README.md for detailed docs!
