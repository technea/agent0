# 🌐 Replit Setup Guide - Run OpenClaw 24/7

## Why Replit?

✅ Python pre-installed  
✅ Free tier available  
✅ Runs 24/7 (with Always On)  
✅ No local setup needed  
✅ Built-in secrets management  
✅ Web-based IDE  

## Step-by-Step Replit Setup

### Step 1: Create Replit Account

1. Go to: **https://replit.com/**
2. Click **"Sign up"**
3. Create account (free)
4. Verify your email

### Step 2: Create New Repl

1. Click **"+ Create Repl"**
2. Choose **"Python"** template
3. Name it: **"openclaw-agent"**
4. Click **"Create Repl"**

### Step 3: Upload Your Files

You have two options:

**Option A: Upload via Interface**
1. Click the **three dots** (•••) next to "Files"
2. Click **"Upload file"**
3. Upload these files ONE BY ONE:
   - `agent.py`
   - `blockchain.py`
   - `social.py`
   - `agent0_integration.py`
   - `requirements.txt`
   - `.gitignore`

**Option B: Use Git (Advanced)**
```bash
# In Replit Shell
git clone <your-repo-url>
cd openclaw-agent
```

### Step 4: Configure Secrets

1. Click the **🔒 Lock icon** in the left sidebar (Secrets)
2. Click **"New Secret"**
3. Add these secrets:

| Key | Value |
|-----|-------|
| `RPC_URL` | `https://sepolia.base.org` |
| `PRIVATE_KEY` | Your wallet private key |
| `FARCASTER_API_KEY` | Your Neynar API key (optional) |
| `FARCASTER_SIGNER_UUID` | Your signer UUID (optional) |
| `X_API_KEY` | Your Twitter/X API key (optional) |
| `X_API_SECRET` | Your Twitter/X API secret (optional) |
| `X_ACCESS_TOKEN` | Your Twitter/X access token (optional) |
| `X_ACCESS_SECRET` | Your Twitter/X access secret (optional) |

**Note:** Only `RPC_URL` and `PRIVATE_KEY` are required. Social media keys are optional.

### Step 5: Install Dependencies

In the Replit Shell (bottom of screen), run:

```bash
pip install web3==6.15.1 eth-account==0.11.0 python-dotenv==1.0.0 requests==2.31.0 requests-oauthlib==1.3.1
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 6: Create .replit Configuration

1. Click **"Show hidden files"** in the Files panel
2. Edit or create `.replit` file:

```toml
run = "python agent.py --agent0"

[nix]
channel = "stable-23_11"

[deployment]
run = ["sh", "-c", "python agent.py --agent0"]
```

### Step 7: Get Test ETH

1. Visit: https://www.coinbase.com/faucets/base-ethereum-goerli-faucet
2. Enter your wallet address
3. Get free Base Sepolia ETH

### Step 8: Test Run

Click the big green **"Run"** button at the top!

You should see:
```
🤖 Initializing OpenClaw Agent...
✅ Connected to blockchain
🔨 Registering agent: OpenClaw
✅ Agent registered!
🆔 Agent ID: 12345678
✅ Agent0 integration enabled
...
```

## 📁 File Structure in Replit

Your Repl should look like this:

```
openclaw-agent/
├── .replit                  ← Run configuration
├── agent.py                 ← Main agent
├── blockchain.py            ← ERC20 deployment
├── social.py                ← Social media
├── agent0_integration.py    ← ERC-8004 integration
├── requirements.txt         ← Dependencies
├── .gitignore              ← Git ignore
├── deployments.json         ← Auto-created on first run
├── agent0_metadata.json     ← Auto-created with --agent0
└── proofs/                  ← Auto-created with --agent0
    └── *.json
```

## 🎮 Running Your Agent

### Quick Test (Once)
In Shell:
```bash
python agent.py --once --agent0
```

### Continuous Mode (Default)
Just click **"Run"** button, or in Shell:
```bash
python agent.py --agent0
```

### Custom Interval
In Shell:
```bash
python agent.py --agent0 --interval 60  # Every 60 minutes
```

## 🔄 Keep It Running 24/7

### Free Tier (Limited)
- Repl sleeps after inactivity
- Use UptimeRobot to ping and keep alive:
  1. Get your Repl URL: `https://openclaw-agent.your-username.repl.co`
  2. Sign up at: https://uptimerobot.com
  3. Add HTTP(s) monitor with your Repl URL
  4. Set interval: 5 minutes

