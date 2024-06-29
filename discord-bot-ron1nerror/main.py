import os
from dotenv import load_dotenv
import discord
from deck import Deck
#images
import aiohttp
from io import BytesIO
from discord import File
import requests
'''
#bot url
#https://discord.com/api/oauth2/authorize?client_id=1181284992588980255&permissions=108544&scope=bot
'''

#Load the token from .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$what are you'):
        await message.channel.send('A discord test bot.')
    if message.content.startswith('$cat'):
        await message.channel.send('https://cataas.com/cat/gif')
    if message.content.startswith('$dog'):
        await message.channel.send('https://random.dog/5f6522a4-8848-4df1-866c-df7394932dd1.jpg')
    if message.content.startswith('$help'):
        await message.channel.send('Commands: $hello, $what are you, $cat, $dog, $lets play or $play')

#main project
    if message.content.startswith('$lets play') or message.content.startswith('$play'):
        # Your existing game setup code here
        deck = Deck()
        Playerscore = 0
        await message.channel.send("time to play")
        Playerscore = await draw_and_calculate_score_player(deck, message, Playerscore)
        Playerscore = await draw_and_calculate_score_player(deck, message, Playerscore)

        await message.channel.send(f"your score is {Playerscore}")
        await message.channel.send("_-_-_-_-_-_-_-_-")
#House Score           ***HOUSE SCORE****
        HouseScore = 0
        HouseScore = await draw_and_calculate_score(deck, message, HouseScore)
        HouseScore = await draw_and_calculate_score(deck, message, HouseScore)
        #await message.channel.send(f"House score is {HouseScore}")

# Asking for more cards     ***ASK FOR MORE CARDS***
        
        await message.channel.send("Do you want to hit or pass? Type '$hit' or '$pass'")

        def check(m):
            return m.author == message.author and m.content.lower() in ('$hit', '$pass')

        response = await client.wait_for('message', check=check)

        while response.content.lower() == '$hit':
            # Handle hitting logic
            Playerscore = await draw_and_calculate_score_player(deck, message, Playerscore)

            await message.channel.send(f"your score is {Playerscore}")
            await message.channel.send("___________")

            if Playerscore > 21:
                await message.channel.send("Bust! Your score is over 21.")
                break

            # Ask again if the player wants to hit
            await message.channel.send("Do you want to hit or pass? Type '$hit' or '$pass'")
            response = await client.wait_for('message', check=check)

        # Handle passing logic
        if response.content.lower()== '$pass':
            await message.channel.send("You chose to pass!")

        # Handle the house logic
        
        while HouseScore < Playerscore:
            if Playerscore > 21:
                break
            HouseScore = await draw_and_calculate_score(deck, message, HouseScore)
            
            #await message.channel.send(f"House score is {HouseScore}")

        if HouseScore > 21:
            await message.channel.send(f"House score is {HouseScore}")
            await message.channel.send("House bust! You Win!")
        else:
            await message.channel.send(f"House score is {HouseScore}")
            await message.channel.send("House wins!")

        
            
#TEST AREA         ***TEST AREA***
'''
    if message.content.startswith('$test'):
        await message.channel.send(file=File('card_back.png'))
        
        deck = Deck()
        Playerscore = 0
        await message.channel.send("time to play")
        Playerscore, cards = await draw_and_calculate_score(deck, message, Playerscore)
        #await image(cards, message)

        await message.channel.send(f"your score is {Playerscore}")
        await message.channel.send("_____________")
        '''
#draw ace card       ***ACE CARD***
async def ace_card(random_number, player_score, message):
    
    await message.channel.send("You drew an Ace! Do you want it to be worth 1 or 11?")
    
    def check(m):
        return m.author == message.author and m.content in ['1', '11']

    response = await client.wait_for('message', check=check)

    if response.content == '1':
        card_value = 1
    else:
        card_value = 11
    
    await message.channel.send(f"You chose {card_value} for the Ace.")
    player_score += card_value

    return player_score, card_value
#player score          ***PLAYER SCORE***
async def draw_and_calculate_score_player(deck, message, player_score):
    cards = deck.draw_card()  # Define the "cards" variable
    await image(cards, message)
    
    random_number = cards["value"]

    #await message.channel.send(str(random_number))
    
    if random_number in ['KING', 'QUEEN', 'JACK']:
        player_score += 10
    elif random_number in ['ACE']:
        player_score, card_value = await ace_card(random_number, player_score, message)
    else: 
        player_score += int(random_number)
    
    
    return player_score
#house score           ***HOUSE SCORE***

async def draw_and_calculate_score(deck, message, HouseScore):
    cards = deck.draw_card()  # Define the "cards" variable
    
    random_number = cards["value"]
    #await message.channel.send(str(random_number))

    if HouseScore == 0:
        await message.channel.send(file=File('card_back.png'))
    else:
        await image(cards, message)

    if random_number in ['KING', 'QUEEN', 'JACK']:
        HouseScore += 10
    elif random_number in ['ACE']:
        if HouseScore >= 11:
            HouseScore += 1
        else:
            HouseScore += 11
    else: 
        HouseScore += int(random_number)

    return HouseScore

async def image(card, message):
    async with aiohttp.ClientSession() as session:
        async with session.get(card["image"]) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))

# Download the image
    response = requests.get('https://www.deckofcardsapi.com/static/img/back.png')

    # Save the image
    with open('card_back.png', 'wb') as f:
        f.write(response.content)
        
# Launch the bot.
client.run(os.environ['DISCORD_TOKEN'])