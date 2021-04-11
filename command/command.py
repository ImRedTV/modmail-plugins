from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "sm7b" in message.content.lower():
            await message.channel.send("fils de pute")
        elif
        
        if(message.content === prefix + "empire"){
      var info_embed = new Discord.RichEmbed()
      .setColor("#ff0000")
      .setTitle(":blue_circle: Pourquoi déconseiller le SM7B et autres micros "Broadcast Dynamiques" ?")
      .addField("Version Courte', '\n Car ils ne sont pas adaptés et n\'amèneront que des problèmes. Les micros dynamiques sont très peu sensibles, ils nécessitent énormément de gain. Parfois 60dBs (soit amplifié 1000x), cela inclus tous les parasites et souffles des composants électroniques qui se situeront sur le chemin. Ils sont fait pour être utilisés très proches, et sont rien que pour ça très peu adaptés à l\'animation en stream.\n \n **Vous êtes l\'animateur de votre stream, vous allez gigoter dans tous les sens, faites des économies d\'argent et de migraine et prenez un statique.** \n\n [Version longue & plus d\'info...](https://discord.com/channels/333720455074676736/812345334536863844/820309055523651584)", `${client.user.tag}`, true)
      .addField("Tag du bot :hash:", `#${client.user.discriminator}`)
      .addField(":id: ", `${client.user.id}`)
      .addField("Nombre de Membres", message.guild.memberCount)
      .addField("En développement par AlexTheKing", "AlexTheKing#0736")
      .setFooter("Info - Bot")
      message.channel.sendEmbed(info_embed);
      console.log("Info");
  }

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
