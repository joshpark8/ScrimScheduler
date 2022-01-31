import discord
import os
import requests
from pathlib import Path

from discord.ext import commands

author = ""
bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('login successful')

@bot.command()
async def scrim(context, role):
    await context.send(role + " react for scrim")
    author = context.author

@bot.event
async def on_reaction_add(reaction, user):
    reacts = set()
    global author
    channel = reaction.message.channel
    async for user in reaction.users():
        reacts.add(user)
        print(reacts)
    if len(reacts) == 2:
        await channel.send(author.mention + " 6 reactions! Scrim time :)")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')

bot.run(os.getenv('ScrimBotKey'))