import disnake
from disnake.ext import commands

import json
import requests

class RolePlay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # ПОЦЕЛОВАТЬ
    @commands.slash_command(description="Поцеловать")
    async def kiss(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя поцеловать нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/kiss') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** поцеловал(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ОБНЯТЬ
    @commands.slash_command(description="Обнять")
    async def hug(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя обнять нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/hug') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** обнял(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ДАТЬ ПОЩЕЧИНУ
    @commands.slash_command(description="Дать пощечину")
    async def slap(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя бить нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/slap') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** дал(-а) пощечину **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ПОПРИВЕТСТВОВАТЬ
    @commands.slash_command(description="Поприветствовать")
    async def wave(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя поприветствовать нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/wave') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** поприветствовал(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # УКУСИТЬ
    @commands.slash_command(description="Укусить")
    async def bite(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя укусить нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/bite') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** укусил(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ЛИЗНУТЬ
    @commands.slash_command(description="Лизнуть")
    async def lick(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя лизнуть нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/lick') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** лизнул(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # СТУКНУТЬ
    @commands.slash_command(description="Стукнуть")
    async def bonk(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя стукнуть нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/bonk') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** стукнул(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ПОГЛАДИТЬ
    @commands.slash_command(description="Погладить")
    async def pat(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя погладить нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/pat') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** погладил(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ЗАДИРАТЬ
    @commands.slash_command(description="Задирать")
    async def bully(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя задирать нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/bully') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** задирает **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ДАТЬ ПЯТЬ
    @commands.slash_command(description="Дать пять")
    async def highfive(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себе дать пять нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/highfive') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** дал(-а) пять **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ДАТЬ ПЯТЬ
    @commands.slash_command(description="Взяться за руку")
    async def handhold(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/handhold') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** взял(-а) за руку **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ПОДМИГНУТЬ
    @commands.slash_command(description="Подмигнуть")
    async def wink(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себе подмигнуть нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/wink') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** подмигнул(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ПОДМИГНУТЬ
    @commands.slash_command(description="Тыкнуть")
    async def poke(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя тыкнуть нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/poke') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** тыкнул(-а) **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

    # ПРИЖАТЬСЯ
    @commands.slash_command(description="Прижаться")
    async def poke(self, ctx, участник: disnake.Member = commands.Param(description="Выберите пользователя")):
        
        if участник.bot:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но боты - не живые люди! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        elif участник == ctx.author:
            
            await ctx.send(embed=disnake.Embed(title='❌ Ошибка', description="К сожалению, но себя тыкнуть нельзя! 😔", color=disnake.Colour.red()), ephemeral=True)
        
        else:

            response = requests.get('https://api.waifu.pics/sfw/cuddle') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = disnake.Embed(
                color = 0x2d2d30, 
                description = f'**{ctx.author}** прижимается к **{участник}**!') # Создание Embed'a
            embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

#################### БЕЗ УПОМИНАНИЯ

    # ПЛАКАТЬ
    @commands.slash_command(description="Плакать")
    async def cry(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/cry') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** плачет!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # КРАСНЕТЬ
    @commands.slash_command(description="Краснеть")
    async def blush(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/blush') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** краснеет!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # УЛЫБНУТЬСЯ
    @commands.slash_command(description="Улыбнуться")
    async def smile(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/cry') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** улыбается!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # КУШАТЬ
    @commands.slash_command(description="Кушать")
    async def eat(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/nom') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** кушает!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # ВЕСЕЛИТЬСЯ
    @commands.slash_command(description="Веселиться")
    async def happy(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/happy') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** веселится!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # ТАНЦЕВАТЬ
    @commands.slash_command(description="Танцевать")
    async def dance(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/dance') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** танцует!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # СМУЩАТЬСЯ
    @commands.slash_command(description="Смущаться")
    async def cringe(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/cringe') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** смущается!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

    # ВЫГЛЯДИТ САМОДОВОЛЬНО
    @commands.slash_command(description="Выглядеть самодовольно")
    async def smug(self, ctx):       

        response = requests.get('https://api.waifu.pics/sfw/smug') # Get-запрос
        json_data = json.loads(response.text) # Извлекаем JSON

        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** выглядит самодовольно!') # Создание Embed'a
        embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed

################## ОСТАЛЬНОЕ
    @commands.slash_command(description="Свое РП действие")
    async def custom(self, ctx, текст: str = commands.Param(description="Напишите свое РП действие")):
        embed = disnake.Embed(
            color = 0x2d2d30, 
            description = f'**{ctx.author}** {текст}!')
        await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(RolePlay(bot))