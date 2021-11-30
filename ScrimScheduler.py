import discord
import os
# from discord.ext.commands.bot import AutoShardedBot
import requests
from pathlib import Path

from discord.ext import commands

reacts = set()
count = 0
author = ""
bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('login successful')

@bot.command()
async def scrim(context, role):
    global author
    await context.send(role + " react for scrim")
    author = context.author

@bot.event
async def on_reaction_add(reaction, user):
    global author
    global count
    global reacts
    channel = reaction.message.channel
    async for user in reaction.users():
        reacts.add(user)
        print(reacts)
    if len(reacts) == 6:
        await channel.send(author.mention)

bot.run(os.getenv('ScrimBotKey'))