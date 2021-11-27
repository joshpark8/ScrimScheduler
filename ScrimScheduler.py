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

@bot.event
async def on_reaction_add(reaction, user):
    print(f"---------------- TESTING ---------------- \n REACTION: {reaction}\n USER: {user}\n ----------------------------------------")
    channel = reaction.message.channel
    await channel.send(f'{user.mention} reacted with {reaction}')

@bot.event
async def on_raw_reaction_remove(payload):
    print(f"---------------- TESTING ---------------- \n PAYLOAD: {payload}\n ----------------------------------------")
    print(payload.emoji)
    channel = await bot.fetch_channel(payload.channel_id)
    user = await bot.fetch_user(payload.user_id)
    await channel.send(f'{user.mention} unreacted with {payload.emoji}')

@bot.command()
async def test(context):
    await context.send("test")

bot.run(os.getenv('ScrimBotKey'))