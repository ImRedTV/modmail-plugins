import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sm7b(self, ctx):
        embed = discord.Embed(
            title=":blue_circle: Pourquoi déconseiller le SM7B et autres micros "Broadcast Dynamiques" ?",
            description="Version Courte', '\n Car ils ne sont pas adaptés et n\'amèneront que des problèmes. Les micros dynamiques sont très peu sensibles, ils nécessitent énormément de gain. Parfois 60dBs (soit amplifié 1000x), cela inclus tous les parasites et souffles des composants électroniques qui se situeront sur le chemin. Ils sont fait pour être utilisés très proches, et sont rien que pour ça très peu adaptés à l\'animation en stream.\n \n **Vous êtes l\'animateur de votre stream, vous allez gigoter dans tous les sens, faites des économies d\'argent et de migraine et prenez un statique.** \n\n [Version longue & plus d\'info...](https://discord.com/channels/333720455074676736/812345334536863844/820309055523651584)",
            color=0xff0000,
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Management Team", icon_url="https://cdn.discordapp.com/attachments/726193232798810132/740629657191186562/7S-.gif")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Test1(bot))
