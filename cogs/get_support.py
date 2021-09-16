import discord, sqlite3, asyncio, json

from discord.ext import commands
from discord.ext.commands import Cog

from datetime import datetime as dt, timezone

class SupportNeeded(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def supp(self, ctx):
        def check(m):
            return ctx.message.author.id == m.author.id

        msg = await ctx.send(f'{ctx.message.author.mention} this command is temporarily unavailable. Please go to the support category, and use the given channels provided.')

        await asyncio.sleep(5)
        await msg.delete()

    @commands.command()
    async def close(self, ctx):
        # def check(m):
        #     return ctx.message.author.id == m.author.id
        # await ctx.message.delete()

        # await ctx.send('Are you sure you want to close this channel? This action cannot be undone. Enter y or n')
        # ans = await self.bot.wait_for('message', check=check)

        # if ans.content.lower() == 'y':
        #     await ctx.channel.delete()
        # else:
        #     msg = await ctx.send('You Said No. Continuing Use Of Channel')
        #     await asyncio.sleep(10)
        #     await ans.delete()
        #     await msg.delete()

        msg = await ctx.send(f'{ctx.message.author.mention} this command is temporarily unavailable. Pinging the head admin for assistance. Thanks')
        
        for role in ctx.guild.roles:
            if role.name == 'staff':
                await ctx.send(f'{role.mention}, {ctx.message.author.display_name} needs assistance')

def setup(bot):
    bot.add_cog(SupportNeeded(bot))