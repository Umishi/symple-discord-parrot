import discord


TOKEN = 'token here'


client = discord.Client()

@client.event
async def on_message(message):
    if message.channel == client.get_channel(channel_1 here):
        channel = client.get_channel(channel_2 here)
        await channel.send(message.content)


client.run(TOKEN)
