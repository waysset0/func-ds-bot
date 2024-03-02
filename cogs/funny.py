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
    # @commands.slash_command(description="Монетка")
    # async def coin(ctx, сторона: str = commands.Param(description="Выберите сторону", choices=["Орёл", "Решка"])):
        
    #     random_r = random.randint(1, 2)
        
    #     if сторона == "Орёл":
            
    #         if random_r == 1:
                
    #             embed = disnake.Embed(
    #                 title="✅ Вы угадали!",
    #                 description="Выпал орёл.",
    #                 color = disnake.Color.green()
    #                 )
    #             embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            
    #         else:
                
    #             embed = disnake.Embed(
    #                 title="❌ Вы не угадали!",
    #                 description="Выпала решка.",
    #                 color = disnake.Color.red()
    #                 )
    #             embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
    #     else:

    #         if random_r == 1:
                
    #             embed = disnake.Embed(
    #                 title="✅ Вы угадали!",
    #                 description="Выпала решка.",
    #                 color = disnake.Color.green()
    #                 )
    #             embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
            
    #         else:
                
    #             embed = disnake.Embed(
    #                 title="❌ Вы не угадали!",
    #                 description="Выпал орёл.",
    #                 color = disnake.Color.red()
    #                 )
    #             embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.display_avatar.url)
    #     await ctx.send(embed=embed)

    @commands.slash_command(description = 'Монетка')
    async def coin(self, inter, сторона: str = commands.Param(description = 'Выберите сторону', choices=["Орёл", "Решка"]), участник: disnake.Member = commands.Param(None, description = 'Выберите участника для игры с вами')):
        
        if участник == None:
            random_r = random.randint(1, 2)
        
            if сторона == "Орёл":   
                
                if random_r == 1:    
                    embed = disnake.Embed(
                        title = "🪙 Монетка",
                        description = "Вы угадали, выпал орёл!",
                        color = disnake.Color.green()
                        )
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                
                else:    
                    embed = disnake.Embed(
                        title = "🪙 Монетка",
                        description = "Вы не угадали, выпала решка!",
                        color = disnake.Color.red()
                        )
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
            
            else:
                if random_r == 1:
                    embed = disnake.Embed(
                        title = "🪙 Монетка",
                        description = "Вы угадали, выпала решка!",
                        color = disnake.Color.green()
                        )
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                
                else:    
                    embed = disnake.Embed(
                        title = "🪙 Монетка",
                        description = "Вы не угадали, выпал орёл!",
                        color = disnake.Color.red()
                        )
                    embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
            await inter.send(embed=embed)
        
        elif участник.bot:
            embed_error = disnake.Embed(
                title = '❌ Ошибка!',
                description = "К сожалению, но на ботов это не действует!",
                color = disnake.Colour.red())
            await inter.send(embed = embed_error, ephemeral = True)
        
        elif участник == inter.author:
            embed_error = disnake.Embed(
                title = '❌ Ошибка!',
                description = "К сожалению, но на себе это не действует!",
                color = disnake.Colour.red())
            await inter.send(embed = embed_error, ephemeral = True)

        else:
            random_r = random.randint(1, 2)
            embed = disnake.Embed(
                title = "🪙 Монетка", 
                description = f"**{inter.author}** предлагает вам сыграть в монетку!",
                color = disnake.Color.green())
            components = [
                disnake.ui.Button(label = "Подтвердить", style = disnake.ButtonStyle.green, custom_id = "confirm"),
                disnake.ui.Button(label = "Отмена", style = disnake.ButtonStyle.red, custom_id = "cancel")
            ]
            await inter.response.send_message(f"{участник.mention}", embed = embed, components = components)
            
            try:
                interaction = await inter.bot.wait_for("button_click", check = lambda i: i.user.id == участник.id and i.component.custom_id in ["confirm", "cancel"], timeout=60)
                
                # buttons
                if interaction.component.custom_id == 'confirm':
                    
                    if сторона == "Орёл":
                        
                        if random_r == 1:    
                            embed = disnake.Embed(
                                title = "🪙 Монетка",
                                description = f"**{inter.author}** угадал, выпал орёл!\n\nПобеда засчитана: **{inter.author}**",
                                color = disnake.Color.green()
                                )
                            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                            await interaction.response.edit_message("", embed = embed, components = None)
                        
                        else:  
                            embed = disnake.Embed(
                                title = "🪙 Монетка",
                                description = f"**{inter.author}** не угадал, выпала решка!\n\nПобеда засчитана: **{участник}**",
                                color = disnake.Color.red()
                                )
                            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                            await interaction.response.edit_message("", embed = embed, components = None)

                    else:
                        
                        if random_r == 1:
                            
                            embed = disnake.Embed(
                                title = "🪙 Монетка",
                                description = f"**{inter.author}** угадал, выпала решка!\n\nПобеда засчитана: **{inter.author}**",
                                color = disnake.Color.green()
                                )
                            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                            await interaction.response.edit_message("", embed = embed, components = None)
                        
                        else:
                            
                            embed = disnake.Embed(
                                title = "🪙 Монетка",
                                description = f"**{inter.author}** не угадал, выпал орёл!\n\nПобеда засчитана: **{участник}**",
                                color = disnake.Color.red()
                                )
                            embed.set_footer(text = f"Запросил: {inter.author.name}", icon_url = inter.author.display_avatar.url)
                            await interaction.response.edit_message("", embed = embed, components = None)

                elif interaction.component.custom_id == 'cancel':
                    embed = disnake.Embed(
                        title = "🪙 Монетка", 
                        description = f"**{участник}** отказался!", 
                        color = disnake.Color.red())
                    await interaction.response.edit_message(f"{inter.author.mention}", embed = embed, components = None)
            
            except asyncio.TimeoutError:
                return

def setup(bot):
    bot.add_cog(Funny(bot))