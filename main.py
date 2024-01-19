import disnake
from disnake.ext import commands

from config import settings

import sqlite3
import json
import requests
import os

intents=disnake.Intents.default()
bot = commands.Bot(command_prefix = "&", intents=intents, help_command=None)

connection = sqlite3.connect('server.db')
cursor = connection.cursor()

# ГОТОВНОСТЬ
@bot.event
async def on_ready():
  cursor.execute("""CREATE TABLE IF NOT EXISTS users (
 name TEXT,
 id INT,
 cash BIGINT,
 bank BIGINT,
 server_id INT
    )""")
 
  for guild in bot.guilds:
      for member in guild.members:
          if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
              cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, {guild.id})")
          else:
              pass

  connection.commit()
  print('Я готов к полёту! От: {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
    if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, {member.guild.id})")
        connection.commit()
    else:
        pass

# УПОМИНАНИЕ БОТА
@bot.event
async def on_message(message):
  if bot.user.mentioned_in(message):
    embed = disnake.Embed(
      title = 'Помощь',
      description = settings['mention'],
      color = settings['color'])
    embed.set_thumbnail(url = settings['avatar_bot'])
    embed.set_footer(text = f"Запросил: {message.author.name}", icon_url = message.author.display_avatar.url)
    await message.reply(embed = embed)

# КОГИ
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(settings['TOKEN'])