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
            color=0xff0000,
            timestamp=ctx.message.created_at
        )
        
        embed.set_footer(text="Management Team", icon_url="https://cdn.discordapp.com/attachments/726193232798810132/740629657191186562/7S-.gif")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Test1(bot))
