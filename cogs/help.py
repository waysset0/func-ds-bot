import disnake
from disnake.ext import commands

from config import settings

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = 'Помощь по командам')
    async def help(ctx):
        embed = disnake.Embed(
            title = '📕 Помощь по командам',
            color = settings['color'])

        embed.add_field(
            name = '❗ Модерация',
            value = '``ban`` ``unban`` ``kick`` ``mute`` ``unmute`` ``slowmode`` ``clear``',
            inline = False)
        embed.add_field(
            name = '🏃‍♂️ Взаимодействия',
            value = '``bite`` ``blush`` ``bonk`` ``bully`` ``cringe`` ``cry`` ``custom`` ``dance`` ``eat`` ``handhold`` ``happy`` ``highfive`` ``hug`` ``kiss`` ``lick`` ``pat`` ``poke`` ``slap`` ``smile`` ``smug`` ``wave`` ``wink``',
            inline = False)
        embed.add_field(
            name = '🎮 Развлечения',
            value = '``ben`` ``animals`` ``coin`` ``nsfw``',
            inline = False)
        embed.add_field(
            name = '💰 Экономика',
            value = '``balance`` ``withdraw`` ``deposit`` ``bet`` ``work`` ``bonus`` ``pay`` ``coin_eco`` ``leaderboard``',
            inline = False)
        embed.add_field(
            name = '⭐ Репутация',
            value = '``reputation-stats`` ``reputation-manage`` ``reputation-leaderboard``',
            inline = False)
        embed.add_field(
            name = '🎫 Другое',
            value = '``say`` ``info`` ``avatar`` ``report`` ``text-symbol``',
            inline = False)
        components=[
            disnake.ui.Button(label = "Добавить бота", style = disnake.ButtonStyle.url, url = settings['add_bot'], emoji = "➕"),
            disnake.ui.Button(label = "Сервер поддержки", style = disnake.ButtonStyle.url, url = settings['support_server'], emoji = "📕")
        ]
        await ctx.send(embed = embed, ephemeral = True, components = components)
def setup(bot):
    bot.add_cog(Help(bot))