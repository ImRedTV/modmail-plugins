import discord
from discord.ext import commands

@bot.command()
async def test(ctx):
    await ctx.send('test')
