import discord, sqlite3

from discord.ext import commands
from discord.ext.commands import Cog 

class onMemberJoining(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(member):
        with sqlite3.connect('main.db') as main_db:
            cur = main_db.cursor()

            sql = 'SELECT member_id FROM members WHERE guild_id=?'
            val = (member.guild.id,)

            result = cur.execute(sql, val).fetchall()

            if result is None:
                sql = 'INSERT INTO members(guild_id, member_id, warings, tempmutes) VALUES (?,?,?,?)'
                val = (member.guild.id, member.id, 0, 0)

                cur.execute(sql, val)
                main_db.commit()
            
        for channel in member.guild.text_channels:
            if channel.name.startswith('welcome') or channel.name.startswith('general'):
                await channel.send('Your new member count is' + len([m for m in member.guild.members if not m.bot]))
            else:
                print('member added')

def setup(bot):
    bot.add_cog(onMemberJoining(bot))