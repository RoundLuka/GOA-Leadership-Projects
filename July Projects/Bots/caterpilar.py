import discord
from discord.ext import commands

import random


intents = discord.Intents.all()

client = commands.Bot(command_prefix = '?',intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready to use")
    print("------------------------")


#Welcome

@client.event
async def on_member_join(member):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Welcome 🐛")
    print("Member joined successfuly welcomed")

#leave
@client.event
async def on_member_leave(memeber):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Goodbye 🐛")
    print("Member left, successfuly sent goodbye")

@client.command()
async def hello(ctx):
    await ctx.send("Wiggle wiggle! 🐛 How can I assist you today?")


@client.command()
async def caterpilar(ctx):
    await ctx.send("Hello! 🐛 I'm here to help you crawl through any issues.")

#joke

@client.command()
async def joke(ctx):
    jokes = [
        "Why dont scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why dont skeletons fight each other? They dont have the guts."
    ]
    await ctx.send("Wiggle wiggle! 🐛" + random.choice(jokes))

#quote
@client.command()
async def quote(ctx):
    quotes = [
        "Believe you can and you're halfway there. Theodore Roosevelt",
        "The only way to do great work is to love what you do. Steve Jobs",
        "The best time to plant a tree was 20 years ago. The second best time is now. Chinese Proverb"
    ]
    await ctx.send("Wiggle wiggle! 🐛" + random.choice(quotes))

#roll
@client.command()
async def roll(ctx):
    number = random.randint(1,100)
    await ctx.send("Wiggle wiggle! 🐛" + f"You rolled a {number}! 🎲")


#events

#member join
#member leave

#commands
#?hello
#?caterpilar
#?joke
#?quote
#?roll











client.run('')
