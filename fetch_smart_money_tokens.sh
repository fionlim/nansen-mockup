#!/bin/bash

# Nansen API - Smart Money Token Accumulation (cURL version)
# Fetches top 3 tokens accumulated by Smart Money wallets in the last 24 hours

# Check if .env file exists and source it
if [ -f .env ]; then
    source .env
else
    echo "Error: .env file not found"
    echo "Please create a .env file with: apiKey=your_nansen_api_key_here"
    exit 1
fi

# Check if API key is set
if [ -z "$apiKey" ]; then
    echo "Error: API key not found in .env file"
    echo "Please add your Nansen API key to .env: apiKey=your_actual_api_key"
    exit 1
fi

echo "Fetching Smart Money token accumulation data..."
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Make API request
curl -s -X POST \
  "https://api.nansen.ai/api/beta/smart-money/holdings" \
  -H "apiKey: $apiKey" \
  -H "Content-Type: application/json" \
  -d '{
    "parameters": {
      "smFilter": ["180D Smart Trader", "Fund", "Smart Trader"],
      "chains": ["ethereum", "solana"],
      "includeStablecoin": true,
      "includeNativeTokens": true,
      "excludeSmFilter": []
    },
    "pagination": {
      "page": 1,
      "recordsPerPage": 3
    }
  }' \
  | jq '.' > smart_money_tokens_response.json

# Check if request was successful
if [ $? -eq 0 ]; then
    echo "Data fetched successfully!"
    echo "Raw response saved to: smart_money_tokens_response.json"
    echo ""
    echo "Top 3 tokens accumulated by Smart Money (Last 24h):"
    echo "=================================================="
    
    # Parse and display the data (requires jq)
    if command -v jq &> /dev/null; then
        echo "Top 3 tokens held by Smart Money wallets:"
        echo "=========================================="
        jq -r '.[0:3] | .[] | "\(.symbol) - $\(.balanceUsd | tostring | .[0:15]) balance - \(.nofHolders) holders"' smart_money_tokens_response.json
    else
        echo "Install jq for better JSON formatting: brew install jq (macOS) or apt-get install jq (Ubuntu)"
        cat smart_money_tokens_response.json
    fi
else
    echo "Error: Failed to fetch data from Nansen API"
    echo "Please check your API key and network connection"
fi
