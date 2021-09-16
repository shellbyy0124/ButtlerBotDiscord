import asyncio
import random
import discord

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.errors import MissingRequiredArgument 

class Games(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    async def eball(self, ctx, *, message):
        embed1 = discord.Embed(
                               color = discord.Colour.random(),
                               title = f'ButtlerBots\' Fortune Teller',
                               description = 'Meditating On Your Question Now. . .'
        )
        
        file = discord.File('./bot_images/communing.jpg')
        embed1.set_image(url='attachment://communing.jpg')

        msg = await ctx.send(file = file, embed=embed1)

        async with ctx.typing():

            await asyncio.sleep(5)

        responses = [
            'Yes', 'Outlook Not So Good', 'Ask Again Later',
            'Don\'t Count On It', 'As I See It, Yes', 'You May Rely On It',
            'Concentrate And Ask Again Later', 'Signs Point To Yes', 'Very Doubtful',
            'It Is Certain', 'Outlook Good', 'My Sources Say No', 
            'Most Likely', 'My Reply Is No', 'Reply Hazy, Try Again',
            'Cannot Predict Now', 'Without A Doubt', 'Better Not Tell You Now', 
            'It Is Decidedly So'
        ]

        embed2 = discord.Embed(
                               color = discord.Colour.random(),
                               title = f'ButtlerBots\' Fortune Teller',
                               description = f'Your Question: {message}\nMy Response: {random.choice(responses)}'
                               )
        
        file = discord.File('./bot_images/cards.jpg')
        embed2.set_image(url='attachment://cards.jpg')

        await msg.delete()
        msg2 = await ctx.send(file = file, embed=embed2)
        await asyncio.sleep(10)
        await msg2.delete()
        await ctx.message.delete()

    @eball.error
    async def eball_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('You are missing the question. Please use `!eball <question>`')

def setup(bot):
    bot.add_cog(Games(bot))