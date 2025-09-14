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
streamlit run streamlit_app.py --server.port 8501
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
