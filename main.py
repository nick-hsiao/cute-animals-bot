import discord
import os
import requests
import json
import random

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "\"" + json_data[0]['q'] + "\" -" + json_data[0]['a']
    return(quote)

def get_gif():
    apikey = os.environ.get('TENOR_KEY')
    limit = 50
    response = requests.get("https://g.tenor.com/v1/trending?key=%s&limit=%s" % (apikey, limit))

    if response.status_code == 200:
        data = response.json()
    else:
        print("no json response")

    gif = random.choice(data["results"])
    gif_url = gif['media'][0]['gif']['url']
    print(gif_url)
    return(gif_url)
    
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #check if message is from ourselves - do nothing
    if message.author == client.user:
        return

    if message.content == ('$hello'):
        await message.channel.send('Hello!')

    if message.content == ('$alex'):
        await message.channel.send('https://media0.giphy.com/media/zdnTlBkg3I32E/giphy.gif?cid=ecf05e47a3wng8zqtlgaspauk2r0nll6tvodu3fy651rzdoh&rid=giphy.gif&ct=g')

    if message.content == ('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content == ('$gif'):
        gif = get_gif()
        await message.channel.send(gif)


key = os.environ.get('DISCORD_CA_KEY')
#print(key)

client.run(key)
