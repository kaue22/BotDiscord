from discord.ext import commands


class Smarts(commands.Cog):
    """ TALKS WITH USER """
    def __init__(self, bot):
        self.bot = bot

    # Func para o bot calcular
    @commands.command(name="calcular", help="calcula uma expressão")
    async def calculate_expression(self, ctx,
                                   *expression):  # *expression é para pegar todos os argumentos passados no parametro expression (tupla)
        expression = ''.join(expression)  # .join para pegar cada elemento da tupla e inserir na string ("")
        response = eval(expression)

        await ctx.send("A Resposta é : " + str(response))


def setup(bot):
    bot.add_cog(Smarts(bot))
