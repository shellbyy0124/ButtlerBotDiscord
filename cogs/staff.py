import sqlite3, asyncio, discord, datetime

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.errors import MissingRequiredArgument 
from datetime import datetime

class staffAbilities(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    async def nuke(self, ctx):
        channel = ctx.channel
        channel_pos = channel.position

        new_channel = await channel.clone()
        await channel.delete()
        await new_channel.edit(position=channel_pos, sync_permissions=True)

        msg = await new_channel.send(f'{ctx.message.author.mention}, I have nuked and replaced {ctx.channel.mention}!')
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    async def purge(self, ctx, num:int):

        await ctx.channel.purge(limit=num, check = lambda m: not m.pinned)
        a = await ctx.channel.send(f'I have purged {num} messages from this channel')
        await asyncio.sleep(5)
        await a.delete()

    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    async def createChannel(self, ctx):
        def check(m):
            return ctx.message.author.id == m.author.id

        embed = discord.Embed(
            color = discord.Colour.random(),
            timestamp = ctx.message.created_at,
            title = 'ButtlerBot Channel Creator',
            description = 'Hi! What is the name of the category that you want a new channel in?',
            inline=False
        ).set_thumbnail(
            url = self.bot.user.avatar_url
        )

        msg = await ctx.send(embed=embed)

        cat = await self.bot.wait_for('message')

        categories = []

        for category in ctx.guild.categories:
            categories.append(category.name)

        tries = 3

        while tries > 0:
            while cat not in categories:
                tries -= 1
                err = await ctx.send(f'That category does not exists. Enter the category name. You have {tries} tries remaining.')

                new_cat = await self.bot.wait_for('message', check=check)

                if new_cat not in categories:
                    tries = tries
                else:
                    cat = new_cat
                    break
            else:
                embed2 = discord.Embed(
                    color = discord.Colour.random(),
                    timestamp = ctx.message.created_at,
                    title = 'ButtlerBot Channel Creator',
                    description = 'What is the name of the new channel?',
                    inline=False
                ).set_thumbnail(
                    url = self.bot.user.avatar_url
                )

                await msg.edit(embed=embed2)

                name = await self.bot.wait_for('message', check=check)

                channel_names = []

                for channel in cat:
                    channel_names.append(channel.name)

                tries = 3

                while tries > 0:
                    if name not in channel_names:
                        new_channel = await ctx.guild.create_text_channel(category=cat, name=name.content, overwrites=None)
                        confirm = await new_channel.send(f'{ctx.message.author.mention} here is your new channel')
                        await asyncio.sleep(3)
                        await confirm.delete()
                        break
                else:
                    tries -= 1
        else:
            await ctx.send(f'{ctx.message.author.mention}, you have run out of tries. Please run the command again.')

    @commands.command()
    @commands.has_any_role('Team Owners','Head Team Member')
    async def prune_members(self, ctx, days=90, compute_to_prune=True, roles=None, reason='Inactive For 90+ Days'):
        num_to_remove = ctx.guild.estimate_pruned_members
        await ctx.send(f'Are you sure you want to remove {num_to_remove} members? y or n')
        

    @purge.error 
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention}, the command setup is\n`<command_prefix>purge <number_of_messages_to_delete>`')
    
    @createChannel.error 
    async def createChannel_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention}, the command setup is\n`<command_prefix>createChannel <category_name> <channel_name> <type_of_channel(voice/text)>`')

def setup(bot):
    bot.add_cog(staffAbilities(bot))