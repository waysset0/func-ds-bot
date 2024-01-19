import disnake
from disnake.ext import commands

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
            title=f"Аватар пользователя – {member}",
            color=0x2d2d30
        )
        # Устанавливаем изображение (аватар) в эмбед.
        embed.set_image(url=member.display_avatar)
        embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.response.send_message(embed=embed)

    # ПИСАТЬ ОТ БОТА
    @commands.slash_command(description="Писать от имени бота")
    async def say(self, ctx, текст: str = commands.Param(description="Напишите текст")):
        try:
            if "@" in текст:
                embed = disnake.Embed(
                    title = "❌ Ошибка",
                    description = "К сожалению, но текст не должен содеражть "@"!",
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

def setup(bot):
    bot.add_cog(Other(bot))