### Always On (Paid)
1. Click **"Always On"** in Repl settings
2. Subscribe to Replit Core ($7/month)
3. Your agent runs 24/7 automatically

## 🛠️ Accessing Files

### View Agent Metadata
```bash
cat agent0_metadata.json
```

### View Deployments
```bash
cat deployments.json
```

### View Reputation Proofs
```bash
ls proofs/
cat proofs/*.json
```

### View Logs
```bash
cat openclaw_agent.log
tail -f openclaw_agent.log  # Follow logs in real-time
```

## 📊 Monitoring Your Agent

### Check Status
In Shell:
```bash
ps aux | grep agent.py
```

### View Recent Logs
```bash
tail -20 openclaw_agent.log
```

### Check Reputation
```python
# In Replit Shell
python
>>> from agent0_integration import Agent0Integration
>>> from web3 import Web3
>>> from eth_account import Account
>>> import os
>>> w3 = Web3(Web3.HTTPProvider(os.environ['RPC_URL']))
>>> account = Account.from_key(os.environ['PRIVATE_KEY'])
>>> agent0 = Agent0Integration(w3, account)
>>> print(f"Agent ID: {agent0.agent_id}")
>>> print(f"Reputation: {agent0.get_reputation_score()}")
```

## 🐛 Troubleshooting Replit

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Secrets not loading"
Make sure secrets are named EXACTLY as shown (case-sensitive):
- `RPC_URL` (not `rpc_url`)
- `PRIVATE_KEY` (not `private_key`)

### "RPC connection failed"
- Check RPC_URL in Secrets
- Try alternative: `https://base-sepolia.blockpi.network/v1/rpc/public`

### "Insufficient balance"
- Get more ETH from faucet
- Check your wallet address

### Repl stops running
**Free Tier:**
- Set up UptimeRobot to ping your Repl
- Or upgrade to Always On

**Paid Tier:**
- Enable "Always On" in settings

## 🚀 Production Tips

### 1. Environment Variables
Instead of `.env` file, Replit uses Secrets (already configured if you followed Step 4)

### 2. Logging
Logs are saved to `openclaw_agent.log`. Download periodically:
```bash
# Download via Shell
zip logs.zip openclaw_agent.log
# Then download via Files panel
```

### 3. Backup Proofs
Regularly backup your `proofs/` folder:
```bash
zip -r proofs_backup.zip proofs/
```

### 4. Update Code
Edit files directly in Replit editor, changes apply immediately.

### 5. Multiple Agents
Create multiple Repls for different agents:
- openclaw-agent-1 (fast: every 10 min)
- openclaw-agent-2 (slow: every 60 min)
- openclaw-agent-test (testing)

## 🎯 Quick Commands Cheat Sheet

```bash
# Install deps
pip install -r requirements.txt

# Test once
python agent.py --once --agent0

# Run continuous
python agent.py --agent0

# View logs
tail -f openclaw_agent.log

# View deployments
cat deployments.json | python -m json.tool

# Check agent status
cat agent0_metadata.json

# View proofs
ls -la proofs/

# Stop agent
Ctrl + C
```

## 📱 Mobile Access

You can monitor and control your agent from your phone:
1. Install Replit Mobile app
2. Login with your account
3. Access your openclaw-agent Repl
4. View logs and files
5. Start/stop the agent

## 💰 Cost Breakdown

| Feature | Free Tier | Core ($7/mo) |
|---------|-----------|--------------|
| Run agent | ✅ Yes (sleeps) | ✅ Always On |
| Storage | 500 MB | 5 GB |
| Private Repls | 5 | Unlimited |
| Secrets | ✅ Yes | ✅ Yes |
| Good for | Testing | Production |

## 🎉 You're Live!

Your agent is now running on Replit with:
- ✅ 24/7 uptime (with Always On or UptimeRobot)
- ✅ Agent0/ERC-8004 integration
- ✅ Automatic deployments
- ✅ Reputation tracking
- ✅ No local setup needed

## 📚 Next Steps

1. ✅ Verify agent is running
2. ✅ Check first deployment in `deployments.json`
3. ✅ Monitor reputation in `proofs/`
4. ✅ Set up UptimeRobot (free tier) or Always On (paid)
5. 🎊 You have a production AI agent!

## 🆘 Need Help?

- Check logs: `cat openclaw_agent.log`
- Read: `README_AGENT0.md` for Agent0 details
- Read: `GETTING_STARTED.md` for overview

---

**Your ERC-8004 compliant agent is running in the cloud!** 🚀☁️
