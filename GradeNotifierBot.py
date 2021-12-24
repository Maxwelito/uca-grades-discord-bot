import discord
from discord.ext import commands, tasks
from ParseHTML import InitChannelList
from secret import tk
import pickle

class GradeNotifier(commands.Bot) :
    def __init__(self, command_prefix='!', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)
        InitChannelList()
        self.check_notes.start()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=5)
    async def check_notes(self):
        with open("channels", 'rb') as file:
            channel_list = pickle.load(file)
        for id in channel_list :
            channel = self.get_channel(id)
            await channel.send('yo')

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

@bot.command()
async def add_channel(ctx) :
    with open("channels", 'rb') as file :
        channel_list = pickle.load(file)
    channel_list.append(ctx.channel.id)
    with open("channels", 'wb') as file :
        pickle.dump(channel_list, file)
    await ctx.send(f"Le channel {ctx.channel} a été ajouté.")

bot.run(tk)