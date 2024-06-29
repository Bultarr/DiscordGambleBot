from PIL import Image
import requests
from io import BytesIO
import discord
import aiohttp

class Deck:
    def __init__(self):
        response = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        if response.status_code == 200:
            json_data = response.json()
            self.deck_id = json_data["deck_id"]
            # Handle the JSON response here
        else:
            # Handle the error here
            pass
    
    def draw_card(self):
        response = requests.get(f"https://www.deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1")
        if response.status_code == 200:
            json_data = response.json()
            return json_data["cards"][0]
        else:
            # Handle the error here
            pass 
    
    # Download the image
    response = requests.get('https://www.deckofcardsapi.com/static/img/back.png')

    # Save the image
    with open('card_back.png', 'wb') as f:
        f.write(response.content)