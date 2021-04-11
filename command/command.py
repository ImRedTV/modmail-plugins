import discord
from discord.ext import commands, tasks

import asyncio

from core import checks
from core.models import PermissionLevel
from core.paginator import EmbedPaginatorSession

import datetime

    @commands.command()
    async def test(self, ctx):
        if self.decay_channels:
            pages = []
            total = 0

            for channel in self.decay_channels:
                total += self.decay_channels[channel]
                
            average = total / len(self.decay_channels)

            front = discord.Embed(color=self.bot.main_color, title="All decay info.")
            front.add_field(
                name="Decay channels:",
                value=str(len(self.decay_channels)),
                inline=True,
            )
            front.add_field(
                name="Average decay time:",
                value=f"{str(average)}ms",
                inline=True,
            )
            front.add_field(
                name="To see channel specific info, use the reactions below.",
                value="\u200b",
                inline=False,
            )
            pages.append(front)

            for channel in self.decay_channels:
                d_channel = self.bot.get_channel(int(channel))
                page = discord.Embed(color=self.bot.main_color, title=f"Decay info of: #{d_channel.name}")
                page.add_field(name="Decay time:", value=f"{str(self.decay_channels[channel])}ms")

                pages.append(page)

            session = EmbedPaginatorSession(ctx, *pages)
            await session.run()    

        else:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="No channels are decaying, to decay a channel use the command: `[p]decay #channel`",
            )
            await ctx.send(embed=embed)
