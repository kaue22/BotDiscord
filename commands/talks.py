from discord.ext import commands


class Talks(commands.Cog):
    """ TALKS WITH USER """

    def __init__(self, bot):
        self.bot = bot

    # Quando digitar o prefixo !oi executa a função send_hello
    @commands.command(name="ola", help="Envia um Olá")
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = "Ola, " + name

        await ctx.send(response)


def setup(bot):
    bot.add_cog(Talks(bot))
