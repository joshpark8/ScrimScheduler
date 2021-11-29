import discord
import os
import requests
from pathlib import Path

from discord.ext import commands

reactionCount = 0
bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

def checkReactions(reactionCount):
    if reactionCount >= 6:
        return(True)
    else:
        return(False)


@bot.event
async def on_ready():
    print('login successful')

@bot.event
async def on_reaction_add(reaction, user):
    park = await bot.fetch_user("397179931223785484")
    global reactionCount 
    reactionCount += 1
    channel = reaction.message.channel
    if checkReactions(reactionCount):
        await channel.send(f'{park.mention} You have 6 reactions! Time to book a scrim :)')
        reactionCount = 0

@bot.event
async def on_raw_reaction_remove(payload):
    global park
    global reactionCount
    reactionCount -= 1
    # channel = await bot.fetch_channel(payload.channel_id)
    # user = await bot.fetch_user(payload.user_id)
    # await channel.send(f'{user.mention} unreacted with {payload.emoji}')

# @bot.command()
# async def test(context):
#     await context.send("test")

@bot.command()
async def scrim(context, role):
    await context.send(role + " react for scrim")

bot.run(os.getenv('ScrimBotKey'))