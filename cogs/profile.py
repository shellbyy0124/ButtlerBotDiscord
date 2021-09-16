import discord, sqlite3, webcolors, asyncio

from colored import fg, bg, attr
from discord.ext import commands

with sqlite3.connect('main.db') as main_db:
    cur = main_db.cursor()

    result = cur.execute('SELECT * FROM guild_info')

    guild_ids = [i for i in result]

class ProfileCreation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def createprof(self, ctx):
        # time = ctx.message.created_at
        # title = 'ButtlerBot Profile Creation Wizard'
        # member = ctx.message.author
        # guild = ctx.message.guild

        # embed = discord.Embed(
        #     color = discord.Colour.random(),
        #     timestamp = time,
        #     title = title,
        #     description = f'Hi, {ctx.message.author.display_name}! In the next view moments, we will be building you an awesome profile to show off to your friends!',
        #     inline = False
        # ).add_field(
        #     name = 'Question 1:',
        #     value = 'When is your birthday? Please use the MM/DD/YYYY format',
        #     inline = False
        # ).set_thumbnail(
        #     url = self.bot.user.avatar_url
        # )

        # msg = await ctx.message.author.send(embed = embed)

        # bday = await self.bot.wait_for('message')

        # month_check = range(1, 12)
        # day_check = range(1, 31)
        # year_check = range(1900, 2021)

        # for month, day, year in bday.content.split('/'):
        #     if int(month) == month_check and int(day) == day_check and int(year) == year_check: 
        #         embed = discord.Embed(
        #             color = discord.Colour.random(),
        #             timestamp = time,
        #             title = title,
        #             description = f'''Member Name: {member.name}
        #                               Member Nick: {member.display_name}
        #                               Member ID: {member.id}
        #                               Member Birthday: {bday.content}
        #                 ''',
        #             inline = False
        #         ).add_field(
        #             name = 'Question 2:',
        #             value = 'What is your favorite color?',
        #             inline = False
        #         ).set_thumbnail(
        #             url = self.bot.user.avatar_url
        #         )

        #         await ctx.message.delete()
        #         await bday.delete()
        #         await msg.delete()
        #         msg = await member.send(embed=embed)

        #         fav_col = await self.bot.wait_for('message')

        #         if all(i.isalpha() for i in fav_col.content):
        #             await msg.delete()
        #             await fav_col.delete()
                    
        #             embed = discord.Embed(
        #                 color = webcolors.name_to_hex(fav_col.content),
        #                 timestamp = time,
        #                 title = title,
        #                 description = f'''Member Name: {member.name}
        #                                   Member Nick: {member.display_name}
        #                                   Member ID: {member.id}
        #                                   Member Birthday: {bday.content}
        #                                   Favorite Color: {fav_col.content}''',
        #                 inline = False
        #             ).add_field(
        #                 name = 'Question 3:',
        #                 value = 'What programming languages do you know?',
        #                 inline = False
        #             ).set_thumbnail(
        #                 url = self.bot.user.avatar_url
        #             )

        #             msg = await member.send(embed=embed)

        #             langs = await self.bot.wait_for('message')

        #             if all(i.isalpha() for i in langs.content.lower()):
        #                 langs = []

        #                 for i in langs.split(''):
        #                     langs.append(i)

        #                 await msg.delete()
        #                 await langs.delete()
                        
        #                 final_embed = discord.Embed(
        #                     color = webcolors.name_to_hex(fav_col.content),
        #                     timestamp = time,
        #                     title = title,
        #                     description = f'''Member Name: {member.name}
        #                                       Member Nick: {member.display_name}
        #                                       Member ID: {member.id}
        #                                       Member Birthday: {bday.content}
        #                                       Favorite Color: {fav_col.content}''',
        #                     inline = False
        #                 ).add_field(
        #                     name = 'Please Review Your Changes!',
        #                     value = 'Please review the information you answered with to ensure that it\
        #                         is accurate. If not, please enter edit, otherwise, enter save',
        #                     inline = False
        #                 ).set_thumbnail(
        #                     url = self.bot.user.avatar_url
        #                 )

        #                 msg = await member.send(embed=final_embed)

        #                 with sqlite3.connect('main.db') as main_db:
        #                     cur = main_db.cursor()
  
        #                     try:
        #                         sql = 'INSERT INTO profiles(guild_id, member_id, member_name, member_nick, fav_color, langs) VALUES (?,?,?,?,?,?)'
        #                         val = (guild.id, member.id, member.name, member.display_name, fav_col.content, langs.content)

        #                     except:
        #                         sql = 'UPDATE profiles SET guild_id=?, member_id=?, member_name=?, member_nick=?, fav_color=?, langs=?'
        #                         val = (guild.id, member.id, member.name, member.display_name, fav_col.content, langs.content)

        #                     cur.execute(sql, val)
        #                     main_db.commit()

        #                 await member.send('I have saved your profile! :)')                   
        #     else:
        #         pass

        msg = await ctx.send(f'{ctx.message.author.mention}, apologies, but this command is temporarily unavailable')
        await asyncio.sleep(5)
        await msg.delete()


def setup(bot):
    bot.add_cog(ProfileCreation(bot))