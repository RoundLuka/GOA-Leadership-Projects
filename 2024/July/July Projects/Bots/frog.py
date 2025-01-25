import discord
from discord.ext import commands

import random

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready to use")
    print("------------------------")


#Welcome

@client.event
async def on_member_join(member):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Hello")
    print("Member joined successfuly welcomed")

#leave
@client.event
async def on_member_leave(memeber):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Goodbye")
    print("Member left, successfuly sent goodbye")

@client.command()
async def hello(ctx):
    await ctx.send("Ribbit! 🐸 How can I help you today?")
    
@client.command()
async def frog(ctx):
    await ctx.send("Ribbit! 🐸")

#joke

@client.command()
async def joke(ctx):
    jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why was the math book sad? Because it had too many problems.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why was the computer cold? It left its Windows open.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "Why did the golfer bring an extra pair of pants? In case he got a hole in one."
    ]

    await ctx.send("Ribbit! 🐸" + random.choice(jokes))

#quote
@client.command()
async def quote(ctx):
    quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. Franklin D. Roosevelt",
    "The purpose of our lives is to be happy. Dalai Lama",
    "Life is what happens when you're busy making other plans. John Lennon",
    "Get busy living or get busy dying. Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. Brian Tracy",
    "Believe you can and you're halfway there. Theodore Roosevelt",
    "The only way to do great work is to love what you do. Steve Jobs",
    "The best time to plant a tree was 20 years ago. The second best time is now. Chinese Proverb",
    "Your time is limited, don't waste it living someone else's life. Steve Jobs",
    "The only impossible journey is the one you never begin. Tony Robbins"
    ]
    await ctx.send("Ribbit! 🐸" + random.choice(quotes))

#roll
@client.command()
async def roll(ctx):
    number = random.randint(1,100)
    await ctx.send("Ribbit! 🐸" + f"You rolled a {number}! 🎲")


#events

#member join
#member leave

#commands
#!hello
#!frog
#!joke
#!quote
#!roll











client.run('MTI2NDE0MzA5MjQ4NzgxOTMzNg.G0sCtN.mkmeqGr6S-cv9JyCASdcvuHh5M5tuoJVsW7WFI')