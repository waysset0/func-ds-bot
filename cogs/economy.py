import disnake
from disnake.ext import commands

import sqlite3
import random
import asyncio

from config import settings

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.connection = sqlite3.connect('/data/users.db')
        self.cursor = self.connection.cursor()
        self.emoji_money = settings['emoji_money']

    # БАЛАНС
    @commands.slash_command(description="Баланс")
    async def balance(self, inter, пользователь: disnake.User = commands.Param(None, description = 'Выберите пользователя')):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
        result = self.cursor.fetchone()
        if result:
            try:
                cash_author = self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(inter.author.id)).fetchone()[0]
                bank_author = self.cursor.execute("SELECT bank FROM users WHERE id = {}".format(inter.author.id)).fetchone()[0]
                all_money = cash_author + bank_author

                if пользователь is None:
                    embed = disnake.Embed(
                        title = "💸 Баланс",
                        description = f"Ваш баланс средств на руках: **{cash_author}** {self.emoji_money}\nВаш баланс средств в банке: **{bank_author}** {self.emoji_money}\nВсего средств: **{all_money}** {self.emoji_money}",
                        color = settings['color'])
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                    await inter.send(embed = embed)
                elif пользователь.bot:
                    embed_error = disnake.Embed(
                        title = '❌ Ошибка!',
                        description = "К сожалению, но на ботов это не действует!",
                        color = disnake.Colour.red())
                    await inter.send(embed = embed_error, ephemeral = True)
                elif пользователь == inter.author:
                    embed_error = disnake.Embed(
                        title = '❌ Ошибка!',
                        description = "К сожалению, но на себе это не действует!",
                        color = disnake.Colour.red())
                    await inter.send(embed = embed_error, ephemeral = True)
                else:
                    cash_member = self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(пользователь.id)).fetchone()[0]
                    bank_member = self.cursor.execute("SELECT bank FROM users WHERE id = {}".format(пользователь.id)).fetchone()[0]
                    all_money = cash_member + bank_member
                    
                    embed = disnake.Embed(
                        title = f"💸 Баланс пользователя — {пользователь}",
                        description = f"Ваш баланс средств на руках: **{cash_member}** {self.emoji_money}\nВаш баланс средств в банке: **{bank_member}** {self.emoji_money}\nВсего средств: **{all_money}** {self.emoji_money}",
                        color = settings['color'])
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                    await inter.send(embed = embed)
            except Exception as e:
                embed_error = disnake.Embed(
                    title = '❌ Ошибка!',
                    description = f"К сожалению, но Вы или данный пользователь, которого вы указали еще не зарегистрированы в нашей базе данных! \n\nОшибка: **{e}**",
                    color = disnake.Colour.red())
                embed_error.set_footer(text = 'Напишите что-нибудь в чат, чтобы бот зарегистрировал Вас')
                await inter.send(embed = embed_error, ephemeral = True)
        else:
            if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)

    # РАБОТА
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.slash_command(description = 'Работа')
    async def work(self, inter):
        money = random.randint(20, 150)
        work_text = ["стоматологом", "грузчиком", "таксистом", "блогером", "продавцом", "программистом", "фрилансером", "учителем", "консультантом"]
        work = work_text[random.randint(0, len(work_text) - 1)]
        
        try:
            self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
            result = self.cursor.fetchone()
            if result:
                embed = disnake.Embed(
                    title = '💰 Работа',
                    description = f'Вы работали {work} и заработали **{money}** {self.emoji_money}!',
                    color = settings['color'])
                embed.set_footer(text = 'Следующее использование данной команды будет доступна через 1 минуту!')
                embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                await inter.send(embed = embed)
                self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(money, inter.author.id))
                self.connection.commit()
            else:
                if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                    self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                    self.connection.commit()
                    await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)
                    self.work.reset_cooldown(inter)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка", 
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Colour.red())
            await inter.send(embed = embed, ephemeral = True)

    # ПОЛОЖИТЬ ДЕНЬГИ В БАНК
    @commands.slash_command(description = 'Положить средства на счёт банка')
    async def deposit(self, inter, число: int = commands.Param(description = 'Введите число, которое хотите положить на счёт банка')):
        self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(inter.author.id))
        result = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
        result1 = self.cursor.fetchone()
        
        if result1:
            if число <= 0:
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'Введите число больше нуля!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            elif result and result[0] < int(число):
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'К сожалению, но у вас не хватает средств на руках!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            else:
                try:
                    embed = disnake.Embed(
                        title = '✅ Успешно',
                        description = f'Вы успешно положили **{число}** {self.emoji_money} к себе на счёт банка!',
                        color = disnake.Color.green())
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                    await inter.send(embed = embed)
                    self.cursor.execute("UPDATE users SET bank = bank + {} WHERE id = {}".format(число, inter.author.id))
                    self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(число, inter.author.id))
                    self.connection.commit()
                except Exception as e:
                    embed = disnake.Embed(
                        title = "❌ Ошибка", 
                        description = f"К сожалению, но произошла ошибка: **{e}**!",
                        color = disnake.Colour.red())
                    await inter.send(embed = embed, ephemeral = True)
        else:
            if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)

    # СНЯТЬ ДЕНЬГИ С БАНКА
    @commands.slash_command(description = 'Снять средства со счёта банка')
    async def withdraw(self, inter, число: int = commands.Param(description = 'Введите число, которое хотите снять со счёта банка')):
        self.cursor.execute("SELECT bank FROM users WHERE id = {}".format(inter.author.id))
        result = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
        result1 = self.cursor.fetchone()
        if result1:
            if число <= 0:
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'Введите число больше нуля!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            elif result and result[0] < int(число):
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'К сожалению, но у вас не хватает средств в банке!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            else:
                try:
                    embed = disnake.Embed(
                        title = '✅ Успешно',
                        description = f'Вы успешно сняли **{число}** {self.emoji_money} со счёта банка!',
                        color = disnake.Color.green())
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                    await inter.send(embed = embed)
                    self.cursor.execute("UPDATE users SET bank = bank - {} WHERE id = {}".format(число, inter.author.id))
                    self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(число, inter.author.id))
                    self.connection.commit()
                except Exception as e:
                    embed = disnake.Embed(
                        title = "❌ Ошибка", 
                        description = f"К сожалению, но произошла ошибка: **{e}**!",
                        color = disnake.Colour.red())
                    await inter.send(embed = embed, ephemeral = True)
        else:
            if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)

    @commands.slash_command(description = 'Ставка')
    async def bet(self, inter, число: int = commands.Param(description = 'Введите число, на которое хотите сыграть')):
        self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(inter.author.id))
        result = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
        result1 = self.cursor.fetchone()
        if result1:
            if число <= 0:
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'Введите число больше нуля!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            elif result and result[0] < int(число):
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'К сожалению, но у вас не хватает средств на руках!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            else:
                win_lose = random.randint(1, 2)
                x = random.randint(1, 2)
                try:
                    if win_lose == 1:
                        if x == 1:
                            amount_win = число * 1.5
                            embed = disnake.Embed(
                                title = '✅ Победа',
                                description = f'Поздравляю, Ваша ставка умножена в 1.5 раза!\nВаш выигрыш: **{round(amount_win)}** {self.emoji_money}!',
                                color = disnake.Color.green())
                            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                            self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(число, inter.author.id))
                            self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(round(amount_win), inter.author.id))
                            await inter.send(embed = embed)
                        elif x == 2:
                            amount_win = число * 2
                            embed = disnake.Embed(
                                title = '✅ Победа',
                                description = f'Поздравляю, Ваша ставка умножена в 2 раза!\nВаш выигрыш: **{amount_win}** {self.emoji_money}!',
                                color = disnake.Color.green())
                            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                            self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(число, inter.author.id))
                            self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(amount_win, inter.author.id))
                            await inter.send(embed = embed)
                    elif win_lose == 2:
                        embed = disnake.Embed(
                            title = '❌ Проигрыш',
                            description = f'К сожалению, но Вы проиграли!\nВаш проигрыш: **{число}** {self.emoji_money}',
                            color = disnake.Color.red())
                        embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                        self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(число, inter.author.id))
                        await inter.send(embed = embed)
                except Exception as e:
                    embed = disnake.Embed(
                        title = "❌ Ошибка", 
                        description = f"К сожалению, но произошла ошибка: **{e}**!",
                        color = disnake.Colour.red())
                    await inter.send(embed = embed, ephemeral = True)
        else:
            if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.slash_command(description = 'Бонус')
    async def bonus(self, inter):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
        result = self.cursor.fetchone()
        bonus = random.randint(150, 400)

        if result:
            embed = disnake.Embed(
                title = '🎁 Бонус',
                description = f'Вы получили бонус в размере **{bonus}** {self.emoji_money}!',
                color = disnake.Color.green())
            embed.set_footer(text = 'Следующий бонус будет доступен через 24 часа!')
            await inter.send(embed = embed)
            self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(bonus, inter.author.id))
            self.connection.commit()
        else:
            if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)
                self.bonus.reset_cooldown(inter)

    # ПЕРЕВОД
    @commands.slash_command(description = 'Перевод денег')
    async def pay(self, inter, участник: disnake.Member = commands.Param(description = 'Введите пользователя'), количество: int = commands.Param(description = 'Введите количество средств, которое хотите перевести')):
        self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(inter.author.id))
        result = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
        result1 = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (участник.id,))
        result2 = self.cursor.fetchone()
        if result1:
            if участник.bot:
                await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете перевести средства боту!", color=disnake.Colour.red()), ephemeral=True)
            elif участник == inter.author:
                await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете перевести средства самому себе!", color=disnake.Colour.red()), ephemeral=True)
            elif not result2:
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'Данный участник не зарегистрирован в экономике!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            elif количество <= 0:
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'Введите количество больше нуля!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            elif result and result[0] < int(количество):
                embed = disnake.Embed(
                    title = '❌ Ошибка',
                    description = 'К сожалению, но у вас не хватает средств на руках!',
                    color = disnake.Color.red())
                await inter.send(embed = embed, ephemeral = True)
            else:
                try:
                    количествоком = количество * 0.85
                    embed = disnake.Embed(
                        title = '✅ Успешно',
                        description = f'Вы успешно перевели **{количество}** {self.emoji_money}!\n\nИтоговая сумма с комиссией: **{round(количествоком)}** {self.emoji_money}',
                        color = disnake.Color.green())
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                    await inter.send(embed = embed)
                    self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(количество, inter.author.id))
                    self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(round(количествоком), участник.id))
                    self.connection.commit()

                except Exception as e:
                    embed = disnake.Embed(
                        title = "❌ Ошибка", 
                        description = f"К сожалению, но произошла ошибка: **{e}**!",
                        color = disnake.Colour.red())
                    await inter.send(embed = embed, ephemeral = True)
        else:
            if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                self.connection.commit()
                await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)

    # МОНЕТКА ЭКО
    # @commands.slash_command(description = 'Монетка с экономикой')
    # async def coin_eco(self, inter, сторона: str = commands.Param(description = 'Выберите сторону', choices=["Орёл", "Решка"]), участник: disnake.Member = commands.Param(None, description = 'Выберите участника для игры с вами'), ставка: int = commands.Param(description = 'Введите ставку')):
    #     try:
    #         self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(inter.author.id,))
    #         result = self.cursor.fetchone()
    #         self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(участник.id,))
    #         result3 = self.cursor.fetchone()

    #         self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
    #         result1 = self.cursor.fetchone()
    #         self.cursor.execute("SELECT * FROM users WHERE id = ?", (участник.id,))
    #         result2 = self.cursor.fetchone()
    #         if result1:
    #             if участник == None:
    #                 random_r = random.randint(1, 2)
    #                 if ставка <= 0:
    #                     embed = disnake.Embed(
    #                         title = '❌ Ошибка',
    #                         description = 'Введите ставку больше нуля!',
    #                         color = disnake.Color.red())
    #                     await inter.send(embed = embed, ephemeral = True)
    #                 elif result and result[0] < int(ставка):
    #                     embed = disnake.Embed(
    #                         title = '❌ Ошибка',
    #                         description = 'К сожалению, но у вас не хватает средств на руках!',
    #                         color = disnake.Color.red())
    #                     await inter.send(embed = embed, ephemeral = True)
                
    #                 elif сторона == "Орёл":   
    #                     if random_r == 1:    
    #                         embed = disnake.Embed(
    #                             title = "🪙 Монетка",
    #                             description = f"Вы угадали, выпал орёл!\n\nВы выиграли **{ставка}** {self.emoji_money}",
    #                             color = disnake.Color.green()
    #                             )
    #                         embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                         await inter.send(embed = embed)
    #                         self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, inter.author.id))
    #                         self.connection.commit()
                        
    #                     else:    
    #                         embed = disnake.Embed(
    #                             title = "🪙 Монетка",
    #                             description = f"Вы не угадали, выпала решка!\n\nВы проиграли **{ставка}** {self.emoji_money}",
    #                             color = disnake.Color.red()
    #                             )
    #                         embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                         await inter.send(embed = embed)
    #                         self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, inter.author.id))
    #                         self.connection.commit()
    #                 else:
    #                     if random_r == 1:
    #                         embed = disnake.Embed(
    #                             title = "🪙 Монетка",
    #                             description = f"Вы угадали, выпала решка!\n\nВы выиграли **{ставка}** {self.emoji_money}",
    #                             color = disnake.Color.green()
    #                             )
    #                         embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                         await inter.send(embed = embed)
    #                         self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, inter.author.id))
    #                         self.connection.commit()
    #                     else:    
    #                         embed = disnake.Embed(
    #                             title = "🪙 Монетка",
    #                             description = f"Вы не угадали, выпал орёл!\n\nВы проиграли **{ставка}** {self.emoji_money}",
    #                             color = disnake.Color.red()
    #                             )
    #                         embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                         await inter.send(embed = embed)
    #                         self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, inter.author.id))
    #                         self.connection.commit()
                
    #             elif участник.bot:
    #                 await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете перевести средства боту!", color=disnake.Colour.red()), ephemeral=True)
    #             elif участник == inter.author:
    #                 await inter.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но Вы не можете перевести средства самому себе!", color=disnake.Colour.red()), ephemeral=True)
    #             elif not result2:
    #                 embed = disnake.Embed(
    #                     title = '❌ Ошибка',
    #                     description = 'Данный участник не зарегистрирован в экономике!',
    #                     color = disnake.Color.red())
    #                 await inter.send(embed = embed, ephemeral = True)
    #             elif ставка <= 0:
    #                 embed = disnake.Embed(
    #                     title = '❌ Ошибка',
    #                     description = 'Введите ставку больше нуля!',
    #                     color = disnake.Color.red())
    #                 await inter.send(embed = embed, ephemeral = True)
    #             elif result and result[0] < int(ставка):
    #                 embed = disnake.Embed(
    #                     title = '❌ Ошибка',
    #                     description = 'К сожалению, но у вас не хватает средств на руках!',
    #                     color = disnake.Color.red())
    #                 await inter.send(embed = embed, ephemeral = True)
    #             elif result3 and result3[0] < int(ставка):
    #                 embed = disnake.Embed(
    #                     title = '❌ Ошибка',
    #                     description = 'К сожалению, но у участника не хватает средств на руках!',
    #                     color = disnake.Color.red())
    #                 await inter.send(embed = embed, ephemeral = True)
    #             else:
    #                 random_r = random.randint(1, 2)
    #                 embed = disnake.Embed(
    #                     title = "🪙 Монетка", 
    #                     description = f"**{inter.author}** предлагает вам сыграть в монетку!\n\nСумма: **{ставка}** {self.emoji_money}",
    #                     color = disnake.Color.green())
    #                 components = [
    #                     disnake.ui.Button(label = "Подтвердить", style = disnake.ButtonStyle.green, custom_id = "confirm"),
    #                     disnake.ui.Button(label = "Отмена", style = disnake.ButtonStyle.red, custom_id = "cancel")
    #                 ]
    #                 await inter.response.send_message(f"{участник.mention}", embed = embed, components = components)
                    
    #                 try:
    #                     interaction = await inter.bot.wait_for("button_click", check = lambda i: i.user.id == участник.id and i.component.custom_id in ["confirm", "cancel"], timeout=60)
                        
    #                     # buttons
    #                     if interaction.component.custom_id == 'confirm':
                            
    #                         if сторона == "Орёл":
                                
    #                             if random_r == 1:    
    #                                 embed = disnake.Embed(
    #                                     title = "🪙 Монетка",
    #                                     description = f"**{inter.author}** угадал, выпал орёл!\n\nПобеда засчитана: **{inter.author}**",
    #                                     color = disnake.Color.green()
    #                                     )
    #                                 embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                                 await interaction.response.edit_message("", embed = embed, components = None)
    #                                 self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, inter.author.id))
    #                                 self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, участник.id))
    #                                 self.connection.commit()
                                
    #                             else:  
    #                                 embed = disnake.Embed(
    #                                     title = "🪙 Монетка",
    #                                     description = f"**{inter.author}** не угадал, выпала решка!\n\nПобеда засчитана: **{участник}**",
    #                                     color = disnake.Color.red()
    #                                     )
    #                                 embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                                 await interaction.response.edit_message("", embed = embed, components = None)
    #                                 self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, inter.author.id))
    #                                 self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, участник.id))
    #                                 self.connection.commit()

    #                         else:
                                
    #                             if random_r == 1:
                                    
    #                                 embed = disnake.Embed(
    #                                     title = "🪙 Монетка",
    #                                     description = f"**{inter.author}** угадал, выпала решка!\n\nПобеда засчитана: **{inter.author}**",
    #                                     color = disnake.Color.green()
    #                                     )
    #                                 embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                                 await interaction.response.edit_message("", embed = embed, components = None)
    #                                 self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, inter.author.id))
    #                                 self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, участник.id))
    #                                 self.connection.commit()

    #                             else:
                                    
    #                                 embed = disnake.Embed(
    #                                     title = "🪙 Монетка",
    #                                     description = f"**{inter.author}** не угадал, выпал орёл!\n\nПобеда засчитана: **{участник}**",
    #                                     color = disnake.Color.red()
    #                                     )
    #                                 embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
    #                                 await interaction.response.edit_message("", embed = embed, components = None)
    #                                 self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, inter.author.id))
    #                                 self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, участник.id))
    #                                 self.connection.commit()

    #                     elif interaction.component.custom_id == 'cancel':
    #                         embed = disnake.Embed(
    #                             title = "🪙 Монетка", 
    #                             description = f"**{участник}** отказался!", 
    #                             color = disnake.Color.red())
    #                         await interaction.response.edit_message(f"{inter.author.mention}", embed = embed, components = None)
                    
    #                 except asyncio.TimeoutError:
    #                     return
    #         else:
    #             if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

    #                 self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
    #                 self.connection.commit()
    #                 await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)
    #     except Exception as e:
    #         await inter.send(f'ошибка {e}')

    @commands.slash_command(description = 'Монетка')
    async def coin_eco(self, inter, сторона: str = commands.Param(description = 'Выберите сторону', choices=["Орёл", "Решка"]), ставка: int = commands.Param(description = 'Введите желаемую ставку')):
        try:
            self.cursor.execute("SELECT cash FROM users WHERE id = {}".format(inter.author.id))
            result = self.cursor.fetchone()
            self.cursor.execute("SELECT * FROM users WHERE id = ?", (inter.author.id,))
            result1 = self.cursor.fetchone()
            if result:
                random_r = random.randint(1, 2)
                if ставка <= 0:
                    embed = disnake.Embed(
                        title = '❌ Ошибка',
                        description = 'Введите ставку больше нуля!',
                        color = disnake.Color.red())
                    await inter.send(embed = embed, ephemeral = True)
                elif result and result[0] < int(ставка):
                    embed = disnake.Embed(
                        title = '❌ Ошибка',
                        description = 'К сожалению, но у вас не хватает средств на руках!',
                        color = disnake.Color.red())
                    await inter.send(embed = embed, ephemeral = True)
            
                elif сторона == "Орёл":   
                    if random_r == 1:    
                        embed = disnake.Embed(
                            title = "🪙 Монетка",
                            description = f"Вы угадали, выпал орёл!\n\nВы выиграли **{ставка}** {self.emoji_money}",
                            color = disnake.Color.green()
                            )
                        embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                        await inter.send(embed = embed)
                        self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, inter.author.id))
                        self.connection.commit()
                    
                    else:    
                        embed = disnake.Embed(
                            title = "🪙 Монетка",
                            description = f"Вы не угадали, выпала решка!\n\nВы проиграли **{ставка}** {self.emoji_money}",
                            color = disnake.Color.red()
                            )
                        embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                        await inter.send(embed = embed)
                        self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, inter.author.id))
                        self.connection.commit()
                else:
                    if random_r == 1:
                        embed = disnake.Embed(
                            title = "🪙 Монетка",
                            description = f"Вы угадали, выпала решка!\n\nВы выиграли **{ставка}** {self.emoji_money}",
                            color = disnake.Color.green()
                            )
                        embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                        await inter.send(embed = embed)
                        self.cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(ставка, inter.author.id))
                        self.connection.commit()
                    else:    
                        embed = disnake.Embed(
                            title = "🪙 Монетка",
                            description = f"Вы не угадали, выпал орёл!\n\nВы проиграли **{ставка}** {self.emoji_money}",
                            color = disnake.Color.red()
                            )
                        embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                        await inter.send(embed = embed)
                        self.cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(ставка, inter.author.id))
                        self.connection.commit()
            else:
                if self.cursor.execute(f"SELECT id FROM users WHERE id = {inter.author.id}").fetchone() is None:

                    self.cursor.execute(f"INSERT INTO users VALUES ({inter.author.id}, 0, 0, '{inter.author}')")
                    self.connection.commit()
                    await inter.send("Вы успешно зарегистрировались в экономике!", ephemeral = True)
        except Exception as e:
            inter.send(f'error **{e}**')            

    @commands.slash_command(description = 'Доска лидеров')
    async def leaderboard(self, inter):
        embed = disnake.Embed(title = 'Топ 5', color = settings['color'])
        counter = 0
     
        for row in self.cursor.execute("SELECT name, cash, bank, cash + bank AS total FROM users ORDER BY total DESC LIMIT 5"):
            counter += 1
            embed.add_field(
                name = f'# {counter} | `{row[0]}`',
                value = f'Средства: **{row[3]}** {self.emoji_money}',
                inline = False
            )
            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
        await inter.send(embed = embed)

def setup(bot):
    bot.add_cog(Economy(bot))