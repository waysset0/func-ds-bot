import disnake
from disnake.ext import commands

from config import settings

import sqlite3
import json
import requests
import os

# ИНТЕНТЫ
intents = disnake.Intents.default()
intents.message_content = True
intents.bans = True

bot = commands.Bot(command_prefix = "&", intents=intents, help_command=None)

# ГОТОВНОСТЬ
@bot.event
async def on_ready():
  print('Я готов к полёту! От: {0.user}'.format(bot))

# УПОМИНАНИЕ БОТА
@bot.event
async def on_message(message):
  if message.author == bot.user:
    pass
  if bot.user in message.mentions:
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

# ОШИБКА СЛЕШ КОМАНДА
@bot.event
async def on_slash_command_error(ctx, error):
  locale = {
    "permissions": {
      "create_instant_invite": "Создавать приглашения",
      "kick_members": "Выгонять участников",
      "ban_members": "Банить участников",
      "administrator": "Администратор",
      "manage_channels": "Управлять каналами",
      "manage_guild": "Управлять сервером",
      "add_reactions": "Добавлять реакции",
      "view_audit_log": "Просматривать журнал аудита",
      "manage_messages": "Управлять сообщениями",
      "embed_links": "Прикреплять ссылки",
      "attach_files": "Прикреплять файлы",
      "read_message_history": "Читать историю сообщений",
      "mention_everyone": "Упоминать всех",
      "external_emojis": "Использовать внешние эмодзи",
      "connect": "Подключаться к голосовым каналам",
      "speak": "Говорить в голосовых каналах",
      "move_members": "Перемещать участников",
      "change_nickname": "Изменять никйнейм",
      "manage_nicknames": "Управлять никнеймами",
      "manage_roles": "Управлять ролями",
      "manage_webhooks": "Управлять вебхуками",
      "manage_emojis": "Управлять эмодзи",
      "moderate_members": "Модерировать участников",
    }
  }
  if isinstance(error, commands.CommandOnCooldown):
    retry_after = str(
      datetime.timedelta(seconds=error.retry_after)).split('.')[0]
    await ctx.send(embed=disnake.Embed(
      title="❌ Ошибка",
      description=
      f"К сожалению, но для того, чтобы выполнить снова данную команду, подождите **{retry_after}** минут/секунд!",
      color=disnake.Colour.red()),
                   ephemeral=True)
  if isinstance(error, commands.MissingPermissions):
    perms = [
      f'— **{locale["permissions"][perm]}**'
      for perm in error.missing_permissions
    ]
    await ctx.send(embed=disnake.Embed(
      title="❌ Ошибка",
      description=
      f"К сожалению, но у Вас недостаточно прав для выполнения данной команды! Необходимые права: \n"
      + "\n".join(perms),
      color=disnake.Colour.red()),
                   ephemeral=True)
  if isinstance(error, commands.BotMissingPermissions):
    perms = [
      f'— **{locale["permissions"][perm]}**'
      for perm in error.missing_permissions
    ]
    await ctx.send(embed=disnake.Embed(
      title="❌ Ошибка",
      description=
      f"К сожалению, но у меня недостаточно прав для выполнения данной команды! Необходимые права: \n"
      + "\n".join(perms),
      color=disnake.Colour.red()),
                   ephemeral=True)

bot.run(settings['TOKEN'])