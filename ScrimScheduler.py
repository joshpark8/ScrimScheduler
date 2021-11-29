import discord
import os
import requests
from pathlib import Path

from discord.ext import commands

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('login successful')

@bot.command()
async def scrim(context, role):
    await context.send(role + " react for scrim")

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if len(reaction.message.reactions) == 6:
        await channel.send("6 reactions")

bot.run(os.getenv('ScrimBotKey'))