import discord
from discord import client
from discord.ext import commands, tasks
from secret import tk


class GradeNotifier(commands.Bot) :
    def __init__(self, command_prefix='!', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)
        self.counter = 0

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=5)
    async def second_background_task(self):
        channel = self.get_channel(919338640776257596)
        await channel.send("ziggy")

    @second_background_task.before_loop
    async def before_second_task(self):
        await self.wait_until_ready()

    '''async def on_message(self, message):
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')
        if message.content.startswith('!start') :
            self.second_background_task.start()'''

    



bot = GradeNotifier()

@bot.command()
async def salut(ctx) :
    await ctx.send("salut")

@bot.command()
async def start(ctx) :
    bot.second_background_task.start()


bot.run(tk)