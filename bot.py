import discord
from discord.ext import commands
import asyncio
import sys, traceback
import time
import os
import math
import json
import sqlite3
import random
import re
import datetime
from datetime import timedelta
from collections import OrderedDict, deque, Counter

bot = commands.Bot(command_prefix='?', case_insensitive=True)
bot.remove_command('help')

initial_extensions = ['cogs.leveling']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('Ready!')
    return await bot.change_presence(activity=discord.Activity(type=1, name='Developing Update', url='https://twitch.tv/twitch'))

@bot.command(pass_context=True)
async def reload(ctx, *, msg):
    """Load a module."""
    await ctx.message.delete()
    try:
        if os.path.exists("custom_cogs/{}.py".format(msg)):
            bot.reload_extension("custom_cogs.{}".format(msg))
        elif os.path.exists("cogs/{}.py".format(msg)):
            bot.reload_extension("cogs.{}".format(msg))
        else:
            raise ImportError("No module named '{}'".format(msg))
    except Exception as e:
        await ctx.send('Failed to reload module: `{}.py`'.format(msg))
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('Reloaded module: `{}.py`'.format(msg))

@bot.command(pass_context=True)
async def unload(ctx, *, msg):
    """Unload a module"""
    await ctx.message.delete()
    try:
        if os.path.exists("cogs/{}.py".format(msg)):
            bot.unload_extension("cogs.{}".format(msg))
        elif os.path.exists("custom_cogs/{}.py".format(msg)):
            bot.unload_extension("custom_cogs.{}".format(msg))
        else:
            raise ImportError("No module named '{}'".format(msg))
    except Exception as e:
        await ctx.send('Failed to unload module: `{}.py`'.format(msg))
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('Unloaded module: `{}.py`'.format(msg))

@bot.command(pass_context=True)
async def load(ctx, *, msg):
    """Load a module"""
    await ctx.message.delete()
    try:
        if os.path.exists("cogs/{}.py".format(msg)):
            bot.load_extension("cogs.{}".format(msg))
        elif os.path.exists("custom_cogs/{}.py".format(msg)):
            bot.load_extension("custom_cogs.{}".format(msg))
        else:
            raise ImportError("No module named '{}'".format(msg))
    except Exception as e:
        await ctx.send('Failed to load module: `{}.py`'.format(msg))
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('Loaded module: `{}.py`'.format(msg))

bot.run(TOKEN)