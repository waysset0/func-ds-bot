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
            value = '``ben`` ``animals`` ``coin`` ``nsfw``')
        embed.add_field(
            name = '🎫 Другое',
            value = '``say`` ``info`` ``avatar``')
        await ctx.send(embed = embed, ephemeral = True)
def setup(bot):
    bot.add_cog(Help(bot))