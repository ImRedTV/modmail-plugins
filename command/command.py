import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def empire(self, ctx):
        embed = discord.Embed(
            title="**Qu'est ce qu'Empire Media Science ?**",
            description="**Empire Media Science** est un consortium de techniciens et d'artistes de l'audiovisuel et des nouveaux médias, créé par <@239744631225581578>, Directeur Technique & Artistique derrière le son et l'image d'une grande partie des grands créateurs de contenu français.",
            color=#ff0000,
            timestamp=ctx.message.created_at
        )
        
        embed.set_footer(text="Empire Media Science", icon_url="https://i.imgur.com/GFGA3dF.jpg")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Test1(bot))
