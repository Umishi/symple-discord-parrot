import discord


TOKEN = 'token here'


client = discord.Client()

@client.event
    if message.channel == client.get_channel(channel_1 here) and not message.author.bot :
        channel = client.get_channel(channel_2 here)
        await channel.send(message.content)

    if message.channel == client.get_channel(channel_2 here) and not message.author.bot :
        channel = client.get_channel(channel_1 here)
        await channel.send(message.content)

client.run(TOKEN)
