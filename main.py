import discord
from counter import *
from constants import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$find'):
        com = message.content.replace('$find',"").strip().replace(' ','-')
        link = f'https://www.aidedd.org/dnd/monstres.php?vo={com}'
        await message.channel.send(link)

    if message.content.startswith('$roll'):
        r = ctr(message.content)
        await message.channel.send(r)

client.run(TOKEN)