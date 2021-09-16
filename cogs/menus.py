import discord

from discord.ext import commands 
from discord.ext.commands import Cog 

class HelpMenus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gencoms(self, ctx):
        embed = discord.Embed(
            color = discord.Colour.random(),
            timestamp = ctx.message.created_at,
            title = 'ButtlerBot General Help Window',
            description = 'The following commands are available for all users\' to use.',
            inline = False
        ).add_field(
            name = '!supp',
            value = 'This command will create you a new support channel for any time you\
                need support, however, your guild owner may limit the number of channels\
                that you may have within his server rules.\n**___This Command Is Temporarily Turned Off___**',
            inline = False
        ).add_field(
            name = '!close',
            value = 'This command may only be used within a text channel under the Support\
                category, and it can only be used by the person who created the support channel.\
                Admins -- you have a close command within your own help command that will close any\
                channel within the Support category.\n**___This Command Is Temporarily Turned Off___**',
                inline = False
        ).add_field(
            name = '!createprof',
            value = 'Lets create you an awesome profile for your friends to see, together!',
            inline = False
        ).add_field(
            name = '!eball <question>',
            value = 'This command is just like having the magic 8 ball within your grasp. Type the\
                command, then add your question after, like: `!eball will i get this job?`, and it\
                will give you it\'s input.',
            inline = False
        ).add_field(
            name = '!pigme <message>',
            value = 'Will translate your message into the Pig-Latin language',
            inline = False
        ).add_field(
            name = '!translate <new_lang> <message>',
            value = 'Will translate your message into the designated language.',
            inline = False
        ).add_field(
            name = '!whois <user_id>',
            value = 'See a server members profile!',
            inline = False
        ).add_field(
            name = '!ping',
            value = 'Returns the bots latency',
            inline = False
        ).add_field(
            name = '!math <expression> -- created by GamingBuddhist',
            value = 'Need help with math? This calculator is only able to use the following expressions\
                `+` `-` `*` `/` `( )` `%` `.`',
            inline = False
        ).add_field(
            name = '!lookzip <zip_code>',
            value = 'Shows the information available for the zip code entered like\
                longitude, latitude, city, state',
            inline = False
        ).add_field(
            name = '!lookcity <city_name>',
            value = 'Show information available for the city entered. See above field for\
                returned details',
            inline = False
        ).set_thumbnail(
            url = ctx.message.author.avatar_url
        )

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def staffhelp(self, ctx):
        embed = discord.Embed(
            color = discord.Colour.random(),
            timestamp = ctx.message.created_at,
            title = 'ButtlerBot Staff Help Menu',
            description = 'The following commands are available to those who have the manage_channels permission',
            inline = False
        ).add_field(
            name = '!createChannel',
            value = 'Creates a new channel for you in the designated category',
            inline = False
        ).add_field(
            name = '!purge',
            value = 'Will delete _n_ number of messages from the channel the command is used in.\
                This command does not give a "Are You Sure" option, so please use wisely.',
            inline = False
        ).add_field(
            name = '!nuke',
            value = 'Will delete, and re-create the channel that the command was used in.\
                This command does not have a "Are You Sure" question, so please use carefully.',
            inline = False
        ).set_thumbnail(
            url = ctx.message.author.avatar_url
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpMenus(bot))