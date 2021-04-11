import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio

# Crée la commande "/empire"
@bot.command()
async def aide(ctx):
    embed = discord.Embed(title="Qu'est ce qu'Empire Media Science ?", description="Test", color=ffc000)
    await ctx.send(embed=embed)
