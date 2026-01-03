import requests
import json
import os

# Configuration
API_KEY = "+d6UnUpCXdLooqq8pYrrdbREO3dJ8lIz/3fbFamD3vvFtRsnfKdjmLw59EnRGH72"
BASE_URL = "https://api.collegefootballdata.com/player/portal"
YEAR = 2025

def fetch_transfers():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json"
    }
    
    params = {
        "year": YEAR
    }

    print(f"Fetching transfer portal data for {YEAR}...")
    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        print(f"Successfully fetched {len(data)} records.")
        
        # Clean and process data
        cleaned_data = []
        for player in data:
            cleaned_data.append({
                "first_name": player.get("firstName"),
                "last_name": player.get("lastName"),
                "position": player.get("position"),
                "origin": player.get("origin"),
                "destination": player.get("destination"),
                "transferDate": player.get("transferDate"),
                "rating": player.get("rating"),
                "stars": player.get("stars")
            })
            
        # Save to JSON
        output_file = "transfers.json"
        with open(output_file, "w") as f:
            json.dump(cleaned_data, f, indent=2)
            
        print(f"Data saved to {output_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        if response.status_code == 401:
            print("Authentication failed. Please check your API Key.")

if __name__ == "__main__":
    fetch_transfers()
