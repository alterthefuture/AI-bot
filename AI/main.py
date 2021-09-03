import discord
import random
import asyncio

people_hello = ['hello','hi','whats up', "Hello", 'Hi', "Whats up", 'yo' ,'Yo', 'hey', 'Hey', 'sup', 'Sup', "wassup", "Wassup"]
greetings = ["Hello there!", "Hi!", "What's up!", "Yo!", "Hey!", "Hey there!", "Hiya!", "Ahoy!", "Ello govnor!", "Howdy!", "Hola!", "Bonjour!", "Hello human. Wait, are you a human? What am I?", "Hi fellow human.", "Hello. Wait, What am I?"]
bot_self = ["Hello human. Wait, are you a human? What am I?", "Hi fellow human.", "Hello. Wait, What am I?"]

client = discord.Client()

@client.event
async def on_ready():
    print("> AI Bot is online.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for word in people_hello:
        if word in message.content:
            bot_choice = random.choice(greetings)
            if bot_choice in bot_self:
                msg = await message.channel.send(bot_choice)
                await asyncio.sleep(.5)
                await msg.edit(content="Error: AI Identifying existance of itself.")
                await asyncio.sleep(1)
                return await msg.edit(content=f"I mean... {random.choice(greetings[:-3])}")
            else:
                return await message.channel.send(random.choice(greetings))

client.run("token-here")
