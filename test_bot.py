import discord
from secret import tk
from discord.ext import tasks

class GradeChecker(discord.Client) :
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.counter = 0
        self.my_background_task.start()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=2)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(919338640776257596)  # channel ID goes here
        self.counter += 1
        await channel.send("Salut @" + "everyone")

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = GradeChecker()
client.run(tk)