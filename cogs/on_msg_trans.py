import discord, googletrans, asyncio

from discord.ext import commands 
from discord.ext.commands import Cog 

class AutoTranslator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name == 'en-english':
            pass
        elif message.channel.name == 'es-espanol':
            pass
        elif message.channel.name == 'fr-francais':
            pass
        else:
            pass

def setup(bot):
    bot.add_cog(AutoTranslator(bot))