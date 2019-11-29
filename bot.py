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

initial_extensions = ['cogs.leveling',
                      'cogs.public']

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
    return await bot.change_presence(activity=discord.Activity(type=3, name='for Levels'))

@bot.event
async def on_guild_join(guild):
    main = sqlite3.connect('Leveling/main.db')
    cursor = main.cursor()
    cursor.execute(f"SELECT enabled FROM glevel WHERE guild_id = '{guild.id}'")
    result = cursor.fetchone()
    if result is None:
        sql = ("INSERT INTO glevel(guild_id, enabled) VALUES(?,?)")
        val = (str(guild.id), 'enabled')
        cursor.execute(sql, val)
        main.commit()
    elif str(result[0]) == 'disabled':
        sql = ("UPDATE glevel SET enabled = ? WHERE guild_id = ?")
        val = ('enabled', str(guild.id))
        cursor.execute(sql, val)
        main.commit()
    cursor.close()
    main.close()


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