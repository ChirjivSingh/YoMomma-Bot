import discord
import requests
import json
import random

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$yomom'):
        a = requests.get("https://api.yomomma.info")
        p = a.json()
        yomomma = p["joke"]
        await message.reply(yomomma)
    
                         
       


client.run('OTUzNTcyMDIwMjU4NDg4MzIw.YjGhJg.rIZiK9sEs_UuT8wiaEhMLYqSNik')
