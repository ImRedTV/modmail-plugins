from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "SM7B" in message.content.lower():
            await message.channel.send("Fils de pute")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
