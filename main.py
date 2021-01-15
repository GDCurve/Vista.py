import discord
import random
from discord.ext import commands
import os

client = commands.Bot(command_prefix='a-')

@client.event
async  def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Es spēlēju pong. {round(client.latency * 1000)}ms')

@client.command(aliases=['palīdzība'.lower(), 'palidziba', 'paliga' ])
async def palidzi(ctx):
    await ctx.send("""
    -----------Palidziba------------
    Prefix = a-
    Ping = testing komanda lol
    8ball = prasi maģiskajai bumbai
    
    vel komandas bus, prieks bugiem raksti A R 4 T 1 C#0409, vai pats salabo github repositorijā:
    
    """)


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx):
    possibilities = [
        "Pēc tā ko redzu, jā.",
        "Paprasi atkal vēlāk.",
        "Labāk nestāstīt tagad.",
        "Nevaru pareģot tagad.",
        "Sitam ir maza iespēja parādīties, es šitos sūdus rakstiju ar roku."
        "Koncentrējies un paprasi vēlreiz.",
        "Nē",
        "Protams",
        "Diezgan liela iespēja, ka jā",
        "Mani ziņotāji saka nē",
        "Jā",
        "Nē",
        "Jā",
        "Nē- vispār nē",
        "Jā protams.",
    ]
    await ctx.send(f'Atbilde: {random.choice(possibilities)}')

@client.command()
async def kick(ctx):
    await ctx.send('kick in progress bruh')

@client.command()
async def ban(ctx):
    await ctx.send('ban in progress bruh')


@client.command()
async def nut(ctx):
    await ctx.send("Honey nut cheerios with extra nut.")


client.run(os.environ['BOT_TOKEN'])