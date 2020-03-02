import discord
from discord.ext import commands, tasks
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
import logging
import dbl
from .utils import checks


class BotList(commands.Cog, name='Ranks'):
    def __init__(self, bot):
        self.bot = bot
        self.token = 'API KEY' # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/dblwebhook', webhook_auth='password', webhook_port=5000)

    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        logger.info('Attempting to post server count')
        try:
            await self.dblpy.post_guild_count()
            logger.info('Posted server count ({})'.format(self.dblpy.guild_count()))
        except Exception as e:
            logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))

        # if you are not using the tasks extension, put the line below

        await asyncio.sleep(1800)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        logger.info('Received an upvote')
        print(data)

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(BotList(bot))
    print('Bot List is Loaded')