from discord.ext import commands


class Talks(commands.Cog):
    """ TALKS WITH USER """
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Talks(bot))
