import discord
from secret import tk

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

'''@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')'''

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        salon = client.get_channel(919338640776257596)
        await salon.send('ziggy')

client.run(tk)