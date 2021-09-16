import discord, asyncio

from discord.ext import commands 
from discord.ext.commands import Cog 
from pyzipcode import ZipCodeDatabase

class ZipCodes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookzip(self, ctx, zip:int):
        zcdb = ZipCodeDatabase()

        color = discord.Colour.random()
        timestamp = ctx.message.created_at

        embed = discord.Embed(
            color = color,
            timestamp = timestamp,
            title = 'ButtlerBot ZipCode Look Up',
            description = f'Searching the zip code. . .{zip}',
            inline = False
        ).set_thumbnail(
            url = self.bot.user.avatar_url
        )

        msg = await ctx.send(embed = embed)

        await asyncio.sleep(5)

        new_zip = zcdb[zip]

        if new_zip is None:
            msg = await ctx.send('That is not a valid zip code. Please try again')

            await asyncio.sleep(4)

            await msg.delete()

        else:
            embed.add_field(
                name = f'The results for . . .{zip}:',
                value = f'''Zip: {new_zip.zip}
                            City: {new_zip.city}
                            State: {new_zip.state}
                            Longitude: {new_zip.longitude}
                            Latitude: {new_zip.latitude}
                            Dst: {new_zip.dst}
                            ''',
                inline = False
            )

            await asyncio.sleep(3)
            await msg.edit(embed=embed)

    @commands.command()
    async def lookcity(self, ctx, city:str):
        def check(m):
            return ctx.message.author.id == m.author.id

        zcdb = ZipCodeDatabase()

        color = discord.Colour.random()
        timestamp = ctx.message.created_at

        embed = discord.Embed(
            color = color,
            timestamp = timestamp,
            title = 'ButtlerBot City Look Up',
            description = f'Searching for city. . .{city}',
            inline = False
        ).set_thumbnail(
            url = self.bot.user.avatar_url
        )

        msg = await ctx.send(embed=embed)

        while city not in zcdb.find_zip(city=city):
            err = await ctx.send('That is not a valid city. Here is a list of cities beginning with {city[:1]}')
            msg1 = await ctx.send([i for i in zcdb.find_zip(city=f'{city[:1]}%')])
            msg2 = await ctx.send('Which city from the list above would you like to see?')
            
            new_city = await self.bot.wait_for('message', check=check)

            if new_city in zcdb.find_zip(city=new_city):
                break
            else:
                pass

        embed.add_field(
            name = f'Results from {city}',
            value = f'''{new_city}'''
        )

def setup(bot):
    bot.add_cog(ZipCodes(bot))