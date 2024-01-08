import disnake
from disnake.ext import commands
import json
import requests

class Animals(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # ЖИВОТНЫЕ
    @commands.slash_command(description="Фотографии животных")
    async def animals(ctx, животное: str = commands.Param(description="Выберите животное", choices=["Лиса", "Кот", "Собака", "Панда", "Красная панда"])):
        if животное == "Лиса":

            response = requests.get('https://some-random-api.com/animal/fox') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0xff9900, 
                title = 'Лиса') # Создание Embed'a
            embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed) # Отправляем Embed

        elif животное == "Кот":

            response = requests.get('https://some-random-api.com/animal/cat') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x7D7D7D, 
                title = 'Кот') # Создание Embed'a
            embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed) # Отправляем Embed

        elif животное == "Собака":

            response = requests.get('https://some-random-api.com/animal/dog') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0xFF9A00, 
                title = 'Собака') # Создание Embed'a
            embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed) # Отправляем Embed

        elif животное == "Панда":

            response = requests.get('https://some-random-api.com/animal/panda') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0xFFFFFF, 
                title = 'Панда') # Создание Embed'a
            embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed) # Отправляем Embed

        elif животное == "Красная панда":

            response = requests.get('https://some-random-api.com/animal/red_panda') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = disnake.Colour.red(), 
                title = 'Панда') # Создание Embed'a
            embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed) # Отправляем Embed

def setup(bot):
    bot.add_cog(Animals(bot))