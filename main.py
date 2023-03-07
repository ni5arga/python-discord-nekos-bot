import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!neko'):
        response = requests.get('https://nekos.life/api/v2/img/neko')
        data = response.json()
        neko_url = data['url']
        await message.channel.send(neko_url)

client.run('YOUR_DISCORD_BOT_TOKEN')
