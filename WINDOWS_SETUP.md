# 🪟 Windows Python Installation Guide

## Step-by-Step Python Installation for Windows

### Step 1: Download Python

1. Open your browser and go to: **https://www.python.org/downloads/**
2. You'll see a big yellow button that says **"Download Python 3.x.x"**
3. Click it to download the installer (about 25 MB)

### Step 2: Run the Installer

1. Open the downloaded file (usually in your Downloads folder)
2. **⚠️ CRITICAL**: Check the box that says **"Add Python to PATH"** at the bottom
   ```
   ☑️ Add Python 3.x to PATH  ← MUST CHECK THIS!
   ```
3. Click **"Install Now"**
4. Wait for installation (takes 2-3 minutes)
5. Click **"Close"** when done

### Step 3: Verify Installation

1. Press `Windows + R`
2. Type `cmd` and press Enter
3. In the command prompt, type:
   ```cmd
   python --version
   ```
4. You should see: `Python 3.x.x`
5. Type:
   ```cmd
   pip --version
   ```
6. You should see: `pip 24.x.x from...`

✅ **If both commands work, you're ready!**

### Step 4: Install Dependencies for OpenClaw

Open PowerShell (right-click Start → Windows PowerShell) and run:

```powershell
# Navigate to your project
cd f:\myagent

# Install required packages
pip install web3==6.15.1
pip install eth-account==0.11.0
pip install python-dotenv==1.0.0
pip install requests==2.31.0
pip install requests-oauthlib==1.3.1
```

Or install all at once:
```powershell
pip install -r requirements.txt
```

### Step 5: Set Up Your Environment

1. Create your `.env` file:
   ```powershell
   copy .env.example .env
   ```

2. Edit `.env` with Notepad:
   ```powershell
   notepad .env
   ```

3. Add your credentials:
   ```env
   RPC_URL=https://sepolia.base.org
   PRIVATE_KEY=your_wallet_private_key_here
   ```

4. Save and close Notepad

### Step 6: Get Test ETH

1. Go to: https://www.coinbase.com/faucets/base-ethereum-goerli-faucet
2. Enter your wallet address
3. Complete the captcha
4. Receive free Base Sepolia ETH (usually 0.1-0.5 ETH)

### Step 7: Run Your Agent!

```powershell
# Test run (basic mode)
python agent.py --once

# Test run (with Agent0/ERC-8004)
python agent.py --once --agent0

# Continuous mode (every 20 minutes)
python agent.py --agent0

# Custom interval (every 60 minutes)
python agent.py --agent0 --interval 60
```

## 🎉 Expected Output

When you run with `--agent0`, you should see:

```
🤖 Initializing OpenClaw Agent...
✅ Connected to blockchain. Address: 0x...
✅ Chain ID: 84532
🔨 Registering agent: OpenClaw
✅ Agent registered!
🆔 Agent ID: 12345678
📍 Address: 0x...
🔧 Capabilities: erc20_deployment, social_posting, autonomous_operation
✅ Agent0 integration enabled
💰 Current balance: 0.05 ETH
💎 Token: OpenFinance ($OFIN)
💰 Supply: 1,000,000
🔨 Deploying token contract...
📝 Transaction sent: 0x...
⏳ Waiting for transaction confirmation...
✅ Token deployed successfully!
📍 Contract Address: 0x...
🔗 Transaction Hash: 0x...
📢 Announcing deployment...
✅ Posted to Farcaster
⚠️ Skipped x: missing_credentials
📝 Submitting reputation proof...
✅ Reputation proof submitted
📄 Proof saved to: proofs/12345678_erc20_deployment_0x....json
⭐ Agent reputation: 1
✅ Cycle #1 completed successfully!
📊 Total deployments: 1
```

## 🐛 Troubleshooting

### "Python is not recognized"
**Solution:**
1. Uninstall Python
2. Reinstall and **MAKE SURE** to check "Add Python to PATH"
3. Restart PowerShell/cmd

### "pip is not recognized"
**Solution:**
```powershell
python -m pip install --upgrade pip
```

### "ModuleNotFoundError: No module named 'web3'"
**Solution:**
```powershell
pip install web3
```

### "ConnectionError: Failed to connect to RPC"
**Solutions:**
- Check your RPC_URL in `.env`
- Try alternative: `https://base-sepolia.blockpi.network/v1/rpc/public`
- Verify internet connection

### "Insufficient balance"
**Solution:**
- Visit: https://www.coinbase.com/faucets/base-ethereum-goerli-faucet
- Get free test ETH
- Each deployment costs ~0.001-0.003 ETH in gas

### Agent runs but no Agent0 integration
**Check:**
```powershell
# Make sure agent0_integration.py exists
dir agent0_integration.py

# Run with --agent0 flag
python agent.py --once --agent0
```

## 📁 Check Your Results

After a successful run:

```powershell
# View agent identity
type agent0_metadata.json

# View deployments
type deployments.json

# View reputation proofs
dir proofs
type proofs\*.json
```

## 🚀 Running 24/7

### Option 1: Keep PowerShell Open
Just leave the window open:
```powershell
python agent.py --agent0 --interval 60
```

### Option 2: Use Windows Task Scheduler
1. Search for "Task Scheduler"
2. Create Basic Task
3. Set trigger (e.g., "At startup")
4. Action: Start a program
5. Program: `python`
6. Arguments: `f:\myagent\agent.py --agent0`
7. Start in: `f:\myagent`

### Option 3: Use Replit (see REPLIT_SETUP.md)
For true 24/7 operation without keeping your PC on.

## 🎯 Next Steps

Once Python is installed and working:

1. ✅ **Test basic deployment**
   ```powershell
   python agent.py --once
   ```

2. ✅ **Test Agent0 integration**
   ```powershell
   python agent.py --once --agent0
   ```

3. ✅ **Check your agent identity**
   ```powershell
   type agent0_metadata.json
   ```

4. ✅ **Run continuously**
   ```powershell
   python agent.py --agent0
   ```

5. 🎉 **You're now running an ERC-8004 compliant AI agent!**

## 📚 Learn More

- Read: `README_AGENT0.md` for Agent0 features
- Read: `GETTING_STARTED.md` for complete guide
- Check: `PROJECT_SUMMARY.txt` for overview

---

**Your agent is production-ready!** Just install Python and go! 🚀
