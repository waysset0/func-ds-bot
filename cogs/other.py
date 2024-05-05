import disnake
from disnake.ext import commands

from config import settings

import pyfiglet

class Other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # АВАТАР
    @commands.slash_command(description="Получить аватарку пользователя")
    async def avatar(self, ctx, пользователь: disnake.Member = commands.Param(None, description="Выберите пользователя")):
        # Если не указан пользователь (member), используем автора команды.
        member = пользователь or ctx.author
        # Создаем эмбед (вложенное сообщение) с информацией о аватаре пользователя.
        embed = disnake.Embed(
            title = f"Аватар пользователя – {member}",
            color = settings['color']
        )
        # Устанавливаем изображение (аватар) в эмбед.
        embed.set_image(url = member.display_avatar)
        embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.response.send_message(embed=embed)

    # ПИСАТЬ ОТ БОТА
    @commands.slash_command(description="Писать от имени бота")
    async def say(self, ctx, текст: str = commands.Param(description="Напишите текст")):
        try:
            if "@" in текст:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но мой создатель запретил мне упоминать кого-либо!",
                    color = disnake.Color.red())
                await ctx.send(embed = embed, ephemeral = True)
            else:
                await ctx.send(текст)
        except:
            embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но произошла неизвестная ошибка!",
                    color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

    @commands.cooldown(1, 10800, commands.BucketType.user)
    @commands.slash_command(description = 'Обращение')
    async def report(self, inter, *, обращение: str = commands.Param(description = 'Напишите развернутое сообщение')):
        try:
            guild = self.bot.get_guild(1205922933256753213)
            channel = await guild.fetch_channel(1217037532165046274)
            embed = disnake.Embed(
                title = '⚠ Новое обращение',
                description = f'Текст обращения: **{обращение}**',
                color = settings['color'])
            components = [
            disnake.ui.Button(style = disnake.ButtonStyle.secondary, label = f'{inter.author} ({inter.author.id})', disabled = True)]
            await channel.send(embed = embed, components = components)
            await inter.send("Спасибо за обращение! В случае, если Ваше обращение окажется полезным, то разработчики добавят Вам репутацию! 💖", ephemeral = True)
        except Exception as e:
            await inter.send(f'ошибка **{e}**')

    @commands.slash_command(name = 'text-symbol', description = 'Текст символами')
    async def text_symbol(self, inter, *, текст: str = commands.Param(description = 'Введите, желаемый текст'), стиль: str = commands.Param(description="Выберите", choices=["Slant", "Graffiti", "Starwars", "Poison"])):
        try:

            if стиль == "Slant":
                ready_text = pyfiglet.figlet_format(текст, font = "slant")

                embed = disnake.Embed(
                    description = f'```{ready_text}```',
                    color = settings['color'])
                await inter.send(embed = embed)
            elif стиль == "Graffiti":
                ready_text = pyfiglet.figlet_format(текст, font = "graffiti")

                embed = disnake.Embed(
                    description = f'```{ready_text}```',
                    color = settings['color'])
                await inter.send(embed = embed)
            elif стиль == "Starwars":
                ready_text = pyfiglet.figlet_format(текст, font = "starwars")

                embed = disnake.Embed(
                    description = f'```{ready_text}```',
                    color = settings['color'])
                await inter.send(embed = embed)
            elif стиль == "Poison":
                ready_text = pyfiglet.figlet_format(текст, font = "poison")

                embed = disnake.Embed(
                    description = f'```{ready_text}```',
                    color = settings['color'])
                await inter.send(embed = embed)
        except Exception as e:
            await inter.send(f"Произошла неизвестная ошибка, попробуйте снова!\n\nТекст ошибки: ``{e}``")

def setup(bot):
    bot.add_cog(Other(bot))