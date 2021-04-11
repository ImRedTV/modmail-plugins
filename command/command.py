import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:")
    await bot.say(embed=embed)
