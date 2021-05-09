import asyncio
import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel


class Moderation(commands.Cog):
    """
    Commandes pour modérer votre serveur._ _
    """

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.api.get_plugin_partition(self)

    async def cog_command_error(self, ctx, error):
        """Checks errors"""
        error = getattr(error, "original", error)
        if isinstance(error, commands.CheckFailure):
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Vous n'avez pas assez d'autorisations pour exécuter cette commande!",
                    color=discord.Color.red(),
                ).set_footer(text="Êtes-vous un modérateur?")
            )
        raise error

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        """Configure les autorisations de rôle muet pour le canal."""
        muterole = await self.db.find_one({"_id": "muterole"})
        if muterole == None:
            return

        if not str(channel.guild.id) in muterole:
            return

        role = channel.guild.get_role(muterole[str(channel.guild.id)])
        if role == None:
            return
        await channel.set_permissions(role, send_messages=False)

    @commands.command(usage="<channel>")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def setlog(self, ctx, channel: discord.TextChannel = None):
        """Configure un channel de logs."""
        if channel == None:
            return await ctx.send_help(ctx.command)

        try:
            await channel.send(
                embed=discord.Embed(
                    description=(
                        "Ce canal a été configuré pour consigner les logs. "
                    ),
                    color=self.bot.main_color,
                )
            )
        except discord.errors.Forbidden:
            await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Je n'ai pas assez d'autorisations pour écrire dans ce canal.",
                    color=discord.Color.red(),
                ).set_footer(text="Veuillez corriger les autorisations.")
            )
        else:
            await self.db.find_one_and_update(
                {"_id": "logging"},
                {"$set": {str(ctx.guild.id): channel.id}},
                upsert=True,
            )
            await ctx.send(
                embed=discord.Embed(
                    title="Success",
                    description=f"{channel.mention} a été configuré comme canal de logs.",
                    color=self.bot.main_color,
                )
            )

    @commands.command(usage="<role>")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def muterole(self, ctx, role: discord.Role = None):
        """Configure le rôle muet."""
        if role is None:
            if (await self.db.find_one({"_id": "muterole"})) is not None:
                if (
                    ctx.guild.get_role(
                        (await self.db.find_one({"_id": "muterole"}))[str(ctx.guild.id)]
                    )
                    != None
                ):
                    return await ctx.send(
                        embed=discord.Embed(
                            title="Error",
                            description="Le rôle muet est déjà configuré.",
                            color=discord.Color.red(),
                        ).set_footer(
                            text="Si vous souhaitez changer de rôle, mentionnez-le simplement."
                        )
                    )
            role = await ctx.guild.create_role(name="Muted")

        await self.db.find_one_and_update(
            {"_id": "muterole"}, {"$set": {str(ctx.guild.id): role.id}}, upsert=True
        )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"Le rôle muet a été défini sur {role.mention}.",
                color=self.bot.main_color,
            )
        )

    @commands.command(usage="<member> [raison]")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def warn(self, ctx, member: discord.Member = None, *, reason=None):
        """
        Warn un membre.
        """
        if member == None:
            return await ctx.send_help(ctx.command)

        if reason != None:
            if not reason.endswith("."):
                reason = reason + "."

        case = await self.get_case()

        msg = f"Vous avez été warn de **{ctx.guild.name}**" + (
            f" pour: {reason}" if reason else "."
        )

        await self.log(
            guild=ctx.guild,
            embed=discord.Embed(
                title="Avertissement",
                description=f"**{ctx.member.mention}** a été warn par {ctx.author.mention}"
                + (f" pour: {reason}" if reason else "."),
                color=self.bot.main_color,
            )
        )

        try:
            await member.send(msg)
        except discord.errors.Forbidden:
            return await ctx.send(
                embed=discord.Embed(
                    title="Logs",
                    description=f"L'avertissement de **{member}** a été enregistré.",
                    color=self.bot.main_color,
                )
            )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"**{member}** a été warn.",
                color=self.bot.main_color,
            )
        )

    @commands.command(usage="<member> [raison]")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        """Kicks un membre."""
        if member == None:
            return await ctx.send_help(ctx.command)

        if reason != None:
            if not reason.endswith("."):
                reason = reason + "."

        msg = f"Vous avez été expulsé de **{ctx.guild.name}**" + (
            f" pour: {reason}" if reason else "."
        )

        try:
            await member.send(msg)
        except discord.errors.Forbidden:
            pass

        try:
            await member.kick(reason=reason)
        except discord.errors.Forbidden:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Je n'ai pas assez d'autorisations pour les expulser.",
                    color=discord.Color.red(),
                ).set_footer(text="Veuillez corriger les autorisations.")
            )

        case = await self.get_case()

        await self.log(
            guild=ctx.guild,
            embed=discord.Embed(
                title="Kick",
                description=f"**{member}** a été expulsé par {ctx.author.mention}"
                + (f" pour: {reason}" if reason else "."),
                color=self.bot.main_color,
            )
        )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"**{member}** has been kicked.",
                color=self.bot.main_color,
            )
        )

    @commands.command(usage="<member> [raison]")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        """Banni un membre."""
        if member == None:
            return await ctx.send_help(ctx.command)

        if reason != None:
            if not reason.endswith("."):
                reason = reason + "."

        msg = f"Vous avez été banni de **{ctx.guild.name}**" + (
            f" pour: {reason}" if reason else "."
        )

        try:
            await member.send(msg)
        except discord.errors.Forbidden:
            pass

        try:
            await member.ban(reason=reason, delete_message_days=0)
        except discord.errors.Forbidden:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Je n'ai pas assez d'autorisations pour les interdire. ",
                    color=discord.Color.red(),
                ).set_footer(text="Veuillez corriger les autorisations.")
            )

        case = await self.get_case()

        await self.log(
            guild=ctx.guild,
            embed=discord.Embed(
                title="Ban",
                description=f"**{member}** a été banni par {ctx.author.mention}"
                + (f" pour: {reason}" if reason else "."),
                color=self.bot.main_color,
            )
        )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"**{member}** a été banni.",
                color=self.bot.main_color,
            )
        )

    @commands.command(usage="<member> [raison]")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def mute(self, ctx, member: discord.Member = None, *, reason=None):
        """Mute un membre."""
        if member == None:
            return await ctx.send_help(ctx.command)
        role = await self.db.find_one({"_id": "muterole"})
        no_role = False
        if role == None:
            no_role = True
        elif str(ctx.guild.id) in role:
            role = ctx.guild.get_role(role[str(ctx.guild.id)])
            if role == None:
                no_role = True

        if reason != None:
            if not reason.endswith("."):
                reason = reason + "."

        if no_role:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description=(
                        "Vous devez d'abord configurer un rôle muet.\n"
                        f"Pour en définir un, exécutez `{ctx.prefix}muterole (@role)`."
                    ),
                    color=discord.Color.red(),
                )
            )

        msg = f"Vous avez été mute de {ctx.guild.name}" + (
            f" pour: {reason}" if reason else "."
        )

        try:
            await member.send(msg)
        except discord.errors.Forbidden:
            pass

        try:
            await member.add_roles(role, reason=reason)
        except discord.errors.Forbidden:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Je n'ai pas assez d'autorisations pour les désactiver.",
                    color=discord.Color.red(),
                ).set_footer(text="Veuillez corriger les autorisations.")
            )

        case = await self.get_case()

        await self.log(
            guild=ctx.guild,
            embed=discord.Embed(
                title="Mute",
                description=f"**{member}** a été mis en sourdine par {ctx.author.mention}"
                + (f" pour: {reason}" if reason else "."),
                color=self.bot.main_color,
            )
        )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"**{member}** a été mis en sourdine.",
                color=self.bot.main_color,
            )
        )

    @commands.command(usage="<member> [raison]")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def unmute(self, ctx, member: discord.Member = None, *, reason=None):
        """Rétablit le son du membre spécifié."""
        if member == None:
            return await ctx.send_help(ctx.command)
        role = await self.db.find_one({"_id": "muterole"})
        no_role = False
        if role == None:
            no_role = True
        elif str(ctx.guild.id) in role:
            role = ctx.guild.get_role(role[str(ctx.guild.id)])
            if role == None:
                no_role = True

        if reason != None:
            if not reason.endswith("."):
                reason = reason + "."

        if no_role:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description=(
                        "You don't have a muted role set up.\n"
                        f"You will have to unmute them manually."
                    ),
                    color=discord.Color.red(),
                )
            )

        try:
            await member.remove_roles(role, reason=reason)
        except discord.errors.Forbidden:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Je n'ai pas assez d'autorisations pour les réactiver.",
                    color=discord.Color.red(),
                ).set_footer(text="Veuillez corriger les autorisations.")
            )

        case = await self.get_case()

        await self.log(
            guild=ctx.guild,
            embed=discord.Embed(
                title="Mute",
                description=f"**{member}** has been unmuted by {ctx.author.mention}"
                + (f" pour: {reason}" if reason else "."),
                color=self.bot.main_color,
            )
        )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"**{member}** a été réactivé.",
                color=self.bot.main_color,
            )
        )

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        """
        Nukes (supprime TOUS les messages dans) un canal.
        Vous pouvez mentionner un canal pour nuancer celui-là à la place.
        """
        if channel == None:
            channel = ctx.channel
        tot = "this" if channel.id == ctx.channel.id else "that"
        message = await ctx.send(
            embed=discord.Embed(
                title="Êtes-vous sûr?",
                description=(
                    f"Cette commande supprimera **CHAQUE MESSAGE** dans ce channel!\nSi vous êtes sûr et responsable de ce qui pourrait arriver, envoyez `oui`."
                ),
                color=discord.Color.red(),
            )
        )

        def surecheck(m):
            return m.author == ctx.message.author

        try:
            sure = await self.bot.wait_for("message", check=surecheck, timeout=30)
        except asyncio.TimeoutError:
            await message.edit(
                embed=discord.Embed(title="Annulé.", color=self.bot.main_color)
            )
            ensured = False
        else:
            if sure.content == "oui":
                ensured = True
            else:
                await message.edit(
                    embed=discord.Embed(title="Annulé.", color=self.bot.main_color)
                )
                ensured = False
        if ensured:
            case = await self.get_case()

            channel_position = channel.position

            try:
                new_channel = await channel.clone()

                await new_channel.edit(position=channel_position)
                await channel.delete()
            except discord.errors.Forbidden:
                return await ctx.send(
                    embed=discord.Embed(
                        title="Error",
                        description=f"Je n'ai pas assez d'autorisations pour bombarder {tot} channel.",
                        color=discord.Color.red(),
                    ).set_footer(text="Veuillez corriger les autorisations.")
                )

            await new_channel.send(
                embed=discord.Embed(
                    title="Nuke",
                    description="Ce channel a été bombardé!",
                    color=self.bot.main_color,
                )
                .set_image(
                    url="https://cdn.discordapp.com/attachments/600843048724987925/600843407228928011/tenor.gif"
                )
                
            )

            await self.log(
                guild=ctx.guild,
                embed=discord.Embed(
                    title="Nuke",
                    description=f"{ctx.author.mention} nuked {new_channel.mention}.",
                    color=self.bot.main_color,
                )
            )

    @commands.command(usage="<amount>")
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def clear(self, ctx, amount: int = 1):
        """Clear le nombre de messages spécifié."""
        max = 2000
        if amount > max:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description=f"Vous ne pouvez clear que 2000 messages.",
                    color=discord.Color.red(),
                ).set_footer(text=f"Utiliser {ctx.prefix}nuke pour clear l'ensemble de la discussion.")
            )

        try:
            await ctx.message.delete()
            await ctx.channel.clear(limit=amount)
        except discord.errors.Forbidden:
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="Je n'ai pas assez d'autorisations pour clear les messages.",
                    color=discord.Color.red(),
                ).set_footer(text="Veuillez corriger les autorisations.")
            )

        case = await self.get_case()
        messages = "messages" if amount > 1 else "message"
        have = "have" if amount > 1 else "has"

        await self.log(
            guild=ctx.guild,
            embed=discord.Embed(
                title="Clear",
                description=f"{amount} {messages} {have} been clear by {ctx.author.mention}.",
                color=self.bot.main_color,
            )
        )

        await ctx.send(
            embed=discord.Embed(
                title="Success",
                description=f"{amount} {messages} messages supprimé.",
                color=self.bot.main_color,
            )
        )

    async def get_case(self):
        """Gives the case number."""
        num = await self.db.find_one({"_id": "cases"})
        if num == None:
            num = 0
        elif "amount" in num:
            num = num["amount"]
            num = int(num)
        else:
            num = 0
        num += 1
        await self.db.find_one_and_update(
            {"_id": "cases"}, {"$set": {"amount": num}}, upsert=True
        )
        suffix = ["th", "st", "nd", "rd", "th"][min(num % 10, 4)]
        if 11 <= (num % 100) <= 13:
            suffix = "th"
        return f"{num}{suffix}"
    async def log(self, guild: discord.Guild, embed: discord.Embed):
        """Sends logs to the log channel."""
        channel = await self.db.find_one({"_id": "logging"})
        if channel == None:
            return
        if not str(guild.id) in channel:
            return
        channel = self.bot.get_channel(channel[str(guild.id)])
        if channel == None:
            return
        return await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(Moderation(bot))
