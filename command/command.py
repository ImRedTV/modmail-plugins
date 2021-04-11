import discord
from discord.ext import commands

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
