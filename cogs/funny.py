import disnake
from disnake.ext import commands

import random
from random import choice

class Funny(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # БЕН
    @commands.slash_command(description='Бен')
    async def ben(self, ctx, *, вопрос: str = commands.Param(description="Задайте свой вопрос Бену")):
        
        random_r = random.randint(1, 4)
        
        if random_r == 1:
            
            embed = disnake.Embed(
                title='🐶 Бен', 
                description=f'Ваш вопрос: **{вопрос}**\n\nБен говорит: **Yes.**', 
                color=disnake.Colour.orange())
            embed.set_thumbnail(url='https://media.tenor.com/6St4vNHkyrcAAAAM/yes.gif')
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)

        elif random_r == 2:
            
            embed = disnake.Embed(
                title='🐶 Бен', 
                description=f'Ваш вопрос: **{вопрос}**\n\nБен говорит: **No.**', 
                color=disnake.Colour.orange())
            embed.set_thumbnail(url='https://media.tenor.com/x2u_MyapWvcAAAAM/no.gif')
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)

        elif random_r == 3:
            
            embed = disnake.Embed(
                title='🐶 Бен', 
                description=f'Ваш вопрос: **{вопрос}**\n\nБен говорит: **Ho-ho-ho.**', 
                color=disnake.Colour.orange())
            embed.set_thumbnail(url='https://media.tenor.com/e8urEO5XU-kAAAAM/hohho-ho.gif')
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)

        elif random_r == 4:
            
            embed = disnake.Embed(
                title='🐶 Бен', 
                description=f'Ваш вопрос: **{вопрос}**\n\nБен говорит: **Ugh.**', 
                color=disnake.Colour.orange())
            embed.set_thumbnail(url='https://media.tenor.com/aomZLSiXCQ8AAAAM/ugh.gif')
            embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    # МОНЕТКА
    @commands.slash_command(description="Монетка")
    async def coin(ctx, сторона: str = commands.Param(description="Выберите сторону", choices=["Орёл", "Решка"])):
        
        random_r = random.randint(1, 2)
        
        if сторона == "Орёл":
            
            if random_r == 1:
                
                embed = disnake.Embed(
                    title="✅ Вы угадали!",
                    description="Выпал орёл.",
                    color = disnake.Color.green()
                    )
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            
            else:
                
                embed = disnake.Embed(
                    title="❌ Вы не угадали!",
                    description="Выпала решка.",
                    color = disnake.Color.red()
                    )
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        else:

            if random_r == 1:
                
                embed = disnake.Embed(
                    title="✅ Вы угадали!",
                    description="Выпала решка.",
                    color = disnake.Color.green()
                    )
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            
            else:
                
                embed = disnake.Embed(
                    title="❌ Вы не угадали!",
                    description="Выпал орёл.",
                    color = disnake.Color.red()
                    )
                embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Funny(bot))