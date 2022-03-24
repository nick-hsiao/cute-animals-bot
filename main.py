import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #check if message is from ourselves - do nothing
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

key = os.environ.get('DISCORD_CA_KEY')
print(key)

client.run(key)
