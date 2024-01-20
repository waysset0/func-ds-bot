# import disnake
# from disnake.ext import commands

# import sqlite3
# import random

# class Economy(commands.Cog):

#     def __init__(self, bot):
#         self.bot = bot

#     # БАЛАНС
#     @commands.slash_command(description = 'Посмотреть баланс')
#     async def balance(self, ctx, пользователь: disnake.Member = commands.Param(None, description="Выберите пользователя")):
#         user_id = ctx.author.id
#         guild_id = ctx.guild.id
#         db = sqlite3.connect(f'{guild_id}.db')
#         cursor = db.cursor()
#         cursor.execute('SELECT cash FROM economy WHERE user_id = ?', (user_id,))
#         result = cursor.fetchone()
#         if result:
#             await ctx.send(f'Ваш текущий баланс: {result[0]}')
#         else:
#             await ctx.send('Вы еще не зарегистрированы в экономике. Используйте команду **/register**')

#     # РЕГИСТРАЦИЯ
#     @commands.slash_command(description = 'Зарегистрироваться в экономике')
#     async def register(self, ctx):
#         user_id = ctx.author.id
#         guild_id = ctx.guild.id
#         db = sqlite3.connect(f'{guild_id}.db')
#         cursor = db.cursor()
#         cursor.execute('''
#             INSERT OR IGNORE INTO economy(user_id, cash, bank)
#             VALUES(?, ?)
#         ''', (user_id, 0, 0))
#         db.commit()
#         db.close()
#         await ctx.send('Вы успешно зарегистрированы в экономике!')

#     # РАБОТА
#     @commands.slash_command(description = 'Заработать игровой валюты')
#     async def work(self, ctx):
#         amount = random.randint(1, 10)

#         await ctx.send(f"ти заработав {amount} крос")

#         cursor.execute("UPDATE s_{} SET cash = cash + {} WHERE id = {}".format(ctx.guild.id, amount, ctx.author.id))
#         connection.commit()


# def setup(bot):
#     bot.add_cog(Economy(bot))