import discord
from discord.ext import commands


class Images(commands.Cog):
    """ TALKS WITH USER """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="foipior", help="FOI PIOR")
    async def foi_pior(self, ctx):
        await ctx.send(file=discord.File('foipior.jpeg'))

    @commands.command(name="jamais", help="JAMAIS")
    async def jamais(self, ctx):
        await ctx.send(file=discord.File('jamais.jpg'))


def setup(bot):
    bot.add_cog(Images(bot))
