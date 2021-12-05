import datetime

from discord.ext import commands, tasks


class Dates(commands.Cog):
    """Work with dates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(minutes=240)
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(917034616177721375)

        await channel.send("Data atual: " + now)


def setup(bot):
    bot.add_cog(Dates(bot))
