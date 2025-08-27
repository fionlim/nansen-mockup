#!/usr/bin/env python3
"""
Nansen API - Smart Money Token Accumulation
Fetches top 3 tokens accumulated by Smart Money wallets in the last 24 hours
"""

import os
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NansenAPI:
    def __init__(self):
        self.base_url = "https://api.nansen.ai/api/beta"
        self.api_key = os.getenv('apiKey')
        
        if not self.api_key:
            raise ValueError("API key not found. Please set 'apiKey' in your .env file")
        
        self.headers = {
            'apiKey': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def get_smart_money_tokens(self, limit: int = 3) -> List[Dict]:
        """
        Fetch top tokens accumulated by Smart Money wallets
        
        Args:
            limit: Number of top tokens to return
            
        Returns:
            List of token data with accumulation metrics
        """
        endpoint = f"{self.base_url}/smart-money/holdings"
        
        payload = {
            "parameters": {
                "smFilter": [
                    "180D Smart Trader",
                    "Fund", 
                    "Smart Trader"
                ],
                "chains": [
                    "ethereum",
                    "solana"
                ],
                "includeStablecoin": True,
                "includeNativeTokens": True,
                "excludeSmFilter": []
            },
            "pagination": {
                "page": 1,
                "recordsPerPage": limit
            }
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            # The response is a list of tokens, not an object with 'data' property
            return data[:limit] if isinstance(data, list) else []
            
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response body: {e.response.text}")
            return []
    
    def format_token_data(self, tokens: List[Dict]) -> str:
        """Format token data for display"""
        if not tokens:
            return "No data available"
        
        output = f"Top {len(tokens)} Tokens Held by Smart Money Wallets\n"
        output += "=" * 60 + "\n\n"
        
        for i, token in enumerate(tokens, 1):
            output += f"{i}. {token.get('symbol', 'Unknown')}\n"
            output += f"   Contract: {token.get('tokenAddress', 'N/A')}\n"
            output += f"   Chain: {token.get('chain', 'N/A')}\n"
            output += f"   Balance USD: ${token.get('balanceUsd', 0):,.2f}\n"
            output += f"   Holders: {token.get('nofHolders', 'N/A')}\n"
            output += f"   Balance Change 24h: {token.get('balancePctChange24h', 0):.2f}%\n"
            output += f"   Market Cap: ${token.get('marketCap', 0):,.0f}\n"
            output += f"   Sectors: {', '.join(token.get('sectors', []))}\n"
            output += "\n"
        
        return output

def main():
    """Main function to fetch and display Smart Money token data"""
    try:
        # Initialize API client
        api = NansenAPI()
        
        print("Fetching Smart Money token accumulation data...")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Fetch top 3 tokens
        tokens = api.get_smart_money_tokens(limit=3)
        
        if tokens:
            # Display formatted results
            print(api.format_token_data(tokens))
            
            # Save raw data to file for reference
            with open('smart_money_tokens_data.json', 'w') as f:
                json.dump({
                    'timestamp': datetime.now().isoformat(),
                    'timeframe': '1d',
                    'data': tokens
                }, f, indent=2)
            print("Raw data saved to 'smart_money_tokens_data.json'")
            
        else:
            print("No Smart Money token data available for the last 24 hours.")
            
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nTo fix this:")
        print("1. Create a .env file in your project root")
        print("2. Add your Nansen API key: apiKey=your_actual_api_key")
        print("3. Make sure the .env file is in your .gitignore")
        
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
