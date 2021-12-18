import discord
from GetHTMLGrades import DeleteOldFile, GetGradesTest, InitFilesTest, RenameFile
from ParseHTML import CheckDiff, GetNewNotes
from secret import tk
from discord.ext import tasks

class GradeChecker(discord.Client) :
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.counter = 0
        self.my_background_task.start()
        InitFilesTest()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=10) 
    async def my_background_task(self):
        channel = self.get_channel(919338640776257596)
        GetGradesTest()
        if(CheckDiff()) :
            list_matieres = GetNewNotes()
            for mat in list_matieres :
                await channel.send("@everyone Nouvelle note de " + mat)
        else :
            await channel.send("y'a R frérot")
        DeleteOldFile()
        RenameFile()
        

    @tasks.loop(seconds=5)
    async def second_background_task(self):
        channel = self.get_channel(919338640776257596)
        await channel.send("ziggy")

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in
    
    @second_background_task.before_loop
    async def before_second_task(self):
        await self.wait_until_ready()


client = GradeChecker()
client.run(tk)