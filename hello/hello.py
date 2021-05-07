from discord.ext import commands

class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        
   
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return
      
        if message.content.startswith("hello"): 
            await message.add_reaction("👋")
        elif message.content.startswith("Hello"):
            await message.add_reaction("👋")
        elif message.content.startswith("HELLO"):
            await message.add_reaction("👋")
        if message.content.startswith("Salut"): 
            await message.add_reaction("👋")
        elif message.content.startswith("salut"):
            await message.add_reaction("👋")
       elif message.content.startswith("bonjour"):
            await message.add_reaction("👋")
       elif message.content.startswith("Bonjour"):
            await message.add_reaction("👋")
       elif message.content.startswith("bonsoir"):
            await message.add_reaction("👋")
       elif message.content.startswith("Bonsoir"):
            await message.add_reaction("👋") 
       elif message.content.startswith("bonne nuit"):
            await message.add_reaction("👋")
       elif message.content.startswith("Bonne nuit"):
            await message.add_reaction("👋") 
       elif message.content.startswith("bienvenue"):
            await message.add_reaction("👋")
       elif message.content.startswith("Bienvenue"):
            await message.add_reaction("👋")  
       elif message.content.startswith("Welcome"):
            await message.add_reaction("👋")
       elif message.content.startswith("welcome"):
            await message.add_reaction("👋")   
            
def setup(bot):
    bot.add_cog(HelloPlugin(bot))
