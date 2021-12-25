import discord
from discord.ext import commands, tasks
from channel_management import get_channels_list, init_channel_list, add_a_channel
from secret import tk
from datetime import datetime

class GradeNotifier(commands.Bot) :
    def __init__(self, command_prefix='!', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)
        init_channel_list()
        self.last_check_time = datetime.now()
        self.check_notes.start()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        await self.define_status()

    @tasks.loop(seconds=15)
    async def check_notes(self):
        channel_list = get_channels_list()
        for id in channel_list :
            channel = self.get_channel(id)
            await channel.send('yo')
        self.last_check_time = datetime.now()

    @check_notes.before_loop
    async def before_check_notes(self):
        await self.wait_until_ready()

    async def define_status(self) :
        game = discord.Game("!help")
        await self.change_presence(status= discord.Status.online, activity=game)


bot = GradeNotifier()

@bot.command()
async def salut(ctx) :
    await ctx.send("salut")

@bot.command(brief = 'Add this channel to receive the notifications here')
async def add_channel(ctx) :
    add_a_channel(ctx.channel.id)
    await ctx.send(f"Le channel {ctx.channel} a été ajouté.")

@bot.command(brief = 'Show when is the next check')
async def next_check(ctx) :
    time_now = datetime.now()
    diff = time_now - bot.last_check_time
    diff_next = 300 - diff.total_seconds()
    time_left = divmod(diff_next, 60)
    await ctx.send(f"Next check in {round(time_left[0])} minutes and {round(time_left[1])} seconds")

bot.help_command = commands.DefaultHelpCommand()

bot.run(tk)