import discord
from discord.ext import commands


class Git(commands.Cog):
    """ TALKS WITH USER """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="git", help="FOI PIOR")
    async def git_help(self, ctx):
        await ctx.send("AJUDE O KAUÊ A MELHORAR ESSE BOT")
        await ctx.send("https://github.com/kaue22/BotDiscord")


def setup(bot):
    bot.add_cog(Git(bot))
