import asyncio, discord, sqlite3

from discord.ext import commands
from discord.ext.commands import Cog 

class UponJoiningServer(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.owner.send('Hi. Give me just a moment to check if you\'re in the database')

        with sqlite3.connect('main.db') as main_db:
            cur = main_db.cursor()

            sql = 'SELECT guild_id FROM guild_info WHERE guild_id=?'
            val = (guild.id,)

            result = cur.execute(sql, val).fetchone()

            if result is None:
                sql = 'INSERT INTO guild_info(guild_id, member_count) VALUES (?,?)'
                val = (guild.id, len([m for m in guild.members if not m.bot]))

                cur.execute(sql, val)
                main_db.commit()

                await guild.owner.send('You have been added to the database, and are ready to go!')
            else:
                await guild.owner.send("You've already been added to the database")

def setup(bot):
    bot.add_cog(UponJoiningServer(bot))