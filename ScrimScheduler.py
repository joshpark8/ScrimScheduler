import discord
import os
import requests
from pathlib import Path

from discord.ext import commands

bot = commands.Bot(command_prefix = '~')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('login successful')

@bot.event
async def on_reaction_add(context, reaction, user):
    embed = reaction.embeds[0]
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji == "emoji 1":
        fixed_channel = bot.get_channel()
        await fixed_channel.send(embed=embed)
    elif emoji == "emoji 2":
        #do stuff
        await context.send('@park#0001 reacted with emoji 2')
    elif emoji == "emoji 3":
        #do stuff
        pass
    else:
        pass

bot.run(os.getenv('ScrimBotKey'))