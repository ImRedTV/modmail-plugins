import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class Commande(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ip(self, ctx):
        await ctx.message.delete()#suprime l'appel
        embed = discord.Embed(
            description="connect play.sunnyisland.fr:30120",
            color=0x93D929)
        
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Commande(bot))

