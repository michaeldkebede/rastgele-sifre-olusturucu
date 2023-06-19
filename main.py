import discord
import random
import webbrowser as web

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
intents=discord.Intents.all()
intents = discord.Intents()
intents.members = True

@client.event
async def on_ready():
    print(f'Hi boyle girdim {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$hello'):
        #web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await message.channel.send("AHAHAHAHAHAHAHAHAHA!")

@client.event
async def on_member_join(member):
    await member.send('Welcome to the server!')

client.run("MTExNzg1NzQ2NDExMzcwOTIxNg.GhBGTN.fw9DD9zs6luVgnmlEQZYtM20TSqSNh2aBG_45o")
