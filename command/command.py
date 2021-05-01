import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
      async def empire(self, ctx, aliases=('e','ems')):
        await ctx.message.delete()#suprime l'appel
        embed = discord.Embed(
            title="**Qu'est ce qu'Empire Media Science ?**",
            description="**Empire Media Science** est un consortium de techniciens et d'artistes de l'audiovisuel et des nouveaux médias, créé par \n<@!239744631225581578>, Directeur Technique & Artistique derrière le son et l\'image de bien des grands créateurs de contenu français.\n\n Si vous êtes venu ici pour savoir comment on a fait le son ou l'image de **LeBouseuh**, **Inoxtag** et bien d'autres, **c\'est ici !**\n\nDes réponses à vos questions se trouveront dans nos **FAQ**.\n► <#812345334536863844> <#831571183723741234> <#831571616646823978>\n\nDans le cas où vous ne trouveriez pas votre réponse, n\'hésitez pas à solliciter l\'aide de la communauté dans les channels d\'entraide.\n► <#751028848874749962> <#813813822116724746> <#831559995635531847>\n\nUn achat en prévision ? Consultez nos recommandations.\n► <#812775265763328000> <#831578523440513054>\n\nAmusez-vous bien et n\'oubliez pas de lire le <#763141753351045152> !",
            color=0xffc000)
       
        embed.set_thumbnail(url="https://i.imgur.com/QvzIt7A.png")
        await ctx.send(embed=embed, delete_after=300)
        
    @commands.command()
    async def sm7b(self, ctx):
        await ctx.message.delete()#suprime l'appel
        embed = discord.Embed(
            title=":blue_circle: Pourquoi déconseiller le SM7B et autres micros 'Broadcast Dynamiques' ?",
            description="Version Courte', '\n Car ils ne sont pas adaptés et n\'amèneront que des problèmes. Les micros dynamiques sont très peu sensibles, ils nécessitent énormément de gain. Parfois 60dBs (soit amplifié 1000x), cela inclus tous les parasites et souffles des composants électroniques qui se situeront sur le chemin. Ils sont fait pour être utilisés très proches, et sont rien que pour ça très peu adaptés à l\'animation en stream.\n \n **Vous êtes l\'animateur de votre stream, vous allez gigoter dans tous les sens, faites des économies d\'argent et de migraine et prenez un statique.** \n\n [Version longue & plus d\'info...](https://discord.com/channels/333720455074676736/812345334536863844/820309055523651584)",
            color=0xffc000)

        embed.set_thumbnail(url="https://i.imgur.com/JpsKGgy.png")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def dynamic(self, ctx):
        await ctx.message.delete()#suprime l'appel
        embed = discord.Embed(
            title=":blue_circle: Pourquoi déconseiller le SM7B et autres micros 'Broadcast Dynamiques' ?",
            description="Version Courte', '\n Car ils ne sont pas adaptés et n\'amèneront que des problèmes. Les micros dynamiques sont très peu sensibles, ils nécessitent énormément de gain. Parfois 60dBs (soit amplifié 1000x), cela inclus tous les parasites et souffles des composants électroniques qui se situeront sur le chemin. Ils sont fait pour être utilisés très proches, et sont rien que pour ça très peu adaptés à l\'animation en stream.\n \n **Vous êtes l\'animateur de votre stream, vous allez gigoter dans tous les sens, faites des économies d\'argent et de migraine et prenez un statique.** \n\n [Version longue & plus d\'info...](https://discord.com/channels/333720455074676736/812345334536863844/820309055523651584)",
            color=0xffc000)

        embed.set_thumbnail(url="https://i.imgur.com/JpsKGgy.png")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def dynamique(self, ctx):
        await ctx.message.delete()#suprime l'appel
        embed = discord.Embed(
            title=":blue_circle: Pourquoi déconseiller le SM7B et autres micros 'Broadcast Dynamiques' ?",
            description="Version Courte', '\n Car ils ne sont pas adaptés et n\'amèneront que des problèmes. Les micros dynamiques sont très peu sensibles, ils nécessitent énormément de gain. Parfois 60dBs (soit amplifié 1000x), cela inclus tous les parasites et souffles des composants électroniques qui se situeront sur le chemin. Ils sont fait pour être utilisés très proches, et sont rien que pour ça très peu adaptés à l\'animation en stream.\n \n **Vous êtes l\'animateur de votre stream, vous allez gigoter dans tous les sens, faites des économies d\'argent et de migraine et prenez un statique.** \n\n [Version longue & plus d\'info...](https://discord.com/channels/333720455074676736/812345334536863844/820309055523651584)",
            color=0xffc000)

        embed.set_thumbnail(url="https://i.imgur.com/JpsKGgy.png")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Test1(bot))
