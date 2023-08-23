import discord
import asyncio
from discord import app_commands
from discord.ext import commands
from pytz import timezone
from datetime import datetime
import random
import os

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "t!", intents = intents, case_insensitive = True)
client.remove_command("help")

TOKEN = "MTE0Mzk4MTU3Mjg4MjY5ODI3MA.G_HxIE.m3psqOe28xX6wuOb7l9Q_s1pimPGR-YtmMbtZM"

tz = timezone('EST')
datetime.now(tz)

@client.command()
async def ping(ctx):
    pingEmbed = discord.Embed(color = 0x6B31A5, timestamp = datetime.now())
    pingEmbed.add_field(name = "**Ping:**", value = f'Latency: {round(client.latency * 1000)}ms', inline = False)
    pingEmbed.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.display_avatar)
    await ctx.send(embed = pingEmbed)

client.run(TOKEN)