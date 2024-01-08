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

def setup(bot):
    bot.add_cog(Other(bot))