import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio


class sell(commands.Cog):
    """
    Envoyer une vente à un canal désigné.
    """

    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

        self.banlist = dict()

        asyncio.create_task(self._set_mod_val())

    async def _update_mod_db(self):
        await self.coll.find_one_and_update(
            {"_id": "mod"}, {"$set": {"banlist": self.banlist,}}, upsert=True,
        )

    async def _set_mod_val(self):
        mod = await self.coll.find_one({"_id": "mod"})

        if mod is None:
            return

        self.banlist = mod["banlist"]

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def offre(self, ctx, *, sell):
        """
        Vendre quelque chose!

        **Usage**:
        [p]offre more plugins!
        """
        if str(ctx.author.id) not in self.banlist:
            async with ctx.channel.typing():
                config = await self.coll.find_one({"_id": "config"})
                if config is None:
                    embed = discord.Embed(
                        title="Canal de vente non défini.", color=self.bot.error_colour
                    )
                    embed.set_author(name="Error.")
                    embed.set_footer(text="Task failed.")
                    await ctx.send(embed=embed)
                else:
                    sell_channel = self.bot.get_channel(
                        int(config["sell-channel"]["channel"])
                    )

                    embed = discord.Embed(title=sell, color=0xffc000)
                    embed.set_author(
                        name=f"{ctx.author} soumet une nouvelle offre :", icon_url=ctx.author.avatar_url
                    )
                    await sell_channel.send(embed=embed)
                    await ctx.message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
        else:
            await ctx.send(embed=discord.Embed(color=self.bot.error_color, title=f"Vous avez été bloqué, {ctx.author.name}#{ctx.author.discriminator}.", description=f"Raison: {self.banlist[str(ctx.author.id)]}"))

    @commands.command(aliases=["ssc"])
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def setsellchannel(self, ctx, channel: discord.TextChannel):
        """
        Définissez le canal où vont les ventes.

        **Usage**:
        [p]setsellchannel #sell
        [p]ssc sells
        [p]ssc 515085600047628288
        """
        await self.coll.find_one_and_update(
            {"_id": "config"},
            {"$set": {"sell-channel": {"channel": str(channel.id)}}},
            upsert=True,
        )
        embed = discord.Embed(
            title=f"Channel définie sur #{channel}.", color=0xffc000
        )
        embed.set_author(name="Succès!")
        embed.set_footer(text="La tâche a réussi.")
        await ctx.send(embed=embed)

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def sellchannel(self, ctx):
        """Affiche le canal de sell."""
        config = await self.coll.find_one({"_id": "config"})
        sell_channel = self.bot.get_channel(
            int(config["sell-channel"]["channel"])
        )
        embed = discord.Embed(
            title=f"Le canal de vente est: #{sell_channel}",
            description="Pour le changer, utilisez [p]setsellchannel.",
            color=0xffc000,
        )
        await ctx.send(embed=embed)

    @checks.has_permissions(PermissionLevel.MOD)
    @commands.group(invoke_without_command=True)
    async def sellmod(self, ctx: commands.Context):
        """Empêchez les utilisateurs d'utiliser la commande de vente."""
        await ctx.send_help(ctx.command)

    @sellmod.command(aliases=["ban"])
    @checks.has_permissions(PermissionLevel.MOD)
    async def block(self, ctx, user: discord.User, *, reason="Raison non précisée."):
        """
        Empêchez un utilisateur d'utiliser la commande.

        **Examples:**
        [p]sellmod block @RED for abuse!
        [p]sellmod ban 211213461009465344 `cause he's the same person!!!
        """
        if str(user.id) in self.banlist:
            embed = discord.Embed(
                colour=self.bot.error_color,
                title=f"{user.name}#{user.discriminator} est déjà bloqué.",
                description=f"Raison: {self.banlist[str(user.id)]}",
            )
        else:
            self.banlist[str(user.id)] = reason
            embed = discord.Embed(
                colour=self.bot.main_color,
                title=f"{user.name}#{user.discriminator} est maintenant bloqué.",
                description=f"Raison: {reason}",
            )

        await self._update_mod_db()
        await ctx.send(embed=embed)

    @sellmod.command(aliases=["unban"])
    @checks.has_permissions(PermissionLevel.MOD)
    async def unblock(self, ctx, user: discord.User):
        """
   Débloquez un utilisateur de l'utilisation de la commande.

        **Examples:**
        [p]sellmod unblock @RED
        [p]sellmod unban 211213461009465344
        """
        if str(user.id) not in self.banlist:
            embed = discord.Embed(
                colour=self.bot.error_color,
                title=f"{user.name}#{user.discriminator} n'est pas bloqué.",
                description=f"Raison: {self.banlist[str(user.id)]}",
            )
        else:
            self.banlist.pop(str(user.id))
            embed = discord.Embed(
                colour=self.bot.main_color, title=f"{user.name}#{user.discriminator} est maintenant débloqué."
            )

        await self._update_mod_db()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(sell(bot))
