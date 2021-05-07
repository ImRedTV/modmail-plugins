import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class Clear(commands.Cog):
    """Plugin pour supprimer plusieurs messages à la fois."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def clear(self, ctx: commands.Context, amount: int):
        """Supprimez plusieurs messages à la fois."""

        if amount < 1:
            raise commands.BadArgument(
                "La quantité de messages à supprimer doit être strictement "
                "entier positif, non `{amount}`."
            )

        try:
            deleted = await ctx.channel.purge(limit=amount + 1)
        except discord.Forbidden:
            embed = discord.Embed(color=self.bot.error_color)

            embed.description = (
                "Cette commande nécessite l'autorisation `Gérer les messages`, "
                "que le bot n'a pas pour le moment."
            )

            return await ctx.send(embed=embed)

        message = f"{len(deleted)} **Les messages ont été supprimés !**"
        to_delete = await ctx.send(message)

        await to_delete.delete(delay=3)


def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))
