import discord, asyncio, sqlite3

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.errors import MemberNotFound 

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whois(self, ctx, member:discord.Member):
        await ctx.message.delete()

        if member.display_name == member.name:
            nickname = None
        else:
            nickname = member.display_name

        embed = discord.Embed(
            color = discord.Colour.random(),
            timestamp = ctx.message.created_at,
            title = f'Who Is. . .{member}',
            description = f'''Member Name: {member.name}
                              Member Nick: {nickname}
                              Member Joined: {member.joined_at.__format__('%m/%d/%y, %H:%M:%S')}
                              Member Created: {member.created_at.__format__('%m/%d/%y, %H:%M:%S')}
                           '''
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send(f'{ctx.message.author.mention} the latency is. . .{self.bot.latency*1000}ms')
        await asyncio.sleep(10)
        await msg.delete()

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, MemberNotFound):
            msg = await ctx.send(f'{ctx.message.author.mention}, that member is not in this discord!')
            await asyncio.sleep(10)
            await msg.delete()

def setup(bot):
    bot.add_cog(GeneralCommands(bot))