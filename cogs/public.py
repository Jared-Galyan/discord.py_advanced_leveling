import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
import os
import time
from collections import OrderedDict, deque, Counter
import math
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import requests
import aiohttp
from .utils import checks


class Public(commands.Cog, name='Ranks'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bot', aliases=['info', 'botinfo'])
    async def _bot(self, ctx):
        embed = discord.Embed(title='Bot Information', description='Created by Jared#5984', color=0xff003d)

        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')
        embed.set_footer(text='Leveling', icon_url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')

        embed.add_field(name='**Total Guilds**', value=f'`{len(list(self.bot.guilds))}`', inline=True)
        embed.add_field(name='**Total Users**', value=f'`{len(list(self.bot.users))}`', inline=True)
        channel_types = Counter(isinstance(c, discord.TextChannel) for c in self.bot.get_all_channels())
        text = channel_types[True]
        embed.add_field(name='**Total Channels**', value=f'`{text}`', inline=True)
        embed.add_field(name='**Python Version**', value='`3.7`', inline=True)
        embed.add_field(name='**Discord.py Version**', value='`1.2.5`', inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title='Invite the bot!', description='[Click Here!](https://discordapp.com/api/oauth2/authorize?client_id=648362865048420373&permissions=8&scope=bot)', color=0xff003d)
        embed.set_footer(text='Leveling', icon_url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    
    @commands.command(name='help')
    async def _help(self, ctx):
        embed = discord.Embed(title="Bot Help", description="Created by Jared#5984", color=0xff003d)

        embed.set_footer(text='Leveling', icon_url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="**Ranks**", value="`?ranks` - Shows info for ranks commands\n`?ranks add` - Adds rank\n`?ranks remove` - Removes rank\n`?ranks list` - Lists all current ranks")
        embed.add_field(name="**Leveling**", value="`?leveling` - Shows info for leveling commands\n`?leveling enable` - Enables leveling (enabled by default)\n`?leveling disable` - Disables leveling")
        embed.add_field(name="**General**", value="`?rank <@user>` - Shows rank info for a user\n`?leaderboard` - Shows top 5 leaderboard")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Public(bot))
    print('Public is Loaded')