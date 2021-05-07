from discord.ext import commands
import discord
import asyncio
import datetime

from core import checks
from core.models import PermissionLevel


def to_emoji(c):
    base = 0x1F1E6
    return chr(base + c)


class sondages(commands.Cog):
    """sondage système de vote."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="sondage", invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def sondage(self, ctx: commands.Context):
        """Créez facilement des sondages."""
        await ctx.send_help(ctx.command)

    @sondage.command()
    @commands.guild_only()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def start(self, ctx, *, question):
        """Crée de manière interactive un sondage."""
        perms = ctx.channel.permissions_for(ctx.me)
        if not perms.add_reactions:
            return await ctx.send("Besoin d'autorisations pour ajouter des réactions.")

        # a list of messages to delete when we're all done
        messages = [ctx.message]
        answers = []

        def check(m):
            return (
                m.author == ctx.author
                and m.channel == ctx.channel
                and len(m.content) <= 100
            )

        for i in range(20):
            messages.append(
                await ctx.send(
                    f"Dites une option de sondage ou **{ctx.prefix}fini** pour publier le sondage."
                )
            )

            try:
                entry = await self.bot.wait_for("message", check=check, timeout=60.0)
            except asyncio.TimeoutError:
                break

            messages.append(entry)

            if entry.clean_content.startswith(f"{ctx.prefix}fini"):
                break

            answers.append((to_emoji(i), entry.clean_content))

        try:
            await ctx.channel.delete_messages(messages)
        except:
            pass  # oh well

        answer = "\n".join(f"{keycap}: {content}" for keycap, content in answers)
        embed = discord.Embed(
            title="**📊 SONDAGE**",
            color=self.bot.main_color,
            description=f"**{question}**\n{answer}",
        )
        embed.set_thumbnail(url="https://i.imgur.com/Ln7dMfn.png")
        sondage = await ctx.send(embed=embed)
        for emoji, _ in answers:
            await sondage.add_reaction(emoji)

    @start.error
    async def sondage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send("Manque la question.")

    @sondage.command()
    @commands.guild_only()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def quick(self, ctx, *questions_and_choices: str):
        """Fait un sondage rapidement.
        Le premier argument est la question et le reste sont les choix.
        par exemple: `!sondage "RED ou LEO?" RED "LEO"`
        ou cela peut être un simple sondage oui ou non, comme:
        `!sondage "Qui est le plus beau?"`
        """

        if len(questions_and_choices) == 0:
            return await ctx.send("Vous devez spécifier une question.")
        elif len(questions_and_choices) == 2:
            return await ctx.send("Vous avez besoin d'au moins 2 choix.")
        elif len(questions_and_choices) > 21:
            return await ctx.send("Vous ne pouvez avoir que 20 choix.")

        perms = ctx.channel.permissions_for(ctx.me)
        if not perms.add_reactions:
            return await ctx.send("Besoin d'autorisations Ajouter des réactions.")
        try:
            await ctx.message.delete()
        except:
            pass
        question = questions_and_choices[0]

        if len(questions_and_choices) == 1:
            embed = discord.Embed(
                title="**📊 SONDAGE**",
                color=self.bot.main_color, description=f"**{question}**",
            )
            embed.set_thumbnail(url="https://i.imgur.com/Ln7dMfn.png")
            sondage = await ctx.send(embed=embed)
            reactions = ["✅", "❌"]
            for emoji in reactions:
                await sondage.add_reaction(emoji)

        else:
            choices = [
                (to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])
            ]

            body = "\n".join(f"{key}: {c}" for key, c in choices)
            embed = discord.Embed(
                color=self.bot.main_color,
                description=f"**{question}**\n{body}",
            )
            sondage = await ctx.send(embed=embed)
            for emoji, _ in choices:
                await sondage.add_reaction(emoji)


def setup(bot):
    bot.add_cog(sondages(bot))
