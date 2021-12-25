import discord
from discord import client
from get_html_page_grades import DeleteOldFile, GetGradesTest, InitFilesTest, RenameFile
from parse_html import CheckDiff, GetNewNotes
from secret import tk
from discord.ext import tasks, commands

description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

class GradeChecker(commands.Bot) :
    def __init__(self, command_prefix, description=None, **options):
        super().__init__(command_prefix, description=description, **options)
        self.counter = 0
        self.check_notes.start()
        InitFilesTest()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=10) 
    async def check_notes(self):
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

    @check_notes.before_loop
    async def prepare_check_notes(self):
        await self.wait_until_ready()
    
    @second_background_task.before_loop
    async def before_second_task(self):
        await self.wait_until_ready()


bot = GradeChecker(command_prefix='zig', description=description)
bot.run(tk)