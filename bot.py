# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hitchhiker_quotes = [
        'Luke, I am Your Father!',
        'YOU SHALL NOT PASS!',
        'With great power come great responcibility.',
        'Why did it have to be snakes?.',

    ]
    if message.content == 'April Moon':
    #if message.content.startswith('$towel'):
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)

client.run(TOKEN)

