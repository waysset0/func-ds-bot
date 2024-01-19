import disnake
from disnake.ext import commands

import sqlite3

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.connection = sqlite3.connect('server.db')
        self.cursor = self.connection.cursor()

    @commands.slash_command(description = 'Посмотреть баланс')
    async def balance(self, ctx, пользователь: disnake.Member = commands.Param(None, description="Выберите пользователя")):
        if пользователь is None:
            await ctx.send(embed = disnake.Embed(
                description = f"""Баланс пользователя **{ctx.author}** составляет **{self.cursor.execute("SELECT cash FROM users WHERE server_id = {} and id = {}".format(ctx.guild.id, ctx.author.id)).fetchone()[0]} :leaves:**"""
            ))
            
        else:
            await ctx.send(embed = disnake.Embed(
                description = f"""Баланс пользователя **{пользователь}** составляет **{self.cursor.execute("SELECT cash FROM users WHERE server_id = {} and id = {}".format(пользователь.guild.id, пользователь.id)).fetchone()[0]} :leaves:**"""
            ))  

def setup(bot):
    bot.add_cog(Economy(bot))