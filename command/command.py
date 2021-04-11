import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def empire(self, ctx):
        embed = discord.Embed(
            title="**Qu'est ce qu'Empire Media Science ?**",
            description="**Empire Media Science** est un consortium de techniciens et d\'artistes de l\'audiovisuel et des nouveaux médias, créé par <@!239744631225581578>, Directeur Technique & Artistique derrière le son et l\'image d\'une grande partie des grands créateurs de contenu français.\n\n*Si vous êtes venu ici pour savoir comment on a fait le son ou l\'image de LeBouseuh ou Inoxtag,* **Vous êtes au bon endroit !**\n\nN\'hésitez pas a visiter notre <#812345334536863844> et nos <#812775265763328000> ou nous poser vos questions dans <#751028848874749962> ou <#813813822116724746>. Nous vous aiderons du mieux qu\'on peut !\n\nAmusez-vous bien et n\'oubliez pas de lire le <#763141753351045152>",
            color=0xffc000,
            Thumbnail('https://i.imgur.com/QvzIt7A.png'),
            timestamp=ctx.message.created_at
        )
        
        embed.set_footer(text="Empire Media Science", icon_url="https://i.imgur.com/GFGA3dF.jpg")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Test1(bot))
