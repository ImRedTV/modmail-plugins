import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio

Import discord
Import time


@Client.command(pass_context=True)
async def ms_ping(ctx):
channel = ctx.message.channel   
try:
    t1 = time.perf_counter()
    await Client.send_typing(channel)
    ta = t1
    t2 = time.perf_counter()
    await Client.send_typing(channel)
    tb = t2
    ra = round((tb - ta) * 1000)
finally:
    pass
try:
    t1a = time.perf_counter()
    await Client.send_typing(channel)
    ta1 = t1a
    t2a = time.perf_counter()
    await Client.send_typing(channel)
    tb1 = t2a
    ra1 = round((tb1 - ta1) * 1000)
finally:
    pass
try:
    t1b = time.perf_counter()
    await Client.send_typing(channel)
    ta2 = t1b
    t2b = time.perf_counter()
    await Client.send_typing(channel)
    tb2 = t2b
    ra2 = round((tb2 - ta2) * 1000)
finally:
    pass
try:
    t1c = time.perf_counter()
    await Client.send_typing(channel)
    ta3 = t1c

    t2c = time.perf_counter()
    await Client.send_typing(channel)
    tb3 = t2c

    ra3 = round((tb3 - ta3) * 1000)
finally:
    pass
try:
    t1d = time.perf_counter()
    await Client.send_typing(channel)
    ta4 = t1d

    t2d = time.perf_counter()
    await Client.send_typing(channel)
    tb4 = t2d

    ra4 = round((tb4 - ta4) * 1000)
finally:
    pass

e = discord.Embed(title="Connection", colour = 909999)
e.add_field(name='Ping 1', value=str(ra))
e.add_field(name='Ping 2', value=str(ra2))
e.add_field(name='Ping 3', value=str(ra3))
e.add_field(name='Ping 4', value=str(ra4))
await Client.say(embed=e)
