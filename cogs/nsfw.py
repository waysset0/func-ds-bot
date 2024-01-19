import disnake
from disnake.ext import commands

import json
import requests

class NSFW(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # ЖИВОТНЫЕ
    @commands.slash_command(description="NSFW")
    async def nsfw(ctx, nsfw: str = commands.Param(description="Выберите", choices=["Waifu", "Neko", "Trap", "Blowjob"])):
        if ctx.channel.nsfw:
            if nsfw == "Waifu":

                response = requests.get('https://api.waifu.pics/nsfw/waifu') # Get-запрос
                json_data = json.loads(response.text) # Извлекаем JSON

                embed = disnake.Embed(
                    color = 0x2d2d30) # Создание Embed'a
                embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed) # Отправляем Embed

            elif nsfw == "Neko":

                response = requests.get('https://api.waifu.pics/nsfw/neko') # Get-запрос
                json_data = json.loads(response.text) # Извлекаем JSON

                embed = disnake.Embed(
                    color = 0x2d2d30) # Создание Embed'a
                embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed) # Отправляем Embed

            elif nsfw == "Trap":

                response = requests.get('https://api.waifu.pics/nsfw/trap') # Get-запрос
                json_data = json.loads(response.text) # Извлекаем JSON

                embed = disnake.Embed(
                    color = 0x2d2d30) # Создание Embed'a
                embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed) # Отправляем Embed

            elif nsfw == "Blowjob":

                response = requests.get('https://api.waifu.pics/nsfw/blowjob') # Get-запрос
                json_data = json.loads(response.text) # Извлекаем JSON

                embed = disnake.Embed(
                    color = 0x2d2d30) # Создание Embed'a
                embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed) # Отправляем Embed
        else:
            embed = disnake.Embed(
                title = "❌ Ошибка",
                description = "К сожалению, но данная команда работает только в NSFW канале!",
                color = disnake.Color.red())
            await ctx.send(embed = embed, ephemeral = True)

def setup(bot):
    bot.add_cog(NSFW(bot))