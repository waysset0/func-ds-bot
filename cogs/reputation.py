import disnake
from disnake.ext import commands

from config import settings

import sqlite3

class Reputation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.connection = sqlite3.connect('/data/reputation.db')
        self.cursor = self.connection.cursor()

    @commands.slash_command(name = 'reputation-stats', description='Посмотреть репутацию')
    async def reputation_stats(self, inter, участник: disnake.Member = commands.Param(None, description = 'Выберите пользователя')):
        self.cursor.execute("SELECT * FROM reputation WHERE id = ?", (inter.author.id,))
        result = self.cursor.fetchone()
        if result:
            if участник is None:
                rep_author = self.cursor.execute("SELECT reputation FROM reputation WHERE id =?", (inter.author.id,)).fetchone()[0]
                embed = disnake.Embed(
                    title = '⭐ Репутация',
                    description = f'Ваша репутация: **{rep_author}** ⭐',
                    color = settings['color'])
                embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                await inter.send(embed=embed)
            if участник.bot:
                await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете посмотреть репутацию бота!", color=disnake.Colour.red()), ephemeral=True)
            elif участник == inter.author:
                await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете таким способом посмотреть свою репутацию!", color=disnake.Colour.red()), ephemeral=True)
            else:
                self.cursor.execute("SELECT * FROM reputation WHERE id = ?", (участник.id,))
                result1 = self.cursor.fetchone()
                if not result1:
                    embed = disnake.Embed(
                        title = '❌ Ошибка',
                        description = 'Данный участник не зарегистрирован в системе репутаций!',
                        color = disnake.Color.red())
                    await inter.send(embed=embed, ephemeral=True)
                else:
                    rep_member = self.cursor.execute("SELECT reputation FROM reputation WHERE id =?", (участник.id,)).fetchone()[0]
                    embed = disnake.Embed(
                        title = f'⭐ Репутация участника — {участник}',
                        description = f'Репутация: **{rep_member}** ⭐',
                        color = settings['color'])
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                    await inter.send(embed = embed)
        else:
            if self.cursor.execute("SELECT id FROM reputation WHERE id =?", (inter.author.id,)).fetchone() is None:
                self.cursor.execute("INSERT INTO reputation VALUES (?, 0, ?)", (inter.author.id, str(inter.author)))
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в системе репутаций!", ephemeral=True)

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.slash_command(name = 'reputation-manage', description = 'Прибавить/убавить репутацию')
    async def reputation_manage(self, inter, участник: disnake.Member = commands.Param(description = 'Выберите участника'), управление: str = commands.Param(description = 'Выберите желаемое:', choices = ["Прибавить", "Убавить"])):
        self.cursor.execute("SELECT * FROM reputation WHERE id = ?", (inter.author.id,))
        result = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM reputation WHERE id = ?", (участник.id,))
        result1 = self.cursor.fetchone()
        if result:
            if участник.bot:
                await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете управлять репутацией бота!", color=disnake.Colour.red()), ephemeral=True)
                self.reputation_manage.reset_cooldown(inter)
            elif участник == inter.author:
                await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете управлять своей репутацией!", color=disnake.Colour.red()), ephemeral=True)
                self.reputation_manage.reset_cooldown(inter)
            elif not result1:
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'Данный участник не зарегистрирован в системе репутаций!',
                    color = disnake.Color.red())
                self.reputation_manage.reset_cooldown(inter)
                await inter.send(embed=embed, ephemeral=True)
            elif управление == "Прибавить":
                embed = disnake.Embed(
                    title = '✅ Успешно',
                    description = 'Вы прибавили **единицу** репутации данному участнику!',
                    color = disnake.Color.green())
                self.cursor.execute("UPDATE reputation SET reputation = reputation + {} WHERE id = {}".format(1, участник.id))
                self.connection.commit()
                await inter.send(embed = embed)
            elif управление == "Убавить":
                embed = disnake.Embed(
                    title = '✅ Успешно',
                    description = 'Вы убавили **единицу** репутации данному участнику!',
                    color = disnake.Color.green())
                self.cursor.execute("UPDATE reputation SET reputation = reputation - {} WHERE id = {}".format(1, участник.id))
                self.connection.commit()
                await inter.send(embed = embed)
        else:
            if self.cursor.execute("SELECT id FROM reputation WHERE id =?", (inter.author.id,)).fetchone() is None:
                self.cursor.execute("INSERT INTO reputation VALUES (?, 0, ?)", (inter.author.id, str(inter.author)))
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в системе репутаций!", ephemeral=True)
                self.reputation_manage.reset_cooldown(inter)

    @commands.slash_command(name = 'reputation-leaderboard', description = 'Доска лидеров репутации')
    async def reputation_leaderboard(self, inter):
        embed = disnake.Embed(title = 'Топ 5', color = settings['color'])
        counter = 0
     
        for row in self.cursor.execute("SELECT name, reputation FROM reputation ORDER BY reputation DESC LIMIT 5"):
            counter += 1
            embed.add_field(
                name = f'# {counter} | `{row[0]}`',
                value = f'Репутация: **{row[1]}**',
                inline = False
            )
            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
        await inter.send(embed = embed)

    # @commands.slash_command()
    # async def rep_add(self, inter, idd, amount: int):
    #     try:
    #         await inter.send(f'крос, добавил ему {amount} репутации')
    #         self.cursor.execute("UPDATE reputation SET reputation = reputation + {} WHERE id = {}".format(amount, idd))
    #         self.connection.commit()
    #     except Exception as e:
    #         await inter.send(f'Ошибка: **{e}**')

    # @commands.slash_command()
    # async def rep_remove(self, inter, idd, amount: int):
    #     try:
    #         await inter.send(f'крос, отобрал у него {amount} репутации')
    #         self.cursor.execute("UPDATE reputation SET reputation = reputation - {} WHERE id = {}".format(amount, idd))
    #         self.connection.commit()
    #     except Exception as e:
    #         await inter.send(f'Ошибка: **{e}**')

def setup(bot):
    bot.add_cog(Reputation(bot))