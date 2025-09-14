# Nansen API - Smart Money Token Analysis

This project fetches the top tokens accumulated by Smart Money wallets using the Nansen API.

## Setup

### 1. Environment Configuration

Create a `.env` file in the project root with your Nansen API key:

```bash
apiKey=your_nansen_api_key_here
```

**Important**: Replace `your_nansen_api_key_here` with your actual Nansen API key.

### 2. Install Dependencies (Python)

```bash
pip install -r requirements.txt
```

### 3. Streamlit Secrets Configuration

Before running the Streamlit app, you must create a `.streamlit/secrets.toml` file in the project root. This file should contain your Nansen API key and authentication credentials:

```toml
apiKey = "YOUR_NANSEN_API_KEY"

[auth]
redirect_uri = "YOUR_REDIRECT_URI"
cookie_secret = "YOUR_COOKIE_SECRET"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
server_metadata_url = "YOUR_SERVER_METADATA_URL"
```

**Note:**

- Replace the example values with your actual credentials.
- This file is required for authentication and API access in the Streamlit app.

## Usage

### Option 1: Python Script (Recommended)

Run the Python script to fetch and display Smart Money token data:

```bash
python smart_money_tokens.py
```

**Features:**

- Fetches top 3 tokens accumulated by Smart Money wallets in the last 24 hours
- Displays formatted results with token details
- Saves raw data to `smart_money_tokens_data.json`
- Includes error handling and validation

### Option 2: cURL Script

Run the shell script for quick data fetching:

```bash
./fetch_smart_money_tokens.sh
```

**Requirements:**

- `jq` for JSON formatting (optional but recommended)
- Install with: `brew install jq` (macOS) or `apt-get install jq` (Ubuntu)

## API Endpoint Details

- **Base URL**: `https://api.nansen.ai/api/beta`
- **Endpoint**: `/smart-money/tokens`
- **Authentication**: `apiKey` header
- **Parameters**:
  - `timeframe`: 1d, 7d, 30d
  - `limit`: Number of results (default: 3)
  - `sort_by`: accumulation_volume
  - `order`: desc

## Output Format

The script displays:

- Token symbol and name
- Contract address
- Blockchain chain
- Accumulation volume (USD)
- Number of Smart Money wallets
- 24-hour price change

## Error Handling

- **Missing API Key**: Prompts to create `.env` file
- **Network Errors**: Displays detailed error messages
- **Rate Limiting**: Follows Nansen API rate limits (20req/s, 500req/min)

## Files

- `smart_money_tokens.py` - Main Python script
- `fetch_smart_money_tokens.sh` - cURL-based shell script
- `requirements.txt` - Python dependencies
- `.env` - API key configuration (create this file)
- `.gitignore` - Excludes `.env` from version control

## Example Output

```
Top 3 Tokens Accumulated by Smart Money (Last 24h)
============================================================

1. ETH (Ethereum)
   Contract: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
   Chain: ethereum
   Accumulation Volume: $12,345,678.90
   Smart Money Wallets: 45
   Price Change 24h: 2.34%

2. USDC (USD Coin)
   Contract: 0xA0b86a33E6441b8C4C8C8C8C8C8C8C8C8C8C8
   Chain: ethereum
   Accumulation Volume: $8,765,432.10
   Smart Money Wallets: 32
   Price Change 24h: 0.12%

3. MATIC (Polygon)
   Contract: 0x7D1AfA7B718fb893dB30A3aBc0Cfc608aCfeBBbb
   Chain: polygon
   Accumulation Volume: $5,432,109.87
   Smart Money Wallets: 28
   Price Change 24h: -1.23%
```

## Launch the Streamlit Dashboard

The Streamlit app provides interactive views for Smart Money Inflows/Holdings, Token Screener, and Flow Intelligence.

1. Ensure your environment variables are set in `.env` at the repo root:

```bash
apiKey=YOUR_NANSEN_API_KEY
NANSEN_BASE_URL=https://api.nansen.ai/api/beta
# Optional: if you later add a documented candles endpoint
# NANSEN_CANDLES_PATH=/tgm/candles
```

2. Install dependencies (recommended to use a virtual environment):

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

4. Open the URL shown in the terminal (usually `http://localhost:8501`).

Notes:

- If you see dependency conflicts (e.g., scipy vs numpy), activate the `.venv` and reinstall requirements.
- The app uses these Nansen endpoints:
  - `/api/beta/smart-money/inflows`
  - `/api/beta/smart-money/holdings`
  - `/api/beta/token-screener`
  - `/api/beta/tgm/flow-intelligence`
- The Token Screener tab lets you select a token and load price history via `/api/beta/tgm/flows`.
