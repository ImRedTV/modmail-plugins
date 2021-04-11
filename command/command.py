import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio

Import discord
Import time


@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:")
    await bot.say(embed=embed)
