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

@bot.command()
async def scrim(context, role):
    await context.send(role + " react for scrim")

@bot.event
async def on_reaction_add(reaction, user):
    # global reactionCount 
    # reactionCount += 1
    # print(reactionCount)
    channel = reaction.message.channel
    if len(reaction.message.reactions) == 6:
        await channel.send("6 reactions")

# @bot.event
# async def on_raw_reaction_remove(payload):
#     global reactionCount
#     reactionCount -= 1
#     if reactionCount < 0:
#         reactionCount = 0
    # print(reactionCount)

    # channel = await bot.fetch_channel(payload.channel_id)
    # user = await bot.fetch_user(payload.user_id)
    # await channel.send(f'{user.mention} unreacted with {payload.emoji}')

# @bot.command()
# async def test(context):
#     await context.send("test")

bot.run(os.getenv('ScrimBotKey'))