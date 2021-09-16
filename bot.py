import discord, json, asyncio, sys, os, random

from discord.ext import commands
from create_db import create_db

with open('master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

token = data["bot_info"]["token"]
cp = data["bot_info"]["command_prefix"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=cp, intents=intents)

@bot.event
async def on_ready():
    print('online')

for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(filename, 'loaded')

@bot.command()
@commands.has_any_role('Team Owners', 'Head Team Member')
async def update(ctx):
    async def start():
        os.system("python bot.py")
    await ctx.send("Bot will be reset")
    await start()
    exit()

@bot.listen('on_message')
async def buttler(message):
    if message.content.startswith("buttler"):
        msg = await message.channel.send(f"my prefix is `{cp}` and you can also access the help menu with `!gencoms`")
        await asyncio.sleep(10)
        await msg.delete()

async def change_presence():
    await bot.wait_until_ready()

    rand_task = [
            'Watching Your DM\'s',
            'Waiting To Assist You',
            f'Staff Applications Are {str(open)}'
        ]

    while not bot.is_closed:
        await bot.change_presence(activity = discord.Game(random.choice(rand_task)))
        await asyncio.sleep(30)

        await bot.change_presence(activity = discord.Game(random.choice(rand_task)))
        await asyncio.sleep(30)

        await bot.change_presence(activity = discord.Game(random.choice(rand_task)))
        await asyncio.sleep(30)

if __name__ == '__main__':
    create_db()
    bot.run(token)