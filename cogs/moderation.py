import disnake
from disnake.ext import commands

import datetime

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # ОЧИСТКА
    @commands.has_permissions(manage_messages = True)
    @commands.slash_command(description = 'Очистка сообщений')
    async def clear(self, ctx, количество: int = commands.Param(description = 'Укажите количество сообщений для удаления')):
        if количество > 1000:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = "К сожалению, но я не могу удалить более 1000 сообщений!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)
        else:
            deleted = await ctx.channel.purge(limit = количество)
            embed = disnake.Embed(
                title = '✅ Успешно',
                description = f'Вы удалили **{len(deleted)}/{количество}** сообщений!',
                color = disnake.Color.green())
            await ctx.send(embed = embed, ephemeral=True)

    # БАН
    @commands.has_permissions(ban_members = True)
    @commands.slash_command(description = 'Забанить')
    async def ban(self, ctx, пользователь: disnake.User = commands.Param(description = 'Выберите пользователя'), причина: str = commands.Param(None, description = 'Укажите причину')):
        try:
            await пользователь.ban(reason = причина)
            embed = disnake.Embed(
                title = "✅ Успешно",
                description = f"Пользователь **{пользователь.name}** (**{пользователь.id}**) был забанен по причине: **{причина}**!",
                color = disnake.Color.green())
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

    # РАЗБАН
    @commands.has_permissions(ban_members = True)
    @commands.slash_command(description = 'Разбанить')
    async def unban(self, ctx, пользователь: disnake.User = commands.Param(description = 'Введите айди пользователя')):
        try:
            await ctx.guild.unban(пользователь)
            embed = disnake.Embed(
                title = "✅ Успешно",
                description = f'Пользователь **{пользователь.name}** (**{пользователь.id}**) был разбанен!',
                color = disnake.Color.green())
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)


    # КИК
    @commands.has_permissions(kick_members = True)
    @commands.slash_command(description = 'Кикнуть')
    async def kick(self, ctx, участник: disnake.Member = commands.Param(description = 'Выберите участника')):
        try:
            await участник.kick()
            embed = disnake.Embed(
                title = "✅ Успешно",
                description = f"Участник **{участник.name}** (**{участник.id}**) был кикнут!",
                color = disnake.Color.green())
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

    # МЬЮТ (ТАЙМАУТ)
    @commands.has_permissions(administrator = True)
    @commands.slash_command(description = 'Выдать затычку')
    async def mute(self, ctx, участник: disnake.Member = commands.Param(description = 'Выберите участника'), время: int = commands.Param(description = 'На сколько Вы хотите заткнуть участника? (минуты)'), причина: str = commands.Param(description = 'Укажите причину')):
        try:
            if участник == ctx.author:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но Вы не можете заткнуть самого себя!",
                    color = disnake.Color.red())
                return await ctx.send(embed = embed, ephemeral = True)
            elif участник.bot:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но Вы не можете заткнуть бота!",
                    color = disnake.Color.red())
                return await ctx.send(embed = embed, ephemeral = True)
            elif время < 1:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но Вы не можете заткнуть на менее, чем 1 минуту!",
                    color = disnake.Color.red())
                return await ctx.send(embed = embed, ephemeral = True)

            время = datetime.datetime.now() + datetime.timedelta(minutes=время)
            await участник.timeout(until = время, reason = причина)
            cool_time = disnake.utils.format_dt(время, style="R")
            embed = disnake.Embed(
                title = "✅ Успешно",
                description = f"""Пользователю **{участник.name}** (**{участник.id}**) была выдана затычка по причине: **{причина}**!
                Затычка будет снята **{cool_time}**""",
                color = disnake.Color.green()
            ).set_thumbnail(url = участник.display_avatar.url)
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

    # РАЗМЬЮТ (РАЗТАЙМАУТ)
    @commands.has_permissions(administrator = True)
    @commands.slash_command(description = 'Снять затычку')
    async def unmute(self, ctx, участник: disnake.Member = commands.Param(description = 'Выберите участника')):
        try:
            if участник == ctx.author:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но Вы не можете снять затычку с самого себя!",
                    color = disnake.Color.red())
                return await ctx.send(embed = embed, ephemeral = True)
            elif участник.bot:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но Вы не можете снять затычку с бота!",
                    color = disnake.Color.red())
                return await ctx.send(embed = embed, ephemeral = True)
            else:
                await участник.timeout(until = None, reason = None)
                embed = disnake.Embed(
                title = "✅ Успешно",
                description = f"С пользователя **{участник.name}** (**{участник.id}**) была снята затычка!",
                color = disnake.Color.green()
            ).set_thumbnail(url = участник.display_avatar.url)
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

    @commands.slash_command(description = 'Поставить медленный режим на текущий канал')
    async def slowmode(self, ctx, время: int = commands.Param(description = 'На сколько Вы хотите медленный режим? (секунды)')):
        try:
            if время < 0:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = f"К сожалению, но нельзя поставить медленный режим меньше 0 секунд!",
                    color = disnake.Color.red())
                await ctx.send(embed = embed, ephemeral = True)
            else:
                await ctx.channel.edit(slowmode_delay = время)
                embed = disnake.Embed(
                    title = '✅ Успешно',
                    description = f'Установлен медленный режим на **{время}** секунд.',
                    color = disnake.Color.green())
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed)
        except Exception as e:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = f"К сожалению, но произошла ошибка: **{e}**!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

def setup(bot):
    bot.add_cog(Moderation(bot))