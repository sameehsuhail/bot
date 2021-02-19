import discord
import sys
import datetime
from discord.ext import commands, timers

bot = commands.Bot(command_prefix="!")
bot.timer_manager = timers.TimerManager(bot)

@bot.event
async def on_ready():
    print("Bot is online.")

@bot.command(name="remind")
async def remind(ctx, time, *, text):
    """Remind to do something on a date.

    The date must be in ``Y/M/D`` format."""
    date = datetime.datetime(*map(int, time.split("/")))

    timers.Timer(bot, "reminder", date, args=(ctx.channel.id, ctx.author.id, text)).start()

@bot.event
async def on_reminder(channel_id, author_id, text):
    channel = bot.get_channel(channel_id)

    await channel.send("Hey <@{0}>, remember to: {1}".format(author_id, text))

#@bot.event()
#async def quit(ctx):
    #sys.exit()

bot.run("ODExOTAwNzAyNTgxODUwMTMy.YC47cw.39vnuoVMG8yOxkPYFhNZe6SJRx0")
