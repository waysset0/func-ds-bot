import disnake
from disnake.ext import commands

from config import settings

import json
import requests
import os

intents=disnake.Intents.default()
bot = commands.Bot(command_prefix = "&", intents=intents, help_command=None)

# ГОТОВНОСТЬ
@bot.event
async def on_ready():
	print('Я готов к полёту! От: {0.user}'.format(bot))

# КОГИ
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(settings['TOKEN'])