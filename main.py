import disnake
from disnake.ext import commands

from config import settings

import sqlite3
import json
import requests
import os
import datetime

# ИНТЕНТЫ
intents = disnake.Intents.default()
intents.message_content = True
intents.bans = True

bot = commands.Bot(command_prefix = "&", intents = intents, help_command = None)

connection = sqlite3.connect('/data/users.db')
cursor = connection.cursor()

connection_rep = sqlite3.connect('/data/reputation.db')
cursor_rep = connection_rep.cursor()

# ГОТОВНОСТЬ
@bot.event
async def on_ready():
  cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT,
    cash BIGINT,
    bank BIGINT,
    name TEXT
  )""")

  for guild in bot.guilds:
    for member in guild.members:
      if cursor.execute(
        f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES (?, 0, 0, ?)", (member.id, str(member)))
  connection.commit()
  cursor_rep.execute("""CREATE TABLE IF NOT EXISTS reputation (
    id INT,
    reputation BIGINT,
    name TEXT
  )""")

  for guild in bot.guilds:
    for member in guild.members:
      if cursor_rep.execute(
        f"SELECT id FROM reputation WHERE id = {member.id}").fetchone() is None:
        cursor_rep.execute(f"INSERT INTO reputation VALUES (?, 0, ?)", (member.id, str(member)))
  connection_rep.commit()
  print('Я готов к полёту! От: {0.user}'.format(bot))

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
      title="❌ Ошибка!",
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
      title="❌ Ошибка!",
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
      title="❌ Ошибка!",
      description=
      f"К сожалению, но у меня недостаточно прав для выполнения данной команды! Необходимые права: \n"
      + "\n".join(perms),
      color=disnake.Colour.red()),
                   ephemeral=True)

# УПОМИНАНИЕ БОТА
@bot.event
async def on_message(message):
  if cursor.execute(f"SELECT id FROM users WHERE id = {message.author.id}").fetchone() is None:

    cursor.execute(f"INSERT INTO users VALUES ({message.author.id}, 0, 0, '{message.author}')")
  connection.commit()

  if cursor_rep.execute(f"SELECT id FROM reputation WHERE id = {message.author.id}").fetchone() is None:

    cursor_rep.execute(f"INSERT INTO reputation VALUES ({message.author.id}, 0, '{message.author}')")
  connection_rep.commit()

# КОГИ
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

# Логирование инвайтов
@bot.event
async def on_guild_join(guild):
  guild = self.bot.get_guild(1205922933256753213)
  channel = await guild.fetch_channel(1205925741749997669)
  guild_count = len(bot.guilds)
  creator = await bot.fetch_user(guild.owner_id)
  embedd = disnake.Embed(title=f"➕ Izumi добавлен на сервер {guild.name}",
                    colour=0xffffff,
                    timestamp=datetime.now())

  embedd.set_author(name=f"Владелец сервера: {creator.name}")

  embedd.add_field(name="О сервере",
              value=f"{guild.name} | {guild.id} (ID)",
              inline=False)
  embedd.add_field(name="Владелец (ID)",
              value=f"{guild.owner_id}",
              inline=False)
  embedd.add_field(name="Количество участников",
              value=f"{guild.member_count}",
              inline=False)

  embedd.set_footer(text=f"Текущее количество серверов: {guild_count}")
  await channell.send(embed=embedd)

@bot.event
async def on_guild_remove(guild):
  guild = self.bot.get_guild(1205922933256753213)
  channel = await guild.fetch_channel(1205925741749997669)
  guild_count = len(bot.guilds)
  creator = await bot.fetch_user(guild.owner_id)
  embedd = disnake.Embed(title=f"➖ Izumi убран с сервера {guild.name}",
                    colour=0xffffff,
                    timestamp=datetime.now())

  embedd.set_author(name=f"Владелец сервера: {creator.name}")

  embedd.add_field(name="О сервере",
              value=f"{guild.name} | {guild.id} (ID)",
              inline=False)
  embedd.add_field(name="Владелец (ID)",
              value=f"{guild.owner_id}",
              inline=False)
  embedd.add_field(name="Количество участников",
              value=f"{guild.member_count}",
              inline=False)

  embedd.set_footer(text=f"Текущее количество серверов: {guild_count}")
  await channell.send(embed=embedd)

# INFOBOT
@bot.slash_command(description='Информация о боте')
async def info(ctx):
    guilds_count = len(bot.guilds)
    users_count = sum(guild.member_count for guild in bot.guilds)
    commands_count = 45
    ping = round(bot.latency * 1000)
    embed = disnake.Embed(
        title = 'ℹ Информация',
        color = settings['color']
    )
    embed.add_field(
      name = 'Открыт:',
      value = '``7 марта 2024 года``',
      inline = False)
    embed.add_field(
      name = 'Разработчик:',
      value = '``youbanan``',
      inline = False)
    embed.add_field(
      name = 'Серверов:',
      value = f'``{guilds_count}``',
      inline = True)
    embed.add_field(
      name = 'Пользователей:',
      value = f'``{users_count}``',
      inline = True)
    embed.add_field(
      name = 'Количество команд:',
      value = f'``{commands_count}``',
      inline = True)
    embed.add_field(
      name = 'Пинг:',
      value = f'``{ping}``',
      inline = True)
    embed.set_footer(text = f"Запросил: {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
    embed.set_thumbnail(url = settings['avatar_bot'])
    components=[
            disnake.ui.Button(label = "Добавить бота", style = disnake.ButtonStyle.url, url = settings['add_bot'], emoji = "➕"),
            disnake.ui.Button(label = "Сервер поддержки", style = disnake.ButtonStyle.url, url = settings['support_server'], emoji = "📕")
        ]
    await ctx.send(embed = embed, components = components)

bot.run(settings['TOKEN'])